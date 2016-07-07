.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/xilinx/xilinx_axienet_main.c

.. _`axienet_dma_in32`:

axienet_dma_in32
================

.. c:function:: u32 axienet_dma_in32(struct axienet_local *lp, off_t reg)

    Memory mapped Axi DMA register read

    :param struct axienet_local \*lp:
        Pointer to axienet local structure

    :param off_t reg:
        Address offset from the base address of the Axi DMA core

.. _`axienet_dma_in32.return`:

Return
------

The contents of the Axi DMA register

This function returns the contents of the corresponding Axi DMA register.

.. _`axienet_dma_out32`:

axienet_dma_out32
=================

.. c:function:: void axienet_dma_out32(struct axienet_local *lp, off_t reg, u32 value)

    Memory mapped Axi DMA register write.

    :param struct axienet_local \*lp:
        Pointer to axienet local structure

    :param off_t reg:
        Address offset from the base address of the Axi DMA core

    :param u32 value:
        Value to be written into the Axi DMA register

.. _`axienet_dma_out32.description`:

Description
-----------

This function writes the desired value into the corresponding Axi DMA
register.

.. _`axienet_dma_bd_release`:

axienet_dma_bd_release
======================

.. c:function:: void axienet_dma_bd_release(struct net_device *ndev)

    Release buffer descriptor rings

    :param struct net_device \*ndev:
        Pointer to the net_device structure

.. _`axienet_dma_bd_release.description`:

Description
-----------

This function is used to release the descriptors allocated in
axienet_dma_bd_init. axienet_dma_bd_release is called when Axi Ethernet
driver stop api is called.

.. _`axienet_dma_bd_init`:

axienet_dma_bd_init
===================

.. c:function:: int axienet_dma_bd_init(struct net_device *ndev)

    Setup buffer descriptor rings for Axi DMA

    :param struct net_device \*ndev:
        Pointer to the net_device structure

.. _`axienet_dma_bd_init.return`:

Return
------

0, on success -ENOMEM, on failure

This function is called to initialize the Rx and Tx DMA descriptor
rings. This initializes the descriptors with required default values
and is called when Axi Ethernet driver reset is called.

.. _`axienet_set_mac_address`:

axienet_set_mac_address
=======================

.. c:function:: void axienet_set_mac_address(struct net_device *ndev, void *address)

    Write the MAC address

    :param struct net_device \*ndev:
        Pointer to the net_device structure

    :param void \*address:
        6 byte Address to be written as MAC address

.. _`axienet_set_mac_address.description`:

Description
-----------

This function is called to initialize the MAC address of the Axi Ethernet
core. It writes to the UAW0 and UAW1 registers of the core.

.. _`netdev_set_mac_address`:

netdev_set_mac_address
======================

.. c:function:: int netdev_set_mac_address(struct net_device *ndev, void *p)

    Write the MAC address (from outside the driver)

    :param struct net_device \*ndev:
        Pointer to the net_device structure

    :param void \*p:
        6 byte Address to be written as MAC address

.. _`netdev_set_mac_address.return`:

Return
------

0 for all conditions. Presently, there is no failure case.

This function is called to initialize the MAC address of the Axi Ethernet
core. It calls the core specific axienet_set_mac_address. This is the
function that goes into net_device_ops structure entry ndo_set_mac_address.

.. _`axienet_set_multicast_list`:

axienet_set_multicast_list
==========================

.. c:function:: void axienet_set_multicast_list(struct net_device *ndev)

    Prepare the multicast table

    :param struct net_device \*ndev:
        Pointer to the net_device structure

.. _`axienet_set_multicast_list.description`:

Description
-----------

This function is called to initialize the multicast table during
initialization. The Axi Ethernet basic multicast support has a four-entry
multicast table which is initialized here. Additionally this function
goes into the net_device_ops structure entry ndo_set_multicast_list. This
means whenever the multicast table entries need to be updated this
function gets called.

.. _`axienet_setoptions`:

axienet_setoptions
==================

.. c:function:: void axienet_setoptions(struct net_device *ndev, u32 options)

    Set an Axi Ethernet option

    :param struct net_device \*ndev:
        Pointer to the net_device structure

    :param u32 options:
        Option to be enabled/disabled

.. _`axienet_setoptions.description`:

Description
-----------

The Axi Ethernet core has multiple features which can be selectively turned
on or off. The typical options could be jumbo frame option, basic VLAN
option, promiscuous mode option etc. This function is used to set or clear
these options in the Axi Ethernet hardware. This is done through
axienet_option structure .

.. _`axienet_device_reset`:

axienet_device_reset
====================

.. c:function:: void axienet_device_reset(struct net_device *ndev)

    Reset and initialize the Axi Ethernet hardware.

    :param struct net_device \*ndev:
        Pointer to the net_device structure

