.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-default-cmap:

===============
fb_default_cmap
===============

*man fb_default_cmap(9)*

*4.6.0-rc5*

get default colormap


Synopsis
========

.. c:function:: const struct fb_cmap * fb_default_cmap( int len )

Arguments
=========

``len``
    size of palette for a depth


Description
===========

Gets the default colormap for a specific screen depth. ``len`` is the
size of the palette for a particular screen depth.

Returns pointer to a frame buffer colormap structure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
