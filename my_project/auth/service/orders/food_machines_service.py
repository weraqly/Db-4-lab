from typing import List
from my_project.auth.dao import FoodMachineDao
from my_project.auth.domain import FoodMachine

class FoodMachineService:
    _dao = FoodMachineDao()

    def create(self, food_machine: FoodMachine) -> None:
        self._dao.create(food_machine)

    def update(self, machine_id: int, food_machine: FoodMachine) -> None:
        self._dao.update(machine_id, food_machine)

    def find_all(self) -> List[FoodMachine]:
        return self._dao.find_all()

    def find_by_id(self, machine_id: int) -> FoodMachine:
        return self._dao.find_by_id(machine_id)

    def delete(self, machine_id: int) -> None:
        self._dao.delete(machine_id)
