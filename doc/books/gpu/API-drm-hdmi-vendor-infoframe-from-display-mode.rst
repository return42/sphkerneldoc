
.. _API-drm-hdmi-vendor-infoframe-from-display-mode:

===========================================
drm_hdmi_vendor_infoframe_from_display_mode
===========================================

*man drm_hdmi_vendor_infoframe_from_display_mode(9)*

*4.6.0-rc1*

fill an HDMI infoframe with data from a DRM display mode


Synopsis
========

.. c:function:: int drm_hdmi_vendor_infoframe_from_display_mode( struct hdmi_vendor_infoframe * frame, const struct drm_display_mode * mode )

Arguments
=========

``frame``
    HDMI vendor infoframe

``mode``
    DRM display mode


Description
===========

Note that there's is a need to send HDMI vendor infoframes only when using a 4k or stereoscopic 3D mode. So when giving any other mode as input this function will return -EINVAL,
error that can be safely ignored.


Return
======

0 on success or a negative error code on failure.
