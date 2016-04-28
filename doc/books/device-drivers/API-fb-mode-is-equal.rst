.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-mode-is-equal:

================
fb_mode_is_equal
================

*man fb_mode_is_equal(9)*

*4.6.0-rc5*

compare 2 videomodes


Synopsis
========

.. c:function:: int fb_mode_is_equal( const struct fb_videomode * mode1, const struct fb_videomode * mode2 )

Arguments
=========

``mode1``
    first videomode

``mode2``
    second videomode


RETURNS
=======

1 if equal, 0 if not


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
