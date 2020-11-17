from datetime import datetime
import random
import sys


#global var

NAV_CONT = ('games', 'cart', 'buy', 'admin', 'exit')
   
game_inv = [                     #product inventory compiled list title,stock,price
	[1,'Ghost of Tsushima',60],
	[2,'Grand Theft Auto 5',35],
	[3,'Spider Man      ',20],
	[4,'Call of Duty   ',20],
	[5,'Mortal Kombat 11',20]
	
]

cart_items = []
cart_sum = []
grand_total = sum(cart_sum)


def menu():
	"""Menu Layout defines input values"""
	
	print("""\t  ---GameRx--- 
	"Dose up on Games"\n
	-View our Games (Type games)
	-Add to Cart (Type cart)  
	-Checkout (Type buy)   
	-Admin(Type admin)   
	-Exit (Type exit)\n""")
	
	
	
def cart_logs(item,num):
	"""adds game to cart_items and game cost to cart_sum"""
	
	cart_items.append(item[num])
	cart_sum.append(item[2])
	return len(cart_items)
		
def display_games():
	"""Print formatted game inventory"""
	print("# \tTitle\t\tPrice")
	for game in game_inv:
		print(f"{game[0]} {game[1]}\t{game[2]}")




#Master Loop

while True:
	menu()
	nav = str(input('Type here: ').lower()) #navigational input
	if nav not in NAV_CONT:
		print(f'OOPS! You can only type {NAV_CONT}')
	elif nav == 'games':
		display_games()
	elif nav == 'cart':
		while True:
			display_games()
			select = int(input('What would you like to add to you cart; Type in the #? '))
			for i,t,p in game_inv:
				if select == i:
					i = i - 1
					cart_logs(game_inv,i)
					print(f'{t} ${p}')
					print(f'Cart items: {len(cart_items)}')
					print(cart_items)
			cart_cfm = input('Finished adding to cart? (y/n): ').lower()
			if cart_cfm == 'y':
				break
	elif nav == 'buy':
		if len(cart_items) == 0:
			print('You have no items in you cart')
		else:
			print(f'Cart:\n {cart_items}')
			
	elif nav == 'admin':
		username = input("Enter Admin UserID: ")
		password = input("Enter Password: ")
		if username == "Admin" and password == "password":
			game = []
			game.append(len(game_inv)+1)
			game.append(input("Enter game Title: "))
			game.append(input("Enter price !!! dont not include '$' !!!: "))	
			game_inv.append(game)
			print(f"Added: {game}")
		else:
			print('Incorrect Username/Password')
							 
	else:
		print('Thank you for visting GameRx!')
		break
		

		

		   
		   		
	



