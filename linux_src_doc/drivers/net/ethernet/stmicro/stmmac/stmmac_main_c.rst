.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/stmicro/stmmac/stmmac_main.c

.. _`stmmac_verify_args`:

stmmac_verify_args
==================

.. c:function:: void stmmac_verify_args( void)

    verify the driver parameters.

    :param void:
        no arguments
    :type void: 

.. _`stmmac_verify_args.description`:

Description
-----------

it checks the driver parameters and set a default in case of
errors.

.. _`stmmac_disable_all_queues`:

stmmac_disable_all_queues
=========================

.. c:function:: void stmmac_disable_all_queues(struct stmmac_priv *priv)

    Disable all queues

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_enable_all_queues`:

stmmac_enable_all_queues
========================

.. c:function:: void stmmac_enable_all_queues(struct stmmac_priv *priv)

    Enable all queues

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_stop_all_queues`:

stmmac_stop_all_queues
======================

.. c:function:: void stmmac_stop_all_queues(struct stmmac_priv *priv)

    Stop all queues

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_start_all_queues`:

stmmac_start_all_queues
=======================

.. c:function:: void stmmac_start_all_queues(struct stmmac_priv *priv)

    Start all queues

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_clk_csr_set`:

stmmac_clk_csr_set
==================

.. c:function:: void stmmac_clk_csr_set(struct stmmac_priv *priv)

    dynamically set the MDC clock

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

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

.. _`stmmac_rx_dirty`:

stmmac_rx_dirty
===============

.. c:function:: u32 stmmac_rx_dirty(struct stmmac_priv *priv, u32 queue)

    Get RX queue dirty

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param queue:
        RX queue index
    :type queue: u32

.. _`stmmac_hw_fix_mac_speed`:

stmmac_hw_fix_mac_speed
=======================

.. c:function:: void stmmac_hw_fix_mac_speed(struct stmmac_priv *priv)

    callback for speed selection

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_hw_fix_mac_speed.description`:

Description
-----------

on some platforms (e.g. ST), some HW system configuration
registers have to be set according to the link speed negotiated.

.. _`stmmac_enable_eee_mode`:

stmmac_enable_eee_mode
======================

.. c:function:: void stmmac_enable_eee_mode(struct stmmac_priv *priv)

    check and enter in LPI mode

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_enable_eee_mode.description`:

Description
-----------

this function is to verify and enter in LPI mode in case of
EEE.

.. _`stmmac_disable_eee_mode`:

stmmac_disable_eee_mode
=======================

.. c:function:: void stmmac_disable_eee_mode(struct stmmac_priv *priv)

    disable and exit from LPI mode

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_disable_eee_mode.description`:

Description
-----------

this function is to exit and disable EEE in case of
LPI state is true. This is called by the xmit.

.. _`stmmac_eee_ctrl_timer`:

stmmac_eee_ctrl_timer
=====================

.. c:function:: void stmmac_eee_ctrl_timer(struct timer_list *t)

    EEE TX SW timer.

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`stmmac_eee_ctrl_timer.description`:

Description
-----------

if there is no data transfer and if we are not in LPI state,
then MAC Transmitter can be moved to LPI state.

.. _`stmmac_eee_init`:

stmmac_eee_init
===============

.. c:function:: bool stmmac_eee_init(struct stmmac_priv *priv)

    init EEE

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_eee_init.description`:

Description
-----------

if the GMAC supports the EEE (from the HW cap reg) and the phy device
can also manage EEE, this function enable the LPI state and start related
timer.

.. _`stmmac_hwtstamp_ioctl`:

stmmac_hwtstamp_ioctl
=====================

.. c:function:: int stmmac_hwtstamp_ioctl(struct net_device *dev, struct ifreq *ifr)

    control hardware timestamping.

    :param dev:
        device pointer.
    :type dev: struct net_device \*

    :param ifr:
        An IOCTL specific structure, that can contain a pointer to
        a proprietary structure used to pass information to the driver.
    :type ifr: struct ifreq \*

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

