from typing import List
from my_project.auth.dao.food_machines_dao import FoodMachineDao
from my_project.auth.domain.orders.FoodMachines import FoodMachine

class FoodMachineController:
    _dao = FoodMachineDao()

    def find_all(self) -> List[FoodMachine]:
        return self._dao.find_all()

    def find_by_id(self, machine_id: int) -> FoodMachine:
        return self._dao.find_by_id(machine_id)

    def create(self, food_machine: FoodMachine) -> None:
        self._dao.create(food_machine)

    def update(self, machine_id: int, food_machine: FoodMachine) -> None:
        self._dao.update(machine_id, food_machine)

    def delete(self, machine_id: int) -> None:
        self._dao.delete(machine_id)
