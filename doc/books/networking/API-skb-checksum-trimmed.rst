
.. _API-skb-checksum-trimmed:

====================
skb_checksum_trimmed
====================

*man skb_checksum_trimmed(9)*

*4.6.0-rc1*

validate checksum of an skb


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_checksum_trimmed( struct sk_buff * skb, unsigned int transport_len, __sum16(*skb_chkf) struct sk_buff *skb )

Arguments
=========

``skb``
    the skb to check

``transport_len``
    the data length beyond the network header

``skb_chkf``
    checksum function to use


Description
===========

Applies the given checksum function skb_chkf to the provided skb. Returns a checked and maybe trimmed skb. Returns NULL on error.

If the skb has data beyond the given transport length, then a trimmed & cloned skb is checked and returned.

Caller needs to set the skb transport header and free any returned skb if it differs from the provided skb.
