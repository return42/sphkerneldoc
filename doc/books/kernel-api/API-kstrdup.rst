.. -*- coding: utf-8; mode: rst -*-

.. _API-kstrdup:

=======
kstrdup
=======

*man kstrdup(9)*

*4.6.0-rc5*

allocate space for and copy an existing string


Synopsis
========

.. c:function:: char * kstrdup( const char * s, gfp_t gfp )

Arguments
=========

``s``
    the string to duplicate

``gfp``
    the GFP mask used in the ``kmalloc`` call when allocating memory


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
