.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-detect-monitor-audio:

========================
drm_detect_monitor_audio
========================

*man drm_detect_monitor_audio(9)*

*4.6.0-rc5*

check monitor audio capability


Synopsis
========

.. c:function:: bool drm_detect_monitor_audio( struct edid * edid )

Arguments
=========

``edid``
    EDID block to scan


Description
===========

Monitor should have CEA extension block. If monitor has 'basic audio',
but no CEA audio blocks, it's 'basic audio' only. If there is any audio
extension block and supported audio format, assume at least 'basic
audio' support, even if 'basic audio' is not defined in EDID.


Return
======

True if the monitor supports audio, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
