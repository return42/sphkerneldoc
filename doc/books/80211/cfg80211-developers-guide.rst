.. -*- coding: utf-8; mode: rst -*-

++++++++++++++++++++++
The cfg80211 subsystem
++++++++++++++++++++++
    cfg80211 is the configuration API for 802.11 devices in Linux. It
    bridges userspace and drivers, and offers some utility functionality
    associated with 802.11. cfg80211 must, directly or indirectly via
    mac80211, be used by all modern wireless drivers in Linux, so that
    they offer a consistent API through nl80211. For backward
    compatibility, cfg80211 also offers wireless extensions to
    userspace, but hides them from drivers completely.

    Additionally, cfg80211 contains code to help enforce regulatory
    spectrum use restrictions.


.. toctree::
    :maxdepth: 1

    cfg80211-developers-guide-000-001
    cfg80211-developers-guide-000-002
    cfg80211-developers-guide-000-003
    cfg80211-developers-guide-000-004
    cfg80211-developers-guide-000-005
    cfg80211-developers-guide-000-006
    cfg80211-developers-guide-000-007
    cfg80211-developers-guide-000-008




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
