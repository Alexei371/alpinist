# models.py
class AlpClub:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.journal = []  # Журнал восхождений

    def __repr__(self):
        return f"AlpClub(name={self.name}, contact_info={self.contact_info})"


class Employee(AlpClub):
    def __init__(self, name: str, contact_info: str, full_name: str, position: str, experience: int):
        super().__init__(name, contact_info)
        self.full_name = full_name
        self.position = position
        self.experience = experience

    def add_to_journal(self, record: str):
        """Добавление записи в журнал восхождений"""
        self.journal.append(record)

    def __repr__(self):
        return (f"Employee(full_name={self.full_name}, position={self.position}, "
                f"experience={self.experience}, club={self.name})")


class Route:
    def __init__(self, name: str, difficulty: str):
        self.name = name
        self.difficulty = difficulty

    def __repr__(self):
        return f"Route(name={self.name}, difficulty={self.difficulty})"


class Location:
    def __init__(self, country: str, region: str):
        self.country = country
        self.region = region

    def __repr__(self):
        return f"Location(country={self.country}, region={self.region})"
