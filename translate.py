def encrypt(text):
    #ethan
    #panetha
    length = len(text)
    encString = "p"
    encString += text[length-2::]
    encString += text[0:2]
    mid = text[2: length-2]
    mid = mid[::-1]
    encString += mid
    encString += "a"
    return encString
def decrypt(text):
    length = len(text)
    decString = text[3:5]
    mid = text[5: length-1]
    mid = mid[::-1]
    decString += mid
    decString += text[1:3]

    return decString



