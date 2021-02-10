#!/usr/bin/env bash
set -e -o pipefail

docker stop ${DB_NAME} || true
docker rm ${DB_NAME} || true

echo "dumping..."
mkdir -p ./tmp
ssh freebox "mysqldump --databases ${DB_NAME} | gzip -9" > ./tmp/dblocal.sql.gz
gunzip -f ./tmp/dblocal.sql.gz

cid=$(docker run --name ${DB_NAME} -d -p ${DB_PORT}:3306 -e MYSQL_ROOT_PASSWORD=${DB_PASSWORD} -v $(pwd)/tmp/dblocal.sql:/docker-entrypoint-initdb.d/dblocal.sql mysql:5.7.26)
docker logs -f $cid
