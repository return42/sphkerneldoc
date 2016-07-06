.. -*- coding: utf-8; mode: rst -*-

.. _AP:

*************************
Access point mode support
*************************

TBD

Some parts of the if_conf should be discussed here instead

Insert notes about VLAN interfaces with hw crypto here or in the hw
crypto chapter.


.. _ps-client:

support for powersaving clients
===============================


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :doc: AP support for powersaving clients


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_get_buffered_bc


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_beacon_get


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_sta_eosp


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_frame_release_type


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_sta_ps_transition


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_sta_ps_transition_ni


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_sta_set_buffered


.. kernel-doc:: include/net/mac80211.h
    :man-sect: 9
    :functions: ieee80211_sta_block_awake




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