.. _`axienet_device_reset.description`:

Description
-----------

This function is called to reset and initialize the Axi Ethernet core. This
is typically called during initialization. It does a reset of the Axi DMA
Rx/Tx channels and initializes the Axi DMA BDs. Since Axi DMA reset lines
areconnected to Axi Ethernet reset lines, this in turn resets the Axi
Ethernet core. No separate hardware reset is done for the Axi Ethernet
core.

.. _`axienet_adjust_link`:

axienet_adjust_link
===================

.. c:function:: void axienet_adjust_link(struct net_device *ndev)

    Adjust the PHY link speed/duplex.

    :param struct net_device \*ndev:
        Pointer to the net_device structure

.. _`axienet_adjust_link.description`:

Description
-----------

This function is called to change the speed and duplex setting after
auto negotiation is done by the PHY. This is the function that gets
registered with the PHY interface through the "of_phy_connect" call.

.. _`axienet_start_xmit_done`:

axienet_start_xmit_done
=======================

.. c:function:: void axienet_start_xmit_done(struct net_device *ndev)

    Invoked once a transmit is completed by the Axi DMA Tx channel.

    :param struct net_device \*ndev:
        Pointer to the net_device structure

.. _`axienet_start_xmit_done.description`:

Description
-----------

This function is invoked from the Axi DMA Tx isr to notify the completion
of transmit operation. It clears fields in the corresponding Tx BDs and
unmaps the corresponding buffer so that CPU can regain ownership of the
buffer. It finally invokes "netif_wake_queue" to restart transmission if
required.

.. _`axienet_check_tx_bd_space`:

axienet_check_tx_bd_space
=========================

.. c:function:: int axienet_check_tx_bd_space(struct axienet_local *lp, int num_frag)

    Checks if a BD/group of BDs are currently busy

    :param struct axienet_local \*lp:
        Pointer to the axienet_local structure

    :param int num_frag:
        The number of BDs to check for

.. _`axienet_check_tx_bd_space.return`:

Return
------

0, on success
NETDEV_TX_BUSY, if any of the descriptors are not free

This function is invoked before BDs are allocated and transmission starts.
This function returns 0 if a BD or group of BDs can be allocated for
transmission. If the BD or any of the BDs are not free the function
returns a busy status. This is invoked from axienet_start_xmit.

.. _`axienet_start_xmit`:

axienet_start_xmit
==================

.. c:function:: int axienet_start_xmit(struct sk_buff *skb, struct net_device *ndev)

    Starts the transmission.

    :param struct sk_buff \*skb:
        sk_buff pointer that contains data to be Txed.

    :param struct net_device \*ndev:
        Pointer to net_device structure.

.. _`axienet_start_xmit.return`:

Return
------

NETDEV_TX_OK, on success
NETDEV_TX_BUSY, if any of the descriptors are not free

This function is invoked from upper layers to initiate transmission. The
function uses the next available free BDs and populates their fields to
start the transmission. Additionally if checksum offloading is supported,
it populates AXI Stream Control fields with appropriate values.

.. _`axienet_recv`:

axienet_recv
============

.. c:function:: void axienet_recv(struct net_device *ndev)

    Is called from Axi DMA Rx Isr to complete the received BD processing.

    :param struct net_device \*ndev:
        Pointer to net_device structure.

.. _`axienet_recv.description`:

Description
-----------

This function is invoked from the Axi DMA Rx isr to process the Rx BDs. It
does minimal processing and invokes "netif_rx" to complete further
processing.

.. _`axienet_tx_irq`:

axienet_tx_irq
==============

.. c:function:: irqreturn_t axienet_tx_irq(int irq, void *_ndev)

    Tx Done Isr.

    :param int irq:
        irq number

    :param void \*_ndev:
        net_device pointer

.. _`axienet_tx_irq.return`:

Return
------

IRQ_HANDLED for all cases.

This is the Axi DMA Tx done Isr. It invokes "axienet_start_xmit_done"
to complete the BD processing.

.. _`axienet_rx_irq`:

axienet_rx_irq
==============

.. c:function:: irqreturn_t axienet_rx_irq(int irq, void *_ndev)

    Rx Isr.

    :param int irq:
        irq number

    :param void \*_ndev:
        net_device pointer

.. _`axienet_rx_irq.return`:

Return
------

IRQ_HANDLED for all cases.

This is the Axi DMA Rx Isr. It invokes "axienet_recv" to complete the BD
processing.

.. _`axienet_open`:

axienet_open
============

.. c:function:: int axienet_open(struct net_device *ndev)

    Driver open routine.

    :param struct net_device \*ndev:
        Pointer to net_device structure

.. _`axienet_open.return`:

Return
------

