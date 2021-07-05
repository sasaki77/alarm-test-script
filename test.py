import filecmp

import pytest

import generate

def test_alarm_files():
    test_dpath = './tests/out/alarm.db'
    test_cpath = './tests/out/alarm-config.xml'

    generate.generate(total=2, group=2, rate='.2 second', count=100, dbpath=test_dpath, confpath=test_cpath)

    assert filecmp.cmp('./tests/alarm-config.xml', test_cpath)
    assert filecmp.cmp('./tests/alarm.db', test_dpath)
