.. -*- coding: utf-8; mode: rst -*-

.. _multi-iface:

**************************************
Supporting multiple virtual interfaces
**************************************

TBD

Note: WDS with identical MAC address should almost always be OK

Insert notes about having multiple virtual interfaces with different MAC
addresses here, note which configurations are supported by mac80211, add
notes about supporting hw crypto with it.


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_iterate_active_interfaces


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_iterate_active_interfaces_atomic




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