.. c:function:: int stmmac_init_ptp(struct stmmac_priv *priv)

    init PTP

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_init_ptp.description`:

Description
-----------

this is to verify if the HW supports the PTPv1 or PTPv2.
This is done by looking at the HW cap. register.
This function also registers the ptp driver.

.. _`stmmac_mac_flow_ctrl`:

stmmac_mac_flow_ctrl
====================

.. c:function:: void stmmac_mac_flow_ctrl(struct stmmac_priv *priv, u32 duplex)

    Configure flow control in all queues

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param duplex:
        *undescribed*
    :type duplex: u32

.. _`stmmac_mac_flow_ctrl.description`:

Description
-----------

It is used for configuring the flow control in all queues

.. _`stmmac_adjust_link`:

stmmac_adjust_link
==================

.. c:function:: void stmmac_adjust_link(struct net_device *dev)

    adjusts the link parameters

    :param dev:
        net device structure
    :type dev: struct net_device \*

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

.. c:function:: void stmmac_check_pcs_mode(struct stmmac_priv *priv)

    verify if RGMII/SGMII is supported

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_check_pcs_mode.description`:

Description
-----------

this is to verify if the HW supports the PCS.
Physical Coding Sublayer (PCS) interface that can be used when the MAC is
configured for the TBI, RTBI, or SGMII PHY interface.

.. _`stmmac_init_phy`:

stmmac_init_phy
===============

.. c:function:: int stmmac_init_phy(struct net_device *dev)

    PHY initialization

    :param dev:
        net device structure
    :type dev: struct net_device \*

.. _`stmmac_init_phy.description`:

Description
-----------

it initializes the driver's PHY state, and attaches the PHY
to the mac driver.

.. _`stmmac_init_phy.return-value`:

Return value
------------

0 on success

.. _`stmmac_clear_rx_descriptors`:

stmmac_clear_rx_descriptors
===========================

.. c:function:: void stmmac_clear_rx_descriptors(struct stmmac_priv *priv, u32 queue)

    clear RX descriptors

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param queue:
        RX queue index
    :type queue: u32

.. _`stmmac_clear_rx_descriptors.description`:

Description
-----------

this function is called to clear the RX descriptors
in case of both basic and extended descriptors are used.

.. _`stmmac_clear_tx_descriptors`:

stmmac_clear_tx_descriptors
===========================

.. c:function:: void stmmac_clear_tx_descriptors(struct stmmac_priv *priv, u32 queue)

    clear tx descriptors

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param queue:
        TX queue index.
    :type queue: u32

.. _`stmmac_clear_tx_descriptors.description`:

Description
-----------

this function is called to clear the TX descriptors
in case of both basic and extended descriptors are used.

.. _`stmmac_clear_descriptors`:

stmmac_clear_descriptors
========================

