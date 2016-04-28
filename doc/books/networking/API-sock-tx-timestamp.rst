.. -*- coding: utf-8; mode: rst -*-

.. _API-sock-tx-timestamp:

=================
sock_tx_timestamp
=================

*man sock_tx_timestamp(9)*

*4.6.0-rc5*

checks whether the outgoing packet is to be time stamped


Synopsis
========

.. c:function:: void sock_tx_timestamp( const struct sock * sk, __u8 * tx_flags )

Arguments
=========

``sk``
    socket sending this packet

``tx_flags``
    completed with instructions for time stamping


Note
====

callers should take care of initial *tx_flags value (usually 0)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
