# TxAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | uniquely identifies a transaction or a sub transaction like a token transaction or trace. | 
**currency** | **str** | crypto currency code | 
**network** | **str** | crypto currency code | 
**tx_hash** | **str** | Transaction hash | 
**height** | [**Height**](Height.md) |  | 
**timestamp** | **int** | Timestamp in posix seconds format | 
**value** | [**Values**](Values.md) |  | 
**from_address** | **str** | Address | 
**to_address** | **str** | Address | 
**tx_type** | **str** |  | defaults to "account"
**token_tx_id** | **int** | identifies a specific token transaction within a tx_hash, (deprecated) use identifier instead in encapsulates all information that uniquely identifies the transaction | [optional] 
**contract_creation** | **bool** | Indicates if this transaction created a new contract. Recipient address is the address of the new contract. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


