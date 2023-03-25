from cli import run

small_triangle = [
       [3],
     [7, 4],
    [2, 4, 6],
  [8, 5, 9, 3]
]

# len 15
triangle = [
                  [75],
                 [95,64],
                [17,47,82],
              [18,35,87,10],
             [20,4,82,47,65],
            [19,1,23,75,3,34],
           [88,2,77,73,7,63,67],
          [99,65,4,28,6,16,70,92],
         [41,41,26,56,83,40,80,70,33],
       [41,48,72,33,47,32,37,16,94,29],
      [53,71,44,65,25,43,91,52,97,51,14],
     [70,11,33,28,77,73,17,78,39,68,17,57],
    [91,71,52,38,17,14,91,43,58,50,27,29,48],
   [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
  [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

# collapse two rows by finding the larger sum for a given node and the two below it
def collapse_rows(upper_row, lower_row):
  collapsed = []
  for i, num in enumerate(upper_row):
    collapsed.append(max(num + lower_row[i], num + lower_row[i+1]))

  return collapsed

def compute_max_path(pyramid: list[list[int]]):
  if len(pyramid) == 1:
    return pyramid[0][0]

  new_bottom_row = collapse_rows(pyramid[-2], pyramid[-1])
  
  return compute_max_path(
    pyramid[0:-2] + [new_bottom_row]
  )

def compute(triangle_size: int):
  if triangle_size < 1 or triangle_size > len(triangle):
    raise RuntimeError('Invalid triangle size')

  if triangle_size < 5:
    return compute_max_path(small_triangle[0:triangle_size])

  return compute_max_path(triangle[0:triangle_size])

if __name__ == "__main__":
    run(compute, 4)