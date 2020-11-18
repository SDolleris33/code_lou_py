from datetime import datetime
import random


#global var
cart_items = []
cart_prices = []
NAV_CONT = ('games', 'add', 'buy', 'admin', 'exit')
   
#product inventory compiled list: title,stock,price
game_inv = [                     
	[1,'Ghost of Tsushima',60],
	[2,'Grand Theft Auto 5',35],
	[3,'Spider Man      ',20],
	[4,'Call of Duty   ',20],
	[5,'Mortal Kombat 11',20]
]


def display_games():
	"""Print formatted game inventory"""
	
	print("# \tTitle\t\tPrice")
	for game in game_inv:
		print(f"{game[0]} {game[1]}\t{game[2]}")


def menu():
	"""Menu Layout defines input values"""
	
	print("""\t  ---GameRx--- 
	"Dose up on Games"\n
	-View our Games (Type games)
	-Add to Cart (Type add)  
	-Checkout (Type buy)   
	-Admin(Type admin)   
	-Exit (Type exit)\n""")
	
def game_names(list):
	"""Interates of list returning index value"""
	return[x[1] for x in list]
			
	
	
def cart_logs(item):
	"""adds game to cart_items and game price to cart_sum"""
	
	item = int(item) - 1
	price = game_inv[item][2]
	cart_items.append(game_inv[item])
	cart_prices.append(price)
	
def order_log(list,str):
	"""formated string in buy() with datetime"""
	
	print(f"""---GameRx---
			--Order Summary--	
		Date: {datetime.now()}
		Customer:{str}
		Games:{game_names(list)}
	Total: ${float(sum(cart_prices))}
	""")
	
	
	
		





#Master Loop

while True:
	menu()
	nav = str(input('Type here: ').lower()) #navigational input
	if nav not in NAV_CONT:
		print(f'OOPS! You can only type {NAV_CONT}')
	elif nav == 'games':
		display_games()
	elif nav == 'add':
		while True:
			display_games()
			try:
				select = int(input('What would you like to add to you cart; Type in the #? '))
			except ValueError:
					print('Thats not a number in our inventory')
					break
			for i,t,p in game_inv:
					if select == len(game_inv):
						cart_logs(select)
						print(f'Game added: {t} ${p}')
						print(f'Cart items: {len(cart_items)}')
					elif select > len(game_inv) or select < len(game_inv):
						print('Thats not a number in our inventory')
			cart_cfm = input('Finished adding to cart? (y/n): ').lower()
			if cart_cfm == 'y':
				break
	elif nav == 'buy':
		if len(cart_items) == 0:
			print('You have no items in your cart')
		else:
			print(f'# of items in Cart: {len(cart_items)} Total: ${sum(cart_prices)}')
			buy_cfm = input('Would you like to finalize your purchase? y/n ').lower()
			if buy_cfm == 'y':
				print('---Writing Bill---')
				name = input('What is your name? ')
				order_log(cart_items,name)
				print(f'Thank you for your business {name}')
				break
			else:
				print('Your order is ready when you are!')
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
		

		

		   
		  