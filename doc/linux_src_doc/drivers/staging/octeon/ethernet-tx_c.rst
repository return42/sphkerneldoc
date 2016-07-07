.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/octeon/ethernet-tx.c

.. _`cvm_oct_xmit`:

cvm_oct_xmit
============

.. c:function:: int cvm_oct_xmit(struct sk_buff *skb, struct net_device *dev)

    transmit a packet

    :param struct sk_buff \*skb:
        Packet to send

    :param struct net_device \*dev:
        Device info structure

.. _`cvm_oct_xmit.description`:

Description
-----------

Returns Always returns NETDEV_TX_OK

.. _`cvm_oct_xmit_pow`:

cvm_oct_xmit_pow
================

.. c:function:: int cvm_oct_xmit_pow(struct sk_buff *skb, struct net_device *dev)

    transmit a packet to the POW

    :param struct sk_buff \*skb:
        Packet to send

    :param struct net_device \*dev:
        Device info structure
        Returns Always returns zero

.. _`cvm_oct_tx_shutdown_dev`:

cvm_oct_tx_shutdown_dev
=======================

.. c:function:: void cvm_oct_tx_shutdown_dev(struct net_device *dev)

    free all skb that are currently queued for TX.

    :param struct net_device \*dev:
        Device being shutdown

.. This file was automatic generated / don't edit.

