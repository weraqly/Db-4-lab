# MenuController.py
from typing import List
from my_project.auth.dao.menu_dao import MenuDao
from my_project.auth.domain.orders.Menu import Menu

class MenuController:
    _dao = MenuDao()

    def find_all(self) -> List[Menu]:
        return self._dao.find_all()

    def create(self, menu: Menu) -> None:
        self._dao.create(menu)

    def find_by_id(self, menu_id: int) -> Menu:
        return self._dao.find_by_id(menu_id)

    def update(self, menu_id: int, menu: Menu) -> None:
        self._dao.update(menu_id, menu)

    def delete(self, menu_id: int) -> None:
        self._dao.delete(menu_id)