.. c:function:: void stmmac_clear_descriptors(struct stmmac_priv *priv)

    clear descriptors

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_clear_descriptors.description`:

Description
-----------

this function is called to clear the TX and RX descriptors
in case of both basic and extended descriptors are used.

.. _`stmmac_init_rx_buffers`:

stmmac_init_rx_buffers
======================

.. c:function:: int stmmac_init_rx_buffers(struct stmmac_priv *priv, struct dma_desc *p, int i, gfp_t flags, u32 queue)

    init the RX descriptor buffer.

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param p:
        descriptor pointer
    :type p: struct dma_desc \*

    :param i:
        descriptor index
    :type i: int

    :param flags:
        gfp flag
    :type flags: gfp_t

    :param queue:
        RX queue index
    :type queue: u32

.. _`stmmac_init_rx_buffers.description`:

Description
-----------

this function is called to allocate a receive buffer, perform
the DMA mapping and init the descriptor.

.. _`stmmac_free_rx_buffer`:

stmmac_free_rx_buffer
=====================

.. c:function:: void stmmac_free_rx_buffer(struct stmmac_priv *priv, u32 queue, int i)

    free RX dma buffers

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

    :param queue:
        RX queue index
    :type queue: u32

    :param i:
        buffer index.
    :type i: int

.. _`stmmac_free_tx_buffer`:

stmmac_free_tx_buffer
=====================

.. c:function:: void stmmac_free_tx_buffer(struct stmmac_priv *priv, u32 queue, int i)

    free RX dma buffers

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

    :param queue:
        RX queue index
    :type queue: u32

    :param i:
        buffer index.
    :type i: int

.. _`init_dma_rx_desc_rings`:

init_dma_rx_desc_rings
======================

.. c:function:: int init_dma_rx_desc_rings(struct net_device *dev, gfp_t flags)

    init the RX descriptor rings

    :param dev:
        net device structure
    :type dev: struct net_device \*

    :param flags:
        gfp flag.
    :type flags: gfp_t

.. _`init_dma_rx_desc_rings.description`:

Description
-----------

this function initializes the DMA RX descriptors
and allocates the socket buffers. It supports the chained and ring
modes.

.. _`init_dma_tx_desc_rings`:

init_dma_tx_desc_rings
======================

.. c:function:: int init_dma_tx_desc_rings(struct net_device *dev)

    init the TX descriptor rings

    :param dev:
        net device structure.
    :type dev: struct net_device \*

.. _`init_dma_tx_desc_rings.description`:

Description
-----------

this function initializes the DMA TX descriptors
and allocates the socket buffers. It supports the chained and ring
modes.

.. _`init_dma_desc_rings`:

init_dma_desc_rings
===================

.. c:function:: int init_dma_desc_rings(struct net_device *dev, gfp_t flags)

    init the RX/TX descriptor rings

    :param dev:
        net device structure
    :type dev: struct net_device \*

    :param flags:
        gfp flag.
    :type flags: gfp_t

.. _`init_dma_desc_rings.description`:

Description
-----------

this function initializes the DMA RX/TX descriptors
and allocates the socket buffers. It supports the chained and ring
modes.

.. _`dma_free_rx_skbufs`:

dma_free_rx_skbufs
==================

.. c:function:: void dma_free_rx_skbufs(struct stmmac_priv *priv, u32 queue)

    free RX dma buffers

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

    :param queue:
        RX queue index
    :type queue: u32

.. _`dma_free_tx_skbufs`:

dma_free_tx_skbufs
==================

.. c:function:: void dma_free_tx_skbufs(struct stmmac_priv *priv, u32 queue)

    free TX dma buffers

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

    :param queue:
        TX queue index
    :type queue: u32

.. _`free_dma_rx_desc_resources`:

free_dma_rx_desc_resources
==========================

.. c:function:: void free_dma_rx_desc_resources(struct stmmac_priv *priv)

    free RX dma desc resources

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

.. _`free_dma_tx_desc_resources`:

free_dma_tx_desc_resources
==========================

.. c:function:: void free_dma_tx_desc_resources(struct stmmac_priv *priv)

    free TX dma desc resources

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

.. _`alloc_dma_rx_desc_resources`:

alloc_dma_rx_desc_resources
===========================

.. c:function:: int alloc_dma_rx_desc_resources(struct stmmac_priv *priv)

    alloc RX resources.

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

.. _`alloc_dma_rx_desc_resources.description`:

Description
-----------

according to which descriptor can be used (extend or basic)
this function allocates the resources for TX and RX paths. In case of
reception, for example, it pre-allocated the RX socket buffer in order to
allow zero-copy mechanism.

.. _`alloc_dma_tx_desc_resources`:

alloc_dma_tx_desc_resources
===========================

.. c:function:: int alloc_dma_tx_desc_resources(struct stmmac_priv *priv)

    alloc TX resources.

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

.. _`alloc_dma_tx_desc_resources.description`:

Description
-----------

according to which descriptor can be used (extend or basic)
this function allocates the resources for TX and RX paths. In case of
reception, for example, it pre-allocated the RX socket buffer in order to
allow zero-copy mechanism.

.. _`alloc_dma_desc_resources`:

alloc_dma_desc_resources
========================

.. c:function:: int alloc_dma_desc_resources(struct stmmac_priv *priv)

    alloc TX/RX resources.

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

.. _`alloc_dma_desc_resources.description`:

Description
-----------

according to which descriptor can be used (extend or basic)
this function allocates the resources for TX and RX paths. In case of
reception, for example, it pre-allocated the RX socket buffer in order to
allow zero-copy mechanism.

.. _`free_dma_desc_resources`:

free_dma_desc_resources
=======================

.. c:function:: void free_dma_desc_resources(struct stmmac_priv *priv)

    free dma desc resources

    :param priv:
        private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_mac_enable_rx_queues`:

stmmac_mac_enable_rx_queues
===========================

