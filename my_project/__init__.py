import os
from http import HTTPStatus
import secrets
from typing import Dict, Any
from sqlalchemy import text

from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

# Константи для роботи з середовищем
SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

# Ініціалізація бази даних
db = SQLAlchemy()

todos = {}

def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """
    Створює Flask-додаток
    """
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)
    _init_trigger(app)
    from my_project.auth.route import register_routes
    register_routes(app)
    _init_swagger(app)
    create_dynamic_tables_procedure(app)
    _init_aggregate_money_transfer_function(app)
    _init_call_aggregate_money_transfer_procedure(app)
    _init_insert_employess_address_procedure(app)
    insert_into_loading_snacks(app, 1, 2, 10)
    _init_insert_into_loading_snacks_procedure(app)
    call_insert_employess_address_procedure(app)
    _init_insert_services_procedure(app)
    insert_service(app, "Maintenance", "2024-11-26 14:00:00", 1, 2)

    return app

#2а Параметризована вставка нових значень

def _init_insert_services_procedure(app: Flask) -> None:

    check_procedure_sql = """
    SELECT COUNT(*)
    FROM information_schema.ROUTINES
    WHERE ROUTINE_TYPE = 'PROCEDURE' AND ROUTINE_NAME = 'InsertIntoServices';
    """

    create_procedure_sql = """
    CREATE PROCEDURE InsertIntoServices(
        IN p_service_type VARCHAR(255),
        IN p_service_date DATETIME,
        IN p_food_machine_id INT,
        IN p_employees_id INT
    )
    BEGIN
        INSERT INTO services (service_type, service_date, food_machine_id, employees_id)
        VALUES (p_service_type, p_service_date, p_food_machine_id, p_employees_id);
    END;
    """

    with app.app_context():
        # Перевірка на існування процедури
        result = db.session.execute(text(check_procedure_sql)).scalar()
        if result == 0:  # Якщо процедура не існує
            db.session.execute(text(create_procedure_sql))
            db.session.commit()
            print("Procedure 'InsertIntoServices' created successfully.")
        else:
            print("Procedure 'InsertIntoServices' already exists.")


def insert_service(app: Flask, service_type: str, service_date: str, food_machine_id: int, employees_id: int) -> None:

    with app.app_context():
        try:
            db.session.execute(
                text("CALL InsertIntoServices(:service_type, :service_date, :food_machine_id, :employees_id)"),
                {
                    'service_type': service_type,
                    'service_date': service_date,
                    'food_machine_id': food_machine_id,
                    'employees_id': employees_id
                }
            )
            db.session.commit()
            print("New service inserted successfully.")
        except Exception as e:
            print(f"Error inserting service: {e}")

#2b Забезпечити реалізацію зв’язку М:М між 2ма таблицями
def _init_insert_into_loading_snacks_procedure(app: Flask) -> None:
    """
    Створює процедуру InsertIntoLoadingSnacks, якщо вона ще не існує.
    """
    check_procedure_sql = """
    SELECT COUNT(*)
    FROM information_schema.ROUTINES
    WHERE ROUTINE_TYPE = 'PROCEDURE' AND ROUTINE_NAME = 'InsertIntoLoadingSnacks';
    """

    create_procedure_sql = """
    CREATE PROCEDURE InsertIntoLoadingSnacks(
        IN p_loading_machine_id INT,
        IN p_snack_id INT,
        IN p_quantity_snacks INT
    )
    BEGIN
        -- Перевірка існування loading_machine
        IF NOT EXISTS (SELECT 1 FROM loading_machine WHERE id = p_loading_machine_id) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Loading machine ID does not exist';
        END IF;

        -- Перевірка існування snack
        IF NOT EXISTS (SELECT 1 FROM snacks WHERE id = p_snack_id) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Snack ID does not exist';
        END IF;

        -- Вставка запису в таблицю loading_snacks
        INSERT INTO loading_snacks (loading_machine_id, snack_id, quantity_snacks)
        VALUES (p_loading_machine_id, p_snack_id, p_quantity_snacks)
        ON DUPLICATE KEY UPDATE quantity_snacks = p_quantity_snacks;
    END;
    """

    with app.app_context():
        result = db.session.execute(text(check_procedure_sql)).scalar()
        if result == 0:
            db.session.execute(text(create_procedure_sql))
            db.session.commit()
            print("Procedure 'InsertIntoLoadingSnacks' created successfully.")
        else:
            print("Procedure 'InsertIntoLoadingSnacks' already exists.")


