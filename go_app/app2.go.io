server {
listen     	127.0.0.1:80;
server_name	app2.go.io;
location /v2 {


	proxy_pass http://app2.go.io:8081/v2;
	proxy_set_header	Host        	$host;
	proxy_set_header	X-Real-IP   	$remote_addr;
	proxy_set_header	X-Forwarded-for $remote_addr;
	port_in_redirect off;
}
}

