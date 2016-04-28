.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-checksum-setup:

==================
skb_checksum_setup
==================

*man skb_checksum_setup(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
