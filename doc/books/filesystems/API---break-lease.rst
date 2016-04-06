
.. _API---break-lease:

=============
__break_lease
=============

*man __break_lease(9)*

*4.6.0-rc1*

revoke all outstanding leases on file


Synopsis
========

.. c:function:: int __break_lease( struct inode * inode, unsigned int mode, unsigned int type )

Arguments
=========

``inode``
    the inode of the file to return

``mode``
    O_RDONLY: break only write leases; O_WRONLY or O_RDWR: break all leases

``type``
    FL_LEASE: break leases and delegations; FL_DELEG: break only delegations


Description
===========

break_lease (inlined for speed) has checked there already is at least some kind of lock (maybe a lease) on this file. Leases are broken on a call to ``open`` or ``truncate``. This
function can sleep unless you specified ``O_NONBLOCK`` to your ``open``.