0, on success.
-ENODEV, if PHY cannot be connected to
non-zero error value on failure

This is the driver open routine. It calls phy_start to start the PHY device.
It also allocates interrupt service routines, enables the interrupt lines
and ISR handling. Axi Ethernet core is reset through Axi DMA core. Buffer
descriptors are initialized.

.. _`axienet_stop`:

axienet_stop
============

.. c:function:: int axienet_stop(struct net_device *ndev)

    Driver stop routine.

    :param struct net_device \*ndev:
        Pointer to net_device structure

.. _`axienet_stop.return`:

Return
------

0, on success.

This is the driver stop routine. It calls phy_disconnect to stop the PHY
device. It also removes the interrupt handlers and disables the interrupts.
The Axi DMA Tx/Rx BDs are released.

.. _`axienet_change_mtu`:

axienet_change_mtu
==================

.. c:function:: int axienet_change_mtu(struct net_device *ndev, int new_mtu)

    Driver change mtu routine.

    :param struct net_device \*ndev:
        Pointer to net_device structure

    :param int new_mtu:
        New mtu value to be applied

.. _`axienet_change_mtu.return`:

Return
------

Always returns 0 (success).

This is the change mtu driver routine. It checks if the Axi Ethernet
hardware supports jumbo frames before changing the mtu. This can be
called only when the device is not up.

.. _`axienet_poll_controller`:

axienet_poll_controller
=======================

.. c:function:: void axienet_poll_controller(struct net_device *ndev)

    Axi Ethernet poll mechanism.

    :param struct net_device \*ndev:
        Pointer to net_device structure

.. _`axienet_poll_controller.description`:

Description
-----------

This implements Rx/Tx ISR poll mechanisms. The interrupts are disabled prior
to polling the ISRs and are enabled back after the polling is done.

.. _`axienet_ethtools_get_settings`:

axienet_ethtools_get_settings
=============================

.. c:function:: int axienet_ethtools_get_settings(struct net_device *ndev, struct ethtool_cmd *ecmd)

    Get Axi Ethernet settings related to PHY.

    :param struct net_device \*ndev:
        Pointer to net_device structure

    :param struct ethtool_cmd \*ecmd:
        Pointer to ethtool_cmd structure

.. _`axienet_ethtools_get_settings.description`:

Description
-----------

This implements ethtool command for getting PHY settings. If PHY could
not be found, the function returns -ENODEV. This function calls the
relevant PHY ethtool API to get the PHY settings.
Issue "ethtool ethX" under linux prompt to execute this function.

.. _`axienet_ethtools_get_settings.return`:

Return
------

0 on success, -ENODEV if PHY doesn't exist

.. _`axienet_ethtools_set_settings`:

axienet_ethtools_set_settings
=============================

.. c:function:: int axienet_ethtools_set_settings(struct net_device *ndev, struct ethtool_cmd *ecmd)

    Set PHY settings as passed in the argument.

    :param struct net_device \*ndev:
        Pointer to net_device structure

    :param struct ethtool_cmd \*ecmd:
        Pointer to ethtool_cmd structure

.. _`axienet_ethtools_set_settings.description`:

Description
-----------

This implements ethtool command for setting various PHY settings. If PHY
could not be found, the function returns -ENODEV. This function calls the
relevant PHY ethtool API to set the PHY.
Issue e.g. "ethtool -s ethX speed 1000" under linux prompt to execute this
function.

.. _`axienet_ethtools_set_settings.return`:

Return
------

0 on success, -ENODEV if PHY doesn't exist

.. _`axienet_ethtools_get_drvinfo`:

axienet_ethtools_get_drvinfo
============================

.. c:function:: void axienet_ethtools_get_drvinfo(struct net_device *ndev, struct ethtool_drvinfo *ed)

    Get various Axi Ethernet driver information.

    :param struct net_device \*ndev:
        Pointer to net_device structure

    :param struct ethtool_drvinfo \*ed:
        Pointer to ethtool_drvinfo structure

.. _`axienet_ethtools_get_drvinfo.description`:

Description
-----------

This implements ethtool command for getting the driver information.
Issue "ethtool -i ethX" under linux prompt to execute this function.

.. _`axienet_ethtools_get_regs_len`:

axienet_ethtools_get_regs_len
=============================

.. c:function:: int axienet_ethtools_get_regs_len(struct net_device *ndev)

    Get the total regs length present in the AxiEthernet core.

    :param struct net_device \*ndev:
        Pointer to net_device structure

.. _`axienet_ethtools_get_regs_len.description`:

Description
-----------

This implements ethtool command for getting the total register length
information.

.. _`axienet_ethtools_get_regs_len.return`:

Return
------

the total regs length

.. _`axienet_ethtools_get_regs`:

