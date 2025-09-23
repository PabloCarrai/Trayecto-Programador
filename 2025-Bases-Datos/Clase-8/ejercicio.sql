/* Creamos la db */
create database tienda;
/* Elegimos la misma */
use tienda;
/*	Creamos la tabla clientes */
create table clientes(
	id_cliente int primary key auto_increment,
	nombre varchar(100),
	direccion varchar(200),
	telefono varchar(20) null
)engine=innodb;
/*	creamos productos*/
create table productos(
	id_producto int primary key auto_increment,
	descripcion varchar(100),
	precio decimal(10,2),
	existencia int
)engine=innodb;
/*	Creamos pedidos */
create table pedidos(
	id_pedido int primary key auto_increment,
	id_cliente int, 
	foreign key(id_cliente)references clientes(id_cliente),
	monto decimal(10,2),
	fecha_registro date
)engine=innodb;
/*	creamos detalle_pedidos*/
create table detalles_pedido(	
	id_pedido int,	
	id_producto int,
	foreign key(id_producto)references productos(id_producto),
	foreign key(id_pedido)references pedidos(id_pedido),
	cantidad int
)engine=innodb;

