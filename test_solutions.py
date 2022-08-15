import p1

def test_p1():
  example = p1.compute(10)
  assert example == 23

  answer = p1.compute(1000)

  assert answer == 233168
  
import p2

def test_p2():
  example = p2.compute(100)
  assert example == 2 + 8 + 34
  answer = p2.compute(4_000_000)
  assert answer == 4613732

import p3

def test_p3():
  example = p3.compute(13195)
  assert example == 29
  answer = p3.compute(600851475143)
  assert answer == 6857

import p4

def test_p4():
  example = p4.compute(2)
  assert example == 9009
  answer = p4.compute(3)
  assert answer == 906609

import p5

def test_p5():
  example = p5.compute(10)
  assert example == 2520
  answer = p5.compute(20)
  assert answer == 232792560

import p6

def test_p6():
  example = p6.compute(10)
  assert example == 2640
  answer = p6.compute(100)
  assert answer == 25164150

import p7

def test_p7():
  example = p7.compute(6)
  assert example == 13
  answer = p7.compute(10_001)
  assert answer == 104743
