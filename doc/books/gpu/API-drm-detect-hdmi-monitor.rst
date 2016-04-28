.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-detect-hdmi-monitor:

=======================
drm_detect_hdmi_monitor
=======================

*man drm_detect_hdmi_monitor(9)*

*4.6.0-rc5*

detect whether monitor is HDMI


Synopsis
========

.. c:function:: bool drm_detect_hdmi_monitor( struct edid * edid )

Arguments
=========

``edid``
    monitor EDID information


Description
===========

Parse the CEA extension according to CEA-861-B.


Return
======

True if the monitor is HDMI, false if not or unknown.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
