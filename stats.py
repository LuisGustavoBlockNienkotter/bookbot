def count_words(text: str) -> int: 
	return len(text.split())

def count_chars(text: str) -> dict:
	chars = {}
	for c in text.lower():
		if c not in chars:
			chars[c] = 0
		chars[c] += 1
	return chars

def format_chars(chars: dict) -> list:
	chars_formated = []
	for c in chars.keys():
		chars_formated.append({
			'char': c,
			'num': chars[c]
		})

	chars_formated.sort(reverse=True, key=sort_on)
	return chars_formated

def sort_on(items):
	return items['num']