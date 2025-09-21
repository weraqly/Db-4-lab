# MoneyTransferController.py
from typing import List
from my_project.auth.dao import MoneyTransferDao
from my_project.auth.domain import MoneyTransfer

class MoneyTransferController:
    _dao = MoneyTransferDao()

    def find_all(self) -> List[MoneyTransfer]:
        return self._dao.find_all()

    def create(self, transfer: MoneyTransfer) -> None:
        self._dao.create(transfer)

    def find_by_id(self, transfer_id: int) -> MoneyTransfer:
        return self._dao.find_by_id(transfer_id)

    def update(self, transfer_id: int, transfer: MoneyTransfer) -> None:
        self._dao.update(transfer_id, transfer)

    def delete(self, transfer_id: int) -> None:
        self._dao.delete(transfer_id)
