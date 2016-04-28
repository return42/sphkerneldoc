.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gtf-mode-complex:

====================
drm_gtf_mode_complex
====================

*man drm_gtf_mode_complex(9)*

*4.6.0-rc5*

create the modeline based on the full GTF algorithm


Synopsis
========

.. c:function:: struct drm_display_mode * drm_gtf_mode_complex( struct drm_device * dev, int hdisplay, int vdisplay, int vrefresh, bool interlaced, int margins, int GTF_M, int GTF_2C, int GTF_K, int GTF_2J )

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

``GTF_M``
    extended GTF formula parameters

``GTF_2C``
    extended GTF formula parameters

``GTF_K``
    extended GTF formula parameters

``GTF_2J``
    extended GTF formula parameters


Description
===========

GTF feature blocks specify C and J in multiples of 0.5, so we pass them
in here multiplied by two. For a C of 40, pass in 80.


Returns
=======

The modeline based on the full GTF algorithm stored in a
drm_display_mode object. The display mode object is allocated with
``drm_mode_create``. Returns NULL when no mode could be allocated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
