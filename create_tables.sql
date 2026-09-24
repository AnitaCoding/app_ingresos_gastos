#Esto lo creamos por si acaso
CREATE TABLE "movimiento" (
	"id"	INTEGER,
	"date"	TEXT NOT NULL,
	"concept"	TEXT NOT NULL,
	"quantity"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);