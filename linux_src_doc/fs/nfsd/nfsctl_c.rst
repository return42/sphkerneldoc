.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfsd/nfsctl.c

.. _`write_unlock_ip`:

write_unlock_ip
===============

.. c:function:: ssize_t write_unlock_ip(struct file *file, char *buf, size_t size)

    Release all locks used by a client

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_unlock_ip.description`:

Description
-----------

Experimental.

.. _`write_unlock_ip.input`:

Input
-----

buf:    '\n'-terminated C string containing a
presentation format IP address
size:   length of C string in \ ``buf``\ 

.. _`write_unlock_ip.on-success`:

On success
----------

returns zero if all specified locks were released;
returns one if one or more locks were not released

.. _`write_unlock_ip.on-error`:

On error
--------

return code is negative errno value

.. _`write_unlock_fs`:

write_unlock_fs
===============

.. c:function:: ssize_t write_unlock_fs(struct file *file, char *buf, size_t size)

    Release all locks on a local file system

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_unlock_fs.description`:

Description
-----------

Experimental.

.. _`write_unlock_fs.input`:

Input
-----

buf:    '\n'-terminated C string containing the
absolute pathname of a local file system
size:   length of C string in \ ``buf``\ 

.. _`write_unlock_fs.on-success`:

On success
----------

returns zero if all specified locks were released;
returns one if one or more locks were not released

.. _`write_unlock_fs.on-error`:

On error
--------

return code is negative errno value

.. _`write_filehandle`:

write_filehandle
================

.. c:function:: ssize_t write_filehandle(struct file *file, char *buf, size_t size)

    Get a variable-length NFS file handle by path

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_filehandle.description`:

Description
-----------

On input, the buffer contains a '\n'-terminated C string comprised of
three alphanumeric words separated by whitespace.  The string may
contain escape sequences.

.. _`write_filehandle.input`:

Input
-----

buf:
domain:         client domain name
path:           export pathname
maxsize:        numeric maximum size of
\ ``buf``\ 
size:   length of C string in \ ``buf``\ 

.. _`write_filehandle.on-success`:

On success
----------

passed-in buffer filled with '\n'-terminated C
string containing a ASCII hex text version
of the NFS file handle;
return code is the size in bytes of the string

.. _`write_filehandle.on-error`:

On error
--------

return code is negative errno value

.. _`write_threads`:

write_threads
=============

.. c:function:: ssize_t write_threads(struct file *file, char *buf, size_t size)

    Start NFSD, or report the current number of running threads

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_threads.input`:

Input
-----

buf:            ignored
size:           zero

buf:            C string containing an unsigned
integer value representing the
number of NFSD threads to start
size:           non-zero length of C string in \ ``buf``\ 

.. _`write_threads.on-success`:

On success
----------

passed-in buffer filled with '\n'-terminated C
string numeric value representing the number of
running NFSD threads;
return code is the size in bytes of the string

NFS service is started;
passed-in buffer filled with '\n'-terminated C
string numeric value representing the number of
running NFSD threads;
return code is the size in bytes of the string

.. _`write_threads.on-error`:

On error
--------

return code is zero

OR

return code is zero or a negative errno value

.. _`write_pool_threads`:

write_pool_threads
==================

.. c:function:: ssize_t write_pool_threads(struct file *file, char *buf, size_t size)

    Set or report the current number of threads per pool

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_pool_threads.input`:

Input
-----

buf:            ignored
size:           zero

OR

buf:            C string containing whitespace-
separated unsigned integer values
representing the number of NFSD
threads to start in each pool
size:           non-zero length of C string in \ ``buf``\ 

.. _`write_pool_threads.on-success`:

On success
----------

passed-in buffer filled with '\n'-terminated C
string containing integer values representing the
number of NFSD threads in each pool;
return code is the size in bytes of the string

.. _`write_pool_threads.on-error`:

On error
--------

return code is zero or a negative errno value

.. _`write_versions`:

write_versions
==============

.. c:function:: ssize_t write_versions(struct file *file, char *buf, size_t size)

    Set or report the available NFS protocol versions

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_versions.input`:

Input
-----

buf:            ignored
size:           zero

buf:            C string containing whitespace-
separated positive or negative
integer values representing NFS
protocol versions to enable ("+n")
or disable ("-n")
size:           non-zero length of C string in \ ``buf``\ 

.. _`write_versions.on-success`:

On success
----------

passed-in buffer filled with '\n'-terminated C
string containing positive or negative integer
values representing the current status of each
protocol version;
return code is the size in bytes of the string

status of zero or more protocol versions has
been updated; passed-in buffer filled with
'\n'-terminated C string containing positive
or negative integer values representing the
current status of each protocol version;
return code is the size in bytes of the string

.. _`write_versions.on-error`:

On error
--------

return code is zero or a negative errno value

OR

return code is zero or a negative errno value

.. _`write_ports`:

write_ports
===========

