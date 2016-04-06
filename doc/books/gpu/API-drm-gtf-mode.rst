
.. _API-drm-gtf-mode:

============
drm_gtf_mode
============

*man drm_gtf_mode(9)*

*4.6.0-rc1*

create the modeline based on the GTF algorithm


Synopsis
========

.. c:function:: struct drm_display_mode ⋆ drm_gtf_mode( struct drm_device * dev, int hdisplay, int vdisplay, int vrefresh, bool interlaced, int margins )

Arguments
=========

``dev``
    drm device

``hdisplay``
    hdisplay size

``vdisplay``
    vdisplay size

``vrefresh``
    vrefresh rate.

``interlaced``
    whether to compute an interlaced mode

``margins``
    desired margin (borders) size


Description
===========

return the modeline based on GTF algorithm

This function is to create the modeline based on the GTF algorithm.


Generalized Timing Formula is derived from
==========================================

GTF Spreadsheet by Andy Morrish (1/5/97)


available at http
=================

//www.vesa.org

And it is copied from the file of xserver/hw/xfree86/modes/xf86gtf.c. What I have done is to translate it by using integer calculation. I also refer to the function of
fb_get_mode in the file of drivers/video/fbmon.c


Standard GTF parameters
=======================

M = 600 C = 40 K = 128 J = 20


Returns
=======

The modeline based on the GTF algorithm stored in a drm_display_mode object. The display mode object is allocated with ``drm_mode_create``. Returns NULL when no mode could be
allocated.
