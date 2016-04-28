.. -*- coding: utf-8; mode: rst -*-

.. _API-eventfd-ctx-fdget:

=================
eventfd_ctx_fdget
=================

*man eventfd_ctx_fdget(9)*

*4.6.0-rc5*

Acquires a reference to the internal eventfd context.


Synopsis
========

.. c:function:: struct eventfd_ctx * eventfd_ctx_fdget( int fd )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