def insert_into_loading_snacks(app: Flask, loading_machine_id: int, snack_id: int, quantity_snacks: int) -> None:

    with app.app_context():
        try:
            db.session.execute(
                text("CALL InsertIntoLoadingSnacks(:loading_machine_id, :snack_id, :quantity_snacks)"),
                {
                    'loading_machine_id': loading_machine_id,
                    'snack_id': snack_id,
                    'quantity_snacks': quantity_snacks
                }
            )
            db.session.commit()
            print(f"Record inserted: LoadingMachine ID = {loading_machine_id}, Snack ID = {snack_id}, Quantity = {quantity_snacks}")
        except Exception as e:
            print(f"Error inserting record: {e}")



#2c Створити пакет, який вставляє 10 стрічок у довільну таблицю БД у форматі < Noname+№> , наприклад: Noname5, Noname6, Noname7 і т.д.

def _init_insert_employess_address_procedure(app: Flask) -> None:
    """
    Створює процедуру InsertEmployessAddress у MySQL, якщо вона ще не існує.
    """
    procedure_sql = """
    CREATE PROCEDURE IF NOT EXISTS InsertEmployessAddress()
    BEGIN
        DECLARE i INT DEFAULT 1;
        WHILE i <= 10 DO
            INSERT INTO employess_address (city, street, street_number, district, city_index, country)
            VALUES (CONCAT('Noname', i), CONCAT('Street', i), CONCAT('SN', i), CONCAT('District', i), i * 1000, 'Country');
            SET i = i + 1;
        END WHILE;
    END;
    """
    with app.app_context():
        try:
            db.session.execute(text(procedure_sql))
            db.session.commit()
            print("Procedure 'InsertEmployessAddress' created successfully.")
        except Exception as e:
            print(f"Error creating procedure: {e}")


def call_insert_employess_address_procedure(app: Flask) -> None:

    with app.app_context():
        try:
            db.session.execute(text("CALL InsertEmployessAddress()"))
            db.session.commit()
            print("10 rows inserted into 'employess_address' successfully.")
        except Exception as e:
            print(f"Error calling procedure: {e}")


# 2d. Написати користувацьку функцію, яка буде шукати Max, Min, Sum чи Avg для стовпця довільної таблиці у БД.
# Написати процедуру, яка буде у SELECT викликати цю функцію.

#Створює функцію AggregateMoneyTransfer у MySQL.
def _init_aggregate_money_transfer_function(app: Flask) -> None:

    function_sql = """
    DROP FUNCTION IF EXISTS AggregateMoneyTransfer;
    """

    create_function_sql = """
    CREATE FUNCTION AggregateMoneyTransfer(operation VARCHAR(10))
    RETURNS FLOAT
    DETERMINISTIC
    BEGIN
        DECLARE result FLOAT;

        IF operation = 'MAX' THEN
            SELECT MAX(sum) INTO result FROM money_transfer;
        ELSEIF operation = 'MIN' THEN
            SELECT MIN(sum) INTO result FROM money_transfer;
        ELSEIF operation = 'SUM' THEN
            SELECT SUM(sum) INTO result FROM money_transfer;
        ELSEIF operation = 'AVG' THEN
            SELECT AVG(sum) INTO result FROM money_transfer;
        ELSE
            SET result = NULL;
        END IF;

        RETURN result;
    END;
    """
    with app.app_context():
        try:
            # Видалити існуючу функцію, якщо вона є
            db.session.execute(text(function_sql))
            db.session.commit()
            # Створити нову функцію
            db.session.execute(text(create_function_sql))
            db.session.commit()
            print("Function 'AggregateMoneyTransfer' created successfully.")
        except Exception as e:
            print(f"Error creating function: {e}")


