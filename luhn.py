def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    if checksum % 10 ==0:
        return True

def validator(card_no,card_name):
    if (card_name.lower()).strip(" ")=="visa":
        if card_no[0]=="4" and (len(card_no)==13 or len(card_no)==16) and luhn_checksum(int(card_no))==True:
            return True
        else:
            return False
    elif (card_name.lower()).strip(" ") in ("mastercard","master card") :
        if card_no[0]=="5" and len(card_no)==16 and luhn_checksum(int(card_no))==True:
            return True
        else:
            return False
    elif (card_name.lower()).strip(" ")=="maestro":
        if card_no[0]=="5" and len(card_no)==19 and luhn_checksum(int(card_no))==True:
            return True
        else:
            return False
    elif (card_name.lower()).strip(" ") in ("americanexpress","american express"):
        if card_no[0]=="3" and len(card_no)==15 and luhn_checksum(int(card_no))==True:
            return True
        else:
            return False
    else:
        return "Invalid"

