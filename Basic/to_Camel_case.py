# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"


def to_camel_case(text):

    if text == '':
        return ''
        
    else:
        strng = ''
        for i in text:
            if i.isalpha():
                strng = strng + i
            else:
                strng = strng + ' '

        to_list = strng.split()
        result = []

        for i in to_list[1:]:
            result.append(i.title())

        final_result = [to_list[0]] + result
        
        return ''.join(final_result)
