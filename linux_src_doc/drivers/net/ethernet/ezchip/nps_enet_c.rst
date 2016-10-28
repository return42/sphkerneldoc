.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/ezchip/nps_enet.c

.. _`nps_enet_poll`:

nps_enet_poll
=============

.. c:function:: int nps_enet_poll(struct napi_struct *napi, int budget)

    NAPI poll handler.

    :param struct napi_struct \*napi:
        Pointer to napi_struct structure.

    :param int budget:
        How many frames to process on one call.

.. _`nps_enet_poll.return`:

Return
------

Number of processed frames

.. _`nps_enet_irq_handler`:

nps_enet_irq_handler
====================

.. c:function:: irqreturn_t nps_enet_irq_handler(s32 irq, void *dev_instance)

    Global interrupt handler for ENET.

    :param s32 irq:
        irq number.

    :param void \*dev_instance:
        device instance.

.. _`nps_enet_irq_handler.return`:

Return
------

IRQ_HANDLED for all cases.

EZchip ENET has 2 interrupt causes, and depending on bits raised in
CTRL registers we may tell what is a reason for interrupt to fire up.
We got one for RX and the other for TX (completion).

.. _`nps_enet_hw_reset`:

nps_enet_hw_reset
=================

.. c:function:: void nps_enet_hw_reset(struct net_device *ndev)

    Reset the network device.

    :param struct net_device \*ndev:
        Pointer to the network device.

.. _`nps_enet_hw_reset.description`:

Description
-----------

This function reset the PCS and TX fifo.
The programming model is to set the relevant reset bits
wait for some time for this to propagate and then unset
the reset bits. This way we ensure that reset procedure
is done successfully by device.

.. _`nps_enet_set_mac_address`:

nps_enet_set_mac_address
========================

.. c:function:: s32 nps_enet_set_mac_address(struct net_device *ndev, void *p)

    Set the MAC address for this device.

    :param struct net_device \*ndev:
        Pointer to net_device structure.

    :param void \*p:
        6 byte Address to be written as MAC address.

.. _`nps_enet_set_mac_address.description`:

Description
-----------

This function copies the HW address from the sockaddr structure to the
net_device structure and updates the address in HW.

.. _`nps_enet_set_mac_address.return`:

Return
------

-EBUSY if the net device is busy or 0 if the address is set
successfully.

.. _`nps_enet_set_rx_mode`:

nps_enet_set_rx_mode
====================

.. c:function:: void nps_enet_set_rx_mode(struct net_device *ndev)

    Change the receive filtering mode.

    :param struct net_device \*ndev:
        Pointer to the network device.

.. _`nps_enet_set_rx_mode.description`:

Description
-----------

This function enables/disables promiscuous mode

.. _`nps_enet_open`:

nps_enet_open
=============

.. c:function:: s32 nps_enet_open(struct net_device *ndev)

    Open the network device.

    :param struct net_device \*ndev:
        Pointer to the network device.

.. _`nps_enet_open.return`:

Return
------

0, on success or non-zero error value on failure.

This function sets the MAC address, requests and enables an IRQ
for the ENET device and starts the Tx queue.

.. _`nps_enet_stop`:

nps_enet_stop
=============

.. c:function:: s32 nps_enet_stop(struct net_device *ndev)

    Close the network device.

    :param struct net_device \*ndev:
        Pointer to the network device.

.. _`nps_enet_stop.description`:

Description
-----------

This function stops the Tx queue, disables interrupts for the ENET device.

.. _`nps_enet_start_xmit`:

nps_enet_start_xmit
===================

.. c:function:: netdev_tx_t nps_enet_start_xmit(struct sk_buff *skb, struct net_device *ndev)

    Starts the data transmission.

    :param struct sk_buff \*skb:
        sk_buff pointer that contains data to be Transmitted.

    :param struct net_device \*ndev:
        Pointer to net_device structure.

.. _`nps_enet_start_xmit.return`:

Return
------

NETDEV_TX_OK, on success
NETDEV_TX_BUSY, if any of the descriptors are not free.

This function is invoked from upper layers to initiate transmission.

.. This file was automatic generated / don't edit.

