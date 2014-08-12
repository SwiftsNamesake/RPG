#
# Dialogue RPG - main.py
# A simple text-based adventure
# 
# Jonatan H Sundqvis
# August 11 2014

# TODO | - Class for entities (colour, personality, etc.)
#		 -

# SPEC | - 
#		 -


class Entity:

	'''
	Docstring goes here

	'''

	def __init__(self, name, colour, agreeability):
		self.name = name
		self.colour = colour
		self.agreeability = agreeability


	def say(self, message, tone):
		print('[%s] (%s) %s' % (self.name, tone, message))



# TODO: Use wintypes to highlight replies on hover (?)
#def carrefour()
def junction(*replies):
	print('\n'.join('  [%d] %s' % (n, reply) for n, reply in enumerate(replies)))
	return int(input())
	

def main():
	you = Entity('YOU', 'red', 0.4)
	ai  = Entity('AI', 'green', 0.3)

	ai.say('And where the hell do you think you\'re going?', 'sternly')
	you.say('Uhm.. Excuse me?', 'flustered')
	
	junction('Heading for greener pastures, sir.',
			 'None of your business!',
			 'Wherever the road may take me. Who\'s asking?')

if __name__ == '__main__':
	main()