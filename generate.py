import pathlib
import argparse

from jinja2 import Environment, FileSystemLoader

def parseArgs():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-t', '-total', dest='total',
                        default=50000, help='Total PVs', metavar=50000,
                        type=int)
    parser.add_argument('-r', '-rate', dest='rate',
                        default='.2 second', help='Ramp Scan Rate',
                        metavar='.2 second')
    parser.add_argument('-a', '-area', dest='area',
                        default=5, help='Number of Areas',
                        metavar=5, type=int)
    parser.add_argument('-s', '-subgroup', dest='sgroup',
                        default=10, help='Number of Sub Groups',
                        metavar=10, type=int)
    parser.add_argument('-u', '-subsubgroup', dest='ssgroup',
                        default=10, help='Number of Sub Sub Groups',
                        metavar=10, type=int)
    parser.add_argument('-d', '-dbgroup', dest='dbgroup',
                        default=250, help='Number of Groups for Alarm Record DB',
                        metavar=250, type=int)
    parser.add_argument('-c', '-count', dest='count',
                        default=50000, help='Number of Count for Ramp Record',
                        metavar=50000, type=int)
    parser.add_argument('-l', '-latch', dest='latch',
                        help='Disable latching', action='store_false')
    parser.add_argument('-o', '-out', dest='out',
                        default='./alarm.db', help='Output Path for DB',
                        metavar='./alarm.db')
    parser.add_argument('-x', '-xml', dest='xml',
                        default='./alarm-config.xml',
                        help='Output Path for XML',
                        metavar='./alarm-config.xml')


    return parser.parse_args()

def checkdir(path):
    parent = path.parent
    if not parent.exists():
        parent.mkdir()

def generate(total, area, sgroup, ssgroup, agroup, rate, count, dbpath, confpath, latch=True):
    dpath = pathlib.Path(dbpath)
    cpath = pathlib.Path(confpath)

    checkdir(dpath)
    checkdir(cpath)

    env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
    tmpl_db = env.get_template('db.template')
    
    db = tmpl_db.render(total=total, group=agroup, rate=rate, count=count)
    
    with open(dpath, 'w') as f:
        f.write(db)
    
    tmpl_config = env.get_template('alarm-config.template')
    
    config = tmpl_config.render(total=total, area=area, sgroup=sgroup, ssgroup=ssgroup, latch=latch)
    
    with open(cpath, 'w') as f:
        f.write(config)

def main():
    args = parseArgs()

    total = args.total
    area = args.area
    sgroup = args.sgroup
    ssgroup = args.ssgroup
    dbgroup = args.dbgroup
    rate = args.rate
    count = args.count
    latch = args.latch
    dbpath = args.out
    confpath = args.xml

    generate(total, area, sgroup, ssgroup, dbgroup, rate, count, dbpath, confpath, latch)
    

if __name__ == '__main__':
    main()
