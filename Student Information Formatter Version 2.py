# Version 2 : Has String Formatting - Program ask for input and output and formats it.
first_name = input("Enter first name:")
last_name = input("Enter last name :")
clean_name1 = first_name.strip().title()
clean_name2 = last_name.strip().title()
name_combined = clean_name1 + " " + clean_name2
name_code = name_combined.upper()
section = input("Enter your section: ")
clean_section = section.strip().upper()
favorite_subject = input("Enter your favorite subject:")
clean_favorite_subject = favorite_subject.strip().title()
character_count = len(name_combined.replace(" ", " "))
print("Name:",clean_name1, clean_name2)
print("Name Code:", name_code)
print("Section:", clean_section)
print("Favorite Subject:", clean_favorite_subject)
print("Character Count:",character_count)



