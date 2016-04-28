.. -*- coding: utf-8; mode: rst -*-

.. _API-fcntl-setlease:

==============
fcntl_setlease
==============

*man fcntl_setlease(9)*

*4.6.0-rc5*

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

Call this fcntl to establish a lease on the file. Note that you also
need to call ``F_SETSIG`` to receive a signal when the lease is broken.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