axienet_ethtools_get_regs
=========================

.. c:function:: void axienet_ethtools_get_regs(struct net_device *ndev, struct ethtool_regs *regs, void *ret)

    Dump the contents of all registers present in AxiEthernet core.

    :param struct net_device \*ndev:
        Pointer to net_device structure

    :param struct ethtool_regs \*regs:
        Pointer to ethtool_regs structure

    :param void \*ret:
        Void pointer used to return the contents of the registers.

.. _`axienet_ethtools_get_regs.description`:

Description
-----------

This implements ethtool command for getting the Axi Ethernet register dump.
Issue "ethtool -d ethX" to execute this function.

.. _`axienet_ethtools_get_pauseparam`:

axienet_ethtools_get_pauseparam
===============================

.. c:function:: void axienet_ethtools_get_pauseparam(struct net_device *ndev, struct ethtool_pauseparam *epauseparm)

    Get the pause parameter setting for Tx and Rx paths.

    :param struct net_device \*ndev:
        Pointer to net_device structure

    :param struct ethtool_pauseparam \*epauseparm:
        Pointer to ethtool_pauseparam structure.

.. _`axienet_ethtools_get_pauseparam.description`:

Description
-----------

This implements ethtool command for getting axi ethernet pause frame
setting. Issue "ethtool -a ethX" to execute this function.

.. _`axienet_ethtools_set_pauseparam`:

axienet_ethtools_set_pauseparam
===============================

.. c:function:: int axienet_ethtools_set_pauseparam(struct net_device *ndev, struct ethtool_pauseparam *epauseparm)

    Set device pause parameter(flow control) settings.

    :param struct net_device \*ndev:
        Pointer to net_device structure

    :param struct ethtool_pauseparam \*epauseparm:
        Pointer to ethtool_pauseparam structure

.. _`axienet_ethtools_set_pauseparam.description`:

Description
-----------

This implements ethtool command for enabling flow control on Rx and Tx
paths. Issue "ethtool -A ethX tx on\|off" under linux prompt to execute this
function.

.. _`axienet_ethtools_set_pauseparam.return`:

Return
------

0 on success, -EFAULT if device is running

.. _`axienet_ethtools_get_coalesce`:

axienet_ethtools_get_coalesce
=============================

.. c:function:: int axienet_ethtools_get_coalesce(struct net_device *ndev, struct ethtool_coalesce *ecoalesce)

    Get DMA interrupt coalescing count.

    :param struct net_device \*ndev:
        Pointer to net_device structure

    :param struct ethtool_coalesce \*ecoalesce:
        Pointer to ethtool_coalesce structure

.. _`axienet_ethtools_get_coalesce.description`:

Description
-----------

This implements ethtool command for getting the DMA interrupt coalescing
count on Tx and Rx paths. Issue "ethtool -c ethX" under linux prompt to
execute this function.

.. _`axienet_ethtools_get_coalesce.return`:

Return
------

0 always

.. _`axienet_ethtools_set_coalesce`:

axienet_ethtools_set_coalesce
=============================

.. c:function:: int axienet_ethtools_set_coalesce(struct net_device *ndev, struct ethtool_coalesce *ecoalesce)

    Set DMA interrupt coalescing count.

    :param struct net_device \*ndev:
        Pointer to net_device structure

    :param struct ethtool_coalesce \*ecoalesce:
        Pointer to ethtool_coalesce structure

.. _`axienet_ethtools_set_coalesce.description`:

Description
-----------

This implements ethtool command for setting the DMA interrupt coalescing
count on Tx and Rx paths. Issue "ethtool -C ethX rx-frames 5" under linux
prompt to execute this function.

.. _`axienet_ethtools_set_coalesce.return`:

Return
------

0, on success, Non-zero error value on failure.

.. _`axienet_dma_err_handler`:

axienet_dma_err_handler
=======================

.. c:function:: void axienet_dma_err_handler(unsigned long data)

    Tasklet handler for Axi DMA Error

    :param unsigned long data:
        Data passed

.. _`axienet_dma_err_handler.description`:

Description
-----------

Resets the Axi DMA and Axi Ethernet devices, and reconfigures the
Tx/Rx BDs.

.. _`axienet_probe`:

axienet_probe
=============

.. c:function:: int axienet_probe(struct platform_device *pdev)

    Axi Ethernet probe function.

    :param struct platform_device \*pdev:
        Pointer to platform device structure.

.. _`axienet_probe.return`:

Return
------

0, on success
Non-zero error value on failure.

This is the probe routine for Axi Ethernet driver. This is called before
any other driver routines are invoked. It allocates and sets up the Ethernet
device. Parses through device tree and populates fields of
axienet_local. It registers the Ethernet device.

.. This file was automatic generated / don't edit.

