import random

def generate_sequence(transition_dict, start_note, length):
    '''Generoidaan sekvenssi Markovin ketjun avulla'''
    sequence = [start_note]
    current_note = start_note
    for i in range(length-1):
        possible_transitions = transition_dict[current_note]
        if not possible_transitions:
            break
        next_note = random.choice(possible_transitions)
        sequence.append(next_note)
        current_note = next_note
    return sequence