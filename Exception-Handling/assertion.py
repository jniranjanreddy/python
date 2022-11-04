age = 20
try: 
    assert age<30
    print("valid Age")
except AssertionError:
    print("raised with assert bcoz age is less than 30")
except:
    print("Exception Occures")