.. -*- coding: utf-8; mode: rst -*-

=============
stmmac_main.c
=============


.. _`stmmac_verify_args`:

stmmac_verify_args
==================

.. c:function:: void stmmac_verify_args ( void)

    verify the driver parameters.

    :param void:
        no arguments



.. _`stmmac_verify_args.description`:

Description
-----------

it checks the driver parameters and set a default in case of
errors.



.. _`stmmac_clk_csr_set`:

stmmac_clk_csr_set
==================

.. c:function:: void stmmac_clk_csr_set (struct stmmac_priv *priv)

    dynamically set the MDC clock

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_clk_csr_set.description`:

Description
-----------

this is to dynamically set the MDC clock according to the csr
clock input.



.. _`stmmac_clk_csr_set.note`:

Note
----

If a specific clk_csr value is passed from the platform
this means that the CSR Clock Range selection cannot be
changed at run-time and it is fixed (as reported in the driver
documentation). Viceversa the driver will try to set the MDC
clock dynamically according to the actual clock input.



.. _`stmmac_hw_fix_mac_speed`:

stmmac_hw_fix_mac_speed
=======================

.. c:function:: void stmmac_hw_fix_mac_speed (struct stmmac_priv *priv)

    callback for speed selection

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_hw_fix_mac_speed.description`:

Description
-----------

on some platforms (e.g. ST), some HW system configuraton
registers have to be set according to the link speed negotiated.



.. _`stmmac_enable_eee_mode`:

stmmac_enable_eee_mode
======================

.. c:function:: void stmmac_enable_eee_mode (struct stmmac_priv *priv)

    check and enter in LPI mode

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_enable_eee_mode.description`:

Description
-----------

this function is to verify and enter in LPI mode in case of
EEE.



.. _`stmmac_disable_eee_mode`:

stmmac_disable_eee_mode
=======================

.. c:function:: void stmmac_disable_eee_mode (struct stmmac_priv *priv)

    disable and exit from LPI mode

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_disable_eee_mode.description`:

Description
-----------

this function is to exit and disable EEE in case of
LPI state is true. This is called by the xmit.



.. _`stmmac_eee_ctrl_timer`:

stmmac_eee_ctrl_timer
=====================

.. c:function:: void stmmac_eee_ctrl_timer (unsigned long arg)

    EEE TX SW timer.

    :param unsigned long arg:
        data hook



.. _`stmmac_eee_ctrl_timer.description`:

Description
-----------

if there is no data transfer and if we are not in LPI state,
then MAC Transmitter can be moved to LPI state.



.. _`stmmac_eee_init`:

stmmac_eee_init
===============

.. c:function:: bool stmmac_eee_init (struct stmmac_priv *priv)

    init EEE

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_eee_init.description`:

Description
-----------

if the GMAC supports the EEE (from the HW cap reg) and the phy device
can also manage EEE, this function enable the LPI state and start related
timer.



.. _`stmmac_hwtstamp_ioctl`:

stmmac_hwtstamp_ioctl
=====================

.. c:function:: int stmmac_hwtstamp_ioctl (struct net_device *dev, struct ifreq *ifr)

    control hardware timestamping.

    :param struct net_device \*dev:
        device pointer.

    :param struct ifreq \*ifr:
        An IOCTL specefic structure, that can contain a pointer to
        a proprietary structure used to pass information to the driver.



.. _`stmmac_hwtstamp_ioctl.description`:

Description
-----------

This function configures the MAC to enable/disable both outgoing(TX)
and incoming(RX) packets time stamping based on user input.



.. _`stmmac_hwtstamp_ioctl.return-value`:

Return Value
------------

0 on success and an appropriate -ve integer on failure.



.. _`stmmac_init_ptp`:

stmmac_init_ptp
===============

.. c:function:: int stmmac_init_ptp (struct stmmac_priv *priv)

    init PTP

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_init_ptp.description`:

Description
-----------

this is to verify if the HW supports the PTPv1 or PTPv2.
This is done by looking at the HW cap. register.
This function also registers the ptp driver.



.. _`stmmac_adjust_link`:

stmmac_adjust_link
==================

