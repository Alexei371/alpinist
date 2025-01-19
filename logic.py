from models import Employee, Route, Location


def create_employee(club_name, contact_info, full_name, position, experience):
    """Создает нового сотрудника клуба"""
    return Employee(club_name, contact_info, full_name, position, experience)


def add_route_to_journal(employee, route_name, difficulty):
    """Добавляет маршрут в журнал восхождений сотрудника"""
    route = Route(route_name, difficulty)
    employee.add_to_journal(f"Route: {route.name}, Difficulty: {route.difficulty}")


def display_journal(employee):
    """Отображает журнал восхождений сотрудника"""
    return employee.journal
