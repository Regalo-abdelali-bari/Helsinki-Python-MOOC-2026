import datetime
def is_it_valid(pic: str):
    try:
        if len(pic) == 11:
            if "A" == pic[6]:
                datetime.datetime(int("20"+pic[4:6]), int(pic[2:4]), int(pic[:2]))
            elif "-" == pic[6]:
                datetime.datetime(int("19"+pic[4:6]), int(pic[2:4]), int(pic[:2]))
            elif "+" == pic[6]:
                datetime.datetime(int("18"+pic[4:6]), int(pic[2:4]), int(pic[:2]))
            number_9= pic[:6]+pic[7:10]
            result = int(number_9) % 31
            remainder = "0123456789ABCDEFHJKLMNPRSTUVWXY"
            if  remainder[result] == pic[-1] :
                return True
        return False
    
    except ValueError:
        return False
    
if __name__ == "__main__":
    print(is_it_valid("080842-720N"))