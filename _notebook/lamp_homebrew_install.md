# LAMP Stack Install via Homebrew

**_Nevermind... decided to go with XAMPP instead_**

## Apache Web Server
Install Apache
```bash
brew install httpd
```

To start httpd now and restart at login
```bash
sudo brew services start httpd
```

If you don't want/need a background service you can just run
```bash
/opt/homebrew/opt/httpd/bin/httpd -D FOREGROUND
```

DocumentRoot
```bash
/opt/homebrew/var/www
```

The default ports have been set in /opt/homebrew/etc/httpd/httpd.conf to 8080 and in /opt/homebrew/etc/httpd/extra/httpd-ssl.conf to 8443 so that httpd can run without sudo.

## PHP
I decided to go with PHP v8.1. This seems like a reasonable choice.
```bash
brew install php@8.1
```

To make a specific version the default on your system, you need to link it

```bash
brew unlink php
brew link --overwrite php@8.1
```

chuck@Mac ~ % brew unlink php
brew link --overwrite php@8.1

Error: No such keg: /opt/homebrew/Cellar/php
Linking /opt/homebrew/Cellar/php@8.1/8.1.31... 148 symlinks created.

If you need to have this software first in your PATH instead consider running:
  echo 'export PATH="/opt/homebrew/opt/php@8.1/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/opt/homebrew/opt/php@8.1/sbin:$PATH"' >> ~/.zshrc
chuck@Mac ~ % php -v
PHP 8.1.31 (cli) (built: Nov 19 2024 15:24:51) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.1.31, Copyright (c) Zend Technologies

Check the PHP version to confirm:
```bash
php -v
```

To enable PHP in Apache add the following to httpd.conf and restart Apache:
    LoadModule php_module /opt/homebrew/opt/php@8.1/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

Finally, check DirectoryIndex includes index.php
    DirectoryIndex index.php index.html

The php.ini and php-fpm.ini file can be found in:
    /opt/homebrew/etc/php/8.1/

php@8.1 is keg-only, which means it was not symlinked into /opt/homebrew,
because this is an alternate version of another formula.

If you need to have php@8.1 first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/php@8.1/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/opt/homebrew/opt/php@8.1/sbin:$PATH"' >> ~/.zshrc

For compilers to find php@8.1 you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/php@8.1/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/php@8.1/include"

To start php@8.1 now and restart at login:
  brew services start php@8.1
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/php@8.1/sbin/php-fpm --nodaemonize
==> Summary
🍺  /opt/homebrew/Cellar/php@8.1/8.1.31: 515 files, 81.9MB
==> Running `brew cleanup php@8.1`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Caveats
==> php@8.1
To enable PHP in Apache add the following to httpd.conf and restart Apache:
    LoadModule php_module /opt/homebrew/opt/php@8.1/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

Finally, check DirectoryIndex includes index.php
    DirectoryIndex index.php index.html

The php.ini and php-fpm.ini file can be found in:
    /opt/homebrew/etc/php/8.1/

php@8.1 is keg-only, which means it was not symlinked into /opt/homebrew,
because this is an alternate version of another formula.

If you need to have php@8.1 first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/php@8.1/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/opt/homebrew/opt/php@8.1/sbin:$PATH"' >> ~/.zshrc

For compilers to find php@8.1 you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/php@8.1/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/php@8.1/include"

To start php@8.1 now and restart at login:
  brew services start php@8.1
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/php@8.1/sbin/php-fpm --nodaemonize

## MariaDB

Install MariaDB
```bash
brew install mariadb
```

Start MariaDB
```bash
brew services start mariadb
```

Secure MariaDB
```bash
mysql_secure_installation
```

Access MariaDB
```bash
mariadb -u root -p
```

==> Caveats
A "/etc/my.cnf" from another install may interfere with a Homebrew-built
server starting up correctly.

MySQL is configured to only allow connections from localhost by default

To start mariadb now and restart at login:
  brew services start mariadb
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/mariadb/bin/mariadbd-safe --datadir\=/opt/homebrew/var/mysql
==> Summary
🍺  /opt/homebrew/Cellar/mariadb/11.6.2: 950 files, 212.3MB
==> Running `brew cleanup mariadb`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Caveats
==> mariadb
A "/etc/my.cnf" from another install may interfere with a Homebrew-built
server starting up correctly.

MySQL is configured to only allow connections from localhost by default

To start mariadb now and restart at login:
  brew services start mariadb
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/mariadb/bin/mariadbd-safe --datadir\=/opt/homebrew/var/mysql

## Test the Stack

Create a test.php file in the Apache web directory (e.g., /usr/local/var/www/) with
```bash
<?php phpinfo(); ?>
```

Access it via your browser at http://localhost/test.php

