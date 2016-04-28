.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-cvt-mode:

============
drm_cvt_mode
============

*man drm_cvt_mode(9)*

*4.6.0-rc5*

create a modeline based on the CVT algorithm


Synopsis
========

.. c:function:: struct drm_display_mode * drm_cvt_mode( struct drm_device * dev, int hdisplay, int vdisplay, int vrefresh, bool reduced, bool interlaced, bool margins )

Arguments
=========

``dev``
    drm device

``hdisplay``
    hdisplay size

``vdisplay``
    vdisplay size

``vrefresh``
    vrefresh rate

``reduced``
    whether to use reduced blanking

``interlaced``
    whether to compute an interlaced mode

``margins``
    whether to add margins (borders)


Description
===========

This function is called to generate the modeline based on CVT algorithm
according to the hdisplay, vdisplay, vrefresh. It is based from the
VESA(TM) Coordinated Video Timing Generator by Graham Loveridge April 9,
2003 available at


http
====

//www.elo.utfsm.cl/~elo212/docs/CVTd6r1.xls

And it is copied from xf86CVTmode in xserver/hw/xfree86/modes/xf86cvt.c.
What I have done is to translate it by using integer calculation.


Returns
=======

The modeline based on the CVT algorithm stored in a drm_display_mode
object. The display mode object is allocated with ``drm_mode_create``.
Returns NULL when no mode could be allocated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
