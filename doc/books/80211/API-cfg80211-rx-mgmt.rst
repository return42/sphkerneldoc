.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-rx-mgmt:

================
cfg80211_rx_mgmt
================

*man cfg80211_rx_mgmt(9)*

*4.6.0-rc5*

notification of received, unprocessed management frame


Synopsis
========

.. c:function:: bool cfg80211_rx_mgmt( struct wireless_dev * wdev, int freq, int sig_dbm, const u8 * buf, size_t len, u32 flags )

Arguments
=========

``wdev``
    wireless device receiving the frame

``freq``
    Frequency on which the frame was received in MHz

``sig_dbm``
    signal strength in mBm, or 0 if unknown

``buf``
    Management frame (header + body)

``len``
    length of the frame data

``flags``
    flags, as defined in enum nl80211_rxmgmt_flags


Description
===========

This function is called whenever an Action frame is received for a
station mode interface, but is not processed in kernel.


Return
======

``true`` if a user space application has registered for this frame. For
action frames, that makes it responsible for rejecting unrecognized
action frames; ``false`` otherwise, in which case for action frames the
driver is responsible for rejecting the frame.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
