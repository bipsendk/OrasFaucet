# OrasFaucet
Home Assistant custom component to intercept Bluetooth BLE announcements from Oras Faucet

Place the content of this folder in a folder named oras_faucet in your custom_components folder, and restart HomeAssistant.

I am no python expert, and I used some code from another custom component (https://github.com/chkuendig/hass-amphiro-ble) to create this one.

This custom component will intercept BLE announcements made from Oras BLE enabled faucets, and register it with the serial number - and get the battery status (only thing announced together with the serial number)

