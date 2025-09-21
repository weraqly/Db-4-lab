# MoneyTransferService.py
from typing import List
from my_project.auth.dao.orders import money_transfer_dao
from my_project.auth.service.orders.general_service import GeneralService
from my_project.auth.domain import MoneyTransfer

class MoneyTransferService(GeneralService):
    _dao = money_transfer_dao

    def create(self, transfer: MoneyTransfer) -> None:
        self._dao.create(transfer)

    def update(self, transfer_id: int, transfer: MoneyTransfer) -> None:
        self._dao.update(transfer_id, transfer)

    def get_all_money_transfers(self) -> List[MoneyTransfer]:
        return self._dao.find_all()

    def get_money_transfer_by_id(self, transfer_id: int) -> MoneyTransfer:
        return self._dao.find_by_id(transfer_id)

