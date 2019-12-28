# Copyright 2019 The Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from fastapi import FastAPI

from .routers import dispatcher
from .routers import domain
from .routers import group
from .routers import jsonrpcs
from .routers import moni
from .routers import mtree
from .routers import ps
from .routers import rpcmethods
from .routers import rtpengine
from .routers import speeddial
from .routers import srv
from .routers import stats
from .routers import subscriber
from .routers import tcp
from .routers import tls
from .routers import trap
from .routers import uacreg
from .routers import ul
from .routers import uptime 


def get_app(config: dict):
    app = FastAPI(
        title="kamcli-API",
        description="Configuration API for Kamailio proxy using kamcli",
        version="1.0.0",
        openapi_url="/api/v1/openapi.json",
    )
    app.include_router(dispatcher.router, tags=['dispatcher'])
    app.include_router(domain.router, tags=['domain'])
    app.include_router(group.router, tags=['group'])
    app.include_router(jsonrpc.router, tags=['jsonrpc'])
    app.include_router(moni.router, tags=['moni'])
    app.include_router(mtree.router, tags=['mtree'])
    app.include_router(ps.router, tags=['ps'])
    app.include_router(rpcmethods.router, tags=['rpcmethods'])
    app.include_router(rtpengine.router, tags=['rtpengine'])
    app.include_router(speeddial.router, tags=['speeddial'])
    app.include_router(srv.router, tags=['srv'])
    app.include_router(stats.router, tags=['stats'])
    app.include_router(subscriber.router, tags=['subscriber'])
    app.include_router(tcp.router, tags=['tcp'])
    app.include_router(tls.router, tags=['tls'])
    app.include_router(trap.router, tags=['trap'])
    app.include_router(uacreg.router, tags=['uacreg'])
    app.include_router(ul.router, tags=['ul'])
    app.include_router(uptime.router, tags=['uptime'])

    return app
