
.. _API-ieee80211-scan-completed:

========================
ieee80211_scan_completed
========================

*man ieee80211_scan_completed(9)*

*4.6.0-rc1*

completed hardware scan


Synopsis
========

.. c:function:: void ieee80211_scan_completed( struct ieee80211_hw * hw, bool aborted )

Arguments
=========

``hw``
    the hardware that finished the scan

``aborted``
    set to true if scan was aborted


Description
===========

When hardware scan offload is used (i.e. the ``hw_scan`` callback is assigned) this function needs to be called by the driver to notify mac80211 that the scan finished. This
function can be called from any context, including hardirq context.
