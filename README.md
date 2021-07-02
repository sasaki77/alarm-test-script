# Alarm test script
## Requirements
```bash
pip install -r requirements.txt
```

## Usage
```bash
usage: generate.py [-h] [-t 50000] [-r .2 second] [-n 200] [-o ./alarm.db] [-x ./alarm-config.xml]

optional arguments:
  -h, --help            show this help message and exit
  -t 50000, -total 50000
                        Total PVs
  -r .2 second, -rate .2 second
                        Ramp Scan Rate
  -n 200, -number 200   Number of Count for Alarm
  -o ./alarm.db, -out ./alarm.db
                        Output Path for DB
  -x ./alarm-config.xml, -xml ./alarm-config.xml
                        Output Path for XML
```

## Demo files
Demo directory has default output files.
