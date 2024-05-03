# Wally's Training Gym - By Matthew Fagan
# This program will calculate how many trainers have enrolled how much members for the gym.
# Declare variables and arrays.
trainerNames = [__name__,__name__,__name__,__name__,__name__,__name__,__name__,__name__,__name__,__name__,__name__,__name__,__name__,__name__,__name__]
newEnrollees = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Category1 = 0
Category2 = 0
Category3 = 0

# Create a for loop so you can input the trainer's names and the number of new enrollees.
for i in range(0,15):
    trainerNames[i] = input("Enter trainer's last name: ")
    newEnrollees[i] = input("Enter number of new enrollees: ")

#Categorize the trainers.
for i in range(0,15):
    if newEnrollees >= 1 and newEnrollees <= 5:
        Category1 = Category1 + 1
    elif newEnrollees >= 5 and newEnrollees <= 10:
        Category2 = Category2 + 1
    elif newEnrollees >= 11 and newEnrollees <= 15:
        Category3 = Category3 + 1

# Display your results.
print("Number of trainers who have enrolled 0-5 members: " + Category1)
print("Number of trainers who have enrolled 6-10 members: " + Category2)
print("Number of trainers who have enrolled 11-15 members: " + Category3)
