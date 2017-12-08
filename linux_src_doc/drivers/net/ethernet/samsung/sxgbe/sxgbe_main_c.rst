.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/samsung/sxgbe/sxgbe_main.c

.. _`sxgbe_verify_args`:

sxgbe_verify_args
=================

.. c:function:: void sxgbe_verify_args( void)

    verify the driver parameters.

    :param  void:
        no arguments

.. _`sxgbe_verify_args.description`:

Description
-----------

it verifies if some wrong parameter is passed to the driver.
Note that wrong parameters are replaced with the default values.

.. _`sxgbe_eee_ctrl_timer`:

sxgbe_eee_ctrl_timer
====================

.. c:function:: void sxgbe_eee_ctrl_timer(struct timer_list *t)

    :param struct timer_list \*t:
        *undescribed*

.. _`sxgbe_eee_ctrl_timer.description`:

Description
-----------

If there is no data transfer and if we are not in LPI state,
then MAC Transmitter can be moved to LPI state.

.. _`sxgbe_eee_init`:

sxgbe_eee_init
==============

.. c:function:: bool sxgbe_eee_init(struct sxgbe_priv_data * const priv)

    :param struct sxgbe_priv_data \* const priv:
        private device pointer

.. _`sxgbe_eee_init.description`:

Description
-----------

If the EEE support has been enabled while configuring the driver,
if the GMAC actually supports the EEE (from the HW cap reg) and the
phy can also manage EEE, so enable the LPI state and start the timer
to verify if the tx path can enter in LPI state.

.. _`sxgbe_clk_csr_set`:

sxgbe_clk_csr_set
=================

.. c:function:: void sxgbe_clk_csr_set(struct sxgbe_priv_data *priv)

    dynamically set the MDC clock

    :param struct sxgbe_priv_data \*priv:
        driver private structure

.. _`sxgbe_clk_csr_set.description`:

Description
-----------

this is to dynamically set the MDC clock according to the csr
clock input.

.. _`sxgbe_adjust_link`:

sxgbe_adjust_link
=================

.. c:function:: void sxgbe_adjust_link(struct net_device *dev)

    :param struct net_device \*dev:
        net device structure

.. _`sxgbe_adjust_link.description`:

Description
-----------

it adjusts the link parameters.

.. _`sxgbe_init_phy`:

sxgbe_init_phy
==============

.. c:function:: int sxgbe_init_phy(struct net_device *ndev)

    PHY initialization

    :param struct net_device \*ndev:
        *undescribed*

.. _`sxgbe_init_phy.description`:

Description
-----------

it initializes the driver's PHY state, and attaches the PHY
to the mac driver.

.. _`sxgbe_init_phy.return-value`:

Return value
------------

0 on success

.. _`sxgbe_clear_descriptors`:

sxgbe_clear_descriptors
=======================

.. c:function:: void sxgbe_clear_descriptors(struct sxgbe_priv_data *priv)

    clear descriptors

    :param struct sxgbe_priv_data \*priv:
        driver private structure

.. _`sxgbe_clear_descriptors.description`:

Description
-----------

this function is called to clear the tx and rx descriptors
in case of both basic and extended descriptors are used.

.. _`sxgbe_free_rx_buffers`:

sxgbe_free_rx_buffers
=====================

.. c:function:: void sxgbe_free_rx_buffers(struct net_device *dev, struct sxgbe_rx_norm_desc *p, int i, unsigned int dma_buf_sz, struct sxgbe_rx_queue *rx_ring)

    free what \ :c:func:`sxgbe_init_rx_buffers`\  allocated

    :param struct net_device \*dev:
        net device structure

    :param struct sxgbe_rx_norm_desc \*p:
        *undescribed*

    :param int i:
        *undescribed*

    :param unsigned int dma_buf_sz:
        *undescribed*

    :param struct sxgbe_rx_queue \*rx_ring:
        ring to be freed

.. _`sxgbe_free_rx_buffers.description`:

Description
-----------

this function initializes the DMA RX descriptor

.. _`init_tx_ring`:

init_tx_ring
============

.. c:function:: int init_tx_ring(struct device *dev, u8 queue_no, struct sxgbe_tx_queue *tx_ring, int tx_rsize)

    init the TX descriptor ring

    :param struct device \*dev:
        net device structure

    :param u8 queue_no:
        *undescribed*

    :param struct sxgbe_tx_queue \*tx_ring:
        ring to be initialised

    :param int tx_rsize:
        ring size

.. _`init_tx_ring.description`:

Description
-----------

this function initializes the DMA TX descriptor

.. _`free_rx_ring`:

free_rx_ring
============

