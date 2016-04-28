.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-scan-done:

==================
cfg80211_scan_done
==================

*man cfg80211_scan_done(9)*

*4.6.0-rc5*

notify that scan finished


Synopsis
========

.. c:function:: void cfg80211_scan_done( struct cfg80211_scan_request * request, bool aborted )

Arguments
=========

``request``
    the corresponding scan request

``aborted``
    set to true if the scan was aborted for any reason, userspace will
    be notified of that


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
