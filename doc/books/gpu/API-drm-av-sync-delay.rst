
.. _API-drm-av-sync-delay:

=================
drm_av_sync_delay
=================

*man drm_av_sync_delay(9)*

*4.6.0-rc1*

compute the HDMI/DP sink audio-video sync delay


Synopsis
========

.. c:function:: int drm_av_sync_delay( struct drm_connector * connector, const struct drm_display_mode * mode )

Arguments
=========

``connector``
    connector associated with the HDMI/DP sink

``mode``
    the display mode


Return
======

The HDMI/DP sink's audio-video sync delay in milliseconds or 0 if the sink doesn't support audio or video.
