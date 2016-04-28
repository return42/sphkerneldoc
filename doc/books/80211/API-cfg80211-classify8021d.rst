.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-classify8021d:

======================
cfg80211_classify8021d
======================

*man cfg80211_classify8021d(9)*

*4.6.0-rc5*

determine the 802.1p/1d tag for a data frame


Synopsis
========

.. c:function:: unsigned int cfg80211_classify8021d( struct sk_buff * skb, struct cfg80211_qos_map * qos_map )

Arguments
=========

``skb``
    the data frame

``qos_map``
    Interworking QoS mapping or ``NULL`` if not in use


Return
======

The 802.1p/1d tag.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
