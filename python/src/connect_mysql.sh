#!/bin/bash

# Esperar un momento para asegurarse de que la base de datos esté lista
sleep 10

# Conectar a MySQL
mysql -h db -u admin -p'xM78%3hU/N^A' -e "SHOW DATABASES;"
