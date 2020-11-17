
#product inventory compiled list x,x,x,x
prod_inv = [[],[],[]]
NAV_CONT = ('show', 'add', 'buy', 'exit')

#Menu Layout defines input values
def menu():
	print('\t    ***GameRx***\n\t  "Dose up on Games"\n\n\tView our Games (Type show)\n\t  Add to Cart (Type add)\n\t   Checkout (Type buy)\n\t    Exit (Type exit)\n')

#Cart


#Invoice




#Master Loop

while True:
	menu()
    #navigational input
	nav = str(input('Type here: ').lower())
	if nav not in NAV_CONT:
		print(f'OOPS! You can only type {NAV_CONT}')
	elif nav == 'show':
		print('show')
	elif nav == 'add':
		print('add')
	elif nav == 'buy':
		print('buy')
	else:
		print('Thank you for visting GameRx!')
		break
		
print('end')
		   
		   		
	



