movies = []


def menu():
    user_input = input(
        "\nEnter\n'a' to add a movie,\n'l' to list your movies,\n'f' to find a movie\n'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            list_all_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("\nInvalid input. Try again")

        user_input = input(
            "\nEnter\n'a' to add a movie,\n'l' to list your movies,\n'f' to find a movie\n'q' to quit: ")


def add_movie():
    name = input("\nEnter the movie name: ")
    director = input("Enter the movie director: ")
    year = int(input("Enter the movie release year: "))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def list_all_movies():
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"\nName: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    find_by = input(
        "\nWhat property of the movie are you looking for? (name/director/year) ")
    looking_for = input("What are you searching for? ")
    if looking_for.isdigit():
        looking_for = int(looking_for)

    find_movie_by_attribute(find_by, looking_for)


def find_movie_by_attribute(find_by, looking_for):
    for movie in movies:
        if movie[find_by] == looking_for:
            show_movie_details(movie)


menu()
