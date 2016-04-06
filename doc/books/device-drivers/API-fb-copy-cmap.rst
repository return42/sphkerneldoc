
.. _API-fb-copy-cmap:

============
fb_copy_cmap
============

*man fb_copy_cmap(9)*

*4.6.0-rc1*

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