.. c:function:: void stmmac_adjust_link (struct net_device *dev)

    adjusts the link parameters

    :param struct net_device \*dev:
        net device structure



.. _`stmmac_adjust_link.description`:

Description
-----------

this is the helper called by the physical abstraction layer
drivers to communicate the phy link status. According the speed and duplex
this driver can invoke registered glue-logic as well.
It also invoke the eee initialization because it could happen when switch
on different networks (that are eee capable).



.. _`stmmac_check_pcs_mode`:

stmmac_check_pcs_mode
=====================

.. c:function:: void stmmac_check_pcs_mode (struct stmmac_priv *priv)

    verify if RGMII/SGMII is supported

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_check_pcs_mode.description`:

Description
-----------

this is to verify if the HW supports the PCS.
Physical Coding Sublayer (PCS) interface that can be used when the MAC is
configured for the TBI, RTBI, or SGMII PHY interface.



.. _`stmmac_init_phy`:

stmmac_init_phy
===============

.. c:function:: int stmmac_init_phy (struct net_device *dev)

    PHY initialization

    :param struct net_device \*dev:
        net device structure



.. _`stmmac_init_phy.description`:

Description
-----------

it initializes the driver's PHY state, and attaches the PHY
to the mac driver.



.. _`stmmac_init_phy.return-value`:

Return value
------------

0 on success



.. _`stmmac_display_ring`:

stmmac_display_ring
===================

.. c:function:: void stmmac_display_ring (void *head, int size, int extend_desc)

    display ring

    :param void \*head:
        pointer to the head of the ring passed.

    :param int size:
        size of the ring.

    :param int extend_desc:
        to verify if extended descriptors are used.



.. _`stmmac_display_ring.description`:

Description
-----------

display the control/status and buffer descriptors.



.. _`stmmac_clear_descriptors`:

stmmac_clear_descriptors
========================

.. c:function:: void stmmac_clear_descriptors (struct stmmac_priv *priv)

    clear descriptors

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_clear_descriptors.description`:

Description
-----------

this function is called to clear the tx and rx descriptors
in case of both basic and extended descriptors are used.



.. _`stmmac_init_rx_buffers`:

stmmac_init_rx_buffers
======================

.. c:function:: int stmmac_init_rx_buffers (struct stmmac_priv *priv, struct dma_desc *p, int i, gfp_t flags)

    init the RX descriptor buffer.

    :param struct stmmac_priv \*priv:
        driver private structure

    :param struct dma_desc \*p:
        descriptor pointer

    :param int i:
        descriptor index

    :param gfp_t flags:
        gfp flag.



.. _`stmmac_init_rx_buffers.description`:

Description
-----------

this function is called to allocate a receive buffer, perform
the DMA mapping and init the descriptor.



.. _`init_dma_desc_rings`:

init_dma_desc_rings
===================

.. c:function:: int init_dma_desc_rings (struct net_device *dev, gfp_t flags)

    init the RX/TX descriptor rings

    :param struct net_device \*dev:
        net device structure

    :param gfp_t flags:
        gfp flag.



.. _`init_dma_desc_rings.description`:

Description
-----------

this function initializes the DMA RX/TX descriptors
and allocates the socket buffers. It suppors the chained and ring
modes.



.. _`alloc_dma_desc_resources`:

alloc_dma_desc_resources
========================

.. c:function:: int alloc_dma_desc_resources (struct stmmac_priv *priv)

    alloc TX/RX resources.

    :param struct stmmac_priv \*priv:
        private structure



.. _`alloc_dma_desc_resources.description`:

Description
-----------

according to which descriptor can be used (extend or basic)
this function allocates the resources for TX and RX paths. In case of
reception, for example, it pre-allocated the RX socket buffer in order to
allow zero-copy mechanism.



.. _`stmmac_dma_operation_mode`:

stmmac_dma_operation_mode
=========================

.. c:function:: void stmmac_dma_operation_mode (struct stmmac_priv *priv)

    HW DMA operation mode

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_dma_operation_mode.description`:

Description
-----------

it is used for configuring the DMA operation mode register in
order to program the tx/rx DMA thresholds or Store-And-Forward mode.



.. _`stmmac_tx_clean`:

stmmac_tx_clean
===============

.. c:function:: void stmmac_tx_clean (struct stmmac_priv *priv)

    to manage the transmission completion

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_tx_clean.description`:

