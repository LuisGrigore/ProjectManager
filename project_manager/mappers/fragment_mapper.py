from project_manager.dtos.fragment_dtos import FragmentCreateDto, FragmentGetDto
from project_manager.model.model import FragmentModel


def fragment_create_dto_to_fragment_model(fragment_create: FragmentCreateDto) -> FragmentModel:
    fragment_model: FragmentModel = FragmentModel.get_FragmentModel(fragment_create.name, fragment_create.project_id)
    return fragment_model

def fragment_model_to_fragment_get_dto(fragment_model: FragmentModel) -> FragmentGetDto:
    fragment_get_dto: FragmentGetDto = FragmentGetDto(fragment_model.name, fragment_model.owner_id)
    return fragment_get_dto