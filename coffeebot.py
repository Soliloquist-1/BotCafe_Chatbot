# main function　
def coffee_bot():
  print('Welcome to the Bot cafe!')
  size = get_size()
  drink_type = get_drink_type()
  temp = hot_or_iced()
  cup = cup_type()
  print('Alright, that\'s a {} {} {} in {} cup!\n'.format(temp, size, drink_type, cup))
  name = input('Can I get your name please?\n')
  print('Thanks, {}! You\'re all set. Your order will be ready shortly!\n'.format(name))
  additional_drink()

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
    return 'mocha'
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

# extra for half the price?
def extra_situation():
  size = get_size()
  drink_type = get_drink_type()
  temp = hot_or_iced()
  cup = cup_type()
  print('Alright, that\'s a {} {} {} in {} cup!\n'.format(temp, size, drink_type, cup))
  print('You\'re all set.')

def additional_drink():
  res = input('By the way, would you like to order an additional drink for half the price? \n[a] Great, why not? \n[b] No, thanks. \n')
  if res == 'a':
    return extra_situation()
  elif res == 'b':
    return print('Got it! Your order will be ready shortly!')
  else:
    print_message()
    return additional_drink()

# Call coffee_bot()!
coffee_bot()