Description
-----------

it reclaims the transmit resources after transmission completes.



.. _`stmmac_tx_err`:

stmmac_tx_err
=============

.. c:function:: void stmmac_tx_err (struct stmmac_priv *priv)

    to manage the tx error

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_tx_err.description`:

Description
-----------

it cleans the descriptors and restarts the transmission
in case of transmission errors.



.. _`stmmac_dma_interrupt`:

stmmac_dma_interrupt
====================

.. c:function:: void stmmac_dma_interrupt (struct stmmac_priv *priv)

    DMA ISR

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_dma_interrupt.description`:

Description
-----------

this is the DMA ISR. It is called by the main ISR.
It calls the dwmac dma routine and schedule poll method in case of some
work can be done.



.. _`stmmac_mmc_setup`:

stmmac_mmc_setup
================

.. c:function:: void stmmac_mmc_setup (struct stmmac_priv *priv)

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_mmc_setup.description`:

Description
-----------

this masks the MMC irq, in fact, the counters are managed in SW.



.. _`stmmac_get_synopsys_id`:

stmmac_get_synopsys_id
======================

.. c:function:: u32 stmmac_get_synopsys_id (struct stmmac_priv *priv)

    return the SYINID.

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_get_synopsys_id.description`:

Description
-----------

this simple function is to decode and return the SYINID
starting from the HW core register.



.. _`stmmac_selec_desc_mode`:

stmmac_selec_desc_mode
======================

.. c:function:: void stmmac_selec_desc_mode (struct stmmac_priv *priv)

    to select among: normal/alternate/extend descriptors

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_selec_desc_mode.description`:

Description
-----------

select the Enhanced/Alternate or Normal descriptors.
In case of Enhanced/Alternate, it checks if the extended descriptors are
supported by the HW capability register.



.. _`stmmac_get_hw_features`:

stmmac_get_hw_features
======================

.. c:function:: int stmmac_get_hw_features (struct stmmac_priv *priv)

    get MAC capabilities from the HW cap. register.

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_get_hw_features.description`:

Description
-----------

new GMAC chip generations have a new register to indicate the
presence of the optional feature/functions.
This can be also used to override the value passed through the
platform and necessary for old MAC10/100 and GMAC chips.



.. _`stmmac_check_ether_addr`:

stmmac_check_ether_addr
=======================

.. c:function:: void stmmac_check_ether_addr (struct stmmac_priv *priv)

    check if the MAC addr is valid

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_check_ether_addr.description`:

Description
-----------

it is to verify if the MAC address is valid, in case of failures it
generates a random MAC address



.. _`stmmac_init_dma_engine`:

stmmac_init_dma_engine
======================

.. c:function:: int stmmac_init_dma_engine (struct stmmac_priv *priv)

    DMA init.

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_init_dma_engine.description`:

Description
-----------

It inits the DMA invoking the specific MAC/GMAC callback.
Some DMA parameters can be passed from the platform;
in case of these are not passed a default is kept for the MAC or GMAC.



.. _`stmmac_tx_timer`:

stmmac_tx_timer
===============

.. c:function:: void stmmac_tx_timer (unsigned long data)

    mitigation sw timer for tx.

    :param unsigned long data:
        data pointer



.. _`stmmac_tx_timer.description`:

Description
-----------

This is the timer handler to directly invoke the stmmac_tx_clean.



.. _`stmmac_init_tx_coalesce`:

stmmac_init_tx_coalesce
=======================

