from fastapi import Query


def get_pagination_params(
        
    offset: int = Query(0, ge=0),
    limit: int = Query(10, gt=0)

    ):

    return {"offset": offset, "limit": limit}