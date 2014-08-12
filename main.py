#
# Dialogue RPG - main.py
# A simple text-based adventure
# 
# Jonatan H Sundqvis
# August 11 2014

# TODO | - Class for entities (colour, personality, etc.)
#        - Audio (?)

# SPEC | - 
#        -

from random import randint

class Entity:

    '''
    Docstring goes here

    '''

    # TODO: Remember encounters with and attitudes towards other Entities

    def __init__(self, name, colour, agreeability):
        self.name = name
        self.colour = colour
        self.agreeability = agreeability

        self.relations = {}


    def say(self, message, tone):
        print('[%s] (%s) %s' % (self.name, tone, message))


    def acquaint(self, entity, attitude):
        # TODO: Add more dimensions and impressions (eg. trustworthy, past encounters)
        self.relations[entity] = attitude


# TODO: Use wintypes to highlight replies on hover (?)
#def carrefour()
def junction(*replies):
    print('\n'.join('  [%d] %s' % (n, reply) for n, reply in enumerate(replies))) # Print each possible reply on its own line, indented and numbered
    choice = int(input()) # TODO: Validate choice
    return replies[choice].lstrip()


def rollDice(number=1, sides=6):
    return tuple(randint(1, sides) for n in range(number))


def main():
    you = Entity('YOU', 'red', 0.4)
    ai  = Entity('AI', 'green', 0.3)

    ai.say('And where the hell do you think you\'re going?', 'sternly')
    you.say('Uhm.. Excuse me?', 'flustered')
    
    choice = junction('Heading for greener pastures, sir.',
                      'None of your business!',
                      'Wherever the road may take me. Who\'s asking?')

    you.say(choice, 'neutral')

if __name__ == '__main__':
    main()