# Version 1 : Contains no string Formatting - Program simply asks for input and onput
first_name = input("Enter first name:")
last_name = input("Enter last name :")
clean_name1 = first_name
clean_name2 = last_name
name_combined = clean_name1 + " " + clean_name2
name_code = name_combined
section = input("Enter your section: ")
clean_section = section
favorite_subject = input("Enter your favorite subject:")
clean_favorite_subject = favorite_subject
character_count = len(name_combined.replace(" ", " "))
print("Name:",clean_name1, clean_name2)
print("Name Code:", name_code)
print("Section:", clean_section)
print("Favorite Subject:", clean_favorite_subject)
print("Character Count:",character_count)



