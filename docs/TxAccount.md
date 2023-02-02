# TxAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | crypto currency code | 
**from_address** | **str** | Address | 
**height** | [**Height**](Height.md) |  | 
**timestamp** | **int** | Timestamp | 
**to_address** | **str** | Address | 
**tx_hash** | **str** | Transaction hash | 
**value** | [**Values**](Values.md) |  | 
**tx_type** | **str** |  | defaults to "account"
**contract_creation** | **bool** | Indicates if this transaction created a new contract. Recipient address is the address of the new contract. | [optional] 
**token_tx_id** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


