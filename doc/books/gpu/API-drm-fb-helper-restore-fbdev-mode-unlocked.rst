.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-restore-fbdev-mode-unlocked:

=========================================
drm_fb_helper_restore_fbdev_mode_unlocked
=========================================

*man drm_fb_helper_restore_fbdev_mode_unlocked(9)*

*4.6.0-rc5*

restore fbdev configuration


Synopsis
========

.. c:function:: int drm_fb_helper_restore_fbdev_mode_unlocked( struct drm_fb_helper * fb_helper )

Arguments
=========

``fb_helper``
    fbcon to restore


Description
===========

This should be called from driver's drm ->lastclose callback when
implementing an fbcon on top of kms using this helper. This ensures that
the user isn't greeted with a black screen when e.g. X dies.


RETURNS
=======

Zero if everything went ok, negative error code otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
