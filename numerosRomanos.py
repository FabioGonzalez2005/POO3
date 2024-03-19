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
            for _ in range(self.entero // numeros[i]):
                numeral += numerales[i]
                self.entero -= numeros[i]
            i += 1
        return numeral

