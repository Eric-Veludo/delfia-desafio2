CREATE DATABASE desafio2;

USE desafio2;

CREATE TABLE TB_celular (
	id INT IDENTITY(1,1) PRIMARY KEY,
	modelo NVARCHAR(50),
	capacidade NVARCHAR(10),
	tamanho_tela NVARCHAR(10),
	preço NVARCHAR(10),
	valor_parcela NVARCHAR(10),
	cor NVARCHAR(10),
	ultimas_pecas INT
);

SELECT * FROM TB_celular;