from fastapi import FastAPI, Request, status, Depends, Response
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
import sys, traceback
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

sys.path.append(BASEDIR)

from database.redis import redis_client, config

from routers.authentication import auth
from routers.user import profile
from routers.misc import geo
from routers.misc import merch
from routers.inventory import category
from routers.inventory import group
from routers.inventory import product
from routers.user import main as users
from routers.user import cust as customer
from routers.user import merchant
from routers.order import base as orders
from routers.accounting import gl_type
from routers.accounting import gl
from routers.accounting import product as fin_product
from routers.accounting import cust_acct
from routers.transaction import type
from routers.transaction import postings
from routers.misc import stats


#system routes
from routers import seed

# Main app section here
app = FastAPI(title="Upteek Admin API Service")

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(geo.router)
app.include_router(merch.router)
app.include_router(category.router)
app.include_router(group.router)
app.include_router(product.router)
app.include_router(users.router)
app.include_router(customer.router)
app.include_router(merchant.router)
app.include_router(orders.router)
app.include_router(gl_type.router)
app.include_router(gl.router)
app.include_router(fin_product.router)
app.include_router(cust_acct.router)
app.include_router(type.router)
app.include_router(postings.router)
app.include_router(stats.router)

#system routes
app.include_router(seed.router)

#Test routers
# app.include_router(external.router)

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = "0"
        response.headers["Pragma"] = "no-cache"
        return response
    except Exception as e:
        err = "Stack Trace - %s \n" % (traceback.format_exc())
        print(err)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder({"detail": str(err)}))


app.middleware('http')(catch_exceptions_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World! Upteek Admin"}

@app.get("/maintenance_mode")
async def maintenance_mode():
    flag = await redis_client.get("maintenance_mode")
    if flag is None:
        await redis_client.set("maintenance_mode", "0")
        flag = "0"
    return {"maintenance_mode": flag}

@app.post("/maintenance_mode/set")
async def set_cache(value: str):
    await redis_client.set("maintenance_mode", value)
    return {"status": "saved"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body, "url": request.base_url}),
    )

add_pagination(app)