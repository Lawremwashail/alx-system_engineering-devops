# fix nginx files limit for more requests

exec {'files limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/bin/env'
}

