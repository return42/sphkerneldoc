
.. _API-skb-pull-rcsum:

==============
skb_pull_rcsum
==============

*man skb_pull_rcsum(9)*

*4.6.0-rc1*

pull skb and update receive checksum


Synopsis
========

.. c:function:: unsigned char ⋆ skb_pull_rcsum( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to update

``len``
    length of data pulled


Description
===========

This function performs an skb_pull on the packet and updates the CHECKSUM_COMPLETE checksum. It should be used on receive path processing instead of skb_pull unless you know
that the checksum difference is zero (e.g., a valid IP header) or you are setting ip_summed to CHECKSUM_NONE.
