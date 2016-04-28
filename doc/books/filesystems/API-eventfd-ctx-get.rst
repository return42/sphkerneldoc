.. -*- coding: utf-8; mode: rst -*-

.. _API-eventfd-ctx-get:

===============
eventfd_ctx_get
===============

*man eventfd_ctx_get(9)*

*4.6.0-rc5*

Acquires a reference to the internal eventfd context.


Synopsis
========

.. c:function:: struct eventfd_ctx * eventfd_ctx_get( struct eventfd_ctx * ctx )

Arguments
=========

``ctx``
    [in] Pointer to the eventfd context.


Returns
=======

In case of success, returns a pointer to the eventfd context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