.. c:function:: ssize_t write_ports(struct file *file, char *buf, size_t size)

    Pass a socket file descriptor or transport name to listen on

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_ports.input`:

Input
-----

buf:            ignored
size:           zero

buf:            C string containing an unsigned
integer value representing a bound
but unconnected socket that is to be
used as an NFSD listener; listen(3)
must be called for a SOCK_STREAM
socket, otherwise it is ignored
size:           non-zero length of C string in \ ``buf``\ 

buf:            C string containing a transport
name and an unsigned integer value
representing the port to listen on,
separated by whitespace
size:           non-zero length of C string in \ ``buf``\ 

.. _`write_ports.on-success`:

On success
----------

passed-in buffer filled with a '\n'-terminated C
string containing a whitespace-separated list of
named NFSD listeners;
return code is the size in bytes of the string

NFS service is started;
passed-in buffer filled with a '\n'-terminated C
string containing a unique alphanumeric name of
the listener;
return code is the size in bytes of the string

returns zero; NFS service is started

.. _`write_ports.on-error`:

On error
--------

return code is zero or a negative errno value

OR

return code is a negative errno value

OR

return code is a negative errno value

.. _`write_maxblksize`:

write_maxblksize
================

.. c:function:: ssize_t write_maxblksize(struct file *file, char *buf, size_t size)

    Set or report the current NFS blksize

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_maxblksize.input`:

Input
-----

buf:            ignored
size:           zero

OR

buf:            C string containing an unsigned
integer value representing the new
NFS blksize
size:           non-zero length of C string in \ ``buf``\ 

.. _`write_maxblksize.on-success`:

On success
----------

passed-in buffer filled with '\n'-terminated C string
containing numeric value of the current NFS blksize
setting;
return code is the size in bytes of the string

.. _`write_maxblksize.on-error`:

On error
--------

return code is zero or a negative errno value

.. _`write_maxconn`:

write_maxconn
=============

.. c:function:: ssize_t write_maxconn(struct file *file, char *buf, size_t size)

    Set or report the current max number of connections

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_maxconn.input`:

Input
-----

buf:            ignored
size:           zero
OR

buf:            C string containing an unsigned
integer value representing the new
number of max connections
size:           non-zero length of C string in \ ``buf``\ 

.. _`write_maxconn.on-success`:

On success
----------

passed-in buffer filled with '\n'-terminated C string
containing numeric value of max_connections setting
for this net namespace;
return code is the size in bytes of the string

.. _`write_maxconn.on-error`:

On error
--------

return code is zero or a negative errno value

.. _`write_leasetime`:

write_leasetime
===============

.. c:function:: ssize_t write_leasetime(struct file *file, char *buf, size_t size)

    Set or report the current NFSv4 lease time

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_leasetime.input`:

Input
-----

buf:            ignored
size:           zero

OR

buf:            C string containing an unsigned
integer value representing the new
NFSv4 lease expiry time
size:           non-zero length of C string in \ ``buf``\ 

.. _`write_leasetime.on-success`:

On success
----------

passed-in buffer filled with '\n'-terminated C
string containing unsigned integer value of the
current lease expiry time;
return code is the size in bytes of the string

.. _`write_leasetime.on-error`:

On error
--------

return code is zero or a negative errno value

.. _`write_gracetime`:

write_gracetime
===============

.. c:function:: ssize_t write_gracetime(struct file *file, char *buf, size_t size)

    Set or report current NFSv4 grace period time

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_gracetime.description`:

Description
-----------

As above, but sets the time of the NFSv4 grace period.

Note this should never be set to less than the \*previous\*
lease-period time, but we don't try to enforce this.  (In the common
case (a new boot), we don't know what the previous lease time was
anyway.)

.. _`write_recoverydir`:

write_recoverydir
=================

.. c:function:: ssize_t write_recoverydir(struct file *file, char *buf, size_t size)

    Set or report the pathname of the recovery directory

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_recoverydir.input`:

Input
-----

buf:            ignored
size:           zero

OR

buf:            C string containing the pathname
of the directory on a local file
system containing permanent NFSv4
recovery data
size:           non-zero length of C string in \ ``buf``\ 

.. _`write_recoverydir.on-success`:

On success
----------

passed-in buffer filled with '\n'-terminated C string
containing the current recovery pathname setting;
return code is the size in bytes of the string

.. _`write_recoverydir.on-error`:

On error
--------

return code is zero or a negative errno value

.. _`write_v4_end_grace`:

write_v4_end_grace
==================

.. c:function:: ssize_t write_v4_end_grace(struct file *file, char *buf, size_t size)

    release grace period for nfsd's v4.x lock manager

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`write_v4_end_grace.input`:

Input
-----

buf:            ignored
size:           zero
OR

buf:            any value
size:           non-zero length of C string in \ ``buf``\ 

.. _`write_v4_end_grace.output`:

Output
------

passed-in buffer filled with "Y" or "N" with a newline
and NULL-terminated C string. This indicates whether
the grace period has ended in the current net
namespace. Return code is the size in bytes of the
string. Writing a string that starts with 'Y', 'y', or
'1' to the file will end the grace period for nfsd's v4
lock manager.

.. This file was automatic generated / don't edit.

