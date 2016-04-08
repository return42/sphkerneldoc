
.. _API-eth-type-trans:

==============
eth_type_trans
==============

*man eth_type_trans(9)*

*4.6.0-rc1*

determine the packet's protocol ID.


Synopsis
========

.. c:function:: __be16 eth_type_trans( struct sk_buff * skb, struct net_device * dev )

Arguments
=========

``skb``
    received socket data

``dev``
    receiving network device


Description
===========

The rule here is that we assume 802.3 if the type field is short enough to be a length. This is normal practice and works for any 'now in use' protocol.
