
.. _API-skb-checksum-setup:

==================
skb_checksum_setup
==================

*man skb_checksum_setup(9)*

*4.6.0-rc1*

set up partial checksum offset


Synopsis
========

.. c:function:: int skb_checksum_setup( struct sk_buff * skb, bool recalculate )

Arguments
=========

``skb``
    the skb to set up

``recalculate``
    if true the pseudo-header checksum will be recalculated
