.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-set-cmap:

===========
fb_set_cmap
===========

*man fb_set_cmap(9)*

*4.6.0-rc5*

set the colormap


Synopsis
========

.. c:function:: int fb_set_cmap( struct fb_cmap * cmap, struct fb_info * info )

Arguments
=========

``cmap``
    frame buffer colormap structure

``info``
    frame buffer info structure


Description
===========

Sets the colormap ``cmap`` for a screen of device ``info``.

Returns negative errno on error, or zero on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
