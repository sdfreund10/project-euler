def generate_fib(max):
  nums = [1, 2]
  while nums[-1] + nums[-2] < max:
    nums.append(nums[-1] + nums[-2])

  return(nums)

def select_even(nums):
  return([x for x in nums if x % 2 == 0])

print(generate_fib(10))
print(sum(select_even(generate_fib(4000000))))