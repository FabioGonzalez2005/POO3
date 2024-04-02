from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        self.day = day
        self.month = month
        self.year = year
        if day <= 0 or day > 31:
            day = 1
        if month <= 0 or month > 12:
            month = 1
        if year < 1900 or year > 2050:
            year = 1900

    @staticmethod
    def is_leap_year(year: int) -> bool:
        '''Calcular si el año es bisiesto'''
        resultado = False
        if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
            resultado = True
        return resultado

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        '''Calcular cuántos días tiene el mes'''
        if month == "FEBRERO":
            if Date.is_leap_year(year) == True:
                return 29  
            else:
                return 28
        elif month in ["ENERO", "MARZO", "MAYO", "JULIO", "AGOSTO", "OCTUBRE", "DICIEMBRE"]:
            return 31
        else:
            return 30

    def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        for x in range(1900, self.year):
            if Date.is_leap_year(x):
                days += 366
            else:
                days += 365
        for y in range(1, self.month):
            days += Date.days_in_month(m, self.year)
        days += self.day - 1
        return days

    @property
    def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        day = self.get_delta_days()
        return (day + 1) % 7

    @property
    def is_weekend(self) -> bool:
        '''Saber si el día es entre lunes y viernes.'''
        if self.weekday > 5:
            return True
        else:
            return False
        
    @property
    def short_date(self) -> str:
        '''02/09/2003'''
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __str__(self):
        '''Ejemplo: MARTES 2 DE SEPTIEMBRE DE 2003'''

        dias_semana = ["DOMINGO", "LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SABADO"]
        meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
        return f"{dias_semana[self.weekday]} {self.weekday} DE {meses[self.month]} DE {self.year}"

    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        ...

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        ...

    def __lt__(self, other: Date) -> bool:
        return self.get_delta_days() < other.get_delta_days()

    def __gt__(self, other: Date) -> bool:
        return self.get_delta_days() > other.get_delta_days()

    def __eq__(self, other: Date) -> bool:
        return self.get_delta_days() == other.get_delta_days()