.. c:function:: void free_rx_ring(struct device *dev, struct sxgbe_rx_queue *rx_ring, int rx_rsize)

    free the RX descriptor ring

    :param struct device \*dev:
        net device structure

    :param struct sxgbe_rx_queue \*rx_ring:
        ring to be initialised

    :param int rx_rsize:
        ring size

.. _`free_rx_ring.description`:

Description
-----------

this function initializes the DMA RX descriptor

.. _`init_rx_ring`:

init_rx_ring
============

.. c:function:: int init_rx_ring(struct net_device *dev, u8 queue_no, struct sxgbe_rx_queue *rx_ring, int rx_rsize)

    init the RX descriptor ring

    :param struct net_device \*dev:
        net device structure

    :param u8 queue_no:
        *undescribed*

    :param struct sxgbe_rx_queue \*rx_ring:
        ring to be initialised

    :param int rx_rsize:
        ring size

.. _`init_rx_ring.description`:

Description
-----------

this function initializes the DMA RX descriptor

.. _`free_tx_ring`:

free_tx_ring
============

.. c:function:: void free_tx_ring(struct device *dev, struct sxgbe_tx_queue *tx_ring, int tx_rsize)

    free the TX descriptor ring

    :param struct device \*dev:
        net device structure

    :param struct sxgbe_tx_queue \*tx_ring:
        ring to be initialised

    :param int tx_rsize:
        ring size

.. _`free_tx_ring.description`:

Description
-----------

this function initializes the DMA TX descriptor

.. _`init_dma_desc_rings`:

init_dma_desc_rings
===================

.. c:function:: int init_dma_desc_rings(struct net_device *netd)

    init the RX/TX descriptor rings

    :param struct net_device \*netd:
        *undescribed*

.. _`init_dma_desc_rings.description`:

Description
-----------

this function initializes the DMA RX/TX descriptors
and allocates the socket buffers. It suppors the chained and ring
modes.

.. _`sxgbe_mtl_operation_mode`:

sxgbe_mtl_operation_mode
========================

.. c:function:: void sxgbe_mtl_operation_mode(struct sxgbe_priv_data *priv)

    HW MTL operation mode

    :param struct sxgbe_priv_data \*priv:
        driver private structure

.. _`sxgbe_mtl_operation_mode.description`:

Description
-----------

it sets the MTL operation mode: tx/rx MTL thresholds
or Store-And-Forward capability.

.. _`sxgbe_tx_queue_clean`:

sxgbe_tx_queue_clean
====================

.. c:function:: void sxgbe_tx_queue_clean(struct sxgbe_tx_queue *tqueue)

    :param struct sxgbe_tx_queue \*tqueue:
        *undescribed*

.. _`sxgbe_tx_queue_clean.description`:

Description
-----------

it reclaims resources after transmission completes.

.. _`sxgbe_tx_all_clean`:

sxgbe_tx_all_clean
==================

.. c:function:: void sxgbe_tx_all_clean(struct sxgbe_priv_data * const priv)

    :param struct sxgbe_priv_data \* const priv:
        driver private structure

.. _`sxgbe_tx_all_clean.description`:

Description
-----------

it reclaims resources after transmission completes.

.. _`sxgbe_restart_tx_queue`:

sxgbe_restart_tx_queue
======================

.. c:function:: void sxgbe_restart_tx_queue(struct sxgbe_priv_data *priv, int queue_num)

    irq tx error mng function

    :param struct sxgbe_priv_data \*priv:
        driver private structure

    :param int queue_num:
        *undescribed*

.. _`sxgbe_restart_tx_queue.description`:

Description
-----------

it cleans the descriptors and restarts the transmission
in case of errors.

.. _`sxgbe_reset_all_tx_queues`:

sxgbe_reset_all_tx_queues
=========================

.. c:function:: void sxgbe_reset_all_tx_queues(struct sxgbe_priv_data *priv)

    irq tx error mng function

    :param struct sxgbe_priv_data \*priv:
        driver private structure

.. _`sxgbe_reset_all_tx_queues.description`:

Description
-----------

it cleans all the descriptors and
restarts the transmission on all queues in case of errors.

.. _`sxgbe_get_hw_features`:

sxgbe_get_hw_features
=====================

.. c:function:: int sxgbe_get_hw_features(struct sxgbe_priv_data * const priv)

    get XMAC capabilities from the HW cap. register.

    :param struct sxgbe_priv_data \* const priv:
        driver private structure

.. _`sxgbe_get_hw_features.description`:

Description
-----------

new GMAC chip generations have a new register to indicate the
presence of the optional feature/functions.
This can be also used to override the value passed through the
platform and necessary for old MAC10/100 and GMAC chips.

.. _`sxgbe_check_ether_addr`:

sxgbe_check_ether_addr
======================

