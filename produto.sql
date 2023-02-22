CREATE table produto (
id int not null,
nome text(100),
categoria_id int not null,
primary key (id),
foreign key(categoria_id) references categiria(id)
)


