#Calculatrice en python avec division par 00 annuler 
print("-Calculatrice scientifique en cours d'activation...")
print("-Calculatrice en cours d'activation :45%")
print("-Calculatrice en cours d'activation :67%")
print("-Calculateice en cours d'activation :89%")
print("-Caculatrice activé..100%")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Nuh uh la division par zero n'est pas permise")
    return x / y

print("-Sélectionnez l'opération xD:")
print("1. Add (somme +)")
print("2. Subtract (moins -)")
print("3. Multiply (Multiplication ×)")
print("4. Divide (Division ÷)")

choice = input("-Entrez votre choix (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("-Entrez le premier nombre: "))
    num2 = float(input("-Entrez le deuxième nombre: "))

    if choice == '1':
        print("Result:", num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print("Result:", num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print("Result:", num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        try:
            print("Result:", num1, "/", num2, "=", divide(num1, num2))
        except ValueError as e:
            print("Error:", e)
else:
    print("Mauvaise manipulation")



