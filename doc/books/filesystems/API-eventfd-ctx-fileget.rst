.. -*- coding: utf-8; mode: rst -*-

.. _API-eventfd-ctx-fileget:

===================
eventfd_ctx_fileget
===================

*man eventfd_ctx_fileget(9)*

*4.6.0-rc5*

Acquires a reference to the internal eventfd context.


Synopsis
========

.. c:function:: struct eventfd_ctx * eventfd_ctx_fileget( struct file * file )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
