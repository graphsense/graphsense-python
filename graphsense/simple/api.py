"""Simple Api frontend to build requests against the graphsense api
"""
import json
import pandas as pd
from graphsense.api_client import ApiClient
from graphsense.configuration import Configuration
from graphsense import apis
from graphsense import models
from graphsense.model_utils import OpenApiModel, ModelSimple
from pandas import DataFrame
from datetime import datetime
from functools import cached_property  # , partial
from typing import List, Union


def get_df_bulk(blkapi, currency, operation, body):
    """Summary

    Args:
        blkapi (TYPE): Description
        currency (TYPE): Description
        operation (TYPE): Description
        body (TYPE): Description

    Returns:
        TYPE: Description
    """
    return pd.read_csv(
        blkapi.bulk_csv(
            currency, operation, body=body, num_pages=1, _preload_content=False
        )
    )


def ensure_list(item):
    """Summary

    Args:
        item (TYPE): Description

    Returns:
        TYPE: Description
    """
    if type(item) == str:
        return [item]
    try:
        iterator = iter(item)
        return list(iterator)
    except TypeError:
        return [item]


def try_to_int(i):
    """Summary

    Args:
        i (TYPE): Description

    Returns:
        TYPE: Description
    """
    if type(i) != float or pd.isna(i):
        return i
    else:
        return int(i)


def try_to_datetime(ts):
    """Tries to convert a unix timestamp to a python datetime object

    Args:
        ts (TYPE): unix timestamp

    Returns:
        TYPE: datetime of original object
    """
    try:
        return datetime.utcfromtimestamp(int(ts)) if not pd.isnull(ts) else ts
    except ValueError:
        return ts


def try_parse_json(data):
    """Summary

    Args:
        data (TYPE): Description

    Returns:
        TYPE: Description
    """
    if type(data) == str and (
        data.strip().startswith("[") or data.strip().startswith("{")
    ):
        # TODO: csv api encodes json data with single quotes which is invalid.
        # this code will fail if data contains other single quotes.
        for x in ["[" + data.replace("'", '"') + "]", data.replace("'", '"')]:
            try:
                return json.loads(x)
            except (json.JSONDecodeError):
                continue
        return data
    else:
        return data


def resolve_timestamps(obj: Union[DataFrame, OpenApiModel, List[OpenApiModel]]):
    """Summary

    Args:
        obj (Union[DataFrame, OpenApiModel, List[OpenApiModel]]): Description

    Returns:
        TYPE: Description

    Raises:
        ValueError: Description
    """
    if isinstance(obj, DataFrame):
        for c in obj.columns:
            if c.endswith("timestamp"):
                obj[c.replace("timestamp", "date")] = obj[c].apply(try_to_datetime)
    elif isinstance(obj, ModelSimple):
        return obj
    elif isinstance(obj, OpenApiModel):
        for k in obj.to_dict().keys():
            if k.endswith("timestamp"):
                obj[k.replace("timestamp", "date")] = try_to_datetime(obj[k])
    elif isinstance(obj, list):
        return [resolve_timestamps(x) for x in obj]
    else:
        raise ValueError(
            f"Timestamps can't be automatically resolved for type {type(obj)}"
        )
    return obj


def throw_on_error(obj: Union[DataFrame, OpenApiModel, List[OpenApiModel]]):
    """Summary

    Args:
        obj (Union[DataFrame, OpenApiModel, List[OpenApiModel]]): Description

    Returns:
        TYPE: Description

    Raises:
        ValueError: Description
    """
    if isinstance(obj, DataFrame):
        if "_error" in obj.columns and any(obj["_error"].apply(pd.notnull)):
            raise ValueError(
                f"Some errors occurred while producing the return value. {obj['_error'].unique()}"
            )
        return obj
    elif isinstance(obj, ModelSimple):
        return obj
    elif isinstance(obj, OpenApiModel):
        if "_error" in obj.to_dict():
            raise ValueError(
                f"Some errors occurred while producing the return value: {obj['_error']}"
            )
    elif isinstance(obj, list):
        return [throw_on_error(x) for x in obj]
    else:
        raise ValueError(f"Can't interpret return value of type {type(obj)}")
    return obj


