###FUNCTIONS EXERCISES
# 1
def display_message():
    """This is to display what i am learning"""
    print('I am learning Functions')
display_message()

#2 
def favorite_book(Title):
    """This is to show my favorite Book"""
    print('The title of my favorite book is: ', Title.title())
favorite_book('python crash course')

#3 
def make_shirt(size, message):
    """This prints a sentence summarizing the size of the shirt and message printed on it"""
    print('\nMake a shirt of size',  size)
    print('With ' + message + ' written on it')
make_shirt(10, 'Python')
make_shirt(size= 10, message='Python')


#4
def make_shirt(message, size='large'):
    """This prints a sentence summarizing the size of the shirt and message printed on it"""
    print('\nMake a shirt of size',  size)
    print('With ' + message + ' written on it')
make_shirt('I love Python')




def large_shirt(size, message='ArewaDS'):
    """This prints a sentence summarizing the size of the shirt and message printed on it"""
    print('\nMake a shirt of size',  size)
    print('With ' + message + ' written on it')
large_shirt('large')
large_shirt('medium')


large_shirt( message= 'I love ArewaDS', size = 'medium')


#5
def describe_city(city, country='Nigeria'):
    """This is to print a simple sentence"""
    print(city, 'is in ', country)
describe_city('Abuja')
describe_city('kaduna')
describe_city('Iceland')


#6
def city_country(city, country):
    """This displays city and country"""
    print(city, country)
city_country('Abuja', 'Nigeria')
city_country('Kaduna', 'Nigeria')
city_country('Santiago', 'Chile')

#7
def make_album(artist_name, title):
    """This functions return a dictionary about a musician"""
    musician = {'artist_name': artist_name, 'title': title }
    return musician
musician_1 = make_album('Maher Zain', 'paradise')
musician_2 = make_album('Zain Bikha', 'Allah is One')
musician_3 = make_album('Sami Yusuf', 'Al-Muallim')
print(musician_1)
print(musician_2)
print(musician_3)


def make_album(artist_name, title, track=''):
    """This functions return a dictionary about a musician"""
    if track:
        musician = artist_name + ' ' + title + ' ' + str(track)
    else:
        musician = artist_name + title
    return musician
    
musician_1 = make_album('Maher Zain', 'paradise', track=1)musician_2 = make_album('Zain Bikha', 'Allah is One')
musician_3 = make_album('Sami Yusuf', 'Al-Muallim', track=7)
print(musician_1)
print(musician_2)
print(musician_3)



#8
def make_album(artist_name, title):
    """This functions return a dictionary about a musician"""
    musician = {'artist_name': artist_name, 'title': title }
    return musician
while True:
    print('\nartist dictionary:')
    print("(enter 'q' at any time to quit)")
        
    artist = input('artist_name:')
    if artist == 'q':
        break
        
    artist_title = input('artist:')
    if artist_title == 'q':
        break
        
musician_album = make_album('Maher Zain', 'paradise')
print(musician_album)

#9
def show_magician(magician_names):
    """ Printing the names of Magicians """
    for magician in magician_names:
        print(magician.title())
magician_names= ['ojo', 'jaguda', 'otori']
show_magician(magician_names)
 
 
#10   
def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)

def make_great(magician_list):
    # Modifying the list by adding "the Great" to each magician's name
    for i in range(len(magician_list)):
        magician_list[i] = "The Great " + magician_list[i]


magicians = ['ojo', 'jaguda', 'otori']
make_great(magicians)

show_magicians(magicians)

#11
def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)

def make_great(magician_list):
    # Modifying the list by adding "the Great" to each magician's name
    for i in range(len(magician_list)):
        magician_list[i] = "the Great " + magician_list[i]
    return magician_list

original_magicians = ['ojo', 'jaguda', 'otori']

# Creating a copy of the original list
modified_magicians = make_great(original_magicians[:])

# Calling show_magicians() to display the original list
print("Original Magicians:")
show_magicians(original_magicians)

# Calling show_magicians() to display the modified list
print("\nModified Magicians:")
show_magicians(modified_magicians)
    

#12
def sandwiches(*toppings) :
    """ This functions print sandwiches that is being ordered""" 
    print("Making a "  +
"sandwiches with the following toppings:")
    for topping in toppings:
       print("- " + topping)
sandwiches('Tomatoes')
sandwiches('Fish') 
sandwiches('Lettuce')

#13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Halimat', 'Muhammadurabiu',
location='Abuja',
field='Biochemistry', language='Ebira')
print(user_profile)


#14
def make_cars(manufacturer, model, **features ):
    """This is a dictionary that contains car details"""
    cars = {}
    cars['manufacturer'] = manufacturer
    cars['model'] = model
    for key, value in features.items():
        cars[key] = value
    return cars

cars = make_cars('subaru', 'outback', color = 'blue', tow_package = True)
print(cars)
    
  
#15   
from printing_functions import print_models, show_completed_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)



#16
from greetings import greet

user_name = input("Enter your name: ")
welcome_message = greet(user_name)
print(welcome_message)

#17
import greetings
from greetings import greet
from greetings import greet as gs
import greetings as gs
from greetings import *

user_name = input("Halimat: ")

welcome_message1 = greetings.greet(user_name)
print(welcome_message1)

welcome_message2 = greet(user_name)
print(welcome_message2)

welcome_message3 = gs(user_name)
print(welcome_message3)

welcome_message4 = gs.greet(user_name)
print(welcome_message4)

welcome_message5 = greet(user_name)
print(welcome_message5)



# 17
#1
def make_shirt(message, size='large'):
    """This prints a sentence summarizing the size of the shirt and message printed on it"""
    print('\nMake a shirt of size',  size)
    print('With ' + message + ' written on it')
make_shirt('I love Python')

#2
def large_shirt(size, message='ArewaDS'):
    """This prints a sentence summarizing the size of the shirt and message printed on it"""
    print('\nMake a shirt of size',  size)
    print('With ' + message + ' written on it')
large_shirt('large')
large_shirt('medium')


large_shirt( message= 'I love ArewaDS', size='medium')


#3
def describe_city(
            city, country='Nigeria'):
    """This is to print a simple sentence"""
    print(city, 'is in ', country)
describe_city('Abuja')
describe_city('kaduna')
describe_city('Iceland')


