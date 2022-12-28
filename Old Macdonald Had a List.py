def get_animals():
    animals_final_list = []
    continue_input = True

    while continue_input:
        animal_name = input('Please enter an animal name (or -1 to quit): ')
        if animal_name == '-1':
            break
        animal_sound = input('Please enter an animal sound: ')
        animals_final_list.append([animal_name, animal_sound])
    print(animals_final_list)
    return animals_final_list


def print_poem(lst):
    animal, sound = lst
    
    print('')
    print('Old MacDonald had a farm, E-I E-I O!')
    print(f'And on that farm there was a {animal}, E-I E-I O!')
    print(f'With a {sound}, {sound} here, and a {sound}, {sound} there,')
    print(f'Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.')
    print('Old MacDonald had a farm, E-I E-I O!')
    print('')



def main():
    animal_list = get_animals()
    for animal in animal_list:
        print_poem(animal)

if __name__ == '__main__':
    main()