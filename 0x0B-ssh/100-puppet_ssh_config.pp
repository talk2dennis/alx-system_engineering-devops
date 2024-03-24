#puppet scriot to cofigure server ssh_config file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no"
}
