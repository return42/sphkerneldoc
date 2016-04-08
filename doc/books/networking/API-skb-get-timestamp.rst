
.. _API-skb-get-timestamp:

=================
skb_get_timestamp
=================

*man skb_get_timestamp(9)*

*4.6.0-rc1*

get timestamp from a skb


Synopsis
========

.. c:function:: void skb_get_timestamp( const struct sk_buff * skb, struct timeval * stamp )

Arguments
=========

``skb``
    skb to get stamp from

``stamp``
    pointer to struct timeval to store stamp in


Description
===========

Timestamps are stored in the skb as offsets to a base timestamp. This function converts the offset back to a struct timeval and stores it in stamp.
