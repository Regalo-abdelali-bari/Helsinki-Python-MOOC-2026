# Write your solution here

def search_by_name(filename: str, word: str):
    with open(filename) as recipes:
        my_list = []
        for recipe in recipes :
            recipe = recipe.strip()
            if word in recipe.lower() and recipe == recipe.capitalize():
                my_list.append(recipe)
    return my_list

def search_by_time(filename: str, prep_time: int):
    with open(filename) as recipes:
        last_word = ""
        my_list = []
        for recipe in recipes:
            recipe = recipe.strip()
            if last_word == last_word.capitalize() and last_word != "":
                if int(recipe) <= prep_time: 
                    my_list.append(f'{last_word}, preparation time {recipe} min')
                last_word = ""
                continue
            last_word = recipe
    return my_list

def search_by_ingredient(filename: str, ingredient: str):
    with open (filename) as ingrediants:
        my_list1 = []
        my_list2 = []
        my_list3 = []
        for ingre in ingrediants:
            ingre = ingre.strip()
            if ingre == "":
                my_list3.append(my_list2)
                my_list2=[]
                continue
            my_list2.append(ingre)
        my_list3.append(my_list2)
        for item in my_list3:
            if ingredient in item:
                my_list1.append(f'{item[0]}, preparation time {item[1]} min')
    return my_list1

        
            
if __name__ == "__main__":
    
        

    found_recipes = search_by_ingredient("recipes1.txt", "milk")

    for recipe in found_recipes:
        print(recipe)