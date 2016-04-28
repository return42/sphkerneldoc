.. -*- coding: utf-8; mode: rst -*-

.. _API-eventfd-ctx-put:

===============
eventfd_ctx_put
===============

*man eventfd_ctx_put(9)*

*4.6.0-rc5*

Releases a reference to the internal eventfd context.


Synopsis
========

.. c:function:: void eventfd_ctx_put( struct eventfd_ctx * ctx )

Arguments
=========

``ctx``
    [in] Pointer to eventfd context.


Description
===========

The eventfd context reference must have been previously acquired either
with ``eventfd_ctx_get`` or ``eventfd_ctx_fdget``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
