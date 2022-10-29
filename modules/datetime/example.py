# import datetime
from datetime import datetime
import pytz
# print(dir(datetime.datetime))
# print(help(datetime))
# print(datetime.datetime.today())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().isweekday)
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().strftime("%y-%m-%d"))
# print(datetime.datetime.now().strftime("%Y-%m-%d"))
# year = datetime.datetime.now().strftime("%Y")
# print(year)
# print(datetime.datetime.now().strftime("%A"))
# print(datetime.datetime.now().strftime("%a"))
req_TimeZone = pytz.timezone("ist") # incomplete 
print(datetime.now(req_TimeZone))
