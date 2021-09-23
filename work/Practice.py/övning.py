
# steel = int(input())
# my_list = []
# for i in range(steel):
#     my_list.append(int(input()))
#     result = (sum(my_list) - (steel -1))

# print(result)

""""""
# word = str(input())
# print((word + ' ') * 3)

""""""

# line = input()
# a, b = line.split()
# a = int(a)
# b = int(b)
# print(a+b)

""""""
# stones = int(input())

# if (stones % 2 == 0):
#     print('Bob')
# else:
#     print('Alice')

""""""
# pressed = int(input())
# values = [int(input()) for a in range(pressed)]
# if (pressed % 2 == 0):
    
#     result = [b-a for a,b in list(zip(values, values[1:]))[::2]]
#     print(sum(result))
# else:
#     print('still running')

""""""
# x = input()
# a, b = x.split()
# a = int(a)
# b = int(b)
# value = [str(input()) for i in range(a)]
# print(b)

""""""
# n,k = input().split()
# n = int(n)
# k = int(k)
# r = [int(input()) for i in range(k)]
# min = (((n-k)*(-3)) + sum(r))/n
# max = (((n-k)*3) + sum(r))/n
# print(min, max)
       
        
""""""
# x = str(input())
# letter = 'e'
# i = x.replace(letter, letter*2)
# print(i)


""""""
# temp = int(input())
# result = 0
# values = [int(i) for i in input().split()]
# for x in values:
#     if x < 0:
#         result += 1
# print(result)

""""""
# statues = int(input())
# days = 0
# printer = 1
# while printer < statues:
#     printer = printer * 2
#     days += 1
# days += 1
# print(days)

""""""

# n = int(input())
# result = 0.0
# for x in range(n):
#     value = [float(x) for x in input().split()]
#     result += value[0] * value[1]
# print("{0:.3f}".format(result))

""""""
# def main():
#     n = int(input())
#     result = 0
#     i = 0
#     while (i < n):
#         nr = int(input()) 
#         base = nr // 10
#         lastDig = int(repr(nr)[-1])
#         result = result + (base**lastDig)
#         i += 1
#     print(result)


# main()

""""""


# def duplicate():
#     s = str(input().upper())
#     s = s.split()
#     s_list = set(s)
#     if len(s_list) != len(s):
#         print('no')
            
#     else:
#         print('yes')
            
# duplicate()

