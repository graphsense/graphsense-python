# TokenConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | ticker symbol of the currency e.g. USDT | 
**decimals** | **int** | the number of digits after the comma. Values are always delivered as integers. This value can be used to set the decimal point at the right place. | 
**peg_currency** | **str** | is set if token is a stablecoin. It holds the thicker symbol of the currency the tokens is pegged to. | [optional] 
**contract_address** | **str** | the contract address of the token on the blockchain. This is only set for tokens that are not native to the blockchain. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


