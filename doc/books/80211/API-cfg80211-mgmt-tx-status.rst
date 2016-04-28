.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-mgmt-tx-status:

=======================
cfg80211_mgmt_tx_status
=======================

*man cfg80211_mgmt_tx_status(9)*

*4.6.0-rc5*

notification of TX status for management frame


Synopsis
========

.. c:function:: void cfg80211_mgmt_tx_status( struct wireless_dev * wdev, u64 cookie, const u8 * buf, size_t len, bool ack, gfp_t gfp )

Arguments
=========

``wdev``
    wireless device receiving the frame

``cookie``
    Cookie returned by cfg80211_ops:: ``mgmt_tx``

``buf``
    Management frame (header + body)

``len``
    length of the frame data

``ack``
    Whether frame was acknowledged

``gfp``
    context flags


Description
===========

This function is called whenever a management frame was requested to be


transmitted with cfg80211_ops
=============================

:``mgmt_tx`` to report the TX status of the transmission attempt.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
