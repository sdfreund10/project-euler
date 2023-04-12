from solutions.cli import run

digit_names = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
}

def generate_english_string(num):
  parts = []
  thousands_digit = num // 1000
  if thousands_digit > 0:
    parts += [
      digit_names[thousands_digit],
      'thousand'
    ]

  hundreds_digit = (num % 1000) // 100

  if hundreds_digit > 0:
    parts += [
      digit_names[hundreds_digit],
      'hundred'
    ]

    

  tens = (num % 100) // 10 * 10
  ones = num % 10

  if len(parts) and (tens or ones):
    parts.append('and')

  if num % 100 < 20 and num % 100 > 0:
    parts.append(digit_names[num % 100])
    return parts

  if tens > 0:
    parts.append(digit_names[tens])

  if ones > 0:
    parts.append(digit_names[ones])

  return parts

def length_of_words(num):
  return sum([len(word) for word in generate_english_string(num)])


def compute(end_num):
  lengths = [
    length_of_words(i) for i in range(1, end_num + 1)
  ]
  return sum(lengths)

if __name__ == "__main__":
    run(compute, 5)