.. c:function:: void sxgbe_check_ether_addr(struct sxgbe_priv_data *priv)

    check if the MAC addr is valid

    :param struct sxgbe_priv_data \*priv:
        driver private structure

.. _`sxgbe_check_ether_addr.description`:

Description
-----------

it is to verify if the MAC address is valid, in case of failures it
generates a random MAC address

.. _`sxgbe_init_dma_engine`:

sxgbe_init_dma_engine
=====================

.. c:function:: int sxgbe_init_dma_engine(struct sxgbe_priv_data *priv)

    DMA init.

    :param struct sxgbe_priv_data \*priv:
        driver private structure

.. _`sxgbe_init_dma_engine.description`:

Description
-----------

It inits the DMA invoking the specific SXGBE callback.
Some DMA parameters can be passed from the platform;
in case of these are not passed a default is kept for the MAC or GMAC.

.. _`sxgbe_init_mtl_engine`:

sxgbe_init_mtl_engine
=====================

.. c:function:: void sxgbe_init_mtl_engine(struct sxgbe_priv_data *priv)

    MTL init.

    :param struct sxgbe_priv_data \*priv:
        driver private structure

.. _`sxgbe_init_mtl_engine.description`:

Description
-----------

It inits the MTL invoking the specific SXGBE callback.

.. _`sxgbe_disable_mtl_engine`:

sxgbe_disable_mtl_engine
========================

.. c:function:: void sxgbe_disable_mtl_engine(struct sxgbe_priv_data *priv)

    MTL disable.

    :param struct sxgbe_priv_data \*priv:
        driver private structure

.. _`sxgbe_disable_mtl_engine.description`:

Description
-----------

It disables the MTL queues by invoking the specific SXGBE callback.

.. _`sxgbe_tx_timer`:

sxgbe_tx_timer
==============

.. c:function:: void sxgbe_tx_timer(struct timer_list *t)

    mitigation sw timer for tx.

    :param struct timer_list \*t:
        timer pointer

.. _`sxgbe_tx_timer.description`:

Description
-----------

This is the timer handler to directly invoke the sxgbe_tx_clean.

.. _`sxgbe_tx_init_coalesce`:

sxgbe_tx_init_coalesce
======================

.. c:function:: void sxgbe_tx_init_coalesce(struct sxgbe_priv_data *priv)

    init tx mitigation options.

    :param struct sxgbe_priv_data \*priv:
        driver private structure

.. _`sxgbe_tx_init_coalesce.this-inits-the-transmit-coalesce-parameters`:

This inits the transmit coalesce parameters
-------------------------------------------

i.e. timer rate,
timer handler and default threshold used for enabling the
interrupt on completion bit.

.. _`sxgbe_open`:

sxgbe_open
==========

.. c:function:: int sxgbe_open(struct net_device *dev)

    open entry point of the driver

    :param struct net_device \*dev:
        pointer to the device structure.

.. _`sxgbe_open.description`:

Description
-----------

This function is the open entry point of the driver.

.. _`sxgbe_open.return-value`:

Return value
------------

0 on success and an appropriate (-)ve integer as defined in errno.h
file on failure.

.. _`sxgbe_release`:

sxgbe_release
=============

.. c:function:: int sxgbe_release(struct net_device *dev)

    close entry point of the driver

    :param struct net_device \*dev:
        device pointer.

.. _`sxgbe_release.description`:

Description
-----------

This is the stop entry point of the driver.

.. _`sxgbe_xmit`:

sxgbe_xmit
==========

.. c:function:: netdev_tx_t sxgbe_xmit(struct sk_buff *skb, struct net_device *dev)

    Tx entry point of the driver

    :param struct sk_buff \*skb:
        the socket buffer

    :param struct net_device \*dev:
        device pointer
        Description : this is the tx entry point of the driver.
        It programs the chain or the ring and supports oversized frames
        and SG feature.

.. _`sxgbe_rx_refill`:

sxgbe_rx_refill
===============

.. c:function:: void sxgbe_rx_refill(struct sxgbe_priv_data *priv)

    refill used skb preallocated buffers

    :param struct sxgbe_priv_data \*priv:
        driver private structure
        Description : this is to reallocate the skb for the reception process
        that is based on zero-copy.

.. _`sxgbe_rx`:

sxgbe_rx
========

.. c:function:: int sxgbe_rx(struct sxgbe_priv_data *priv, int limit)

    receive the frames from the remote host

    :param struct sxgbe_priv_data \*priv:
        driver private structure

    :param int limit:
        napi bugget.
        Description :  this the function called by the napi poll method.
        It gets all the frames inside the ring.

.. _`sxgbe_poll`:

sxgbe_poll
==========

