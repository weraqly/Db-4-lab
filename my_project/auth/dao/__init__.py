"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Orders DB imports for DAOs corresponding to each entity, using HelloWorld naming
# Orders DB imports for DAOs corresponding to each entity

from my_project.auth.dao.orders.service_dao import ServiceDao
from my_project.auth.dao.orders.adress_machine_dao import AddressMachineDao
from my_project.auth.dao.orders.employees_dao import EmployeesDao
from my_project.auth.dao.orders.employess_address_dao import EmployessAddressDao
from my_project.auth.dao.orders.food_machines_dao import FoodMachineDao
from my_project.auth.dao.orders.loading_machine_dao import LoadingMachineDao
from my_project.auth.dao.orders.loading_snacks_dao import LoadingSnacksDao
from my_project.auth.dao.orders.machine_manifecture_dao import MachineManifectureDao
from my_project.auth.dao.orders.menu_dao import MenuDao
from my_project.auth.dao.orders.snacks_dao import SnacksDao
from my_project.auth.dao.orders.snacks_creator_dao import SnacksCreatorDao
from my_project.auth.dao.orders.money_loading_dao import MoneyLoadingDao
from my_project.auth.dao.orders.money_transfer_dao import MoneyTransferDao
from my_project.auth.dao.orders.saled_snacks_dao import SaledSnacksDao
from my_project.auth.dao.orders.currency_denomination_dao import CurrencyDenominationsDao

# Initialize DAOs for each entity with HelloWorld naming style


serviceDao = ServiceDao()
addressMachineDao = AddressMachineDao()
employeesDao = EmployeesDao()
employessAddressDao = EmployessAddressDao()
foodMachinesDap = FoodMachineDao()
loadingMachineDao = LoadingMachineDao()
loadingSnacksDao = LoadingSnacksDao()
machineManifectureDao = MachineManifectureDao()
menuDao = MenuDao()
snacksDao = SnacksDao()
snacksCreatorDao = SnacksCreatorDao()
moneyLoadingDao = MoneyLoadingDao()
moneyTransferDao = MoneyTransferDao()
saledSnacksDao = SaledSnacksDao()
currencyDenominationsDao = CurrencyDenominationsDao()