.. c:function:: void stmmac_mac_enable_rx_queues(struct stmmac_priv *priv)

    Enable MAC rx queues

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_mac_enable_rx_queues.description`:

Description
-----------

It is used for enabling the rx queues in the MAC

.. _`stmmac_start_rx_dma`:

stmmac_start_rx_dma
===================

.. c:function:: void stmmac_start_rx_dma(struct stmmac_priv *priv, u32 chan)

    start RX DMA channel

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param chan:
        RX channel index
    :type chan: u32

.. _`stmmac_start_rx_dma.description`:

Description
-----------

This starts a RX DMA channel

.. _`stmmac_start_tx_dma`:

stmmac_start_tx_dma
===================

.. c:function:: void stmmac_start_tx_dma(struct stmmac_priv *priv, u32 chan)

    start TX DMA channel

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param chan:
        TX channel index
    :type chan: u32

.. _`stmmac_start_tx_dma.description`:

Description
-----------

This starts a TX DMA channel

.. _`stmmac_stop_rx_dma`:

stmmac_stop_rx_dma
==================

.. c:function:: void stmmac_stop_rx_dma(struct stmmac_priv *priv, u32 chan)

    stop RX DMA channel

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param chan:
        RX channel index
    :type chan: u32

.. _`stmmac_stop_rx_dma.description`:

Description
-----------

This stops a RX DMA channel

.. _`stmmac_stop_tx_dma`:

stmmac_stop_tx_dma
==================

.. c:function:: void stmmac_stop_tx_dma(struct stmmac_priv *priv, u32 chan)

    stop TX DMA channel

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param chan:
        TX channel index
    :type chan: u32

.. _`stmmac_stop_tx_dma.description`:

Description
-----------

This stops a TX DMA channel

.. _`stmmac_start_all_dma`:

stmmac_start_all_dma
====================

.. c:function:: void stmmac_start_all_dma(struct stmmac_priv *priv)

    start all RX and TX DMA channels

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_start_all_dma.description`:

Description
-----------

This starts all the RX and TX DMA channels

.. _`stmmac_stop_all_dma`:

stmmac_stop_all_dma
===================

.. c:function:: void stmmac_stop_all_dma(struct stmmac_priv *priv)

    stop all RX and TX DMA channels

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_stop_all_dma.description`:

Description
-----------

This stops the RX and TX DMA channels

.. _`stmmac_dma_operation_mode`:

stmmac_dma_operation_mode
=========================

.. c:function:: void stmmac_dma_operation_mode(struct stmmac_priv *priv)

    HW DMA operation mode

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_dma_operation_mode.description`:

Description
-----------

it is used for configuring the DMA operation mode register in
order to program the tx/rx DMA thresholds or Store-And-Forward mode.

.. _`stmmac_tx_clean`:

stmmac_tx_clean
===============

.. c:function:: int stmmac_tx_clean(struct stmmac_priv *priv, int budget, u32 queue)

    to manage the transmission completion

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param budget:
        *undescribed*
    :type budget: int

    :param queue:
        TX queue index
    :type queue: u32

.. _`stmmac_tx_clean.description`:

Description
-----------

it reclaims the transmit resources after transmission completes.

.. _`stmmac_tx_err`:

stmmac_tx_err
=============

.. c:function:: void stmmac_tx_err(struct stmmac_priv *priv, u32 chan)

    to manage the tx error

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param chan:
        channel index
    :type chan: u32

.. _`stmmac_tx_err.description`:

Description
-----------

it cleans the descriptors and restarts the transmission
in case of transmission errors.

.. _`stmmac_set_dma_operation_mode`:

stmmac_set_dma_operation_mode
=============================

.. c:function:: void stmmac_set_dma_operation_mode(struct stmmac_priv *priv, u32 txmode, u32 rxmode, u32 chan)

    Set DMA operation mode by channel

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param txmode:
        TX operating mode
    :type txmode: u32

    :param rxmode:
        RX operating mode
    :type rxmode: u32

    :param chan:
        channel index
    :type chan: u32

.. _`stmmac_set_dma_operation_mode.description`:

Description
-----------

it is used for configuring of the DMA operation mode in
runtime in order to program the tx/rx DMA thresholds or Store-And-Forward
mode.

