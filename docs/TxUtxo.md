# TxUtxo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | crypto currency code | 
**tx_hash** | **str** | Transaction hash | 
**coinbase** | **bool** | Coinbase transaction flag | 
**height** | [**Height**](Height.md) |  | 
**no_inputs** | **int** | number of input addresses | 
**no_outputs** | **int** | number of output addresses | 
**timestamp** | **int** | Timestamp in posix seconds format | 
**total_input** | [**Values**](Values.md) |  | 
**total_output** | [**Values**](Values.md) |  | 
**tx_type** | **str** |  | defaults to "utxo"
**inputs** | [**TxValues**](TxValues.md) |  | [optional] 
**outputs** | [**TxValues**](TxValues.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


