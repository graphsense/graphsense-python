# Tx


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_type** | **str** |  | defaults to "account"
**inputs** | [**TxValues**](TxValues.md) |  | [optional] 
**outputs** | [**TxValues**](TxValues.md) |  | [optional] 
**token_tx_id** | **int** | identifies a specific token transaction within a tx_hash, (deprecated) use identifier instead in encapsulates all information that uniquely identifies the transaction | [optional] 
**contract_creation** | **bool** | Indicates if this transaction created a new contract. Recipient address is the address of the new contract. | [optional] 
**currency** | **str** | crypto currency code | [optional] 
**tx_hash** | **str** | Transaction hash | [optional] 
**coinbase** | **bool** | Coinbase transaction flag | [optional] 
**height** | [**Height**](Height.md) |  | [optional] 
**no_inputs** | **int** | number of input addresses | [optional] 
**no_outputs** | **int** | number of output addresses | [optional] 
**timestamp** | **int** | Timestamp in posix seconds format | [optional] 
**total_input** | [**Values**](Values.md) |  | [optional] 
**total_output** | [**Values**](Values.md) |  | [optional] 
**identifier** | **str** | uniquely identifies a transaction or a sub transaction like a token transaction or trace. | [optional] 
**network** | **str** | crypto currency code | [optional] 
**value** | [**Values**](Values.md) |  | [optional] 
**from_address** | **str** | Address | [optional] 
**to_address** | **str** | Address | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


