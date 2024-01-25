# Entity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | crypto currency code | 
**entity** | **int** | Entity id | 
**root_address** | **str** | Address | 
**balance** | [**Values**](Values.md) |  | 
**first_tx** | [**TxSummary**](TxSummary.md) |  | 
**last_tx** | [**TxSummary**](TxSummary.md) |  | 
**in_degree** | **int** |  | 
**out_degree** | **int** |  | 
**no_addresses** | **int** | number of contained addresses | 
**no_incoming_txs** | **int** |  | 
**no_outgoing_txs** | **int** |  | 
**total_received** | [**Values**](Values.md) |  | 
**total_spent** | [**Values**](Values.md) |  | 
**no_address_tags** | **int** | number of address tags | 
**token_balances** | [**TokenValues**](TokenValues.md) |  | [optional] 
**total_tokens_received** | [**TokenValues**](TokenValues.md) |  | [optional] 
**total_tokens_spent** | [**TokenValues**](TokenValues.md) |  | [optional] 
**actors** | [**LabeledItemRefs**](LabeledItemRefs.md) |  | [optional] 
**best_address_tag** | [**AddressTag**](AddressTag.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


