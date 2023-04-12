import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--problem")

args = parser.parse_args()

problem_num = args.problem

if not problem_num.isnumeric():
  print(f"Invalid problem number: '{problem_num}'")
  raise SystemExit(1)

solution_file = Path(f'solutions/p{problem_num}.py')
test_file = Path(f'tests/test_p{problem_num}.py')

if solution_file.exists():
  print(f"Solution file for problem #{problem_num} already exists")
  raise SystemExit(1)

if test_file.exists():
  print(f"Solution file for problem #{problem_num} already exists")
  raise SystemExit(1)

    
solution_file.touch()
solution_scaffold = \
f'''\
from solutions.cli import run

def compute(param):
  return 'ADD FUNCTIONS TO COMPUTE ANSWER AND ADD CALL HERE'

if __name__ == "__main__":
    run(compute, 'REPLACE WITH SUITABLE DEFAULT VALUE')
    
'''
solution_file.write_text(solution_scaffold)

test_scaffold = \
f'''\
import pytest
import solutions.p{problem_num} as p{problem_num}

def test_p{problem_num}():
  pytest.skip("add tests for solution here")

'''
test_file.write_text(test_scaffold)

print(f'Generated solution and test files for Problem #{problem_num}')
