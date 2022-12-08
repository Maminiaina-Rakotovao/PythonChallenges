# Ex: "This is an example!" ==> "sihT si na !elpmaxe"
# Ex: "double  spaces"      ==> "elbuod  secaps"

# Create the function
def Reverse_words(text):
    text_split = text.split(' ')

    result = []
    for i in text_split:
        text_reverse=i[::-1]
        result.append(text_reverse)

    print(' '.join(result))

Reverse_words("double  spaces!")
