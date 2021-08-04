#########################
# define the main function with while loops
def coffee_bot():
  print('Welcome to the Bot cafe!')
  order_drink = 'y'
  drinks = []
  while order_drink in ['y', 'yes', 'yeah', 'yep', 'sure']:
    size = get_size()
    drink_type = get_drink_type()
    temp = hot_or_iced()
    cup = cup_type()
    drink = '{} {} {}'.format(temp, size, drink_type)
    print('Alright, that\'s a {} {} {} in {} cup!\n'.format(temp, size, drink_type, cup))
    drinks.append(drink)

    while True:
      order_drink = input('Would you like to order another drink? (y/n) \n>')
      if order_drink in ['y', 'n', 'yes', 'sure', 'yep', 'yeah', 'no', 'nah']:
        break

  print('Okay, so I have: ')
  for drink in drinks:
    print('-', drink)

  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! You\'re all set. Your order will be ready shortly!\n'.format(name))


#########################
# get drink size
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

# set up error message
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

# get drink type
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n')
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

# extra option for latte
def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n')
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

# extra option for mocha
def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n')
    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
    
    print_message()

# hot or iced
def hot_or_iced():
  res = input('Great, would you like your drink hot or iced? \n[a] Hot \n[b] Iced \n')
  if res == 'a':
    return 'hot'
  elif res == 'b':
    return 'iced'
  else:
    print_message()
    return hot_or_iced()

# get cup type
def cup_type():
  res = input('What cup would you like to use? \n[a] A plastic cup \n[b] A paper cup \n[c] I got my own cup\n')
  if res == 'a':
    return 'a plastic'
  elif res == 'b':
    return 'a paper'
  elif res == 'c':
    return 'your own'
  else:
    print_message()
    return cup_type()


# call the main function
coffee_bot()

