class Convertidor:
    def __init__(self, entero, romano) -> None:
        self.entero = entero
        self.romano = romano

    def convertirARomano(self):
        numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        numeral = ''
        i = 0
        while self.entero > 0:
            for x in range(self.entero // numeros[i]):
                numeral += numerales[i]
                self.entero -= numeros[i]
            i += 1
        return numeral

    def convertirAEntero(self):
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        entero = 0
        for i in range(len(self.romano)):
            if i > 0 and romanos[self.romano[i]] > romanos[self.romano[i - 1]]:
                entero += romanos[self.romano[i]] - 2 * romanos[self.romano[i - 1]]
            else:
                entero += romanos[self.romano[i]]
        return entero

if __name__ == "__main__":
    convertidor = Convertidor(60, 'LX')
    print(convertidor.convertirARomano())
    print(convertidor.convertirAEntero())