
.. _API-eventfd-ctx-fileget:

===================
eventfd_ctx_fileget
===================

*man eventfd_ctx_fileget(9)*

*4.6.0-rc1*

Acquires a reference to the internal eventfd context.


Synopsis
========

.. c:function:: struct eventfd_ctx ⋆ eventfd_ctx_fileget( struct file * file )

Arguments
=========

``file``
    [in] Eventfd file pointer.


Description
===========

Returns a pointer to the internal eventfd context, otherwise the error


pointer
=======

-EINVAL : The ``fd`` file descriptor is not an eventfd file.
