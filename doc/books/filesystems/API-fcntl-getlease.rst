
.. _API-fcntl-getlease:

==============
fcntl_getlease
==============

*man fcntl_getlease(9)*

*4.6.0-rc1*

Enquire what lease is currently active


Synopsis
========

.. c:function:: int fcntl_getlease( struct file * filp )

Arguments
=========

``filp``
    the file


Description
===========

The value returned by this function will be one of (if no lease break is pending):

``F_RDLCK`` to indicate a shared lease is held.

``F_WRLCK`` to indicate an exclusive lease is held.

``F_UNLCK`` to indicate no lease is held.

(if a lease break is pending):

``F_RDLCK`` to indicate an exclusive lease needs to be changed to a shared lease (or removed).

``F_UNLCK`` to indicate the lease needs to be removed.


XXX
===

sfr & willy disagree over whether F_INPROGRESS should be returned to userspace.
