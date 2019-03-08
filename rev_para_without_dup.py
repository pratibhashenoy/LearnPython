from collections import OrderedDict

def rev_str(s):
    return s [::-1]

def re_dup(str):
    return " ".join(OrderedDict.fromkeys(reverse))

input_str = "Python is an amazing and easy and python is the best and I love Python."

    

    

if __name__ == "__main__":
    print ("Input paragraph =", input_str)
    reverse = rev_str(input_str.lower())
    # print ("Output reversed paragraph =", reverse)
    reverse = reverse.split(" ")
    print ("Output of reversed paragraph without duplicates =", re_dup(reverse))
   

    