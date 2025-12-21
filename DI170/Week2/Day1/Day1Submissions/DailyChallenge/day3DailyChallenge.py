#Challenge 1: Letter Index Dictionary

#review each char in str
#for each, pay attention to index and what char
#check char against what's already in the dictionary's keys
#if in dict, add index to char's list
#else, made new dict key value pair
#char = key, index = value

user_word = input('Enter a word: ')
word_dict = {}
for i, char in enumerate(user_word):
    if char in word_dict:
        word_dict[char].append#(i)
    else:
        word_dict[char] = [i]
print(word_dict)


#Challenge 2: Affordable Items

# items_purchase = {[resources] : (price)}
# wallet = (num_total)
# clean_price = int(price.replace('$', ''))
# print(type(clean_price))
# basket = [add resources < wallet, when >=0]
#if basket = null, print 'Nothing'; else print[sorted(basket)]


# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"
# for each k-v pair, look at value 
# clean value & convert to integer
# reassociate cleaned value with the same key in the dictionary

items_purchase = {}
wallet = ('')
for key, value in items_purchase.items():
    no_sign = value.replace('$', '')
    no_comma = no_sign.replace(',', '')
    price = int(no_comma)
    items_purchase[key] = price

no_sign_w = wallet.replace('$', '')
no_comma_w = no_sign_w.replace(',', '')
my_wallet = int(no_comma_w)

basket = []
for key, value in items_purchase.items():
    if value <= my_wallet:
        basket.append(key)
        my_wallet -= value

if len(basket) == 0:
    print('Nothing')
else:
    sorted_basket = sorted(basket)
    print(sorted_basket)