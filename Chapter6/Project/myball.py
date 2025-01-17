import random

my_collection = ['rouge', 'rose', 'orange', 'rouge', 'rose', 'jaune', 'rose', 'jaune']
bag_of_balls = ['rose', 'bleu', 'vert', 'orange', 'rouge', 'pourpre', 'vert', 'bleu', 'bleu', 'rouge', 'vert', 'poupre', 'jaune', 'rouge', 'rose', 'rouge', 'vert', 'jaune']
balls_outputs = []

remaining_draws = 5

for number in range(5):
    if remaining_draws > 0:
        selection = random.choice(bag_of_balls)
        balls_outputs.append(selection)
        remaining_draws -= 1  # remaining_draws = remaining_draws - 1

        if selection == 'vert':
            my_collection.append(selection)
            print("Excellent! Tu as tiré ta bille verte!")
            print("Il restait " + str(remaining_draws) + " tirages.")
            break

if not ('vert' in my_collection):
    print("Tous les tirages sont faits. Aucunne bille verte.")

print("Billes sorties pour ce tirage: ")
print(balls_outputs)
print("La nouvelle collection contient: ")
print(my_collection)

