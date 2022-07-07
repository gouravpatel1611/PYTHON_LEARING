# some more methods to add data in our list
# insert methode
# how to join (concatenate) two list
# extend method 
# difference between oppend and extend method 


# insert method
toyota=["innova" ,"fortuner"]
suzuki=["baleno","desire","claz"]
suzuki.insert(2, "ertiga")
print(suzuki)

# how two to join (concatenate) two list
cars=toyota+suzuki
print(cars)

# extend method 
toyota.extend(suzuki)
print(toyota)

# difference detween extend and append
toyota.append(suzuki)
print(toyota)

