# Mean calculator
def mean():
     num_list = list()
     add_more = True
     while add_more:
          numbers = int(input('Enter a number: '))
          num_list.append(numbers)
          add_num = input('Add more numbers? ').lower()
          if add_num == 'y'.lower() or add_num == '+':
               continue
          else:
               return sum(num_list) / len(num_list)
               break

print(mean()) 
