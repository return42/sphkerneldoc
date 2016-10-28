.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/calxeda/xgmac.c

.. _`xgmac_dma_desc_rings_init`:

xgmac_dma_desc_rings_init
=========================

.. c:function:: int xgmac_dma_desc_rings_init(struct net_device *dev)

    init the RX/TX descriptor rings

    :param struct net_device \*dev:
        net device structure

.. _`xgmac_dma_desc_rings_init.description`:

Description
-----------

this function initializes the DMA RX/TX descriptors
and allocates the socket buffers.

.. _`xgmac_tx_complete`:

xgmac_tx_complete
=================

.. c:function:: void xgmac_tx_complete(struct xgmac_priv *priv)

    :param struct xgmac_priv \*priv:
        private driver structure

.. _`xgmac_tx_complete.description`:

Description
-----------

it reclaims resources after transmission completes.

.. _`xgmac_open`:

xgmac_open
==========

.. c:function:: int xgmac_open(struct net_device *dev)

    open entry point of the driver

    :param struct net_device \*dev:
        pointer to the device structure.

.. _`xgmac_open.description`:

Description
-----------

This function is the open entry point of the driver.

.. _`xgmac_open.return-value`:

Return value
------------

0 on success and an appropriate (-)ve integer as defined in errno.h
file on failure.

.. _`xgmac_stop`:

xgmac_stop
==========

.. c:function:: int xgmac_stop(struct net_device *dev)

    close entry point of the driver

    :param struct net_device \*dev:
        device pointer.

.. _`xgmac_stop.description`:

Description
-----------

This is the stop entry point of the driver.

.. _`xgmac_xmit`:

xgmac_xmit
==========

.. c:function:: netdev_tx_t xgmac_xmit(struct sk_buff *skb, struct net_device *dev)

    :param struct sk_buff \*skb:
        the socket buffer

    :param struct net_device \*dev:
        device pointer
        Description : Tx entry point of the driver.

.. _`xgmac_poll`:

xgmac_poll
==========

.. c:function:: int xgmac_poll(struct napi_struct *napi, int budget)

    xgmac poll method (NAPI)

    :param struct napi_struct \*napi:
        pointer to the napi structure.

    :param int budget:
        maximum number of packets that the current CPU can receive from
        all interfaces.
        Description :
        This function implements the the reception process.
        Also it runs the TX completion thread

.. _`xgmac_tx_timeout`:

xgmac_tx_timeout
================

.. c:function:: void xgmac_tx_timeout(struct net_device *dev)

    :param struct net_device \*dev:
        Pointer to net device structure

.. _`xgmac_tx_timeout.description`:

Description
-----------

this function is called when a packet transmission fails to
complete within a reasonable tmrate. The driver will mark the error in the
netdev structure and arrange for the device to be reset to a sane state
in order to transmit a new packet.

.. _`xgmac_set_rx_mode`:

xgmac_set_rx_mode
=================

.. c:function:: void xgmac_set_rx_mode(struct net_device *dev)

    entry point for multicast addressing

    :param struct net_device \*dev:
        pointer to the device structure

.. _`xgmac_set_rx_mode.description`:

Description
-----------

This function is a driver entry point which gets called by the kernel
whenever multicast addresses must be enabled/disabled.

.. _`xgmac_set_rx_mode.return-value`:

Return value
------------

void.

.. _`xgmac_change_mtu`:

xgmac_change_mtu
================

.. c:function:: int xgmac_change_mtu(struct net_device *dev, int new_mtu)

    entry point to change MTU size for the device.

    :param struct net_device \*dev:
        device pointer.

    :param int new_mtu:
        the new MTU size for the device.

.. _`xgmac_change_mtu.description`:

Description
-----------

the Maximum Transfer Unit (MTU) is used by the network layer
to drive packet transmission. Ethernet has an MTU of 1500 octets
(ETH_DATA_LEN). This value can be changed with ifconfig.

.. _`xgmac_change_mtu.return-value`:

Return value
------------

0 on success and an appropriate (-)ve integer as defined in errno.h
file on failure.

.. _`xgmac_probe`:

xgmac_probe
===========

.. c:function:: int xgmac_probe(struct platform_device *pdev)

    :param struct platform_device \*pdev:
        platform device pointer

.. _`xgmac_probe.description`:

Description
-----------

the driver is initialized through platform_device.

.. _`xgmac_remove`:

xgmac_remove
============

.. c:function:: int xgmac_remove(struct platform_device *pdev)

    :param struct platform_device \*pdev:
        platform device pointer

.. _`xgmac_remove.description`:

Description
-----------

this function resets the TX/RX processes, disables the MAC RX/TX
changes the link status, releases the DMA descriptor rings,
unregisters the MDIO bus and unmaps the allocated memory.

.. This file was automatic generated / don't edit.

