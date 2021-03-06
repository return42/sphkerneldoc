.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/arc/emac_main.c

.. _`arc_emac_tx_avail`:

arc_emac_tx_avail
=================

.. c:function:: int arc_emac_tx_avail(struct arc_emac_priv *priv)

    Return the number of available slots in the tx ring.

    :param priv:
        Pointer to ARC EMAC private data structure.
    :type priv: struct arc_emac_priv \*

.. _`arc_emac_tx_avail.return`:

Return
------

the number of slots available for transmission in tx the ring.

.. _`arc_emac_adjust_link`:

arc_emac_adjust_link
====================

.. c:function:: void arc_emac_adjust_link(struct net_device *ndev)

    Adjust the PHY link duplex.

    :param ndev:
        Pointer to the net_device structure.
    :type ndev: struct net_device \*

.. _`arc_emac_adjust_link.description`:

Description
-----------

This function is called to change the duplex setting after auto negotiation
is done by the PHY.

.. _`arc_emac_get_drvinfo`:

arc_emac_get_drvinfo
====================

.. c:function:: void arc_emac_get_drvinfo(struct net_device *ndev, struct ethtool_drvinfo *info)

    Get EMAC driver information.

    :param ndev:
        Pointer to net_device structure.
    :type ndev: struct net_device \*

    :param info:
        Pointer to ethtool_drvinfo structure.
    :type info: struct ethtool_drvinfo \*

.. _`arc_emac_get_drvinfo.description`:

Description
-----------

This implements ethtool command for getting the driver information.
Issue "ethtool -i ethX" under linux prompt to execute this function.

.. _`arc_emac_tx_clean`:

arc_emac_tx_clean
=================

.. c:function:: void arc_emac_tx_clean(struct net_device *ndev)

    clears processed by EMAC Tx BDs.

    :param ndev:
        Pointer to the network device.
    :type ndev: struct net_device \*

.. _`arc_emac_rx`:

arc_emac_rx
===========

.. c:function:: int arc_emac_rx(struct net_device *ndev, int budget)

    processing of Rx packets.

    :param ndev:
        Pointer to the network device.
    :type ndev: struct net_device \*

    :param budget:
        How many BDs to process on 1 call.
    :type budget: int

.. _`arc_emac_rx.return`:

Return
------

Number of processed BDs

Iterate through Rx BDs and deliver received packages to upper layer.

.. _`arc_emac_rx_miss_handle`:

arc_emac_rx_miss_handle
=======================

.. c:function:: void arc_emac_rx_miss_handle(struct net_device *ndev)

    handle R_MISS register

    :param ndev:
        Pointer to the net_device structure.
    :type ndev: struct net_device \*

.. _`arc_emac_rx_stall_check`:

arc_emac_rx_stall_check
=======================

.. c:function:: void arc_emac_rx_stall_check(struct net_device *ndev, int budget, unsigned int work_done)

    check RX stall

    :param ndev:
        Pointer to the net_device structure.
    :type ndev: struct net_device \*

    :param budget:
        How many BDs requested to process on 1 call.
    :type budget: int

    :param work_done:
        How many BDs processed
    :type work_done: unsigned int

.. _`arc_emac_rx_stall_check.description`:

Description
-----------

Under certain conditions EMAC stop reception of incoming packets and
continuously increment R_MISS register instead of saving data into
provided buffer. This function detect that condition and restart
EMAC.

.. _`arc_emac_poll`:

arc_emac_poll
=============

.. c:function:: int arc_emac_poll(struct napi_struct *napi, int budget)

    NAPI poll handler.

    :param napi:
        Pointer to napi_struct structure.
    :type napi: struct napi_struct \*

    :param budget:
        How many BDs to process on 1 call.
    :type budget: int

.. _`arc_emac_poll.return`:

Return
------

Number of processed BDs

.. _`arc_emac_intr`:

arc_emac_intr
=============

.. c:function:: irqreturn_t arc_emac_intr(int irq, void *dev_instance)

    Global interrupt handler for EMAC.

    :param irq:
        irq number.
    :type irq: int

    :param dev_instance:
        device instance.
    :type dev_instance: void \*

.. _`arc_emac_intr.return`:

Return
------

IRQ_HANDLED for all cases.

