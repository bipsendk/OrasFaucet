from __future__ import annotations

import logging
import struct
import codecs

from bluetooth_data_tools import short_address
from bluetooth_sensor_state_data import BluetoothData
from home_assistant_bluetooth import BluetoothServiceInfo
from sensor_state_data import DeviceClass, Units

from .const import COMPANY_IDENTIFIER

_LOGGER = logging.getLogger(__name__)


def _convert_advertisement(
    raw_data: bytes,
) -> tuple[str | None, dict[tuple[DeviceClass, Units], float]] | None:
    """
    Convert a Oras advertisement to a dictionary of sensor values.
    """
    if raw_data[-5:] == b"\x00\x20\x20\x20\x20":  # Last 5 bytes Seems to be static "0x0020202020"
        val = raw_data.hex()

        # https://gitlab.com/baze/amphiro_oras_bluetooth_shower_hub/-/blob/main/read_Ampiro_shower.py#L109
        # Construct v1 containing spaced out representation of the raw data
        v1 = ""
        BatteryPct = int(val[2:4],16)
        v1 += str(val)[2:4] + " "

        serialNo = str(val)[6:26]
        v1 += str(val)[6:26] + " "

        data = {};
        data["battery_pct"]=BatteryPct
        data["serial"]=serialNo
        data = {
            (DeviceClass.BATTERY,Units.PERCENTAGE):BatteryPct
        }
        _LOGGER.debug(v1)
        return data
    _LOGGER.error("ORAS data format not supported: %s", raw_data)

    return None


class OrasBluetoothDeviceData(BluetoothData):
    """Data for Oras BLE sensors."""

    def _start_update(self, service_info: BluetoothServiceInfo) -> None:
        try:
            raw_data = service_info.manufacturer_data[COMPANY_IDENTIFIER]
        except (KeyError, IndexError):
            _LOGGER.debug("Manufacturer ID not found in data")
            return None

        result = _convert_advertisement(raw_data)
        if result is None:
            return
        val = raw_data.hex()
        serial_hex = str(val)[6:26]
        serial = codecs.decode(serial_hex,"hex").decode("ASCII")
        self.set_device_type(f"ORAS Faucet")
        self.set_device_manufacturer("ORAS")
        identifier = short_address(service_info.address)
        self.set_device_name(f"{service_info.name} {serial}")
        for (device_class, unit), value in result.items():
            self.update_sensor(
                key=device_class,
                device_class=device_class,
                native_unit_of_measurement=unit,
                native_value=value,
            )
