def get_product(nums: list[int]):
  product = 1
  for num in nums:
    product *= num
  return product
