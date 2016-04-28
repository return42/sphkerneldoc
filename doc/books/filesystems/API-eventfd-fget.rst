.. -*- coding: utf-8; mode: rst -*-

.. _API-eventfd-fget:

============
eventfd_fget
============

*man eventfd_fget(9)*

*4.6.0-rc5*

Acquire a reference of an eventfd file descriptor.


Synopsis
========

.. c:function:: struct file * eventfd_fget( int fd )

Arguments
=========

``fd``
    [in] Eventfd file descriptor.


Description
===========

Returns a pointer to the eventfd file structure in case of success, or
the


following error pointer
=======================

-EBADF : Invalid ``fd`` file descriptor. -EINVAL : The ``fd`` file
descriptor is not an eventfd file.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
