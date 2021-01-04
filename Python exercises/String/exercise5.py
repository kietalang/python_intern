def swap(a, b):
  a = b[:2] + a[2:]
  b = a[:2] + b[2:]

  return a + ' ' + b

print(swap('abc', 'xyz'))