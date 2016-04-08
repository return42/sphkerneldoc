
.. _API-copy-from-user-toio:

===================
copy_from_user_toio
===================

*man copy_from_user_toio(9)*

*4.6.0-rc1*

copy data from user-space to mmio-space


Synopsis
========

.. c:function:: int copy_from_user_toio( volatile void __iomem * dst, const void __user * src, size_t count )

Arguments
=========

``dst``
    the destination pointer on mmio-space

``src``
    the source pointer on user-space

``count``
    the data size to copy in bytes


Description
===========

Copies the data from user-space to mmio-space.


Return
======

Zero if successful, or non-zero on failure.
