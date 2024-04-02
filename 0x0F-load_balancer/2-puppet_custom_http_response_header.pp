$server_hostname = $::facts['hostname']
$config = "server {
	listen 80 default_server;
        listen [::]:80 default_server;\n
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
  ensure  => installed,
  require => package('apt_update'),
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file {'/var/www/html/custom_404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

# configure nginx to listen on port 80 and add a custom header

file {'/etc/nginx/sites-available/default':
  ensure  => present,
  content => $config,
}

# remove file
exec { 'rm_default':
  command => '/usr/bin/rm /etc/nginx/sites-enabled/default',
  path    => '/usr/bin',
}


# symlink file
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure => running,
  require => 'nginx',
}
