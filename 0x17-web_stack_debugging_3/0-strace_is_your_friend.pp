# puppet file to fix php typo in wp-settings.php

exec { 'fix php typo':
    command => "sed -i.bak 's/.phpp/.php/g' /var/www/html/wp-settings.php",
    path    => ['/usr/bin', '/usr/sbin']
}
