
# TODO - write has_teen
def has_teen(a, b, c):
	if a >= 13 and a <= 19:
		return True

	if b >= 13 and b <= 19:
		return True

	if c >= 13 and c <= 19:
		return True

	return False

print has_teen(1, 1, 1)    # expect False
print has_teen(20, 20, 20) # expect False
print has_teen(14, 1, 1)   # expect True
print has_teen(1, 14, 1)   # expect True
print has_teen(1, 1, 14)   # expect True
print has_teen(14, 14, 14) # expect True
print has_teen(18, 16, 14) # expect True

print

def not_string(str):
	lower_str = str.lower()
	if lower_str.startswith("not"):
		return str + "not"

	return "not" + str

print not_string("Not Apples")
print not_string("Oranges")

print

def icy_hot(x, y):
	hot = False
	cold = False

	if x > 100 or y > 100:
		hot = True

	if x < 0 or y < 0:
		cold = True

	if cold and hot:
		return True

	return False

print icy_hot(50, 50) # expect False
print icy_hot(110, -10) # expect True
print icy_hot(-10, 110) # expect True

print

def closer_to(target, guess1, guess2):
	difference1 = abs(target - guess1)
	difference2 = abs(target - guess2)

	if difference1 < difference2:
		return guess1

	if difference1 > difference2:
		return guess2

	if difference1 == difference2:
		return 0

print closer_to(10, 5, 6) # expect 6
print closer_to(10, 7, 5) # expect 7
print closer_to(10, 5, 5) # expect 0
print closer_to(10, 12, 11) # expect 11

print

def two_as_one(int1, int2, int3):
	if int1 + int2 == int3:
		return True

	if int1 + int3 == int2:
		return True

	if int2 + int3 == int1:
		return True

	return False

print two_as_one(1, 1, 2)  # expect True
print two_as_one(1, 2, 1)  # expect True
print two_as_one(2, 1, 1)  # expect True
print two_as_one(1, 1, 10) # expect False

print

# TODO - write pig_latinify
def pig_latinify(word):
	text = word.strip()
	lower_word = text.lower()
	starts_vowel = False
	if lower_word.startswith("a"):
		starts_vowel = True

	if lower_word.startswith("e"):
		starts_vowel = True

	if lower_word.startswith("i"):
		starts_vowel = True

	if lower_word.startswith("o"):
		starts_vowel = True

	if lower_word.startswith("u"):
		starts_vowel = True

	if starts_vowel:
		return word + "way"

	if not starts_vowel:
		return text[1:] + text[:1] + "ay"

print pig_latinify("Apple")
print pig_latinify(" Apple ")
print pig_latinify(" apple")
print pig_latinify("Car")
print pig_latinify(" Car")
print pig_latinify("stack")
