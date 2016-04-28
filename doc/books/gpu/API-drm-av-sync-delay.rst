.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-av-sync-delay:

=================
drm_av_sync_delay
=================

*man drm_av_sync_delay(9)*

*4.6.0-rc5*

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

The HDMI/DP sink's audio-video sync delay in milliseconds or 0 if the
sink doesn't support audio or video.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
