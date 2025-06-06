from database import db

class Venta(db.Model):
    __tablename__ = "ventas"
    id = db.Column(db.Integer,primary_key = True)
    fecha = db.Column(db.DateTime,nullable=False)
    cantidad = db.Column(db.Integer,nullable=False)
    cliente_id = db.Column(db.Integer,db.ForeignKey('clientes.id'),nullable=False)
    producto_id = db.Column(db.Integer,db.ForeignKey('productos.id'),nullable=False)
    
    cliente = db.relationship('Cliente',back_populates='ventas')
    producto = db.relationship('Producto',back_populates='ventas')
    
    def __init__(self, fecha, cantidad, cliente_id, producto_id):
        self.fecha= fecha
        self.cantidad= cantidad
        self.cliente_id= cliente_id
        self.producto_id= producto_id 
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Venta.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Venta.query.get(id)
    
    def update(self,fecha=None,cantidad=None,cliente_id=None,producto_id=None):
        if fecha and cantidad and cliente_id and producto_id:
            self.fecha=fecha
            self.cantidad=cantidad
            self.cliente_id=cliente_id
            self.producto_id=producto_id
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()