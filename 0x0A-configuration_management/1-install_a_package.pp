# puppet script to install flask using pip3
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

# install Werkzeug 2.1.1

package {'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
