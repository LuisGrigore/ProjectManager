from typing import Optional

from project_manager.model.model import FragmentModel
from project_manager.repos import repos


def save_fragment(fragment: FragmentModel) -> Optional[FragmentModel]:
    return repos.save_entity(fragment)


def get_fragment(id: str) -> Optional[FragmentModel]:
    return repos.get_entity_by_id(id, FragmentModel)