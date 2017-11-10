def sum_multiples(max):
  nums = []
  for num in range(1, max):
    if (num % 3 == 0 or num % 5 == 0):
      nums.append(num)

  return(sum(nums))

print(sum_multiples(10))
print(sum_multiples(1000))