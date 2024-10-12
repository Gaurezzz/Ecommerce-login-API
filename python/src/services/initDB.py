from services.database import Base, engine, SessionLocal
from models.permiso import Permiso
from models.rol import Rol
from models.rolPermiso import RolPermiso
from models.historialAcceso import HistorialAcceso
from models.usuario import Usuario

def addStaticRecord(table, record, id):
    session = SessionLocal()
    try:
        if not session.query(table).filter_by(id=id).first():
            session.add(record)
            session.commit()
            print(f"Record {record} added to table {table}")
    finally:
        session.close()


def init_db():
    Base.metadata.create_all(bind=engine)
    #rellenando tablas estaticas
    
    admin = Rol(1, "administrador")
    trabajador = Rol(2, "trabajador")
    cliente = Rol(3, "cliente")

    ecommerce = Permiso(1, "ecommerce", "permiso para acceder a la tienda online")
    administrar_usuarios = Permiso(2, "administrar_usuarios", "permiso para administrar usuarios")
    inventario = Permiso(3, "inventario", "permiso para administrar el inventario")
    contabilidad = Permiso(4, "contabilidad", "permiso para administrar la contabilidad")
    auditoria = Permiso(5, "auditoria", "permiso para acceder al historial de accesos y logs")

    addStaticRecord(Rol, admin, 1)
    addStaticRecord(Rol, trabajador, 2)
    addStaticRecord(Rol, cliente, 3)
    addStaticRecord(Permiso, ecommerce, 1)
    addStaticRecord(Permiso, administrar_usuarios, 2)
    addStaticRecord(Permiso, inventario, 3)
    addStaticRecord(Permiso, contabilidad, 4)
    addStaticRecord(Permiso, auditoria, 5)
    addStaticRecord(RolPermiso, RolPermiso(1, 1), 1)
    addStaticRecord(RolPermiso, RolPermiso(1, 2), 2)
    addStaticRecord(RolPermiso, RolPermiso(1, 3), 3)
    addStaticRecord(RolPermiso, RolPermiso(1, 4), 4)
    addStaticRecord(RolPermiso, RolPermiso(1, 5), 5)
    addStaticRecord(RolPermiso, RolPermiso(2, 1), 6)
    addStaticRecord(RolPermiso, RolPermiso(2, 3), 7)
    addStaticRecord(RolPermiso, RolPermiso(2, 4), 8)
    addStaticRecord(RolPermiso, RolPermiso(3, 1), 9)
    

