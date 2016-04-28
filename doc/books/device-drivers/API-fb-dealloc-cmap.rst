.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-dealloc-cmap:

===============
fb_dealloc_cmap
===============

*man fb_dealloc_cmap(9)*

*4.6.0-rc5*

deallocate a colormap


Synopsis
========

.. c:function:: void fb_dealloc_cmap( struct fb_cmap * cmap )

Arguments
=========

``cmap``
    frame buffer colormap structure


Description
===========

Deallocates a colormap that was previously allocated with
``fb_alloc_cmap``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
