'''Mike has made the decision to organize a competition. The contest is that Mike has a word with him
written on the notepad and if the participants names contain both the initial and second letterof the
word he has. He will affirm and present the gift after saying it is True '''
str1=input("Enter a string:")
str2=input("Enter another string:")
if str1[0] in str2 and str1[1] in str2:
    print("Yes, starting 2 characters of First string is present in string 2 ")
else:
    print("No, starting 2 characters of first string is not present in string 2")