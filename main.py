from stats import count_words, count_chars, format_chars
import sys

def get_book_text(file_path):
	file_contents = ''
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def pretty_print(filepath, chars, words_count):
	print('============ BOOKBOT ============')
	print(f'Analyzing book found at {filepath}...')
	print('----------- Word Count ----------')
	print(f'Found {words_count} total words')
	print('--------- Character Count -------')
	for char_count in chars:
		print(f'{char_count["char"]}: {char_count["num"]}')
	print('============= END ===============')

def main():
	args = sys.argv
	if len(args) < 2:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)
		return

	filepath = args[1]
	file_contents = get_book_text(filepath)

	words_number = count_words(file_contents)
	chars_count = count_chars(file_contents)
	chars_formated = format_chars(chars_count)

	print(pretty_print(filepath, chars_formated, words_number))

main()