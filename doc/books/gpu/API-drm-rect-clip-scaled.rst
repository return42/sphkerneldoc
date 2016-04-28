.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rect-clip-scaled:

====================
drm_rect_clip_scaled
====================

*man drm_rect_clip_scaled(9)*

*4.6.0-rc5*

perform a scaled clip operation


Synopsis
========

.. c:function:: bool drm_rect_clip_scaled( struct drm_rect * src, struct drm_rect * dst, const struct drm_rect * clip, int hscale, int vscale )

Arguments
=========

``src``
    source window rectangle

``dst``
    destination window rectangle

``clip``
    clip rectangle

``hscale``
    horizontal scaling factor

``vscale``
    vertical scaling factor


Description
===========

Clip rectangle ``dst`` by rectangle ``clip``. Clip rectangle ``src`` by
the same amounts multiplied by ``hscale`` and ``vscale``.


RETURNS
=======

``true`` if rectangle ``dst`` is still visible after being clipped,
``false`` otherwise


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
