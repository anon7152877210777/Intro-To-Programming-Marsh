ingredient_1 = input("Enter your first ingredient: ")
ingredient_1_o = float(input("Ounces of " + ingredient_1 + ": "))
ingredient_2 = input("Enter your second ingredient: ")
ingredient_2_o = float(input("Ounces of " + ingredient_2 + ": "))
ingredient_3 = input("Enter your third ingredient: ")
ingredient_3_o = float(input("Ounces of " + ingredient_3 + ": "))
servings = int(input("Enter the amount of servings: "))

total_ing1 = ingredient_1_o * servings
print("Total ounces of " + ingredient_1 + ": " + str(total_ing1))
total_ing2 = ingredient_2_o * servings
print("Total ounces of " + ingredient_2 + ": " + str(total_ing2))
total_ing3 = ingredient_3_o * servings
print("Total ounces of " + ingredient_3 + ": " + str(total_ing3))
