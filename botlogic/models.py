from dataclasses import dataclass


@dataclass
class Specialist:
    first_name: str
    last_name: str
    images: str
    description: str


@dataclass
class SpecialistPagedMessage:
    total_pages: int
    current_page: int
    next_page: str | None
    previous_page: str | None
    specialist: Specialist
