# hacs-crypto-aggregator

An attempt to aggregate Crypto wallet balance and unpaid pool balance from various source :
- get Wallet balance from Etherscan
Support Ethermine pool wallet [Ethermine](https://ethermine.org/)

## Usage
`configuration.yaml`:
```yaml
sensor:
  - platform: hacs-crypto-aggregator
    name: "My ETH balance"
    api_key: "EK-vgDMJ-AehSCSu-Y59U5"
    wallet: "0x6450a23bcbca15b6baa385825ff9f091fda105bf"
    crypto : "ETH"
    fiat : "EUR"

```

## Options
|Name|Type|Necessity|Default|Description|
|----|:--:|:-------:|:-----:|-----------|
|`platform`|string|**Required**|`hacs-crypto-aggregator`|The platform name|
|`api_key`|string|**Required**||Your personal API key from https://my.etherscqn.io/|
|`wallet`|string|**Required**||The wallet address which you want to know the balance|
|`crypto`|string|Optional|`ETH`|Which Crypto is your wallet|
|`fiat`|string|Optional|`EUR`|In which fiat you want to convert the crypto wallet balance value|
|`name`|string|Optional|`Minerstat`|Custom name for the sensor|

## Support this project
From parent project ! hacs minterstat
**Buy me a ~~coffee~~ beer 🍺**: https://www.buymeacoffee.com/gilson

**BTC**: 33TwXHzMTpSNMJZ4JcwExLExsF3BshBUPE

**ETH**: 0xa772c6bab9d175256ff635843c461d3f65a7236b

**LTC**: M9adpiNQXsbEf7j5ZVnuDCGNoXT7oMW3vd
