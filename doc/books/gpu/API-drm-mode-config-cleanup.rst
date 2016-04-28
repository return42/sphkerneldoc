.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-config-cleanup:

=======================
drm_mode_config_cleanup
=======================

*man drm_mode_config_cleanup(9)*

*4.6.0-rc5*

free up DRM mode_config info


Synopsis
========

.. c:function:: void drm_mode_config_cleanup( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Free up all the connectors and CRTCs associated with this DRM device,
then free up the framebuffers and associated buffer objects.

Note that since this /should/ happen single-threaded at driver/device
teardown time, no locking is required. It's the driver's job to ensure
that this guarantee actually holds true.


FIXME
=====

cleanup any dangling user buffer objects too


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
