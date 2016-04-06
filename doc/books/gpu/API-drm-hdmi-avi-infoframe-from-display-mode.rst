
.. _API-drm-hdmi-avi-infoframe-from-display-mode:

========================================
drm_hdmi_avi_infoframe_from_display_mode
========================================

*man drm_hdmi_avi_infoframe_from_display_mode(9)*

*4.6.0-rc1*

fill an HDMI AVI infoframe with data from a DRM display mode


Synopsis
========

.. c:function:: int drm_hdmi_avi_infoframe_from_display_mode( struct hdmi_avi_infoframe * frame, const struct drm_display_mode * mode )

Arguments
=========

``frame``
    HDMI AVI infoframe

``mode``
    DRM display mode


Return
======

0 on success or a negative error code on failure.
