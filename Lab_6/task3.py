def modify_set(A, x):
    if x not in A:
        A.add(x)
    else:
        A.discard(x)
    return A

def get_set_A_from_user():
    try:
        A = set(input("Введіть елементи множини A через пробіл: ").split())
        return A
    except ValueError:
        print("Будь ласка, введіть символи.")

def get_x_from_user():
    try:
        x = input("Введіть символ x: ")
        return x
    except ValueError:
        print("Будь ласка, введіть символ x.")

A = get_set_A_from_user()
x = get_x_from_user()
B = modify_set(A, x)

if isinstance(B, set):
    print("Множина B:", B)
else:
    print("Множина B:", set(B))
