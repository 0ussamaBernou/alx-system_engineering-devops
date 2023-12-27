# puppet script to configure ssh
include stdlib

file_line { 'Declare identity file':
  ensure  => present,
  path    => '~/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Turn off passwd auth':
  path    => '~/.ssh/config',
  line    => 'PasswordAuthentication no',
  replace => true,
}
