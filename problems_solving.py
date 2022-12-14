#Task 1
word = "Hello"
for index in range(len(word) -1, -1, -1):
    print(word[index])


#Task 2
# greeting1 = 'good'
# greeting2 = 'day'
# result1 = greeting1.replace("g", "G")
# result2 = greeting2.replace("d", "D")
# results = result1 + " " + result2
# print(results)


phrase = 'good day, how are you this morning?'
#expected: 'Good Day'
final_string = ""


for char in phrase:
    print(char)

for index in range(len(phrase)):
    if phrase[index - 1] == " " or index == 0:
        final_string += phrase[index].upper()
    else:
        final_string += phrase[index]

print(final_string)



#Task 3
#A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	
#Write code that takes a user input and checks to see if it is a Palindrome and reports the result


user_input = input("Type a word to see if it is a palindrome.")
print(user_input)
