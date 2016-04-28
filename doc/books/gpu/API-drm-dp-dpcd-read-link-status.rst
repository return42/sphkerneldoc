.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-dpcd-read-link-status:

============================
drm_dp_dpcd_read_link_status
============================

*man drm_dp_dpcd_read_link_status(9)*

*4.6.0-rc5*

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

Returns the number of bytes transferred on success or a negative error
code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
