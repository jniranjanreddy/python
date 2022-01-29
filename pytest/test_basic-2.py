#!/usr/bin/env python3
import pytest
def test_always_passes():
    assert True

def test_always_fails():
    assert False
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]
