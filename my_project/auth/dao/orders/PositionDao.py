from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Position import Position


class PositionDAO(GeneralDAO):
    _domain_type = Position

    def create(self, position: Position) -> None:
        self._session.add(position)
        self._session.commit()

    def find_all(self) -> List[Position]:
        return self._session.query(Position).all()