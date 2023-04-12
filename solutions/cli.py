import sys
import time

def run(function, default):
  start_time = time.time()
  args = sys.argv
  arg = default
  if args and len(args) > 1:
    arg = int(args[1])
  result = function(arg)
  print('Answer:', result)
  total_time = (time.time() - start_time)
  print('Took', total_time, 'seconds')