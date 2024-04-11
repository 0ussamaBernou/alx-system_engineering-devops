0x17-web_stack_debugging_3

Debugging steps:

- Used `strace` to find out that the `apache` process was trying to access a file that didn't exist.

```
stat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffcb86bf5b0) = -1 ENOENT (No such file or directory)
```

- The file was supposed to be `class-wp-locale.php` but the extension was wrong.
- greped the file and found the file mentioned with the wrong extension in the `wp-settings.php` file.
- fixed the file extension and the server started working.
