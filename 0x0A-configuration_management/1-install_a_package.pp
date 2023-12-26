# instal flask
#class { 'python3':
#  ensure => present,
#}
#package { 'python3-pip':
#  ensure => present,
#}
package { 'flask==2.1.0':
  ensure   => present,
  provider => 'pip3',
}
