# A puppet script to kill a process

exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
