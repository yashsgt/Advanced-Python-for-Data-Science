# Coding:
# If the word contains atleast 3 characters, remove the first letter and append it at the end 
# now append three random characters at the starting and the end
# else:
# Simply reverse the string
# 
# Decoding:
# If the word contains less than 3 characters, reverse it
# else:
#     remove 3 random characters from start and end. Now remove the last letter and append it to beginning

# Your program should ask whether you want to code or decode.

st = input("Enter Message: ")
words = st.split(" ")
coding = input("Enter 1 for coding or 0 for decoding: ")
coding = True if (coding=="1") else False
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "dsf"
            r2 = "udr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))


else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3: -3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))









  