def strip_internal_fields(obj: Union[DataFrame, OpenApiModel, List[OpenApiModel]]):
    """Summary

    Args:
        obj (Union[DataFrame, OpenApiModel, List[OpenApiModel]]): Description

    Returns:
        TYPE: Description

    Raises:
        ValueError: Description
    """
    if isinstance(obj, DataFrame):
        return obj.drop(columns=[c for c in obj.columns if c.startswith("_")])
    elif isinstance(obj, ModelSimple):
        return obj
    elif isinstance(obj, OpenApiModel):
        for k in obj.to_dict().keys():
            if k.startswith("_"):
                del obj[k]
    elif isinstance(obj, list):
        return [strip_internal_fields(x) for x in obj]
    else:
        raise ValueError(f"Can't interpret return value of type {type(obj)}")
    return obj


def strip_internal_all_nan_fields(
    obj: Union[DataFrame, OpenApiModel, List[OpenApiModel]]
):
    """Summary

    Args:
        obj (Union[DataFrame, OpenApiModel, List[OpenApiModel]]): Description

    No Longer Returned:
        TYPE: Description

    No Longer Raises:
        ValueError: Description
    """
    if isinstance(obj, DataFrame):
        nc = [c for c in obj.columns if c.startswith("_") and pd.isnull(obj[c]).all()]
        return obj.drop(columns=nc)
    elif isinstance(obj, ModelSimple):
        return obj
    elif isinstance(obj, OpenApiModel):
        return obj
    elif isinstance(obj, list):
        return obj
    else:
        raise ValueError(f"Can't interpret return value of type {type(obj)}")
    return obj


def entityId_to_int(obj: Union[DataFrame, OpenApiModel, List[OpenApiModel]]):
    """Summary

    Args:
        obj (Union[DataFrame, OpenApiModel, List[OpenApiModel]]): Description

    Returns:
        TYPE: Description

    Raises:
        ValueError: Description
    """
    if isinstance(obj, DataFrame):
        for c in obj.columns:
            if "entity" == c:
                obj[c] = obj[c].apply(try_to_int)
    elif isinstance(obj, ModelSimple):
        return obj
    elif isinstance(obj, OpenApiModel):
        if "entity" in obj.to_dict() and type(obj["entity"]) == float:
            obj["entity"] = try_to_int(obj["entity"])
    elif isinstance(obj, list):
        return [entityId_to_int(x) for x in obj]
    else:
        raise ValueError(f"Can't interpret return value of type {type(obj)}")
    return obj


def parse_json_columns(obj: Union[DataFrame, OpenApiModel, List[OpenApiModel]]):
    """Summary

    Args:
        obj (Union[DataFrame, OpenApiModel, List[OpenApiModel]]): Description

    Returns:
        TYPE: Description

    Raises:
        ValueError: Description
    """
    if isinstance(obj, DataFrame):
        for c in obj.columns:
            obj[c] = obj[c].apply(try_parse_json)
    elif isinstance(obj, ModelSimple):
        return obj
    elif isinstance(obj, OpenApiModel):
        for k in obj.to_dict().keys():
            obj[k] = try_parse_json(obj[k])
    elif isinstance(obj, list):
        return [entityId_to_int(x) for x in obj]
    else:
        raise ValueError(f"Can't interpret return value of type {type(obj)}")
    return obj