.. _`stmmac_dma_interrupt`:

stmmac_dma_interrupt
====================

.. c:function:: void stmmac_dma_interrupt(struct stmmac_priv *priv)

    DMA ISR

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_dma_interrupt.description`:

Description
-----------

this is the DMA ISR. It is called by the main ISR.
It calls the dwmac dma routine and schedule poll method in case of some
work can be done.

.. _`stmmac_mmc_setup`:

stmmac_mmc_setup
================

.. c:function:: void stmmac_mmc_setup(struct stmmac_priv *priv)

    setup the Mac Management Counters (MMC)

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_mmc_setup.description`:

Description
-----------

this masks the MMC irq, in fact, the counters are managed in SW.

.. _`stmmac_get_hw_features`:

stmmac_get_hw_features
======================

.. c:function:: int stmmac_get_hw_features(struct stmmac_priv *priv)

    get MAC capabilities from the HW cap. register.

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

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

.. c:function:: void stmmac_check_ether_addr(struct stmmac_priv *priv)

    check if the MAC addr is valid

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_check_ether_addr.description`:

Description
-----------

it is to verify if the MAC address is valid, in case of failures it
generates a random MAC address

.. _`stmmac_init_dma_engine`:

stmmac_init_dma_engine
======================

.. c:function:: int stmmac_init_dma_engine(struct stmmac_priv *priv)

    DMA init.

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_init_dma_engine.description`:

Description
-----------

It inits the DMA invoking the specific MAC/GMAC callback.
Some DMA parameters can be passed from the platform;
in case of these are not passed a default is kept for the MAC or GMAC.

.. _`stmmac_tx_timer`:

stmmac_tx_timer
===============

.. c:function:: void stmmac_tx_timer(struct timer_list *t)

    mitigation sw timer for tx.

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`stmmac_tx_timer.description`:

Description
-----------

This is the timer handler to directly invoke the stmmac_tx_clean.

.. _`stmmac_init_tx_coalesce`:

stmmac_init_tx_coalesce
=======================

.. c:function:: void stmmac_init_tx_coalesce(struct stmmac_priv *priv)

    init tx mitigation options.

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_init_tx_coalesce.this-inits-the-transmit-coalesce-parameters`:

This inits the transmit coalesce parameters
-------------------------------------------

i.e. timer rate,
timer handler and default threshold used for enabling the
interrupt on completion bit.

.. _`stmmac_set_tx_queue_weight`:

stmmac_set_tx_queue_weight
==========================

.. c:function:: void stmmac_set_tx_queue_weight(struct stmmac_priv *priv)

    Set TX queue weight

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_set_tx_queue_weight.description`:

Description
-----------

It is used for setting TX queues weight

.. _`stmmac_configure_cbs`:

stmmac_configure_cbs
====================

.. c:function:: void stmmac_configure_cbs(struct stmmac_priv *priv)

    Configure CBS in TX queue

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_configure_cbs.description`:

Description
-----------

It is used for configuring CBS in AVB TX queues

.. _`stmmac_rx_queue_dma_chan_map`:

stmmac_rx_queue_dma_chan_map
============================

.. c:function:: void stmmac_rx_queue_dma_chan_map(struct stmmac_priv *priv)

    Map RX queue to RX dma channel

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_rx_queue_dma_chan_map.description`:

Description
-----------

It is used for mapping RX queues to RX dma channels

.. _`stmmac_mac_config_rx_queues_prio`:

stmmac_mac_config_rx_queues_prio
================================

.. c:function:: void stmmac_mac_config_rx_queues_prio(struct stmmac_priv *priv)

    Configure RX Queue priority

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_mac_config_rx_queues_prio.description`:

Description
-----------

It is used for configuring the RX Queue Priority

.. _`stmmac_mac_config_tx_queues_prio`:

stmmac_mac_config_tx_queues_prio
================================

.. c:function:: void stmmac_mac_config_tx_queues_prio(struct stmmac_priv *priv)

    Configure TX Queue priority

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_mac_config_tx_queues_prio.description`:

Description
-----------

It is used for configuring the TX Queue Priority

.. _`stmmac_mac_config_rx_queues_routing`:

stmmac_mac_config_rx_queues_routing
===================================

