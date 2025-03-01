#!/usr/bin/env python3
import sys

import func
import pytest

print(sys.version_info)
func.FUNC_OM("Sita")

@pytest.mark.skip
def test_skip():
    assert True

@pytest.mark.skipif(sys.version_info>(2,5),reason="Python Version not supported")
def test_skipIF():
    print("Python version Matched")
    assert True

@pytest.mark.xfail
def test_mark_xfail():
    assert True

@pytest.mark.xfail
def test_mark_xpass():
    assert False

@pytest.mark.smoke
def test_always_passes():
    assert True
    
@pytest.mark.regression
def test_always_fails():
    assert True

@pytest.mark.smoke
def test_str():
    name = "Jenkins"
    title = "Jenkins is a CI/CD Tool."
    assert name in title , "Title Doesnt match"