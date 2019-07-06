docker container stop jaya-mysql jaya-prestashop
docker container rm jaya-mysql jaya-prestashop
docker volume prune -f
docker network create jaya-net
docker run -ti --name jaya-mysql --network jaya-net -e MYSQL_ROOT_PASSWORD=Yahoo123 -p 3306:3306 -d mysql:5.7
docker run -ti --name jaya-prestashop --network jaya-net -e DB_SERVER=jaya-mysql -p 8080:80 -d prestashop/prestashop
