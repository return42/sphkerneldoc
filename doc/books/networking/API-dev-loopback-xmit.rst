.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-loopback-xmit:

=================
dev_loopback_xmit
=================

*man dev_loopback_xmit(9)*

*4.6.0-rc5*

loop back ``skb``


Synopsis
========

.. c:function:: int dev_loopback_xmit( struct net * net, struct sock * sk, struct sk_buff * skb )

Arguments
=========

``net``
    network namespace this loopback is happening in

``sk``
    sk needed to be a netfilter okfn

``skb``
    buffer to transmit


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
