import p1

def test_p1():
  example = p1.compute(10)
  assert example == 23
  answer = p1.compute(1000)
  print('Problem 1 solution:', answer)
  assert answer == 233168
  
import p2

def test_p2():
  example = p2.compute(100)
  assert example == 2 + 8 + 34
  answer = p2.compute(4_000_000)
  print('Problem 2 solution:', answer)
  assert answer == 4613732

import p3

def test_p3():
  example = p3.compute(13195)
  assert example == 29
  answer = p3.compute(600851475143)
  print('Problem 3 solution:', answer)
  assert answer == 6857

import p4

def test_p4():
  example = p4.compute(2)
  assert example == 9009
  answer = p4.compute(3)
  print('Problem 4 solution:', answer)
  assert answer == 906609

import p5

def test_p5():
  example = p5.compute(10)
  assert example == 2520
  answer = p5.compute(20)
  print('Problem 5 solution:', answer)
  assert answer == 232792560

import p6

def test_p6():
  example = p6.compute(10)
  assert example == 2640
  answer = p6.compute(100)
  print('Problem 6 solution:', answer)
  assert answer == 25164150

import p7

def test_p7():
  example = p7.compute(6)
  assert example == 13
  answer = p7.compute(10_001)
  print('Problem 7 solution:', answer)
  assert answer == 104743

import p8

def test_p8():
  example = p8.compute(4)
  assert example == 5832
  answer = p8.compute(13)
  print('Problem 8 solution:', answer)
  assert answer == 23514624000

import p9

def test_p9():
  example = p9.compute(12)
  assert example == 3 * 4 * 5
  answer = p9.compute(1000)
  print('Problem 9 solution:', answer)
  assert answer == 31875000


import p10

def test_p10():
  example = p10.compute(10)
  assert example == 17
  answer = p10.compute(2_000_000)
  print('Problem 10 solution:', answer)
  assert answer == 142913828922

import p11

def test_p11():
  example = p11.compute(1)
  assert example == 99
  answer = p11.compute(4)
  print('Problem 11 solution:', answer)
  assert answer == 70600674
import p12

def test_p12():
  example = p12.compute(5)
  assert example == 28
  answer = p12.compute(500)
  print('Problem 12 solution:', answer)
  assert answer == 76576500


import p13

def test_p13():
  example = p13.compute(2)
  assert example == 55
  answer = p13.compute(10)
  print('Problem 13 solution:', answer)
  assert answer == 5537376230

import p14

def test_p14():
  example = p14.generate_collatz_sequence(13)
  assert example == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
  answer = p14.compute(1000000)
  print('Problem 14 solution:', answer)
  assert answer == (837799, 525)

import p15

def test_p15():
  example = p15.compute(2)
  assert example == 6
  answer = p15.compute(20)
  print('Problem 15 solution:', answer)
  assert answer == 137846528820

import p16

def test_p16():
  example = p16.compute(15)
  assert example == 26
  answer = p16.compute(1000)
  print('Problem 16 solution:', answer)
  assert answer == 1366

import p17

def test_p17():
  example = p17.compute(5)
  assert example == 19
  assert p17.length_of_words(342) == 23
  assert p17.length_of_words(115) == 20
  answer = p17.compute(1000)
  print('Problem 17 solution:', answer)
  assert answer == 21124

import p18

def test_p18():
  example = p18.compute(4)
  assert example == 23
  answer = p18.compute(15)
  print('Problem 18 solution:', answer)
  assert answer == 1074