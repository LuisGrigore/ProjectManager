from returns.result import Success, Failure


def save_entity(create_dto, error, persist_funct, create_dto_to_model_funct, model_to_get_dto_funct):
    model = create_dto_to_model_funct(create_dto)
    model_persisted = persist_funct(model)
    if model_persisted:
        get_dto = model_to_get_dto_funct(model_persisted)
        return Success(get_dto)
    return Failure(error)

def find_by_id(id,find_in_db_funct,error, model_to_get_dto_funct):
    '''hola'''
    model = find_in_db_funct(id)
    if model:
        return Success(model_to_get_dto_funct(model))
    return Failure(error)