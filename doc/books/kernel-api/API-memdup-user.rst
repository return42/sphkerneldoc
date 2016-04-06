
.. _API-memdup-user:

===========
memdup_user
===========

*man memdup_user(9)*

*4.6.0-rc1*

duplicate memory region from user space


Synopsis
========

.. c:function:: void ⋆ memdup_user( const void __user * src, size_t len )

Arguments
=========

``src``
    source address in user space

``len``
    number of bytes to copy


Description
===========

Returns an ``ERR_PTR`` on failure.
