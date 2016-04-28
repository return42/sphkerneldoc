.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-hsync:

==============
drm_mode_hsync
==============

*man drm_mode_hsync(9)*

*4.6.0-rc5*

get the hsync of a mode


Synopsis
========

.. c:function:: int drm_mode_hsync( const struct drm_display_mode * mode )

Arguments
=========

``mode``
    mode


Returns
=======

``modes``'s hsync rate in kHz, rounded to the nearest integer.
Calculates the value first if it is not yet set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
