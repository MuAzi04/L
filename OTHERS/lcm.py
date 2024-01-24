def prime_eratosthenes(n):
    nonprime_list = []
    for i in range(2, n+1):
        if i not in nonprime_list:
            print(i)
            for j in range(i*i, n+1, i):
                nonprime_list.append(j)
    # print(nonprime_list)

prime_eratosthenes(100)

# arr = []
# n = int(input("Enter the size: "))
# for i in range(n):
#     arr[i] = i + 1

# index = 0

# for number in arr:
#     if (number % prime_numbers[index] == 0):
#         number /= prime_numbers[index]
    




# 1 2 3 4 5 6 7 8 9 10

# 2   1 1 3 2 5 3 7 4 9 5
# 2   1 1 3 1 5 3 7 2 9 5
# 2   1 1 3 1 5 3 7 1 9 5
# 3   1 1 1 1 5 1 7 1 3 5
# 3   1 1 1 1 5 1 7 1 1 5
# 5   1 1 1 1 1 1 7 1 1 1
# 7   1 1 1 1 1 1 1 1 1 1