.. c:function:: void stmmac_init_tx_coalesce (struct stmmac_priv *priv)

    init tx mitigation options.

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_init_tx_coalesce.this-inits-the-transmit-coalesce-parameters`:

This inits the transmit coalesce parameters
-------------------------------------------

i.e. timer rate,
timer handler and default threshold used for enabling the
interrupt on completion bit.



.. _`stmmac_hw_setup`:

stmmac_hw_setup
===============

.. c:function:: int stmmac_hw_setup (struct net_device *dev, bool init_ptp)

    setup mac in a usable state.

    :param struct net_device \*dev:
        pointer to the device structure.

    :param bool init_ptp:

        *undescribed*



.. _`stmmac_hw_setup.description`:

Description
-----------

this is the main function to setup the HW in a usable state because the
dma engine is reset, the core registers are configured (e.g. AXI,
Checksum features, timers). The DMA is ready to start receiving and
transmitting.



.. _`stmmac_hw_setup.return-value`:

Return value
------------

0 on success and an appropriate (-)ve integer as defined in errno.h
file on failure.



.. _`stmmac_open`:

stmmac_open
===========

.. c:function:: int stmmac_open (struct net_device *dev)

    open entry point of the driver

    :param struct net_device \*dev:
        pointer to the device structure.



.. _`stmmac_open.description`:

Description
-----------

This function is the open entry point of the driver.



.. _`stmmac_open.return-value`:

Return value
------------

0 on success and an appropriate (-)ve integer as defined in errno.h
file on failure.



.. _`stmmac_release`:

stmmac_release
==============

.. c:function:: int stmmac_release (struct net_device *dev)

    close entry point of the driver

    :param struct net_device \*dev:
        device pointer.



.. _`stmmac_release.description`:

Description
-----------

This is the stop entry point of the driver.



.. _`stmmac_xmit`:

stmmac_xmit
===========

.. c:function:: netdev_tx_t stmmac_xmit (struct sk_buff *skb, struct net_device *dev)

    Tx entry point of the driver

    :param struct sk_buff \*skb:
        the socket buffer

    :param struct net_device \*dev:
        device pointer



.. _`stmmac_xmit.description`:

Description 
------------

this is the tx entry point of the driver.
It programs the chain or the ring and supports oversized frames
and SG feature.



.. _`stmmac_rx_refill`:

stmmac_rx_refill
================

.. c:function:: void stmmac_rx_refill (struct stmmac_priv *priv)

    refill used skb preallocated buffers

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_rx_refill.description`:

Description 
------------

this is to reallocate the skb for the reception process
that is based on zero-copy.



.. _`stmmac_rx`:

stmmac_rx
=========

.. c:function:: int stmmac_rx (struct stmmac_priv *priv, int limit)

    manage the receive process

    :param struct stmmac_priv \*priv:
        driver private structure

    :param int limit:
        napi bugget.



.. _`stmmac_rx.description`:

Description 
------------

this the function called by the napi poll method.
It gets all the frames inside the ring.



.. _`stmmac_poll`:

stmmac_poll
===========

.. c:function:: int stmmac_poll (struct napi_struct *napi, int budget)

    stmmac poll method (NAPI)

    :param struct napi_struct \*napi:
        pointer to the napi structure.

    :param int budget:
        maximum number of packets that the current CPU can receive from
        all interfaces.



.. _`stmmac_poll.description`:

Description 
------------

To look at the incoming frames and clear the tx resources.



.. _`stmmac_tx_timeout`:

stmmac_tx_timeout
=================

.. c:function:: void stmmac_tx_timeout (struct net_device *dev)

    :param struct net_device \*dev:
        Pointer to net device structure



.. _`stmmac_tx_timeout.description`:

Description
-----------

this function is called when a packet transmission fails to
complete within a reasonable time. The driver will mark the error in the
netdev structure and arrange for the device to be reset to a sane state
in order to transmit a new packet.



.. _`stmmac_set_rx_mode`:

stmmac_set_rx_mode
==================

.. c:function:: void stmmac_set_rx_mode (struct net_device *dev)

    entry point for multicast addressing

    :param struct net_device \*dev:
        pointer to the device structure



.. _`stmmac_set_rx_mode.description`:

Description
-----------

This function is a driver entry point which gets called by the kernel
whenever multicast addresses must be enabled/disabled.



.. _`stmmac_set_rx_mode.return-value`:

Return value
------------

void.



.. _`stmmac_change_mtu`:

stmmac_change_mtu
=================

