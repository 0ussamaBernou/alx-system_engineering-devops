# !(sky is the limit)
exec {'update ulimit':
  command  => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  provider => 'shell',
}
-> exec {'restart nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}
