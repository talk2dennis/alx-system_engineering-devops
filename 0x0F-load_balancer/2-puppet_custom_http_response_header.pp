$server_hostname = $::facts['hostname']
$config = "server {\n
	listen 80;\n
	root /var/www/html;\n
	index index.html index.htm index.nginx-debian.html;\n\n
	server_name _;\n\n
	error_page 404 /custom_404.html;\n
	# custom header
	add_header X-Served-By ${server_hostname};\n
	location /redirect_me {\n
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n
	}\n
}"


# update the app catalog
exec {'apt_update':
  command     => '/usr/bin/apt update',
  path        => '/usr/bin',
  refreshonly => 'true',
}

# install nginx
package {'nginx':
  ensure => installed,
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  mode    => '0644',
}

file {'/var/www/html/custom_404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
  mode    => '0644',
}

# configure nginx to listen on port 80 and add a custom header

file {'/etc/nginx/sites-available/default':
  ensure  => present,
  content => $config,
}

# symlink file
file { '/etc/nginx/sites-available/default':
  ensure => link,
  target => '/etc/nginx/sites-enabled/default',
}
