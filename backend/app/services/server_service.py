from app.models.server import Server
from app.database.db import SessionLocal


def get_or_create_server(
    hostname,
    os,
    os_version
):

    db = SessionLocal()

    try:

        server = (
            db.query(Server)
            .filter(Server.hostname == hostname)
            .first()
        )

        if server:
            return server.id

        server = Server(
            hostname=hostname,
            os=os,
            os_version=os_version
        )

        db.add(server)

        db.commit()

        db.refresh(server)

        return server.id

    finally:

        db.close()


def get_all_servers():

    db = SessionLocal()

    try:

        servers = db.query(Server).all()

        result = []

        for server in servers:

            result.append(
                {
                    "id": server.id,
                    "hostname": server.hostname,
                    "os": server.os,
                    "os_version": server.os_version
                }
            )

        return result

    finally:

        db.close()


def get_server_by_id(server_id):

    db = SessionLocal()

    try:

        server = (
            db.query(Server)
            .filter(Server.id == server_id)
            .first()
        )

        if not server:

            return {
                "message": "Server not found"
            }

        return {
            "id": server.id,
            "hostname": server.hostname,
            "os": server.os,
            "os_version": server.os_version
        }

    finally:

        db.close()