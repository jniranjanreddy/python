#!/usr/bin/env python3
import pytest

@pytest.mark.smoke
def test_always_passes():
    assert True
    
# @pytest.mark.regression
# def test_always_fails():
#     assert True

# @pytest.mark.smoke
# def test_str():
#     name = "Jenkins"
#     title = "Jenkins is a CI/CD Tool."
#     assert name in title , "Title Doesnt match"