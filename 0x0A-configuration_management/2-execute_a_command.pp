# executes a command using puppet
exec { 'kill_process':
  command => '/usr/bin/pkill -f killmenow',
}
