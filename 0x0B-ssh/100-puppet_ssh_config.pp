# puppet script to configure ssh
include stdlib

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
# match              => '[\s]*IdentityFile.*',
# replace            => true,
# append_on_no_match => true
}

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
# match              => '[\s]*PasswordAuthentication.*',
# replace            => true,
# append_on_no_match => true
}
