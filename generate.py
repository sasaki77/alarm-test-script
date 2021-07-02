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
    parser.add_argument('-n', '-number', dest='number',
                        default=200, help='Number of Count for Alarm',
                        metavar=200, type=int)
    parser.add_argument('-o', '-out', dest='out',
                        default='./alarm.db', help='Output Path for DB',
                        metavar='./alarm.db')
    parser.add_argument('-x', '-xml', dest='xml',
                        default='./alarm-config.xml',
                        help='Output Path for XML',
                        metavar='./alarm-config.xml')


    return parser.parse_args()

def main():
    args = parseArgs()

    total = args.total
    n = args.number
    rate = args.rate
    
    env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
    tmpl_db = env.get_template('db.template')
    
    db = tmpl_db.render(total=total, n=n, rate=rate)
    
    with open(args.out, 'w') as f:
        f.write(db)
    
    tmpl_config = env.get_template('alarm-config.template')
    
    config = tmpl_config.render(total=total, n=n)
    
    with open(args.xml, 'w') as f:
        f.write(config)

if __name__ == '__main__':
    main()
