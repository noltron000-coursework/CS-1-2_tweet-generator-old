import random # psuedo-random number generator module
import sys # module allows program to access terminal parameters

def rearrange(input_data):
	if (type(input_data) is str:
		input_data = input_data.split(' ')
	return stringify_list(randomify_list(input_data))

def randomify_list(input_list):
	output_list = []
	while len(input_list) > 0:
		digit_rand = random.randint(0, len(input_list) - 1)
		input_rand = input_list.pop(digit_rand)
		output_list += input_rand
	return output_list

def stringify_list(input_list):
	output_text = ''
	for input_item in input_list:
		if output_text != '':
			output_text += ' '
		output_text += input_item
	return output_text

if __name__ == '__main__':
	input_list = sys.argv[1:]
	print(rearrange(input_list))