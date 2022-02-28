age = 9
name = 'Vladimir'
money = 150.1
is_admin = True
accounnts = [2, 10, name, is_admin]  # list
accounts_tuple = (2, 10, name, is_admin)  # tuple
bank_accounts = {'Alice': 200.10, name: 100.10}  # dict
print('Hi', name)

# print(age / 2)
# print(age // 2)
# print(age % 2)  # Деление по модулю, выполняем для определения остатка или для определение кратное ли число 2
# print(age ** 2)

name = input('Input name:')
print(age + 10)
print(accounnts[1], bank_accounts['Alice'])
