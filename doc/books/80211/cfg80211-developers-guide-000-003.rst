.. -*- coding: utf-8; mode: rst -*-

==============================
Scanning and BSS list handling
==============================

The scanning process itself is fairly simple, but cfg80211 offers quite
a bit of helper functionality. To start a scan, the scan operation will
be invoked with a scan definition. This scan definition contains the
channels to scan, and the SSIDs to send probe requests for (including
the wildcard, if desired). A passive scan is indicated by having no
SSIDs to probe. Additionally, a scan request may contain extra
information elements that should be added to the probe request. The IEs
are guaranteed to be well-formed, and will not exceed the maximum length
the driver advertised in the wiphy structure.

When scanning finds a BSS, cfg80211 needs to be notified of that,
because it is responsible for maintaining the BSS list; the driver
should not maintain a list itself. For this notification, various
functions exist.

Since drivers do not maintain a BSS list, there are also a number of
functions to search for a BSS and obtain information about it from the
BSS structure cfg80211 maintains. The BSS list is also made available to
userspace.


.. toctree::
    :maxdepth: 1

    API-struct-cfg80211-ssid
    API-struct-cfg80211-scan-request
    API-cfg80211-scan-done
    API-struct-cfg80211-bss
    API-struct-cfg80211-inform-bss
    API-cfg80211-inform-bss-frame-data
    API-cfg80211-inform-bss-data
    API-cfg80211-unlink-bss
    API-cfg80211-find-ie
    API-ieee80211-bss-get-ie




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
