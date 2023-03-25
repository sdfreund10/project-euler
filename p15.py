from cli import run

# coord: num_paths
steps_to_end = {}

def num_steps_to_end(start_coords: tuple[int, int], end_coords: tuple[int, int]):
  # if at end of array, it took 1 step to get here from previous position
  if start_coords == end_coords:
    return 1

  # check cache for existing values to reduce duplication
  if start_coords in steps_to_end:
    return steps_to_end[start_coords]

  steps_from_right = 0
  # can move right if not at far end of lattice
  if start_coords[0] != end_coords[0]:
    steps_from_right = num_steps_to_end((start_coords[0] + 1, start_coords[1]), end_coords)

  steps_from_left = 0
  # can move down if not at far end of lattice
  if start_coords[1] != end_coords[1]:
    steps_from_left = num_steps_to_end((start_coords[0], start_coords[1] + 1), end_coords)

  steps_to_end[start_coords] = steps_from_right + steps_from_left
  return steps_from_right + steps_from_left


def compute(grid_size: int):
  # clear cache from last run
  steps_to_end.clear()
  return num_steps_to_end((0,0), (grid_size, grid_size))

if __name__ == "__main__":
    run(compute, 2)