class Api:

    """Helper class to quickly create graphsense api requests with different output formats.

    Attributes:
        api_client (TYPE): Description
        return_transformation_functions (TYPE): Description
    """

    def __init__(self, api_key, host=None):
        """Summary

        Args:
            api_key (TYPE): Description
            host (None, optional): Description
        """
        self.api_client = ApiClient(
            Configuration(api_key={"api_key": api_key}, host=host)
        )
        self.return_transformation_functions = [
            resolve_timestamps,
            parse_json_columns,
            strip_internal_all_nan_fields,
            entityId_to_int,
        ]

    def _change_return_transformation(self, nf, activate=True):
        """Summary

        Args:
            nf (TYPE): Description
            activate (bool, optional): Description

        Returns:
            TYPE: Description
        """
        self.return_transformation_functions = [
            f for f in self.return_transformation_functions if f != nf
        ]
        if activate:
            self.return_transformation_functions += [nf]
        return self

    def throw_on_error(self, activate=True):
        """Summary

        Args:
            activate (bool, optional): Description

        Returns:
            TYPE: Description
        """
        return self._change_return_transformation(throw_on_error, activate)

    def entityId_to_int(self, activate=True):
        """Summary

        Args:
            activate (bool, optional): Description

        Returns:
            TYPE: Description
        """
        return self._change_return_transformation(entityId_to_int, activate)

    def strip_internal_fields(self, activate=True):
        """Summary

        Args:
            activate (bool, optional): Description

        Returns:
            TYPE: Description
        """
        return self._change_return_transformation(strip_internal_fields, activate)

    def parse_json_columns(self, activate=True):
        """Summary

        Args:
            activate (bool, optional): Description

        Returns:
            TYPE: Description
        """
        return self._change_return_transformation(parse_json_columns, activate)

    def _run_return_transformations(self, obj):
        """Summary

        Args:
            obj (TYPE): Description

        Returns:
            TYPE: Description
        """
        r = obj
        for f in self.return_transformation_functions:
            r = f(r)
        return r

    def __enter__(self):
        """Summary

        Returns:
            TYPE: Description
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Summary

        Args:
            exc_type (TYPE): Description
            exc_value (TYPE): Description
            traceback (TYPE): Description
        """
        if self.api_client:
            self.api_client.close()
            self.api_client = None

    @cached_property
    def block(self) -> "BlockApi":
        """Summary

        Returns:
            BlockApi: Description
        """
        return BlockApi(self)

    @cached_property
    def address(self) -> "AddressApi":
        """Summary

        Returns:
            AddressApi: Description
        """
        return AddressApi(self)

    @cached_property
    def cluster(self) -> "ClusterApi":
        """Query cluster information

        Returns:
            ClusterApi: Description
        """
        return ClusterApi(self)

    @cached_property
    def rates(self) -> "RatesApi":
        """Summary

        Returns:
            RatesApi: Description
        """
        return RatesApi(self)

    @cached_property
    def tags(self) -> "TagsApi":
        """Summary

        Returns:
            TagsApi: Description
        """
        return TagsApi(self)

    @cached_property
    def general(self) -> "GeneralApi":
        """Summary

        Returns:
            GeneralApi: Description
        """
        return GeneralApi(self)

    @cached_property
    def txs(self) -> "TxApi":
        """Summary

        Returns:
            TxApi: Description
        """
        return TxApi(self)


