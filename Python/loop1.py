answer = input("what is the capital of france?" )
answer=answer.title()

while answer != "Paris":
    answer=input("incorect try again: ")
    answer==answer.title()
    counter =counter + 1
print("correct well done",counter,"attempts")