# strace is your friend

exec { 'fix-apache-wp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin:/bin',
}
