#Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
import csv

def csv_test():
    with open('videogames.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Genre', 'Platform', 'Price'])

        while True:
            name = input('Enter the name of the video game: ')
            genre = input('Enter the genre of the video game: ')
            platform = input('Enter the platform of the video game: ')
            price = input('Enter the price of the video game: ')

            writer.writerow([name, genre, platform, price])

            response = input('Do you want to enter another video game? (yes/no): ')
            if response.lower() not in ['yes', 'y']:
                break

    print('The videogames have been saved successfully')
    print("Videogame list:")

    with open('videogames.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

csv_test()