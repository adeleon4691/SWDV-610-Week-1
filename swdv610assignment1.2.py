#A common punishment for school children is to write out a sentence multiple times.  Write a Python stand-alone program
#that will write the following sentence one hundred times: "I will never spam my friends again."

phrase="I will never spam my friends again."

for i in range(1, 101):
    print(i,":",phrase)