class TxApi:

    """Query general information

    Attributes:
        api_frontend (Api): Description
    """

    def __init__(self, api: Api):
        """Summary

        Args:
            api (Api): Description
        """
        self.api_frontend = api
        self._api = apis.TxsApi(self.api_frontend.api_client)
        self._bulk_api = apis.BulkApi(self.api_frontend.api_client)

    def get_as_df(
        self, currency: str, tx_hash: Union[str, List[str]], **kwargs
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            tx_hash (Union[str, List[str]]): Description
            **kwargs: Description

        Deleted Parameters:
            height (Union[int, List[int]]): Description

        No Longer Returned:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "get_tx",
                {"tx_hash": ensure_list(tx_hash), **kwargs},
            )
        )

    def get(self, currency: str, tx_hash: str, **kwargs) -> models.Tx:
        """Summary

        Args:
            currency (str): Description
            tx_hash (str): Description
            **kwargs: Description

        Returns:
            models.Tx: Description

        Deleted Parameters:
            height (int): Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_tx(currency, tx_hash, **kwargs)
        )

    def inputs(self, currency: str, tx_hash: str) -> models.TxValues:
        """Summary

        Args:
            currency (str): Description
            tx_hash (str): Description

        Returns:
            models.TxValues: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_tx_io(currency, tx_hash, io="inputs")
        )

    def outputs(self, currency: str, tx_hash: str) -> models.TxValues:
        """Summary

        Args:
            currency (str): Description
            tx_hash (str): Description

        Returns:
            models.TxValues: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_tx_io(currency, tx_hash, io="outputs")
        )


class TagsApi:

    """Query general information

    Attributes:
        api_frontend (Api): Description
    """

    def __init__(self, api: Api):
        """Summary

        Args:
            api (Api): Description
        """
        self.api_frontend = api
        self._api = apis.TagsApi(self.api_frontend.api_client)

    def get(self, label: str, **kwargs) -> models.AddressTags:
        """Summary

        Args:
            label (str): Description
            **kwargs: Description

        Returns:
            models.AddressTags: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_address_tags(label, **kwargs)
        )

    def get_as_df(self, label: str, **kwargs) -> models.AddressTags:
        """Summary

        Args:
            label (str): Description
            **kwargs: Description

        Returns:
            models.AddressTags: Description
        """
        pagesize = kwargs.get("pagesize", 1000)
        np = None
        df = pd.DataFrame()
        while True:
            ret = (
                self._api.list_address_tags(label, page=np, pagesize=pagesize)
                if np
                else self._api.list_address_tags(label, pagesize=pagesize)
            )
            df = pd.concat([df, pd.DataFrame(ret.to_dict().get("address_tags", []))])
            if "next_page" in ret:
                np = ret["next_page"]
            else:
                break

        return self.api_frontend._run_return_transformations(df)

    def actor(self, actor_id) -> models.Actor:
        """Summary

        Returns:
            models.Actor: Description

        Deleted Parameters:
            currency (str): Description
            height (int): Description

        Args:
            actor_id (TYPE): Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_actor(actor_id)
        )

    def actor_tags(self, actor_id, **kwargs) -> models.AddressTags:
        """Summary

        Returns:
            models.AddressTags: Description

        Deleted Parameters:
            currency (str): Description
            height (int): Description

        Args:
            actor_id (TYPE): Description
            **kwargs: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_actor_tags(actor_id, **kwargs)
        )

    def actor_tags_as_df(self, actor_id, **kwargs) -> models.AddressTags:
        """Summary

        Returns:
            models.AddressTags: Description

        Deleted Parameters:
            currency (str): Description
            height (int): Description

        Args:
            actor_id (TYPE): Description
            **kwargs: Description
        """
        pagesize = kwargs.get("pagesize", 1000)
        np = None
        df = pd.DataFrame()
        while True:
            ret = (
                self._api.get_actor_tags(actor_id, page=np, pagesize=pagesize)
                if np
                else self._api.get_actor_tags(actor_id, pagesize=pagesize)
            )
            df = pd.concat([df, pd.DataFrame(ret.to_dict().get("address_tags", []))])
            if "next_page" in ret:
                np = ret["next_page"]
            else:
                break

        return self.api_frontend._run_return_transformations(df)

    def concepts_as_df(self, taxonomy: str) -> DataFrame:
        """Summary

        Args:
            taxonomy (str): Description

        Returns:
            DataFrame: Description
        """
        return pd.DataFrame([x.to_dict() for x in self.concepts(taxonomy)])

    def concepts(self, taxonomy: str) -> List[models.Concept]:
        """Summary

        Args:
            taxonomy (str): Description

        Returns:
            List[models.Concept]: Description

        Deleted Parameters:
            label (str): Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_concepts(taxonomy)
        )

    def taxonomies_as_df(self) -> DataFrame:
        """Summary

        Returns:
            DataFrame: Description
        """
        return pd.DataFrame([x.to_dict() for x in self.taxonomies()])

    def taxonomies(self) -> List[models.Taxonomy]:
        """Summary

        Returns:
            List[models.Taxonomy]: Description

        Deleted Parameters:
            label (str): Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_taxonomies()
        )


