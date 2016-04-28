.. -*- coding: utf-8; mode: rst -*-

.. _API-memdup-user:

===========
memdup_user
===========

*man memdup_user(9)*

*4.6.0-rc5*

duplicate memory region from user space


Synopsis
========

.. c:function:: void * memdup_user( const void __user * src, size_t len )

Arguments
=========

``src``
    source address in user space

``len``
    number of bytes to copy


Description
===========

Returns an ``ERR_PTR`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
