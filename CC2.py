Enter = ''

print('''
CoinCalculator version2  -by Snickersbrot
''')
print('--------------------------------------------------------------')
print('Enter as many information as you can')
print('''Skip unknown with pressing Enter and letting them blank''')
print('''do not use commas''')
print('--------------------------------------------------------------')

One_Bitcoin = input('''how much is one coin worth?:
''')
coins = input('''with how much coins do you want to calculate?(example: 0.00435):
''')
price_of_the_coins = input('''how much are the *coins* worth?:
''')

if One_Bitcoin == '':
    One_Bitcoin_end = float(price_of_the_coins) / float(coins)
    print('')
    print(One_Bitcoin_end)
    print('''
press Enter to exit''')
    if input() == Enter:
        exit()

if coins == '':
    coins_end = float(price_of_the_coins) / float(One_Bitcoin)
    print('')
    print(coins_end)
    print('''
press Enter to exit''')
    if input() == Enter:
        exit()

if price_of_the_coins == '':
    potc = float(One_Bitcoin) * float(coins)
    print('')
    print(potc)
    print('''
press Enter to exit''')
    if input() == Enter:
        exit()
