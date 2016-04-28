.. -*- coding: utf-8; mode: rst -*-

.. _API-vunmap:

======
vunmap
======

*man vunmap(9)*

*4.6.0-rc5*

release virtual mapping obtained by ``vmap``


Synopsis
========

.. c:function:: void vunmap( const void * addr )

Arguments
=========

``addr``
    memory base address


Description
===========

Free the virtually contiguous memory area starting at ``addr``, which
was created from the page array passed to ``vmap``.

Must not be called in interrupt context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
