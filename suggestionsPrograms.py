print("\t***SUGGESTION PROGRAMS***")
print("Press 1 for MOVIE SUGGESTION \nPress 2 for CARS SUGGESTION \nPress 3 for PET SUGGESTION\nPress 4 for MOBILE PHONE SUGGESTION")
choice=eval(input())
if choice==1:
    print("MOVIE SUGGESTION")
    category=input("Would you like to watch HOLLYWOOD MOVIES or BOLLYWOOD MOVIES?").lower()
    genre=input("Tell me what genre movie would you like? (Horror/Animation/Action/Sci-Fi)").lower()
    if category=="hollywood" and genre=="action":
        movie="Venom:The last dance"
    elif category=="hollywood" and genre=="horror":
        movie="The Conjuring"
    elif category=="hollywood" and genre=="animation":
        movie="Toy Story"
    elif category=="hollywood" and genre=="sci-fi":
        movie="Intersteller"
    elif category=="bollywood" and genre=="action":
        movie="Savi"
    elif category=="bollywood" and genre=="horror":
        movie="Shaitan"
    elif category=="bollywood" and genre=="animation":
        movie="Jumbo"
    elif category=="bollywood" and genre=="sci-fi":
        movie="Kalki"
    else:
        movie="No movie match your criteria"
    print(movie)
elif choice==2:
    print("CARS SUGGESTION")
    model=input("What model car do you want? (2008-2014/2014-2024)").lower()
    size=input("What size car would you like? (Sedan/Hatchback)").lower()
    gear_type=input("What type car do you want? (Manual/Automatic)").lower()
    if model=="2008-2014" and size=="sedan" and gear_type=="manual":
        car="Toyota Corolla GLI"
    elif model=="2008-2014" and size=="sedan" and gear_type=="automatic":
        car="Honda Civic Reborn VTI"
    elif model=="2008-2014" and size=="hatchback" and gear_type=="manual":
        car="Suzuki Cultus VXRi"
    elif model=="2008-2014" and size=="hatchback" and gear_type=="automatic":
        car="Daihutsu Mira"
    elif model=="2014_2024" and size=="sedan" and gear_type=="manual":
        car="Honda Civic Rebirth VTi"
    elif model=="2014=2024" and size=="sedan" and gear_type=="automatic":
        car="Hyundai Elantra"
    elif model=="2014-2024" and size=="hatchback" and gear_type=="manual":
        car="Suzuki WagonR VXL"
    elif model=="2014-2024" and size=="hatchback" and gear_type=="automatic":
        car="Toyota Aqua"
    else:
        car="A low maintainence Suzuki Mehran"
    print(car)
elif choice==3:
    print("PET SUGGESTION")
    size=input("What size of pet would you like? (Small/Big)").lower()
    activity=input("What kind of pet would you like? (Playful/Calm)").lower()
    if size=="small" and activity=="playful":
        pet="A small playful kitten"
    elif size=="small" and activity=="calm":
        pet="A small calm hamster"
    elif size=="big" and activity=="playful":
        pet="A big playful dog"
    elif size=="big" and activity=="calm":
        pet="A big calm cow"
    else:
        pet="A small low maintainence fish"
    print(pet)
elif choice==4:
    print("MOBILE PHONE SUGGESTION")
    brand=input("Which brand phone would you like? (Android/Apple)").lower()
    camera=input("What type of camera quality would you like? (Good/Excellent)").lower()
    rom=input("How much ROM would you like? (32GB/64GB)").lower()
    if brand=="android" and camera=="good" and rom=="32gb":
        phone="Tecno Pop 5 lite"
    elif brand=="android" and camera=="good" and rom=="64gb":
        phone="Tecno Camon"
    elif brand=="android" and camera=="excellent" and rom=="32gb":
        phone="Pixel"
    elif brand=="android" and camera=="excellent" and rom=="64gb":
        phone="Samsung Z Fold"
    elif brand=="apple" and camera=="good" and rom=="32gb":
        phone="IPhone 7"
    elif brand=="apple" and camera=="good" and rom=="64gb":
        phone="Iphone 8"
    elif brand=="apple" and camera=="excellent" and rom=="32gb":
        phone="Iphone 11"
    elif brand=="apple" and camera=="excellent" and rom=="64gb":
        phone="Iphone 14 Pro"
    else:
        phone="Nokia 3310"
    print(phone)
else:
    print("Invalid choice")
    