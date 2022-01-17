#!/usr/bin/env python3
#date:21/12/21
#creator: OmegaGae

from lib.packages.editfiles import editfile as edit


def counter_sonar_sweep(sonar_sweep: list):
    deepest = int(sonar_sweep[0].rstrip())
    counter = 0
    for deep in sonar_sweep:
        deep_check = int(deep.rstrip())
        if deep_check > deepest:
            counter +=1
        deepest = int(deep_check)
    
    return counter




def sum_by_three(sonar_sweep: list):
    
    sonar_sweep_clean = [int(deep.rstrip()) for deep in sonar_sweep]
    sumbythree =[str(sum(sonar_sweep_clean[:3]))]
    for ind,deep in enumerate(sonar_sweep_clean):
        if ind + 1 == len(sonar_sweep_clean) - 2:
            break
        sumbythree.append(str(sum(sonar_sweep_clean[ind+1:ind+4])))
        
    return sumbythree

        

if __name__ == '__main__':
    input_sw = edit.Editfile('input.txt')
    print(counter_sonar_sweep(sum_by_three(input_sw.read())))
 
