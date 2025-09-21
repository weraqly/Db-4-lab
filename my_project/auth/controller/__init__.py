# правильні прямі імпорти з модулів у controller/orders
from my_project.auth.controller.orders.adress_machine_controller import AddressMachineController
from my_project.auth.controller.orders.currency_denomination_controller import CurrencyDenominationsController
from my_project.auth.controller.orders.employees_address_controller import EmployessAddressController
from my_project.auth.controller.orders.employees_controller import EmployeesController
from my_project.auth.controller.orders.food_machine_controller import FoodMachineController
from my_project.auth.controller.orders.loading_machine_controller import LoadingMachineController
from my_project.auth.controller.orders.loading_snacks_controller import LoadingSnacksController
from my_project.auth.controller.orders.machine_manifecture_controller import MachineManifectureController
from my_project.auth.controller.orders.menu_controller import MenuController
from my_project.auth.controller.orders.money_loading_controller import MoneyLoadingController
from my_project.auth.controller.orders.money_transfer_controller import MoneyTransferController
from my_project.auth.controller.orders.saled_snacks_controller import SaledSnacksController
from my_project.auth.controller.orders.service_controller import ServiceController
from my_project.auth.controller.orders.snacks_controller import SnacksController
from my_project.auth.controller.orders.snacks_creator_controller import SnacksCreatorController


# Initialize controllers
addressMachineController = AddressMachineController()
currencyDenominationsController = CurrencyDenominationsController()
employessAddressController = EmployessAddressController()
employeesController = EmployeesController()
foodMachinesController = FoodMachineController()
loadingMachineController = LoadingMachineController()
loadingSnacksController = LoadingSnacksController()
machineManifectureController = MachineManifectureController()
menuController = MenuController()
moneyLoadingController = MoneyLoadingController()
moneyTransferController = MoneyTransferController()
saledSnacksController = SaledSnacksController()
serviceController = ServiceController()
snacksController = SnacksController()
snacksCreatorController = SnacksCreatorController()
