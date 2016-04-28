.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-calc-aspect-ratio:

======================
v4l2_calc_aspect_ratio
======================

*man v4l2_calc_aspect_ratio(9)*

*4.6.0-rc5*

calculate the aspect ratio based on bytes 0x15 and 0x16 from the EDID.


Synopsis
========

.. c:function:: struct v4l2_fract v4l2_calc_aspect_ratio( u8 hor_landscape, u8 vert_portrait )

Arguments
=========

``hor_landscape``
    byte 0x15 from the EDID.

``vert_portrait``
    byte 0x16 from the EDID.


Description
===========

Determines the aspect ratio from the EDID. See VESA Enhanced EDID
standard, release A, rev 2, section 3.6.2: “Horizontal and Vertical
Screen Size or Aspect Ratio”


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
