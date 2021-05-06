# hacs-Crypto-aggregator

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

An attempt to aggregate Crypto wallet balance and unpaid pool balance from various source
and A integration with [Minerstart](https://minerstat.com/) to create a sensor from your rig's hashrate.

## Usage
`configuration.yaml`:
```yaml
sensor:
  - platform: hacs-minerstat
    name: "My Awesome Rig"
    access_key: "00000000"
    rig_name: "RIG1"
```

## Options
|Name|Type|Necessity|Default|Description|
|----|:--:|:-------:|:-----:|-----------|
|`platform`|string|**Required**|`hacs-minerstat`|The platform name|
|`access_key`|string|**Required**||Your personal access key from https://my.minerstat.com/|
|`rig_name`|string|**Required**||The name that you defined for your rig at Minerstat|
|`name`|string|Optional|`Minerstat`|Custom name for the sensor|

## Support this project
From parent project ! hacs minterstat
**Buy me a ~~coffee~~ beer 🍺**: https://www.buymeacoffee.com/gilson

**BTC**: 33TwXHzMTpSNMJZ4JcwExLExsF3BshBUPE

**ETH**: 0xa772c6bab9d175256ff635843c461d3f65a7236b

**LTC**: M9adpiNQXsbEf7j5ZVnuDCGNoXT7oMW3vd
