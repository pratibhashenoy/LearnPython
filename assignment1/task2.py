#freq definition
def freq(str):
    #convert the words in the sentence to lowercase
    str = str.lower()
    #using split function, break sentence into list of words
    str = str.split()

    #create an empty list
    str2 = []

    #Get the list of words in sentence and add it to the str2's empty list
    for i in str:

        if i not in str2:
            str2.append(i)

    #Count the freq of words in sentence
    for i in range(0,len(str2)):
        print(str2[i], ": ", str.count(str2[i]))
            

#main definition
def main():
    str = "Python is an amazing and easy and python is the best and I love Python."
    print ("Input = ",str)
    print("Output = ")
    #calling freq function
    freq(str)

#calling main function
if __name__ == "__main__":
    main()

    
