
.. _API-sys-flock:

=========
sys_flock
=========

*man sys_flock(9)*

*4.6.0-rc1*

``flock`` system call.


Synopsis
========

.. c:function:: long sys_flock( unsigned int fd, unsigned int cmd )

Arguments
=========

``fd``
    the file descriptor to lock.

``cmd``
    the type of lock to apply.


Description
===========

Apply a ``FL_FLOCK`` style lock to an open file descriptor. The ``cmd`` can be one of

``LOCK_SH`` -- a shared lock.

``LOCK_EX`` -- an exclusive lock.

``LOCK_UN`` -- remove an existing lock.

``LOCK_MAND`` -- a `mandatory' flock. This exists to emulate Windows Share Modes.

``LOCK_MAND`` can be combined with ``LOCK_READ`` or ``LOCK_WRITE`` to allow other processes read and write access respectively.
