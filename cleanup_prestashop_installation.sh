docker exec -it jaya-prestashop rm -rf /var/www/html/install/

docker exec -it jaya-prestashop mv /var/www/html/admin /var/www/html/secret_admin
