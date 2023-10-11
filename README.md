# OrasFaucet
Home Assistant custom component to intercept Bluetooth BLE announcements from Oras Faucet

Place the content of this folder in a folder named oras_faucet in your custom_components folder, and restart HomeAssistant.
After that, let the BLE Proxy run, so it hopefully intercepts the announcement from the faucet - and then you should be able to add the integration

I am no python expert, and I used some code from another custom component (https://github.com/chkuendig/hass-amphiro-ble) to create this one.

This custom component will intercept BLE announcements made from Oras BLE enabled faucets, and register it with the serial number - and get the battery status (only thing announced together with the serial number)

You will need a BLE proxy or similar to get this data into HomeAssistant.
