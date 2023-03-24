# install 'puppet-lint'

package { 'flask':
  ensure   => '2.1.o',
  provider => 'pip3',
}
