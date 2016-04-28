.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-tx-error:

============
skb_tx_error
============

*man skb_tx_error(9)*

*4.6.0-rc5*

report an sk_buff xmit error


Synopsis
========

.. c:function:: void skb_tx_error( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer that triggered an error


Description
===========

Report xmit error if a device callback is tracking this skb. skb must be
freed afterwards.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
