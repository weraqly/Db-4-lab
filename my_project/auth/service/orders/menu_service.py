# MenuService.py
from typing import List
from my_project.auth.dao.orders import menu_dao
from my_project.auth.service.orders.general_service import GeneralService
from my_project.auth.domain import Menu

class MenuService(GeneralService):
    _dao = menu_dao

    def create(self, menu: Menu) -> None:
        self._dao.create(menu)

    def update(self, menu_id: int, menu: Menu) -> None:
        self._dao.update(menu_id, menu)

    def get_all_menus(self) -> List[Menu]:
        return self._dao.find_all()

    def get_menu_by_id(self, menu_id: int) -> Menu:
        return self._dao.find_by_id(menu_id)

