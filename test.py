import filecmp

import pytest

import generate

def test_alarm_files():
    test_dpath = './tests/out/alarm.db'
    test_cpath = './tests/out/alarm-config.xml'

    generate.generate(total=16, area=2, sgroup=2, ssgroup=2, agroup=4, rate='.2 second', count=100, dbpath=test_dpath, confpath=test_cpath)

    assert filecmp.cmp('./tests/alarm-config.xml', test_cpath)
    assert filecmp.cmp('./tests/alarm.db', test_dpath)

def test_alarm_files_without_latch():
    test_dpath = './tests/out/alarm-wo-latch.db'
    test_cpath = './tests/out/alarm-config-wo-latch.xml'

    generate.generate(total=16, area=2, sgroup=2, ssgroup=2, agroup=4, rate='.2 second', count=100, dbpath=test_dpath, confpath=test_cpath, latch=False)

    assert filecmp.cmp('./tests/alarm-config-wo-latch.xml', test_cpath)
    assert filecmp.cmp('./tests/alarm.db', test_dpath)
