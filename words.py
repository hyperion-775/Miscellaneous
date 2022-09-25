def get_input(word):
  input('Type a(n) {}\n' .format(word))
  
get_input('adjective')
get_input('verb')
get_input('noun')

def fill_in_blank(input):
  print('{}' .format(input))

fill_in_blank(get_input('adjective'))
