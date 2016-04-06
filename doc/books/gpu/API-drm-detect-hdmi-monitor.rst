
.. _API-drm-detect-hdmi-monitor:

=======================
drm_detect_hdmi_monitor
=======================

*man drm_detect_hdmi_monitor(9)*

*4.6.0-rc1*

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
