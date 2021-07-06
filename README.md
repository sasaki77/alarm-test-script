# Alarm test script
## Requirements
```bash
pip install -r requirements.txt
```

## Usage
```bash
usage: generate.py [-h] [-t 50000] [-r .2 second] [-a 5] [-s 10] [-u 10] [-d 250] [-c 50000] [-o ./alarm.db] [-x ./alarm-config.xml]

optional arguments:
  -h, --help            show this help message and exit
  -t 50000, -total 50000
                        Total PVs
  -r .2 second, -rate .2 second
                        Ramp Scan Rate
  -a 5, -area 5         Number of Areas
  -s 10, -subgroup 10   Number of Sub Groups
  -u 10, -subsubgroup 10
                        Number of Sub Sub Groups
  -d 250, -dbgroup 250  Number of Groups for Alarm Record DB
  -c 50000, -count 50000
                        Number of Count for Ramp Record
  -o ./alarm.db, -out ./alarm.db
                        Output Path for DB
  -x ./alarm-config.xml, -xml ./alarm-config.xml
                        Output Path for XML
```

## Test
```bash
pip install pytest
pytest test.py
```
