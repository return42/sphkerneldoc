
.. _API-cfg80211-classify8021d:

======================
cfg80211_classify8021d
======================

*man cfg80211_classify8021d(9)*

*4.6.0-rc1*

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
