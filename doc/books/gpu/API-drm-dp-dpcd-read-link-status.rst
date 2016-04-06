
.. _API-drm-dp-dpcd-read-link-status:

============================
drm_dp_dpcd_read_link_status
============================

*man drm_dp_dpcd_read_link_status(9)*

*4.6.0-rc1*

read DPCD link status (bytes 0x202-0x207)


Synopsis
========

.. c:function:: int drm_dp_dpcd_read_link_status( struct drm_dp_aux * aux, u8 status[DP_LINK_STATUS_SIZE] )

Arguments
=========

``aux``
    DisplayPort AUX channel

``status[DP_LINK_STATUS_SIZE]``
    buffer to store the link status in (must be at least 6 bytes)


Description
===========

Returns the number of bytes transferred on success or a negative error code on failure.
