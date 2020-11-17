
#global var

NAV_CONT = ('games', 'cart', 'buy', 'admin', 'exit')
   
game_inv = [                     #product inventory compiled list title,stock,price
	['Ghost of Tsushima',10,60],
	['Grand Theft Auto 5',10,35],
	['Spider Man      ',10,20],
	['Call of Duty   ',10,20],
	['Mortal Kombat 11',10,20]
	
]

cart_items = []
cart_sum = []
grand_total = sum(cart_sum)


def menu():
	"""Menu Layout defines input values"""
	
	print("""\t  ---GameRx--- 
	"Dose up on Games"\n
	-View our Games (Type games)
	-View Cart (Type cart)  
	-Checkout (Type buy)   
	-Admin(Type admin)   
	-Exit (Type exit)\n""")
	
def cart_logs(item):
	"""adds game to cart_items and game cost to cart_sum"""
	
	cart_items.append(item)
	cart_sum.append(item[2])
		
def display_games():
	print("\tTitle\t\tIn Stock\tPrice")
	for game in game_inv:
		print(f"-{game[0]}\t  {game[1]}\t\t {game[2]}")




#Master Loop

while True:
	menu()
	nav = str(input('Type here: ').lower()) #navigational input
	if nav not in NAV_CONT:
		print(f'OOPS! You can only type {NAV_CONT}')
	elif nav == 'games':
		display_games()
	elif nav == 'cart':
		print('cart')
	elif nav == 'buy':
		print('buy')
	elif nav == 'admin':
		print('admin')
	else:
		print('Thank you for visting GameRx!')
		break
		
print('end')
		   
		   		
	