def _init_call_aggregate_money_transfer_procedure(app: Flask) -> None:
    """
    Створює процедуру CallAggregateMoneyTransfer у MySQL.
    """
    drop_procedure_sql = """
    DROP PROCEDURE IF EXISTS CallAggregateMoneyTransfer;
    """

    create_procedure_sql = """
    CREATE PROCEDURE CallAggregateMoneyTransfer(IN operation VARCHAR(10))
    BEGIN
        DECLARE result FLOAT;
        SET result = AggregateMoneyTransfer(operation);
        SELECT result AS result;
    END
    """
    with app.app_context():
        try:
            db.session.execute(text(drop_procedure_sql))
            db.session.commit()

            db.session.execute(text(create_procedure_sql))
            db.session.commit()
            print("Procedure 'CallAggregateMoneyTransfer' created successfully.")
        except Exception as e:
            print(f"Error creating procedure: {e}")



def call_aggregate_money_transfer(app: Flask, operation: str) -> None:
    """
    Викликає процедуру CallAggregateMoneyTransfer для отримання результату.
    """
    with app.app_context():
        try:
            result = db.session.execute(
                text("CALL CallAggregateMoneyTransfer(:operation)"),
                {'operation': operation}
            ).fetchone()
            print(f"Result of {operation}: {result['result']}")
        except Exception as e:
            print(f"Error calling procedure: {e}")

#2е Використання курсора для створення таблиць із випадковою кількістю стовпців і назвами з таблиці

def create_dynamic_tables_procedure(app: Flask) -> None:
    """
    Створення процедури CreateTablesWithRandomColumns
    """
    drop_procedure_sql = """
    DROP PROCEDURE IF EXISTS CreateTablesWithRandomColumns;
    """

    create_procedure_sql = """
    CREATE PROCEDURE CreateTablesWithRandomColumns()
    BEGIN
        DECLARE table_name VARCHAR(128);
        DECLARE done INT DEFAULT 0;

        DECLARE table_cursor CURSOR FOR SELECT DISTINCT id FROM snacks;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

        OPEN table_cursor;

        read_loop: LOOP
            FETCH table_cursor INTO table_name;

            IF done THEN
                LEAVE read_loop;
            END IF;

            SET @dynamic_table_name = CONCAT(table_name, '_', DATE_FORMAT(NOW(), '%Y%m%d%H%i%s'));
            SET @create_table_sql = CONCAT('CREATE TABLE ', @dynamic_table_name, ' (id INT PRIMARY KEY, name VARCHAR(50));');

            PREPARE stmt FROM @create_table_sql;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;
        END LOOP;

        CLOSE table_cursor;
    END;
    """
    with app.app_context():
        try:
            # Спочатку видалити існуючу процедуру
            db.session.execute(text(drop_procedure_sql))
            db.session.commit()

            # Створити нову процедуру
            db.session.execute(text(create_procedure_sql))
            db.session.commit()
            print("Procedure created successfully.")
        except Exception as e:
            print(f"Error creating procedure: {e}")


def _init_swagger(app: Flask) -> None:
    """
    Ініціалізація Swagger для документації API
    """
    restx_api = Api(app, title='Pavelchak Test Backend', description='A simple backend')

    @restx_api.route('/number/<string:todo_id>')
    class TodoSimple(Resource):
        @staticmethod
        def get(todo_id):
            return todos, 202

        @staticmethod
        def put(todo_id):
            todos[todo_id] = todo_id
            return todos, HTTPStatus.CREATED

    @app.route("/hi")
    def hello_world():
        return todos, HTTPStatus.OK

