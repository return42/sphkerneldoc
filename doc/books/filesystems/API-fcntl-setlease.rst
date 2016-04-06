
.. _API-fcntl-setlease:

==============
fcntl_setlease
==============

*man fcntl_setlease(9)*

*4.6.0-rc1*

sets a lease on an open file


Synopsis
========

.. c:function:: int fcntl_setlease( unsigned int fd, struct file * filp, long arg )

Arguments
=========

``fd``
    open file descriptor

``filp``
    file pointer

``arg``
    type of lease to obtain


Description
===========

Call this fcntl to establish a lease on the file. Note that you also need to call ``F_SETSIG`` to receive a signal when the lease is broken.
