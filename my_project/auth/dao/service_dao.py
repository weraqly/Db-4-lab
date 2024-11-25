from typing import List
from my_project import db
from my_project.auth.domain.orders.Services import Services

class ServiceDao:
    """
    DAO для роботи з таблицею 'service'.
    """

    @staticmethod
    def create(service: Services) -> None:
        """
        Додає новий запис обслуговування до бази даних.
        :param service: об'єкт Service, який потрібно додати
        """
        db.session.add(service)
        db.session.commit()

    @staticmethod
    def update(service_id: int, service: Services) -> None:
        """
        Оновлює існуючий запис обслуговування в базі даних.
        :param service_id: ID обслуговування, яке потрібно оновити
        :param service: об'єкт Service з оновленими даними
        """
        db.session.query(Services).filter_by(id=service_id).update({
            "service_type": service.service_type,
            "service_date": service.service_date,
            "food_machine_id": service.food_machine_id,
            "employees_id": service.employees_id,
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[Services]:
        """
        Повертає всі записи обслуговування з бази даних.
        :return: список об'єктів Service
        """
        return db.session.query(Services).all()

    @staticmethod
    def find_by_id(service_id: int) -> Services:
        """
        Знаходить запис обслуговування за ID.
        :param service_id: ID обслуговування
        :return: об'єкт Service
        """
        return db.session.query(Services).filter_by(id=service_id).first()

    @staticmethod
    def find_by_type(service_type: str) -> List[Services]:
        """
        Знаходить записи обслуговування за типом.
        :param service_type: значення типу обслуговування
        :return: список об'єктів Service з відповідним типом
        """
        return db.session.query(Services).filter_by(service_type=service_type).all()

    @staticmethod
    def find_by_date(service_date: str) -> List[Services]:
        """
        Знаходить записи обслуговування за датою.
        :param service_date: значення дати обслуговування
        :return: список об'єктів Service з відповідною датою
        """
        return db.session.query(Services).filter_by(service_date=service_date).all()
