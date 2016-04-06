
.. _API-fb-set-cmap:

===========
fb_set_cmap
===========

*man fb_set_cmap(9)*

*4.6.0-rc1*

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
