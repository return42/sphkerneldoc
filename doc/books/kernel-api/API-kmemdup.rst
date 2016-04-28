.. -*- coding: utf-8; mode: rst -*-

.. _API-kmemdup:

=======
kmemdup
=======

*man kmemdup(9)*

*4.6.0-rc5*

duplicate region of memory


Synopsis
========

.. c:function:: void * kmemdup( const void * src, size_t len, gfp_t gfp )

Arguments
=========

``src``
    memory region to duplicate

``len``
    memory region length

``gfp``
    GFP mask to use


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
