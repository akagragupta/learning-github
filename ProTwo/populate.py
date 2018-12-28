import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen=Faker()

name=['ion','kok','lol','ipo','jij']
sirname=['gupta','sharma','chadda','tikk','mittal']

def populate(N=5):
	for i in range(N):
		user = User.objects.get_or_create(first_name=random.choice(name),last_name=random.choice(sirname),email=fakegen.name())[0]

if __name__ == '__main__':
	print("populating script")
	populate(5)
	print("populating complete")