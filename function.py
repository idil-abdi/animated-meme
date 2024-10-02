######## Function ########
occation_input = input('what is the occation? ')
name_input = input('what is your name? ')
def create_greet_card(occasion, name):
    if occasion == 'birthday':
        print(f'happy birthday, {name}')
    elif occasion == 'morning':
        print(f'good morning,{name}')
    else: 
        print(f'good day, {name}')
create_greet_card(occation_input, name_input)
