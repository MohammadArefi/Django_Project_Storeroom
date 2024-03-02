# write your validators here
import re
from datetime import datetime


def persian_valid(value):
    persian = re.search("^[\u0600-\u06FF\s]+$", value)
    if not persian:
        return False
    else:
        return True


english_number = "/^[0-9]{10}$/"




def date_valid(value):
    if (bool(datetime.strptime(value, "%Y-%m-%d %H:%M"))) == True:
        if value < datetime.now().strftime("%Y-%m-%d %H:%M"):
            return True
        else:
            return False
    else:
        return False
