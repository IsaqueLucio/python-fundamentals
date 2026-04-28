'''
Peça o nome, o prato favorito e a cidade de nascimento usando input(). 
Retorne uma única frase formatada com f-string (ex: "Olá, [nome], vi que você é de [cidade] e adora comer [prato].").
'''
# 1. Creating the variable
name = input("Input your name: ")
city_of_birth = input("Input your city of birth: ")
favorite_dish = input("Input your favorite dish: ")

# 2. Printing the greetings
print(f"Hello ,",name,", i noticed you're from ",city_of_birth," and love to eat ",favorite_dish,".")

