print(43*'\033[30;1m=')
print('\033[1;34m S E Q U E N C I A  D E  F I B O N A C C I')
print(43*'\033[1;30m=')
print('\033[m\033[32mOpa! Seja Bem Vindo(a) ao meu pequeno\nprograma que irá te mostrar a quantidade\nde termos que você quiser da sequência\nde \033[1mFibonacci\033[m.')
qtermos = int(input('\033[30;1mQuantos termos você deseja ver? '))
print('Os termos são:')
print('0 -> 0 -> 1', end=' -> ')
t1 = 1
t2 = 1
qtermos -= 3
for c in range(0, qtermos):
    t3 = t1+t2
    print(f'{t3} ', end='-> ')
    t1 = t2
    t2 = t3
print('FIM!')
print(43*'\033[1;30m=')


