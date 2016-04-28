.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-get-timestamp:

=================
skb_get_timestamp
=================

*man skb_get_timestamp(9)*

*4.6.0-rc5*

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

Timestamps are stored in the skb as offsets to a base timestamp. This
function converts the offset back to a struct timeval and stores it in
stamp.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