class GeneralApi:

    """Query general information

    Attributes:
        api_frontend (Api): Description
    """

    def __init__(self, api: Api):
        """Summary

        Args:
            api (Api): Description
        """
        self.api_frontend = api
        self._api = apis.GeneralApi(self.api_frontend.api_client)
        self._tokens_api = apis.TokensApi(self.api_frontend.api_client)

    def statistics_as_df(self) -> DataFrame:
        """Summary

        Returns:
            DataFrame: Description

        Deleted Parameters:
            currency (str): Description
            height (Union[int, List[int]]): Description
        """
        x = pd.DataFrame(self.statistics().to_dict())
        currency_stats = pd.json_normalize(x["currencies"])
        return self.api_frontend._run_return_transformations(
            pd.concat([x.drop(columns=["currencies"]), currency_stats], axis=1)
        )

    def statistics(self) -> models.Stats:
        """Summary

        Returns:
            models.Stats: Description

        Deleted Parameters:
            currency (str): Description
            height (int): Description
        """
        return self.api_frontend._run_return_transformations(self._api.get_statistics())

    def search(self, query: str, **kwargs) -> models.SearchResult:
        """Summary

        Returns:
            models.SearchResult: Description

        Deleted Parameters:
            currency (str): Description
            height (int): Description

        Args:
            query (str): Description
            **kwargs: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.search(query, **kwargs)
        )

    def supported_tokens(self, currency: str) -> models.TokenConfigs:
        """Summary

        Args:
            currency (str): Description

        Returns:
            models.TokenConfigs: Description
        """
        return self.api_frontend._run_return_transformations(
            self._tokens_api.list_supported_tokens(currency)
        )

    def supported_tokens_as_df(self, currency: str) -> DataFrame:
        """Summary

        Args:
            currency (str): Description

        Returns:
            DataFrame: Description
        """
        df = pd.DataFrame(
            self._tokens_api.list_supported_tokens(currency)
            .to_dict()
            .get("token_configs", [])
        )

        return self.api_frontend._run_return_transformations(df)


class RatesApi:

    """Query exchange rate data

    Attributes:
        api_frontend (Api): Description
    """

    def __init__(self, api: Api):
        """Summary

        Args:
            api (Api): Description
        """
        self.api_frontend = api
        self._api = apis.RatesApi(self.api_frontend.api_client)
        self._bulk_api = apis.BulkApi(self.api_frontend.api_client)

    def get_as_df(self, currency: str, height: Union[int, List[int]]) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            height (Union[int, List[int]]): Description

        Returns:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "get_exchange_rates",
                {"height": ensure_list(height)},
            )
        )

    def get(self, currency: str, height: int) -> models.Rates:
        """Summary

        Args:
            currency (str): Description
            height (int): Description

        Returns:
            models.Rates: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_exchange_rates(currency, height)
        )


class BlockApi:

    """Query block data

    Attributes:
        api_frontend (Api): Description
    """

    def __init__(self, api: Api):
        """Summary

        Args:
            api (Api): Description
        """
        self.api_frontend = api
        self._api = apis.BlocksApi(self.api_frontend.api_client)
        self._bulk_api = apis.BulkApi(self.api_frontend.api_client)

    def get_as_df(self, currency: str, height: Union[int, List[int]]) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            height (Union[int, List[int]]): Description

        Returns:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api, currency, "get_block", {"height": ensure_list(height)}
            )
        )

    def get(self, currency: str, height: int) -> models.Block:
        """Summary

        Args:
            currency (str): Description
            height (int): Description

        Returns:
            models.Block: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_block(currency, height)
        )

    def txs_as_df(self, currency: str, height: Union[int, List[str]]) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            height (Union[int, List[str]]): Description

        Returns:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_block_txs",
                {"height": ensure_list(height)},
            )
        )

    def txs(self, currency: str, height: int) -> List[models.Tx]:
        """Summary

        Args:
            currency (str): Description
            height (int): Description

        Returns:
            List[models.Tx]: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_block_txs(currency, height)
        )


