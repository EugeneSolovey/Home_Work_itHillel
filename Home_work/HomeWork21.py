'''Создать класс "налоговой системы", у которой будет метод, что принимает набор предпринимателей и для каждого выводит сумму налогов, которую он должен заплатить за 1 квартал.
Так же тут нужны будут классы предпринимателей, которые могут отличаться в зависимости от группы ФОП, которую они выберут:
Если что, ЕСВ (единый социальный взнос) сейчас - 1430 грн.
(если что - реализуйте только формулу по налогам и лимиты, не изучайте все нюансы этих групп)
У предпринимателя должен быть метод "подать отчетность", который будет сохранять как атрибуты 2 суммы - оборот и расходы по бизнесу. Потом пригодятся в подсчете налогов.
Продумайте еще что делать, если оборот предпринимателя превысил допустимый лимит.
Остальные атрибуты и методы - на усмотрение. Подумайте, где пропишете логику подсчета налогов для каждой группы :)
В конце надо создать N ФОПов, подать отчетность за них, и передать их всех на подсчет налогов.'''

import abc
from abc import ABC

minimum_wage = 6500
subsistence_minimum=2600


class TaxSystem:
    def __init__(self, name: str, income: float, expenses: float):
        self.name = name # имя предпринимателя
        self.income = income # Оборот предпринимателя
        self.expenses = expenses # Расходы по бизнесу
        self.tax = 0 # Налог за один квартал
        self.revenue_limit = 0 # Лимит на оборот
        self.tax_rate = 0 # Ставка налога за один квартал

    def __repr__(self):
        return f'{self.name} {self.income} {self.expenses} {self.tax}' # вывод в консоль

    @abc.abstractmethod
    def tax_calculation(self): # Подсчет налога
        pass


class FOP1Tax:
    def __init__(self, revenue_limit: float, tax_rate: float):
        return 1000000, (0.22 * minimum_wage + 0.1 * subsistence_minimum)



class FOP2Tax:
    def __init__(self, revenue_limit: float, tax_rate: float) -> None:
        self.revenue_limit = revenue_limit
        self.tax_rate = tax_rate

        self.revenue_limit = 5000000
        self.tax_rate = 0.22 * minimum_wage + 0.2 * minimum_wage


class FOP3TaxVAT:
    def __init__(self, revenue_limit: float, tax_rate: float):
        self.revenue_limit = revenue_limit
        self.tax_rate = tax_rate

        self.revenue_limit = 7000000
        self.tax_rate = 0.03 * income + (income - expenses) / 6


class FOP3TaxNoVAT:
    def __init__(self, revenue_limit: float, tax_rate: float):
        self.revenue_limit = revenue_limit
        self.tax_rate = tax_rate

        self.revenue_limit = 7000000
        self.tax_rate = 0.05 * income #


class Calculator(TaxSystem):
    def tax_calculation(self):
        if self.revenue_limit/365*92 < self.income:
            self.tax = self.tax_rate
        else:
            self.tax = self.tax_rate + (self.income - self.revenue_limit / 365 * 92) * 0.15


class FOP1(TaxSystem, FOP1Tax):
    def tax_calculation(self):
        self.tax = self.tax_rate


class FOP2( TaxSystem, FOP2Tax, ABC ):
    pass


class FOP3(TaxSystem, FOP3TaxVAT):
    pass


class FOP3NoVAT(TaxSystem, FOP3TaxNoVAT):
    pass




first_fop = FOP1('ФОП Петров', 1000000, 855555)
second_fop = FOP2('ФОП Иванов', 5000000, 0)

print(first_fop)
print(second_fop)