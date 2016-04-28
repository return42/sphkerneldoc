.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-is-stereo:

==================
drm_mode_is_stereo
==================

*man drm_mode_is_stereo(9)*

*4.6.0-rc5*

check for stereo mode flags


Synopsis
========

.. c:function:: bool drm_mode_is_stereo( const struct drm_display_mode * mode )

Arguments
=========

``mode``
    drm_display_mode to check


Returns
=======

True if the mode is one of the stereo modes (like side-by-side), false
if not.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