.. c:function:: void stmmac_mac_config_rx_queues_routing(struct stmmac_priv *priv)

    Configure RX Queue Routing

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_mac_config_rx_queues_routing.description`:

Description
-----------

It is used for configuring the RX queue routing

.. _`stmmac_mtl_configuration`:

stmmac_mtl_configuration
========================

.. c:function:: void stmmac_mtl_configuration(struct stmmac_priv *priv)

    Configure MTL

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_mtl_configuration.description`:

Description
-----------

It is used for configurring MTL

.. _`stmmac_hw_setup`:

stmmac_hw_setup
===============

.. c:function:: int stmmac_hw_setup(struct net_device *dev, bool init_ptp)

    setup mac in a usable state.

    :param dev:
        pointer to the device structure.
    :type dev: struct net_device \*

    :param init_ptp:
        *undescribed*
    :type init_ptp: bool

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

.. c:function:: int stmmac_open(struct net_device *dev)

    open entry point of the driver

    :param dev:
        pointer to the device structure.
    :type dev: struct net_device \*

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

.. c:function:: int stmmac_release(struct net_device *dev)

    close entry point of the driver

    :param dev:
        device pointer.
    :type dev: struct net_device \*

.. _`stmmac_release.description`:

Description
-----------

This is the stop entry point of the driver.

.. _`stmmac_tso_allocator`:

stmmac_tso_allocator
====================

.. c:function:: void stmmac_tso_allocator(struct stmmac_priv *priv, unsigned int des, int total_len, bool last_segment, u32 queue)

    close entry point of the driver

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param des:
        buffer start address
    :type des: unsigned int

    :param total_len:
        total length to fill in descriptors
    :type total_len: int

    :param last_segment:
        *undescribed*
    :type last_segment: bool

    :param queue:
        TX queue index
    :type queue: u32

.. _`stmmac_tso_allocator.description`:

Description
-----------

This function fills descriptor and request new descriptors according to
buffer length to fill

.. _`stmmac_tso_xmit`:

stmmac_tso_xmit
===============

.. c:function:: netdev_tx_t stmmac_tso_xmit(struct sk_buff *skb, struct net_device *dev)

    Tx entry point of the driver for oversized frames (TSO)

    :param skb:
        the socket buffer
    :type skb: struct sk_buff \*

    :param dev:
        device pointer
    :type dev: struct net_device \*

.. _`stmmac_tso_xmit.description`:

Description
-----------

this is the transmit function that is called on TSO frames
(support available on GMAC4 and newer chips).

.. _`stmmac_tso_xmit.diagram-below-show-the-ring-programming-in-case-of-tso-frames`:

Diagram below show the ring programming in case of TSO frames
-------------------------------------------------------------


First Descriptor
--------
\| DES0 \|---> buffer1 = L2/L3/L4 header
\| DES1 \|---> TCP Payload (can continue on next descr...)
\| DES2 \|---> buffer 1 and 2 len
\| DES3 \|---> must set TSE, TCP hdr len-> [22:19]. TCP payload len [17:0]
--------
\|
...
\|
--------
\| DES0 \| --\| Split TCP Payload on Buffers 1 and 2
\| DES1 \| --\|
\| DES2 \| --> buffer 1 and 2 len
\| DES3 \|
--------

mss is fixed when enable tso, so w/o programming the TDES3 ctx field.

.. _`stmmac_xmit`:

stmmac_xmit
===========

.. c:function:: netdev_tx_t stmmac_xmit(struct sk_buff *skb, struct net_device *dev)

    Tx entry point of the driver

    :param skb:
        the socket buffer
    :type skb: struct sk_buff \*

    :param dev:
        device pointer
        Description : this is the tx entry point of the driver.
        It programs the chain or the ring and supports oversized frames
        and SG feature.
    :type dev: struct net_device \*

.. _`stmmac_rx_refill`:

stmmac_rx_refill
================

.. c:function:: void stmmac_rx_refill(struct stmmac_priv *priv, u32 queue)

    refill used skb preallocated buffers

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param queue:
        RX queue index
        Description : this is to reallocate the skb for the reception process
        that is based on zero-copy.
    :type queue: u32

.. _`stmmac_rx`:

stmmac_rx
=========

