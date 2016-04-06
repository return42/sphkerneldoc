
.. _API-memdup-user-nul:

===============
memdup_user_nul
===============

*man memdup_user_nul(9)*

*4.6.0-rc1*

duplicate memory region from user space and NUL-terminate


Synopsis
========

.. c:function:: void ⋆ memdup_user_nul( const void __user * src, size_t len )

Arguments
=========

``src``
    source address in user space

``len``
    number of bytes to copy


Description
===========

Returns an ``ERR_PTR`` on failure.
