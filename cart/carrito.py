from datetime import datetime
class Producto:
    def __init__(self, id, nombre, imagen, tipo, cantidad, descripcion, precio_total, id_carrito):
        self.id = id
        self.nombre = nombre
        self.imagen = imagen
        self.tipo = tipo
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.precio_total = precio_total
        self.id_carrito=id_carrito

    def __str__(self):
        return f"id: {self.id} cantidad: {self.cantidad}"

class Carrito:
    def __init__(self):
        self.productos=[]
        self.num=0
        

    def agregar(self,producto):
        self.productos.append(producto)
        self.num+=1

    def quitar(self,pos):
        self.productos.pop(pos)
        self.num-=1

    def limpiar(self):
        self.productos.clear()
        self.num=0

    def __len__(self):
        return self.num
    
    def total_pagar(self):
        prec_total=0
        for producto in self.productos:
            prec_total+=producto.precio_total
        return prec_total
    
    def __str__(self):
        cad=""
        for producto in self.productos:
            cad+=f"{producto}--"
        return cad


    
            
carrito=Carrito()
num=len(carrito)
# prod1=Producto(1,3)
# prod2=Producto(2,3)
# prod3=Producto(1,5)
# prod4=Producto(5,3)

# carrito.agregar(prod1)
# carrito.agregar(prod2)
# carrito.agregar(prod3)
# carrito.agregar(prod4)
# print(len(carrito))
# print(carrito.productos[0].id) ##Es el id del primer producto

# for i in range(len(carrito)):
#     print(carrito[i])
# carrito.quitar(2)
# print(len(carrito))
# for i in range(len(carrito)):
#     print(carrito[i])