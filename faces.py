#get user input, assign to variable "answer"
answer = input()

#print user's input but replace the either ":)" or ":(" with the assigned emojis
if ":)" in answer:
    answer = answer.replace(":)", "🙂")
if ":(" in answer:
    answer = answer.replace(":(", "🙁")

print(answer)
