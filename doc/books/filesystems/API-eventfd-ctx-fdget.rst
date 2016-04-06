
.. _API-eventfd-ctx-fdget:

=================
eventfd_ctx_fdget
=================

*man eventfd_ctx_fdget(9)*

*4.6.0-rc1*

Acquires a reference to the internal eventfd context.


Synopsis
========

.. c:function:: struct eventfd_ctx ⋆ eventfd_ctx_fdget( int fd )

Arguments
=========

``fd``
    [in] Eventfd file descriptor.


Description
===========

Returns a pointer to the internal eventfd context, otherwise the error


pointers returned by the following functions
============================================

eventfd_fget
