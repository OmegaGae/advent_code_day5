
"""--------------------------------------------------------------------------

 * File Name : 2021_day3.py

 * Purpose : day 3 and part 2 of advent of code

 * Creation Date : 29-12-2021

 * Last Modified : Wed Jan  5 17:06:44 2022

 * Created by : OmegaGae

-----------------------------------------------------------------------------"""

from lib.packages.editfiles import editfile as edit




def get_epsilon(gamma: list):
    
    epsilon = []
    for bit in gamma:
        if bit == 1:
            epsilon.append(0)
        else:
            epsilon.append(1)

    return epsilon


def binary_to_decimal(binary_value: list):

    decimal_value = 0

    for i,bit in enumerate(reversed(binary_value)):
        decimal_value += bit * 2**i  
        
    return decimal_value
    

def binary_decoder(binary_code: list):

    nber_of_bits = len(binary_code[0].rstrip())
    bit_position = 0
    gamma = []
    
    while bit_position < nber_of_bits:
        
        counter_bit_1 = 0
        counter_bit_0 = 0
        
        for binary in binary_code:

            if int(binary.rstrip()[bit_position]) == 1:
                counter_bit_1 += 1
                
            else:
                counter_bit_0 += 1
            
        bit_position += 1
        if counter_bit_0 > counter_bit_1:
           gamma.append(0)
        else:
            gamma.append(1)

    return binary_to_decimal(gamma) * binary_to_decimal(get_epsilon(gamma))



def reset_parameters():
        
    counter_bit_1 = 0
    counter_bit_0 = 0
    potentials_rating_value_0 = []
    potentials_rating_value_1 = []

    return counter_bit_0,counter_bit_1,potentials_rating_value_0,potentials_rating_value_1



def loop_for_binary_data(binary_code: list,bit_position:int):
    
    counter_bit_0,counter_bit_1,potentials_rating_value_0,potentials_rating_value_1 = reset_parameters()


    for binary in binary_code:

        if int(binary.rstrip()[bit_position]) == 1:
            counter_bit_1 += 1
            potentials_rating_value_1.append(binary)
        else:
            counter_bit_0 += 1
            potentials_rating_value_0.append(binary)
    

    return counter_bit_0,counter_bit_1,potentials_rating_value_0,potentials_rating_value_1



def get_oxygene_rating(binary_code: list):
    
    nber_of_bits = len(binary_code[0].rstrip())
    bit_position = 0
    filter_binary_code = binary_code

    while bit_position < nber_of_bits:

        counter_bit_0,counter_bit_1,potentials_rating_value_0,potentials_rating_value_1 = loop_for_binary_data(filter_binary_code,bit_position)
        
        if counter_bit_0 > counter_bit_1:
            filter_binary_code = potentials_rating_value_0
        
        elif counter_bit_0 < counter_bit_1:
            filter_binary_code = potentials_rating_value_1
        
        else:
            filter_binary_code = potentials_rating_value_1

        
        if len(filter_binary_code) == 1:
    
            break
        
        bit_position += 1

    return [int(filter_binary_code[0].rstrip()[p])  for p in range(0,nber_of_bits)]




def get_co2_scrubber(binary_code: list):
    
    nber_of_bits = len(binary_code[0].rstrip())
    bit_position = 0
    filter_binary_code = binary_code

    while bit_position < nber_of_bits:

        counter_bit_0,counter_bit_1,potentials_rating_value_0,potentials_rating_value_1 = loop_for_binary_data(filter_binary_code,bit_position)

        if counter_bit_0 > counter_bit_1:
            filter_binary_code = potentials_rating_value_1
        
        elif counter_bit_0 < counter_bit_1:
            filter_binary_code = potentials_rating_value_0
        
        else:
            filter_binary_code = potentials_rating_value_0

        
        if len(filter_binary_code) == 1:
   
            break
        
        bit_position += 1

    return [int(filter_binary_code[0].rstrip()[p])  for p in range(0,nber_of_bits)]


def life_rating_support(binary_code:list):
    return binary_to_decimal(get_oxygene_rating(binary_code)) * binary_to_decimal(get_co2_scrubber(binary_code))

if __name__ == '__main__':
    input_day3 = edit.Editfile('input_day3.txt')

    print(life_rating_support(input_day3.read()))
 





























