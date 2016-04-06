
.. _API-fb-dealloc-cmap:

===============
fb_dealloc_cmap
===============

*man fb_dealloc_cmap(9)*

*4.6.0-rc1*

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

Deallocates a colormap that was previously allocated with ``fb_alloc_cmap``.
