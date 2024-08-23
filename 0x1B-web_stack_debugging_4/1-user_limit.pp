# increase holberton user's file limits
file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton soft nofile 65536\nholberton hard nofile 65536\n",
  mode    => '0644',
}

user { 'holberton':
  ensure     => present,
  managehome => true,
  shell      => '/bin/bash',
}

exec { 'reload-limits':
  command     => '/sbin/sysctl -p',
  refreshonly => true,
  subscribe   => File['/etc/security/limits.d/holberton.conf'],
}
