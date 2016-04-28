.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-copy-cmap:

============
fb_copy_cmap
============

*man fb_copy_cmap(9)*

*4.6.0-rc5*

copy a colormap


Synopsis
========

.. c:function:: int fb_copy_cmap( const struct fb_cmap * from, struct fb_cmap * to )

Arguments
=========

``from``
    frame buffer colormap structure

``to``
    frame buffer colormap structure


Description
===========

Copy contents of colormap from ``from`` to ``to``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
