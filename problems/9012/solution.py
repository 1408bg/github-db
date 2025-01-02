n = int(input())

for i in range(0, n):
  s = input()
  stack = []
  try:
    for j in range(0, len(s)):
      if s[j] == '(':
        stack.append(0)
      else:
        stack.pop()
    if len(stack) != 0:
      raise Error()
    print('YES')      
  except:
    print('NO')          