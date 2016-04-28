.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-equal-no-clocks:

========================
drm_mode_equal_no_clocks
========================

*man drm_mode_equal_no_clocks(9)*

*4.6.0-rc5*

test modes for equality


Synopsis
========

.. c:function:: bool drm_mode_equal_no_clocks( const struct drm_display_mode * mode1, const struct drm_display_mode * mode2 )

Arguments
=========

``mode1``
    first mode

``mode2``
    second mode


Description
===========

Check to see if ``mode1`` and ``mode2`` are equivalent, but don't check
the pixel clocks.


Returns
=======

True if the modes are equal, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
