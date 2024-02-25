from typing import Any

from .models import Specialist, SpecialistPagedMessage


class Serializer:
    def __init__(self, data: dict) -> None:
        self.data = data

    def serialize(self) -> Any:
        pass


class SpecialistSerializer(Serializer):

    def serialize(self) -> Any:
        first_name = self.data.get('first_name', '')
        last_name = self.data.get('last_name', '')
        images = self.data.get('avatar_img', {}).get('image', '')
        return Specialist(first_name=first_name, last_name=last_name, images=images, description='')


class SpecialistPagedSerializer(Serializer):
    def serialize(self) -> Any:
        total_pages = self.data.get('count')
        if total_pages != 1:
            next_page = self.data.get('next')
            previous_page = self.data.get('previous')
            if next_page is None:
                current_page = total_pages
            elif previous_page is None:
                current_page = 1
            else:
                current_page = int(next_page[-1])
        else:
            current_page = 1
            next_page = None
            previous_page = None
        specialists = self.data.get('results', [])
        if specialists:
            specialist_data = specialists[0]
            specialist = SpecialistSerializer(data=specialist_data)
            specialist = specialist.serialize()
        else:
            raise Exception

        return SpecialistPagedMessage(
            current_page=current_page,
            next_page=next_page,
            previous_page=previous_page,
            total_pages=total_pages,
            specialist=specialist,
        )