.. c:function:: int sxgbe_poll(struct napi_struct *napi, int budget)

    sxgbe poll method (NAPI)

    :param struct napi_struct \*napi:
        pointer to the napi structure.

    :param int budget:
        maximum number of packets that the current CPU can receive from
        all interfaces.
        Description :
        To look at the incoming frames and clear the tx resources.

.. _`sxgbe_tx_timeout`:

sxgbe_tx_timeout
================

.. c:function:: void sxgbe_tx_timeout(struct net_device *dev)

    :param struct net_device \*dev:
        Pointer to net device structure

.. _`sxgbe_tx_timeout.description`:

Description
-----------

this function is called when a packet transmission fails to
complete within a reasonable time. The driver will mark the error in the
netdev structure and arrange for the device to be reset to a sane state
in order to transmit a new packet.

.. _`sxgbe_common_interrupt`:

sxgbe_common_interrupt
======================

.. c:function:: irqreturn_t sxgbe_common_interrupt(int irq, void *dev_id)

    main ISR

    :param int irq:
        interrupt number.

    :param void \*dev_id:
        to pass the net device pointer.

.. _`sxgbe_common_interrupt.description`:

Description
-----------

this is the main driver interrupt service routine.
It calls the DMA ISR and also the core ISR to manage PMT, MMC, LPI
interrupts.

.. _`sxgbe_tx_interrupt`:

sxgbe_tx_interrupt
==================

.. c:function:: irqreturn_t sxgbe_tx_interrupt(int irq, void *dev_id)

    TX DMA ISR

    :param int irq:
        interrupt number.

    :param void \*dev_id:
        to pass the net device pointer.

.. _`sxgbe_tx_interrupt.description`:

Description
-----------

this is the tx dma interrupt service routine.

.. _`sxgbe_rx_interrupt`:

sxgbe_rx_interrupt
==================

.. c:function:: irqreturn_t sxgbe_rx_interrupt(int irq, void *dev_id)

    RX DMA ISR

    :param int irq:
        interrupt number.

    :param void \*dev_id:
        to pass the net device pointer.

.. _`sxgbe_rx_interrupt.description`:

Description
-----------

this is the rx dma interrupt service routine.

.. _`sxgbe_set_rx_mode`:

sxgbe_set_rx_mode
=================

.. c:function:: void sxgbe_set_rx_mode(struct net_device *dev)

    entry point for setting different receive mode of a device. unicast, multicast addressing

    :param struct net_device \*dev:
        pointer to the device structure

.. _`sxgbe_set_rx_mode.description`:

Description
-----------

This function is a driver entry point which gets called by the kernel
whenever different receive mode like unicast, multicast and promiscuous
must be enabled/disabled.

.. _`sxgbe_set_rx_mode.return-value`:

Return value
------------

void.

.. _`sxgbe_poll_controller`:

sxgbe_poll_controller
=====================

.. c:function:: void sxgbe_poll_controller(struct net_device *dev)

    entry point for polling receive by device

    :param struct net_device \*dev:
        pointer to the device structure

.. _`sxgbe_poll_controller.description`:

Description
-----------

This function is used by NETCONSOLE and other diagnostic tools
to allow network I/O with interrupts disabled.

.. _`sxgbe_poll_controller.return-value`:

Return value
------------

Void.

.. _`sxgbe_hw_init`:

sxgbe_hw_init
=============

.. c:function:: int sxgbe_hw_init(struct sxgbe_priv_data * const priv)

    Init the GMAC device

    :param struct sxgbe_priv_data \* const priv:
        driver private structure

.. _`sxgbe_hw_init.description`:

Description
-----------

this function checks the HW capability
(if supported) and sets the driver's features.

.. _`sxgbe_drv_probe`:

sxgbe_drv_probe
===============

.. c:function:: struct sxgbe_priv_data *sxgbe_drv_probe(struct device *device, struct sxgbe_plat_data *plat_dat, void __iomem *addr)

    :param struct device \*device:
        device pointer

    :param struct sxgbe_plat_data \*plat_dat:
        platform data pointer

    :param void __iomem \*addr:
        iobase memory address

.. _`sxgbe_drv_probe.description`:

Description
-----------

this is the main probe function used to
call the alloc_etherdev, allocate the priv structure.

.. _`sxgbe_drv_remove`:

sxgbe_drv_remove
================

.. c:function:: int sxgbe_drv_remove(struct net_device *ndev)

    :param struct net_device \*ndev:
        net device pointer

.. _`sxgbe_drv_remove.description`:

Description
-----------

this function resets the TX/RX processes, disables the MAC RX/TX
changes the link status, releases the DMA descriptor rings.

.. This file was automatic generated / don't edit.

