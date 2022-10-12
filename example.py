from operator import truediv
from xmlrpc.server import SimpleXMLRPCServer


def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


def isPrime(a):
    aux = True
    for i in range(2, a - 1):
        if (a % i == 0):
            aux = False
            break
    return aux


if __name__ == '__main__':
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Conectado na porta 8000...")
    server.register_function(sum, "sum")
    server.register_function(subtract, "subtract")
    server.register_function(multiply, "multiply")
    server.register_function(division, "division")
    server.register_function(isPrime, "isPrime")
    server.serve_forever()


# import xmlrpc.client

# with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
#     print("A soma é: %s" % str(proxy.sum(3, 5)))
#     print("A subtracao é: %s" % str(proxy.subtract(5, 3)))
#     print("A multiplicacao é: %s" % str(proxy.multiply(5, 3)))
#     print("A divisao é: %s" % str(proxy.subtract(6, 3)))
#     print(": %s" % str(proxy.isPrime(5, 3)))
    