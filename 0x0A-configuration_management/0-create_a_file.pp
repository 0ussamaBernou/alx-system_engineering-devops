# creates the file /tmp/school with the content "I love Puppet"
file { '/tmp/school':
   ensure => 'present',
   mode  => '0744',
   owner => 'www-data',
   group => 'www-data',
   content => "I love Puppet\n",
}
