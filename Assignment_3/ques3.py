#   Given a sentence, return a sentence with the words reversed
#   reversed_words('I am home') --> 'home am I’
#   reversed_words('We are ready') --> 'ready are We’
#   Note: The .join() method may be useful here. The .join() method allows you to join together
#   strings in a list with some connector string.

def reversed_word(sen):
    res = sen.split()
    res = res[::-1]
    print(res)

sen = input("Enter a sentence : ")
reversed_word(sen)
