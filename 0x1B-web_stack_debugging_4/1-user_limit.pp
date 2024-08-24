# Enables the user for 'holberton' to login and open files without error

exec { 'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/^holberton.*hard.*nofile/s/[0-9]\+/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton.*soft.*nofile/s/[0-9]\+/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