class ClusterApi:

    """Summary

    Attributes:
        api_frontend (TYPE): Description
    """

    def __init__(self, api: Api):
        """Summary

        Args:
            api (Api): Description
        """
        self.api_frontend = api
        self._api = apis.EntitiesApi(self.api_frontend.api_client)
        self._bulk_api = apis.BulkApi(self.api_frontend.api_client)

    def get_as_df(
        self, currency: str, eid: Union[int, List[int]], **kwargs
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (Union[int, List[int]]): Description
            **kwargs: Description

        Deleted Parameters:
            exclude_best_address_tag (bool, optional): Description
            include_actors (bool, optional): Description

        No Longer Returned:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "get_entity",
                {"entity": ensure_list(eid), **kwargs},
            )
        )

    def get(self, currency: str, eid: int, **kwargs) -> models.Entity:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description

        Returns:
            models.Entity: Description

        Deleted Parameters:
            exclude_best_address_tag (bool, optional): Description
            include_actors (bool, optional): Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_entity(currency, eid, **kwargs)
        )

    def tags_as_df(self, currency: str, eid: Union[int, List[int]]) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (Union[int, List[int]]): Description

        Returns:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_address_tags_by_entity",
                {"entity": ensure_list(eid)},
            )
        )

    def tags(self, currency: str, eid: int, **kwargs) -> models.AddressTags:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description

        Returns:
            models.AddressTags: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_address_tags_by_entity(currency, eid)
        )

    def addresses_as_df(self, currency: str, eid: Union[int, List[int]]) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (Union[int, List[int]]): Description

        Returns:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_entity_addresses",
                {"entity": ensure_list(eid)},
            )
        )

    def addresses(self, currency: str, eid: int, **kwargs) -> models.EntityAddresses:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description

        Returns:
            models.EntityAddresses: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_entity_addresses(currency, eid, **kwargs)
        )

    def links_as_df(
        self, currency: str, eid: Union[int, List[int]], neighbor: Union[int, List[int]]
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (Union[int, List[int]]): Description
            neighbor (Union[int, List[int]]): Description

        No Longer Returned:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_entity_links",
                {"entity": ensure_list(eid), "neighbor": ensure_list(neighbor)},
            )
        )

    def links(
        self, currency: str, eid: int, neighbor: int, **kwargs
    ) -> models.EntityAddresses:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            neighbor (int): Description
            **kwargs: Description

        No Longer Returned:
            models.EntityAddresses: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_entity_links(currency, eid, neighbor, **kwargs)
        )

    def incoming_neighbors_as_df(
        self, currency: str, eid: Union[int, List[int]]
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (Union[int, List[int]]): Description
        """
        return self.neighbors_as_df(currency, eid, "in")

    def outgoing_neighbors_as_df(
        self, currency: str, eid: Union[int, List[int]]
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (Union[int, List[int]]): Description
        """
        return self.neighbors_as_df(currency, eid, "out")

    def neighbors_as_df(
        self, currency: str, eid: Union[int, List[int]], direction: str, **kwargs
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (Union[int, List[int]]): Description
            direction (str): Description
            **kwargs: Description

        No Longer Returned:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_entity_neighbors",
                {"entity": ensure_list(eid), "direction": direction, **kwargs},
            )
        )

    def incoming_neighbors(
        self, currency: str, eid: int, **kwargs
    ) -> models.NeighborEntities:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description
        """
        return self.neighbors(currency, eid, "in", **kwargs)

    def outgoing_neighbors(
        self, currency: str, eid: int, **kwargs
    ) -> models.NeighborEntities:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description
        """
        return self.neighbors(currency, eid, "in", **kwargs)

    def neighbors(
        self, currency: str, eid: int, direction: str, **kwargs
    ) -> models.NeighborEntities:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            direction (str): Description
            **kwargs: Description

        No Longer Returned:
            models.NeighborEntities: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_entity_neighbors(currency, eid, direction, **kwargs)
        )

    def incoming_txs_as_df(self, currency: str, eid: int, **kwargs) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description

        Returns:
            DataFrame: Description
        """
        na = {**kwargs, **{"direction": "in"}}
        return self.txs_as_df(currency, eid, **na)

    def outgoing_txs_as_df(self, currency: str, eid: int, **kwargs) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description

        Returns:
            DataFrame: Description
        """
        na = {**kwargs, **{"direction": "out"}}
        return self.txs_as_df(currency, eid, **na)

    def txs_as_df(self, currency: str, eid: int, **kwargs) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description

        Returns:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_entity_txs",
                {"entity": ensure_list(eid), **kwargs},
            )
        )

    def incoming_txs(self, currency: str, eid: int, **kwargs) -> models.AddressTxs:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description

        Returns:
            models.AddressTxs: Description
        """
        kwargs["direction"] = "in"
        return self.txs(currency, eid, **kwargs)

    def outgoing_txs(self, currency: str, eid: int, **kwargs) -> models.AddressTxs:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description

        Returns:
            models.AddressTxs: Description
        """
        kwargs["direction"] = "out"
        return self.txs(currency, eid, **kwargs)

    def txs(self, currency: str, eid: int, **kwargs) -> models.AddressTxs:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description

        Returns:
            models.AddressTxs: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_entity_txs(currency, eid, **kwargs)
        )


