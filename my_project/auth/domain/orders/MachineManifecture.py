from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class MachineManifecture(db.Model, IDto):
    __tablename__ = "machine_manifecture"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MachineManifecture:
        return MachineManifecture(**dto_dict)