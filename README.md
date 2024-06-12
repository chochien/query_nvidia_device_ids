## query-nvidia-device_ids

The script is used to query nvidia device ids drivers readiness from nvidia.com 

## Usage
```
$ python query nvidia device_ids.py
Enter the driver version: 550.90.07
Enter the device ID: 28b9
Device ID 28B9 is supported by driver version 550.90.07.

$ python query nvidia device_ids.py
Enter the driver version: 550.90.07
Enter the device ID: 2999
Device ID 2999 is NOT supported by driver version 550.90.07.
