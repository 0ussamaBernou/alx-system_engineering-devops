file { '/etc/security/limits.d/nofile.conf':
  ensure  => present,
  content => "* soft nofile 65536\n* hard nofile 65536\n",
  mode    => '0644',
}

exec { 'reload-limits':
  command     => '/sbin/sysctl -p',
  refreshonly => true,
  subscribe   => File['/etc/security/limits.d/nofile.conf'],
}
