pet_species = input("Enter your pet species: ")
petLower = pet_species.lower()

ageOfPet = input("Enter pet age: ")
ageInt = int(ageOfPet)

if pet_species == "dog":
    if ageInt < 2:
        recommededFood = "Puppy Food"
    else:
        recommededFood = "Adult Dog Food"
elif pet_species == "cat":
    if ageInt > 5:
        recommededFood = "Senior Cat Food"
    else:
        recommededFood = "Kitten Food"
else:
    recommededFood = "No Information"

print("Pet species:", pet_species, " and recommeded food:",recommededFood)