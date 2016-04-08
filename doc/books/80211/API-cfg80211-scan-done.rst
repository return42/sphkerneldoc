
.. _API-cfg80211-scan-done:

==================
cfg80211_scan_done
==================

*man cfg80211_scan_done(9)*

*4.6.0-rc1*

notify that scan finished


Synopsis
========

.. c:function:: void cfg80211_scan_done( struct cfg80211_scan_request * request, bool aborted )

Arguments
=========

``request``
    the corresponding scan request

``aborted``
    set to true if the scan was aborted for any reason, userspace will be notified of that
