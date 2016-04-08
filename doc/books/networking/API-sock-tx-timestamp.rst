
.. _API-sock-tx-timestamp:

=================
sock_tx_timestamp
=================

*man sock_tx_timestamp(9)*

*4.6.0-rc1*

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

callers should take care of initial ⋆tx_flags value (usually 0)
