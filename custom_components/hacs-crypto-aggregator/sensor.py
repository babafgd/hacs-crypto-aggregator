from homeassistant.helpers import entity
from homeassistant.components.sensor import PLATFORM_SCHEMA
from datetime import timedelta
import voluptuous as vol
import urllib.request, json
import homeassistant.helpers.config_validation as cv

__version__ = "1.1.0"

CONF_NAME = "name"
CONF_APIKEY = "api_key"
CONF_WALLET = "wallet"
CONF_CRYPTO = "crypto"
CONF_FIAT = "fiat"
DEFAULT_NAME = "ETH_balance"
DEFAULT_CRYPTO = "ETH"
DEFAULT_FIAT = "EUR"
DEFAULT_SCAN_INTERVAL = timedelta(minutes=15)
SCAN_INTERVAL = timedelta(minutes=15)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_WALLET): str,
        vol.Required(CONF_APIKEY): str,
        vol.Optional(CONF_CRYPTO, default=DEFAULT_CRYPTO): cv.string,
        vol.Optional(CONF_FIAT, default=DEFAULT_FIAT): cv.string,
    }
)


def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([Minerstat(hass, config)])


class Minerstat(entity.Entity):
    def __init__(self, hass, config):
        self.hass = hass
        self._config = config
        self._state = None
        self._unit = None
        self._status = None
        self.update()

    @property
    def name(self):
        return self._config[CONF_NAME]

    @property
    def icon(self):
        return "mdi:bitcoin"

    @property
    def state(self):
        return self._state

    def update(self):
        req = urllib.request.Request(
            f"https://api.ethplorer.io/getAddressInfo/{self._config[CONF_WALLET]}?apiKey={self._config[CONF_APIKEY]}",
            headers={"User-Agent": "Home-assistant.io"},
        )

        with urllib.request.urlopen(req) as url:
            data = json.loads(url.read().decode())

            self._state = data[self._config[CONF_CRYPTO]]["balance"]
            self._unit = self._config[CONF_CRYPTO]

    @property
    def device_state_attributes(self):
        return {"unit_of_measurement": self._unit, "status": self._status}
