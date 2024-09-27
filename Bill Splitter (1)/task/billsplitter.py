import random
# write your code here
n = int(input('Enter the number of friends joining (including you):'))

if n <=0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    name_list=[]
    for i in range(n):
        names = input()
        name_list.append(names)


    total_bill = int(input('Enter the total bill value:'))
    individual_bill = round(total_bill / n,2)

    friends_dictionary = dict.fromkeys(name_list, individual_bill)

    luck = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if luck == 'Yes':
        random_key = random.choice(list(friends_dictionary.keys()))
        print(f'{random_key} is the lucky one!')
    else:
        print('No one is going to be lucky')
    #print(friends_dictionary)