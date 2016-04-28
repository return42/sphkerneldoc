.. -*- coding: utf-8; mode: rst -*-

.. _API-copy-to-user-fromio:

===================
copy_to_user_fromio
===================

*man copy_to_user_fromio(9)*

*4.6.0-rc5*

copy data from mmio-space to user-space


Synopsis
========

.. c:function:: int copy_to_user_fromio( void __user * dst, const volatile void __iomem * src, size_t count )

Arguments
=========

``dst``
    the destination pointer on user-space

``src``
    the source pointer on mmio

``count``
    the data size to copy in bytes


Description
===========

Copies the data from mmio-space to user-space.


Return
======

Zero if successful, or non-zero on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