class AddressApi:

    """Summary

    Attributes:
        api_frontend (TYPE): Description
    """

    def __init__(self, api: Api):
        """Summary

        Args:
            api (Api): Description
        """
        self.api_frontend = api
        self._api = apis.AddressesApi(self.api_frontend.api_client)
        self._bulk_api = apis.BulkApi(self.api_frontend.api_client)

    def get_as_df(self, currency: str, address: Union[str, List[str]]) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (Union[str, List[str]]): Description

        Deleted Parameters:
            exclude_best_address_tag (bool, optional): Description
            include_actors (bool, optional): Description
            eid (Union[int, List[int]]): Description
            **kwargs: Description

        No Longer Returned:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "get_address",
                {"address": ensure_list(address)},
            )
        )

    def get(self, currency: str, address: str) -> models.Address:
        """Summary

        Args:
            currency (str): Description
            address (str): Description

        Returns:
            models.Address: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_address(currency, address)
        )

    def cluster_as_df(self, currency: str, address: Union[str, List[str]]) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (Union[str, List[str]]): Description

        Returns:
            DataFrame: Description

        Deleted Parameters:
            eid (Union[int, List[str]]): Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "get_address_entity",
                {"address": ensure_list(address)},
            )
        )

    def cluster(self, currency: str, address: str) -> models.Entity:
        """Summary

        Args:
            currency (str): Description
            address (str): Description

        Returns:
            models.Entity: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.get_address_entity(currency, address)
        )

    def tags_as_df(self, currency: str, address: Union[str, List[str]]) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (Union[str, List[str]]): Description

        Returns:
            DataFrame: Description

        Deleted Parameters:
            eid (Union[int, List[str]]): Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_tags_by_address",
                {"address": ensure_list(address)},
            )
        )

    def tags(self, currency: str, address: str, **kwargs) -> models.AddressTags:
        """Summary

        Args:
            currency (str): Description
            address (str): Description
            **kwargs: Description

        Returns:
            models.AddressTags: Description

        Deleted Parameters:
            eid (int): Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_tags_by_address(currency, address)
        )

    def links_as_df(
        self,
        currency: str,
        address: Union[str, List[str]],
        neighbor: Union[str, List[str]],
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (Union[str, List[str]]): Description
            neighbor (Union[str, List[str]]): Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_address_links",
                {"address": ensure_list(address), "neighbor": ensure_list(neighbor)},
            )
        )

    def links(
        self, currency: str, address: str, neighbor: str, **kwargs
    ) -> models.Links:
        """Summary

        Args:
            currency (str): Description
            address (str): Description
            neighbor (str): Description
            **kwargs: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_address_links(currency, address, neighbor, **kwargs)
        )

    def incoming_neighbors_as_df(
        self, currency: str, address: Union[str, List[str]]
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (Union[str, List[str]]): Description
        """
        return self.neighbors_as_df(currency, address, "in")

    def outgoing_neighbors_as_df(
        self, currency: str, address: Union[str, List[str]]
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (Union[str, List[str]]): Description
        """
        return self.neighbors_as_df(currency, address, "out")

    def neighbors_as_df(
        self, currency: str, address: Union[str, List[str]], direction: str, **kwargs
    ) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (Union[str, List[str]]): Description
            direction (str): Description
            **kwargs: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_address_neighbors",
                {"address": ensure_list(address), "direction": direction, **kwargs},
            )
        )

    def incoming_neighbors(
        self, currency: str, address: str, **kwargs
    ) -> models.NeighborAddresses:
        """Summary

        Args:
            currency (str): Description
            address (str): Description
            **kwargs: Description
        """
        return self.neighbors(currency, address, "in", **kwargs)

    def outgoing_neighbors(
        self, currency: str, eid: int, **kwargs
    ) -> models.NeighborAddresses:
        """Summary

        Args:
            currency (str): Description
            eid (int): Description
            **kwargs: Description
        """
        return self.neighbors(currency, eid, "in", **kwargs)

    def neighbors(
        self, currency: str, address: str, direction: str, **kwargs
    ) -> models.NeighborAddresses:
        """Summary

        Args:
            currency (str): Description
            address (str): Description
            direction (str): Description
            **kwargs: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_address_neighbors(currency, address, direction, **kwargs)
        )

    def incoming_txs_as_df(self, currency: str, address: str, **kwargs) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (str): Description
            **kwargs: Description

        Returns:
            DataFrame: Description
        """
        na = {**kwargs, **{"direction": "in"}}
        return self.txs_as_df(currency, address, **na)

    def outgoing_txs_as_df(self, currency: str, address: str, **kwargs) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (str): Description
            **kwargs: Description

        Returns:
            DataFrame: Description
        """
        na = {**kwargs, **{"direction": "out"}}
        return self.txs_as_df(currency, address, **na)

    def txs_as_df(self, currency: str, address: str, **kwargs) -> DataFrame:
        """Summary

        Args:
            currency (str): Description
            address (address): Description
            **kwargs: Description

        Returns:
            DataFrame: Description
        """
        return self.api_frontend._run_return_transformations(
            get_df_bulk(
                self._bulk_api,
                currency,
                "list_address_txs",
                {"address": ensure_list(address), **kwargs},
            )
        )

    def incoming_txs(self, currency: str, address: str, **kwargs) -> models.AddressTxs:
        """Summary

        Args:
            currency (str): Description
            address (str): Description
            **kwargs: Description

        Returns:
            models.AddressTxs: Description
        """
        kwargs["direction"] = "in"
        return self.txs(currency, address, **kwargs)

    def outgoing_txs(self, currency: str, address: str, **kwargs) -> models.AddressTxs:
        """Summary

        Args:
            currency (str): Description
            address (str): Description
            **kwargs: Description

        Returns:
            models.AddressTxs: Description
        """
        kwargs["direction"] = "out"
        return self.txs(currency, address, **kwargs)

    def txs(self, currency: str, address: str, **kwargs) -> models.AddressTxs:
        """Summary

        Args:
            currency (str): Description
            address (str): Description
            **kwargs: Description

        Returns:
            models.AddressTxs: Description
        """
        return self.api_frontend._run_return_transformations(
            self._api.list_address_txs(currency, address, **kwargs)
        )
