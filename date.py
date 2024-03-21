from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        
        def __init__(self, day: int, month: int, year: int):
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
        resultado = False
        if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
            resultado = True
        return resultado

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        if month == "FEBRERO":
            if Date.is_leap_year(year):
                return 29  


    def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        ...

    @property
    def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        ...

    @property
    def is_weekend(self) -> bool:
        ...

    @property
    def short_date(self) -> str:
        '''02/09/2003'''
        ...

    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        ...

    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        ...

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        ...

    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...

    def __eq__(self, other) -> bool:
        ...