.. c:function:: int stmmac_rx(struct stmmac_priv *priv, int limit, u32 queue)

    manage the receive process

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

    :param limit:
        napi bugget
    :type limit: int

    :param queue:
        RX queue index.
        Description :  this the function called by the napi poll method.
        It gets all the frames inside the ring.
    :type queue: u32

.. _`stmmac_napi_poll`:

stmmac_napi_poll
================

.. c:function:: int stmmac_napi_poll(struct napi_struct *napi, int budget)

    stmmac poll method (NAPI)

    :param napi:
        pointer to the napi structure.
    :type napi: struct napi_struct \*

    :param budget:
        maximum number of packets that the current CPU can receive from
        all interfaces.
        Description :
        To look at the incoming frames and clear the tx resources.
    :type budget: int

.. _`stmmac_tx_timeout`:

stmmac_tx_timeout
=================

.. c:function:: void stmmac_tx_timeout(struct net_device *dev)

    :param dev:
        Pointer to net device structure
    :type dev: struct net_device \*

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

.. c:function:: void stmmac_set_rx_mode(struct net_device *dev)

    entry point for multicast addressing

    :param dev:
        pointer to the device structure
    :type dev: struct net_device \*

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

.. c:function:: int stmmac_change_mtu(struct net_device *dev, int new_mtu)

    entry point to change MTU size for the device.

    :param dev:
        device pointer.
    :type dev: struct net_device \*

    :param new_mtu:
        the new MTU size for the device.
    :type new_mtu: int

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

.. c:function:: irqreturn_t stmmac_interrupt(int irq, void *dev_id)

    main ISR

    :param irq:
        interrupt number.
    :type irq: int

    :param dev_id:
        to pass the net device pointer.
    :type dev_id: void \*

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

.. c:function:: int stmmac_ioctl(struct net_device *dev, struct ifreq *rq, int cmd)

    Entry point for the Ioctl

    :param dev:
        Device pointer.
    :type dev: struct net_device \*

    :param rq:
        An IOCTL specefic structure, that can contain a pointer to
        a proprietary structure used to pass information to the driver.
    :type rq: struct ifreq \*

    :param cmd:
        IOCTL command
    :type cmd: int

.. _`stmmac_ioctl.description`:

Description
-----------

Currently it supports the phy_mii_ioctl(...) and HW time stamping.

.. _`stmmac_hw_init`:

stmmac_hw_init
==============

.. c:function:: int stmmac_hw_init(struct stmmac_priv *priv)

    Init the MAC device

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

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

.. c:function:: int stmmac_dvr_probe(struct device *device, struct plat_stmmacenet_data *plat_dat, struct stmmac_resources *res)

    :param device:
        device pointer
    :type device: struct device \*

    :param plat_dat:
        platform data pointer
    :type plat_dat: struct plat_stmmacenet_data \*

    :param res:
        stmmac resource pointer
    :type res: struct stmmac_resources \*

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

.. c:function:: int stmmac_dvr_remove(struct device *dev)

    :param dev:
        device pointer
    :type dev: struct device \*

.. _`stmmac_dvr_remove.description`:

Description
-----------

this function resets the TX/RX processes, disables the MAC RX/TX
changes the link status, releases the DMA descriptor rings.

.. _`stmmac_suspend`:

stmmac_suspend
==============

.. c:function:: int stmmac_suspend(struct device *dev)

    suspend callback

    :param dev:
        device pointer
    :type dev: struct device \*

.. _`stmmac_suspend.description`:

Description
-----------

this is the function to suspend the device and it is called
by the platform driver to stop the network queue, release the resources,
program the PMT register (for WoL), clean and release driver resources.

.. _`stmmac_reset_queues_param`:

stmmac_reset_queues_param
=========================

.. c:function:: void stmmac_reset_queues_param(struct stmmac_priv *priv)

    reset queue parameters

    :param priv:
        *undescribed*
    :type priv: struct stmmac_priv \*

.. _`stmmac_resume`:

stmmac_resume
=============

.. c:function:: int stmmac_resume(struct device *dev)

    resume callback

    :param dev:
        device pointer
    :type dev: struct device \*

.. _`stmmac_resume.description`:

Description
-----------

when resume this function is invoked to setup the DMA and CORE
in a usable state.

.. This file was automatic generated / don't edit.