ARC EMAC has only 1 interrupt line, and depending on bits raised in
STATUS register we may tell what is a reason for interrupt to fire.

.. _`arc_emac_open`:

arc_emac_open
=============

.. c:function:: int arc_emac_open(struct net_device *ndev)

    Open the network device.

    :param ndev:
        Pointer to the network device.
    :type ndev: struct net_device \*

.. _`arc_emac_open.return`:

Return
------

0, on success or non-zero error value on failure.

This function sets the MAC address, requests and enables an IRQ
for the EMAC device and starts the Tx queue.
It also connects to the phy device.

.. _`arc_emac_set_rx_mode`:

arc_emac_set_rx_mode
====================

.. c:function:: void arc_emac_set_rx_mode(struct net_device *ndev)

    Change the receive filtering mode.

    :param ndev:
        Pointer to the network device.
    :type ndev: struct net_device \*

.. _`arc_emac_set_rx_mode.description`:

Description
-----------

This function enables/disables promiscuous or all-multicast mode
and updates the multicast filtering list of the network device.

.. _`arc_free_tx_queue`:

arc_free_tx_queue
=================

.. c:function:: void arc_free_tx_queue(struct net_device *ndev)

    free skb from tx queue

    :param ndev:
        Pointer to the network device.
    :type ndev: struct net_device \*

.. _`arc_free_tx_queue.description`:

Description
-----------

This function must be called while EMAC disable

.. _`arc_free_rx_queue`:

arc_free_rx_queue
=================

.. c:function:: void arc_free_rx_queue(struct net_device *ndev)

    free skb from rx queue

    :param ndev:
        Pointer to the network device.
    :type ndev: struct net_device \*

.. _`arc_free_rx_queue.description`:

Description
-----------

This function must be called while EMAC disable

.. _`arc_emac_stop`:

arc_emac_stop
=============

.. c:function:: int arc_emac_stop(struct net_device *ndev)

    Close the network device.

    :param ndev:
        Pointer to the network device.
    :type ndev: struct net_device \*

.. _`arc_emac_stop.description`:

Description
-----------

This function stops the Tx queue, disables interrupts and frees the IRQ for
the EMAC device.
It also disconnects the PHY device associated with the EMAC device.

.. _`arc_emac_stats`:

arc_emac_stats
==============

.. c:function:: struct net_device_stats *arc_emac_stats(struct net_device *ndev)

    Get system network statistics.

    :param ndev:
        Pointer to net_device structure.
    :type ndev: struct net_device \*

.. _`arc_emac_stats.description`:

Description
-----------

Returns the address of the device statistics structure.
Statistics are updated in interrupt handler.

.. _`arc_emac_tx`:

arc_emac_tx
===========

.. c:function:: int arc_emac_tx(struct sk_buff *skb, struct net_device *ndev)

    Starts the data transmission.

    :param skb:
        sk_buff pointer that contains data to be Transmitted.
    :type skb: struct sk_buff \*

    :param ndev:
        Pointer to net_device structure.
    :type ndev: struct net_device \*

.. _`arc_emac_tx.return`:

Return
------

NETDEV_TX_OK, on success
NETDEV_TX_BUSY, if any of the descriptors are not free.

This function is invoked from upper layers to initiate transmission.

.. _`arc_emac_set_address`:

arc_emac_set_address
====================

.. c:function:: int arc_emac_set_address(struct net_device *ndev, void *p)

    Set the MAC address for this device.

    :param ndev:
        Pointer to net_device structure.
    :type ndev: struct net_device \*

    :param p:
        6 byte Address to be written as MAC address.
    :type p: void \*

.. _`arc_emac_set_address.description`:

Description
-----------

This function copies the HW address from the sockaddr structure to the
net_device structure and updates the address in HW.

.. _`arc_emac_set_address.return`:

Return
------

-EBUSY if the net device is busy or 0 if the address is set
successfully.

.. _`arc_emac_restart`:

arc_emac_restart
================

.. c:function:: void arc_emac_restart(struct net_device *ndev)

    Restart EMAC

    :param ndev:
        Pointer to net_device structure.
    :type ndev: struct net_device \*

.. _`arc_emac_restart.description`:

Description
-----------

This function do hardware reset of EMAC in order to restore
network packets reception.

.. This file was automatic generated / don't edit.

