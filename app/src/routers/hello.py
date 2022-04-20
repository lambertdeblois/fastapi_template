from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..models.Hello import Hello

hello = APIRouter(
    prefix="/hello",
    responses={
        404: {"msg": "Not found"}
    }
)

@hello.get('/')
def hello_world():
    hello = Hello('World!')
    return {"msg": hello.greet()}