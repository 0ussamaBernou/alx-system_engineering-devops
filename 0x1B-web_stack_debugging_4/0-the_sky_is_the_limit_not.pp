# increase file descriptor limit
# Set file descriptor limits for nginx user
file { '/etc/security/limits.d/nginx.conf':
  ensure  => present,
  content => "nginx soft nofile 65536\nnginx hard nofile 65536\n",
  mode    => '0644',
}

# Ensure the nginx user exists
user { 'nginx':
  ensure => present,
  system => true,
}

# Reload system limits
exec { 'reload-limits':
  command     => '/sbin/sysctl -p',
  refreshonly => true,
  subscribe   => File['/etc/security/limits.d/nginx.conf'],
}

# Modify nginx.service to set higher limit
file { '/etc/systemd/system/nginx.service.d':
  ensure => directory,
}

file { '/etc/systemd/system/nginx.service.d/limits.conf':
  ensure  => present,
  content => "[Service]\nLimitNOFILE=65536\n",
  notify  => Exec['systemctl-daemon-reload'],
}

exec { 'systemctl-daemon-reload':
  command     => '/bin/systemctl daemon-reload',
  refreshonly => true,
}
