.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-equal:

==============
drm_mode_equal
==============

*man drm_mode_equal(9)*

*4.6.0-rc5*

test modes for equality


Synopsis
========

.. c:function:: bool drm_mode_equal( const struct drm_display_mode * mode1, const struct drm_display_mode * mode2 )

Arguments
=========

``mode1``
    first mode

``mode2``
    second mode


Description
===========

Check to see if ``mode1`` and ``mode2`` are equivalent.


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