.. c:function:: int stmmac_change_mtu (struct net_device *dev, int new_mtu)

    entry point to change MTU size for the device.

    :param struct net_device \*dev:
        device pointer.

    :param int new_mtu:
        the new MTU size for the device.



.. _`stmmac_change_mtu.description`:

Description
-----------

the Maximum Transfer Unit (MTU) is used by the network layer
to drive packet transmission. Ethernet has an MTU of 1500 octets
(ETH_DATA_LEN). This value can be changed with ifconfig.



.. _`stmmac_change_mtu.return-value`:

Return value
------------

0 on success and an appropriate (-)ve integer as defined in errno.h
file on failure.



.. _`stmmac_interrupt`:

stmmac_interrupt
================

.. c:function:: irqreturn_t stmmac_interrupt (int irq, void *dev_id)

    main ISR

    :param int irq:
        interrupt number.

    :param void \*dev_id:
        to pass the net device pointer.



.. _`stmmac_interrupt.description`:

Description
-----------

this is the main driver interrupt service routine.



.. _`stmmac_interrupt.it-can-call`:

It can call
-----------

o DMA service routine (to manage incoming frame reception and transmission
status)



.. _`stmmac_interrupt.o-core-interrupts-to-manage`:

o Core interrupts to manage
---------------------------

remote wake-up, management counter, LPI
interrupts.



.. _`stmmac_ioctl`:

stmmac_ioctl
============

.. c:function:: int stmmac_ioctl (struct net_device *dev, struct ifreq *rq, int cmd)

    Entry point for the Ioctl

    :param struct net_device \*dev:
        Device pointer.

    :param struct ifreq \*rq:
        An IOCTL specefic structure, that can contain a pointer to
        a proprietary structure used to pass information to the driver.

    :param int cmd:
        IOCTL command



.. _`stmmac_ioctl.description`:

Description
-----------

Currently it supports the phy_mii_ioctl(...) and HW time stamping.



.. _`stmmac_hw_init`:

stmmac_hw_init
==============

.. c:function:: int stmmac_hw_init (struct stmmac_priv *priv)

    Init the MAC device

    :param struct stmmac_priv \*priv:
        driver private structure



.. _`stmmac_hw_init.description`:

Description
-----------

this function is to configure the MAC device according to
some platform parameters or the HW capability register. It prepares the
driver to use either ring or chain modes and to setup either enhanced or
normal descriptors.



.. _`stmmac_dvr_probe`:

stmmac_dvr_probe
================

.. c:function:: int stmmac_dvr_probe (struct device *device, struct plat_stmmacenet_data *plat_dat, struct stmmac_resources *res)

    :param struct device \*device:
        device pointer

    :param struct plat_stmmacenet_data \*plat_dat:
        platform data pointer

    :param struct stmmac_resources \*res:
        stmmac resource pointer



.. _`stmmac_dvr_probe.description`:

Description
-----------

this is the main probe function used to
call the alloc_etherdev, allocate the priv structure.



.. _`stmmac_dvr_probe.return`:

Return
------

returns 0 on success, otherwise errno.



.. _`stmmac_dvr_remove`:

stmmac_dvr_remove
=================

.. c:function:: int stmmac_dvr_remove (struct net_device *ndev)

    :param struct net_device \*ndev:
        net device pointer



.. _`stmmac_dvr_remove.description`:

Description
-----------

this function resets the TX/RX processes, disables the MAC RX/TX
changes the link status, releases the DMA descriptor rings.



.. _`stmmac_suspend`:

stmmac_suspend
==============

.. c:function:: int stmmac_suspend (struct net_device *ndev)

    suspend callback

    :param struct net_device \*ndev:
        net device pointer



.. _`stmmac_suspend.description`:

Description
-----------

this is the function to suspend the device and it is called
by the platform driver to stop the network queue, release the resources,
program the PMT register (for WoL), clean and release driver resources.



.. _`stmmac_resume`:

stmmac_resume
=============

.. c:function:: int stmmac_resume (struct net_device *ndev)

    resume callback

    :param struct net_device \*ndev:
        net device pointer



.. _`stmmac_resume.description`:

Description
-----------

when resume this function is invoked to setup the DMA and CORE
in a usable state.