def _init_db(app: Flask) -> None:
    """
    Ініціалізація бази даних
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain  # Імпорт моделей
    with app.app_context():
        db.create_all()

def _init_trigger(app: Flask) -> None:
    """
    Створення тригерів для перевірки цілісності таблиці food_machine
    """
    with app.app_context():
        # Видалення старих тригерів, якщо вони існують
        db.session.execute('DROP TRIGGER IF EXISTS trigger_food_machine_insert;')
        db.session.execute('DROP TRIGGER IF EXISTS trigger_food_machine_update;')
        db.session.commit()

        db.session.execute('DROP TRIGGER IF EXISTS trigger_snacks_calories;')
        db.session.execute('DROP TRIGGER IF EXISTS trigger_snacks_calories_update;')
        db.session.commit()

        db.session.execute('DROP TRIGGER IF EXISTS trigger_prevent_delete_machine_manifecture;')
        db.session.execute('DROP TRIGGER IF EXISTS trigger_prevent_update_snacks_creator;')

        # Тригер для перевірки перед вставкою
        db.session.execute('''
        CREATE TRIGGER trigger_food_machine_insert
        BEFORE INSERT ON food_machine
        FOR EACH ROW
        BEGIN
            -- Перевірка: чи існує address_machine з таким id
            IF NOT EXISTS (SELECT 1 FROM address_machine WHERE id = NEW.address_machine_id) THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Address machine ID does not exist';
            END IF;

            -- Перевірка: name не може бути NULL або порожнім
            IF NEW.name IS NULL OR NEW.name = '' THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Name cannot be null or empty';
            END IF;
        END;
        ''')

        # Тригер для перевірки перед оновленням
        db.session.execute('''
        CREATE TRIGGER trigger_food_machine_update
        BEFORE UPDATE ON food_machine
        FOR EACH ROW
        BEGIN
            -- Перевірка: чи існує address_machine з таким id
            IF NOT EXISTS (SELECT 1 FROM address_machine WHERE id = NEW.address_machine_id) THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Address machine ID does not exist';
            END IF;

            -- Перевірка: name не може бути NULL або порожнім
            IF NEW.name IS NULL OR NEW.name = '' THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Name cannot be null or empty';
            END IF;
        END;
        ''')

# 3а закінчується на 2 нулі
        db.session.execute('''
                CREATE TRIGGER trigger_snacks_calories
        BEFORE INSERT ON snacks
        FOR EACH ROW
        BEGIN
            -- Перевірка: значення calories не може закінчуватися на 00
            IF NEW.calories % 100 = 0 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Calories cannot end with 00';
            END IF;
        END;
                ''')

        # Тригер для перевірки перед оновленням
        db.session.execute('''
                CREATE TRIGGER trigger_snacks_calories_update
        BEFORE UPDATE ON snacks
        FOR EACH ROW
        BEGIN
            -- Перевірка: значення calories не може закінчуватися на 00
            IF NEW.calories % 100 = 0 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Calories cannot end with 00';
            END IF;
        END;
                ''')
        db.session.commit()

#3с видалення рядка
        db.session.execute('''
                CREATE TRIGGER trigger_prevent_delete_machine_manifecture
                BEFORE DELETE ON machine_manifecture
                FOR EACH ROW
                BEGIN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Deleting rows from machine_manifecture is not allowed';
                END;
                ''')
#3б заборона оновлення
        db.session.execute('''
                CREATE TRIGGER trigger_prevent_update_snacks_creator
                BEFORE UPDATE ON snacks_creator
                FOR EACH ROW
                BEGIN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Updating rows in snacks_creator is not allowed';
                END;
                ''')


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Обробка вхідної конфігурації
    """
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
