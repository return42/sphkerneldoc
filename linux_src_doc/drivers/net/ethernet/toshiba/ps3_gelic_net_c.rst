.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/toshiba/ps3_gelic_net.c

.. _`gelic_descr_get_status`:

gelic_descr_get_status
======================

.. c:function:: enum gelic_descr_dma_status gelic_descr_get_status(struct gelic_descr *descr)

    - returns the status of a descriptor

    :param descr:
        descriptor to look at
    :type descr: struct gelic_descr \*

.. _`gelic_descr_get_status.description`:

Description
-----------

returns the status as in the dmac_cmd_status field of the descriptor

.. _`gelic_card_disable_txdmac`:

gelic_card_disable_txdmac
=========================

.. c:function:: void gelic_card_disable_txdmac(struct gelic_card *card)

    disables the transmit DMA controller

    :param card:
        card structure
    :type card: struct gelic_card \*

.. _`gelic_card_disable_txdmac.description`:

Description
-----------

gelic_card_disable_txdmac terminates processing on the DMA controller by
turing off DMA and issuing a force end

.. _`gelic_card_enable_rxdmac`:

gelic_card_enable_rxdmac
========================

.. c:function:: void gelic_card_enable_rxdmac(struct gelic_card *card)

    enables the receive DMA controller

    :param card:
        card structure
    :type card: struct gelic_card \*

.. _`gelic_card_enable_rxdmac.description`:

Description
-----------

gelic_card_enable_rxdmac enables the DMA controller by setting RX_DMA_EN
in the GDADMACCNTR register

.. _`gelic_card_disable_rxdmac`:

gelic_card_disable_rxdmac
=========================

.. c:function:: void gelic_card_disable_rxdmac(struct gelic_card *card)

    disables the receive DMA controller

    :param card:
        card structure
    :type card: struct gelic_card \*

.. _`gelic_card_disable_rxdmac.description`:

Description
-----------

gelic_card_disable_rxdmac terminates processing on the DMA controller by
turing off DMA and issuing a force end

.. _`gelic_descr_set_status`:

gelic_descr_set_status
======================

.. c:function:: void gelic_descr_set_status(struct gelic_descr *descr, enum gelic_descr_dma_status status)

    - sets the status of a descriptor

    :param descr:
        descriptor to change
    :type descr: struct gelic_descr \*

    :param status:
        status to set in the descriptor
    :type status: enum gelic_descr_dma_status

.. _`gelic_descr_set_status.description`:

Description
-----------

changes the status to the specified value. Doesn't change other bits
in the status

.. _`gelic_card_reset_chain`:

gelic_card_reset_chain
======================

.. c:function:: void gelic_card_reset_chain(struct gelic_card *card, struct gelic_descr_chain *chain, struct gelic_descr *start_descr)

    reset status of a descriptor chain

    :param card:
        card structure
    :type card: struct gelic_card \*

    :param chain:
        address of chain
    :type chain: struct gelic_descr_chain \*

    :param start_descr:
        address of descriptor array
    :type start_descr: struct gelic_descr \*

.. _`gelic_card_reset_chain.description`:

Description
-----------

Reset the status of dma descriptors to ready state
and re-initialize the hardware chain for later use

.. _`gelic_card_free_chain`:

gelic_card_free_chain
=====================

.. c:function:: void gelic_card_free_chain(struct gelic_card *card, struct gelic_descr *descr_in)

    free descriptor chain

    :param card:
        card structure
    :type card: struct gelic_card \*

    :param descr_in:
        address of desc
    :type descr_in: struct gelic_descr \*

.. _`gelic_card_init_chain`:

gelic_card_init_chain
=====================

.. c:function:: int gelic_card_init_chain(struct gelic_card *card, struct gelic_descr_chain *chain, struct gelic_descr *start_descr, int no)

    links descriptor chain

    :param card:
        card structure
    :type card: struct gelic_card \*

    :param chain:
        address of chain
    :type chain: struct gelic_descr_chain \*

    :param start_descr:
        address of descriptor array
    :type start_descr: struct gelic_descr \*

    :param no:
        number of descriptors
    :type no: int

.. _`gelic_card_init_chain.description`:

Description
-----------

we manage a circular list that mirrors the hardware structure,
except that the hardware uses bus addresses.

returns 0 on success, <0 on failure

.. _`gelic_descr_prepare_rx`:

gelic_descr_prepare_rx
======================

.. c:function:: int gelic_descr_prepare_rx(struct gelic_card *card, struct gelic_descr *descr)

    reinitializes a rx descriptor

    :param card:
        card structure
    :type card: struct gelic_card \*

    :param descr:
        descriptor to re-init
    :type descr: struct gelic_descr \*

.. _`gelic_descr_prepare_rx.description`:

Description
-----------

return 0 on success, <0 on failure

allocates a new rx skb, iommu-maps it and attaches it to the descriptor.
Activate the descriptor state-wise

.. _`gelic_card_release_rx_chain`:

gelic_card_release_rx_chain
===========================

.. c:function:: void gelic_card_release_rx_chain(struct gelic_card *card)

    free all skb of rx descr

    :param card:
        card structure
    :type card: struct gelic_card \*

.. _`gelic_card_fill_rx_chain`:

gelic_card_fill_rx_chain
========================

.. c:function:: int gelic_card_fill_rx_chain(struct gelic_card *card)

    fills descriptors/skbs in the rx chains

    :param card:
        card structure
    :type card: struct gelic_card \*

.. _`gelic_card_fill_rx_chain.fills-all-descriptors-in-the-rx-chain`:

fills all descriptors in the rx chain
-------------------------------------

allocates skbs
and iommu-maps them.
returns 0 on success, < 0 on failure

.. _`gelic_card_alloc_rx_skbs`:

gelic_card_alloc_rx_skbs
========================

.. c:function:: int gelic_card_alloc_rx_skbs(struct gelic_card *card)

    allocates rx skbs in rx descriptor chains

    :param card:
        card structure
    :type card: struct gelic_card \*

.. _`gelic_card_alloc_rx_skbs.description`:

Description
-----------

returns 0 on success, < 0 on failure

.. _`gelic_descr_release_tx`:

gelic_descr_release_tx
======================

.. c:function:: void gelic_descr_release_tx(struct gelic_card *card, struct gelic_descr *descr)

    processes a used tx descriptor

    :param card:
        card structure
    :type card: struct gelic_card \*

    :param descr:
        descriptor to release
    :type descr: struct gelic_descr \*

.. _`gelic_descr_release_tx.description`:

Description
-----------

releases a used tx descriptor (unmapping, freeing of skb)

.. _`gelic_card_release_tx_chain`:

gelic_card_release_tx_chain
===========================

.. c:function:: void gelic_card_release_tx_chain(struct gelic_card *card, int stop)

    processes sent tx descriptors

    :param card:
        adapter structure
    :type card: struct gelic_card \*

    :param stop:
        net_stop sequence
    :type stop: int

.. _`gelic_card_release_tx_chain.description`:

Description
-----------

releases the tx descriptors that gelic has finished with

.. _`gelic_net_set_multi`:

gelic_net_set_multi
===================

.. c:function:: void gelic_net_set_multi(struct net_device *netdev)

    sets multicast addresses and promisc flags

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`gelic_net_set_multi.description`:

Description
-----------

gelic_net_set_multi configures multicast addresses as needed for the
netdev interface. It also sets up multicast, allmulti and promisc
flags appropriately

.. _`gelic_net_stop`:

gelic_net_stop
==============

.. c:function:: int gelic_net_stop(struct net_device *netdev)

    called upon ifconfig down

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`gelic_net_stop.description`:

Description
-----------

always returns 0

.. _`gelic_card_get_next_tx_descr`:

gelic_card_get_next_tx_descr
============================

.. c:function:: struct gelic_descr *gelic_card_get_next_tx_descr(struct gelic_card *card)

    returns the next available tx descriptor

    :param card:
        device structure to get descriptor from
    :type card: struct gelic_card \*

.. _`gelic_card_get_next_tx_descr.description`:

Description
-----------

returns the address of the next descriptor, or NULL if not available.

.. _`gelic_descr_set_tx_cmdstat`:

gelic_descr_set_tx_cmdstat
==========================

.. c:function:: void gelic_descr_set_tx_cmdstat(struct gelic_descr *descr, struct sk_buff *skb)

    sets the tx descriptor command field

    :param descr:
        descriptor structure to fill out
    :type descr: struct gelic_descr \*

    :param skb:
        packet to consider
    :type skb: struct sk_buff \*

.. _`gelic_descr_set_tx_cmdstat.description`:

Description
-----------

fills out the command and status field of the descriptor structure,
depending on hardware checksum settings. This function assumes a \ :c:func:`wmb`\ 
has executed before.

.. _`gelic_descr_prepare_tx`:

gelic_descr_prepare_tx
======================

.. c:function:: int gelic_descr_prepare_tx(struct gelic_card *card, struct gelic_descr *descr, struct sk_buff *skb)

    setup a descriptor for sending packets

    :param card:
        card structure
    :type card: struct gelic_card \*

    :param descr:
        descriptor structure
    :type descr: struct gelic_descr \*

    :param skb:
        packet to use
    :type skb: struct sk_buff \*

.. _`gelic_descr_prepare_tx.description`:

Description
-----------

returns 0 on success, <0 on failure.

.. _`gelic_card_kick_txdma`:

gelic_card_kick_txdma
=====================

.. c:function:: int gelic_card_kick_txdma(struct gelic_card *card, struct gelic_descr *descr)

    enables TX DMA processing

    :param card:
        card structure
    :type card: struct gelic_card \*

    :param descr:
        descriptor address to enable TX processing at
    :type descr: struct gelic_descr \*

.. _`gelic_net_xmit`:

gelic_net_xmit
==============

.. c:function:: netdev_tx_t gelic_net_xmit(struct sk_buff *skb, struct net_device *netdev)

    transmits a frame over the device

    :param skb:
        packet to send out
    :type skb: struct sk_buff \*

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`gelic_net_xmit.description`:

Description
-----------

returns NETDEV_TX_OK on success, NETDEV_TX_BUSY on failure

.. _`gelic_net_pass_skb_up`:

gelic_net_pass_skb_up
=====================

.. c:function:: void gelic_net_pass_skb_up(struct gelic_descr *descr, struct gelic_card *card, struct net_device *netdev)

    takes an skb from a descriptor and passes it on

    :param descr:
        descriptor to process
    :type descr: struct gelic_descr \*

    :param card:
        card structure
    :type card: struct gelic_card \*

    :param netdev:
        net_device structure to be passed packet
    :type netdev: struct net_device \*

.. _`gelic_net_pass_skb_up.description`:

Description
-----------

iommu-unmaps the skb, fills out skb structure and passes the data to the
stack. The descriptor state is not changed.

.. _`gelic_card_decode_one_descr`:

gelic_card_decode_one_descr
===========================

.. c:function:: int gelic_card_decode_one_descr(struct gelic_card *card)

    processes an rx descriptor

    :param card:
        card structure
    :type card: struct gelic_card \*

.. _`gelic_card_decode_one_descr.description`:

Description
-----------

returns 1 if a packet has been sent to the stack, otherwise 0

processes an rx descriptor by iommu-unmapping the data buffer and passing
the packet up to the stack

.. _`gelic_net_poll`:

gelic_net_poll
==============

.. c:function:: int gelic_net_poll(struct napi_struct *napi, int budget)

    NAPI poll function called by the stack to return packets

    :param napi:
        napi structure
    :type napi: struct napi_struct \*

    :param budget:
        number of packets we can pass to the stack at most
    :type budget: int

.. _`gelic_net_poll.description`:

Description
-----------

returns the number of the processed packets

.. _`gelic_card_interrupt`:

gelic_card_interrupt
====================

.. c:function:: irqreturn_t gelic_card_interrupt(int irq, void *ptr)

    event handler for gelic_net

    :param irq:
        *undescribed*
    :type irq: int

    :param ptr:
        *undescribed*
    :type ptr: void \*

.. _`gelic_net_poll_controller`:

gelic_net_poll_controller
=========================

.. c:function:: void gelic_net_poll_controller(struct net_device *netdev)

    artificial interrupt for netconsole etc.

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`gelic_net_poll_controller.description`:

Description
-----------

see Documentation/networking/netconsole.txt

.. _`gelic_net_open`:

gelic_net_open
==============

.. c:function:: int gelic_net_open(struct net_device *netdev)

    called upon ifconfig up

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`gelic_net_open.description`:

Description
-----------

returns 0 on success, <0 on failure

gelic_net_open allocates all the descriptors and memory needed for
operation, sets up multicast list and enables interrupts

.. _`gelic_net_tx_timeout_task`:

gelic_net_tx_timeout_task
=========================

.. c:function:: void gelic_net_tx_timeout_task(struct work_struct *work)

    task scheduled by the watchdog timeout function (to be called not under interrupt status)

    :param work:
        work is context of tx timout task
    :type work: struct work_struct \*

.. _`gelic_net_tx_timeout_task.description`:

Description
-----------

called as task when tx hangs, resets interface (if interface is up)

.. _`gelic_net_tx_timeout`:

gelic_net_tx_timeout
====================

.. c:function:: void gelic_net_tx_timeout(struct net_device *netdev)

    called when the tx timeout watchdog kicks in.

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`gelic_net_tx_timeout.description`:

Description
-----------

called, if tx hangs. Schedules a task that resets the interface

.. _`gelic_ether_setup_netdev_ops`:

gelic_ether_setup_netdev_ops
============================

.. c:function:: void gelic_ether_setup_netdev_ops(struct net_device *netdev, struct napi_struct *napi)

    initialization of net_device operations

    :param netdev:
        net_device structure
    :type netdev: struct net_device \*

    :param napi:
        *undescribed*
    :type napi: struct napi_struct \*

.. _`gelic_ether_setup_netdev_ops.description`:

Description
-----------

fills out function pointers in the net_device structure

.. _`gelic_net_setup_netdev`:

gelic_net_setup_netdev
======================

.. c:function:: int gelic_net_setup_netdev(struct net_device *netdev, struct gelic_card *card)

    initialization of net_device

    :param netdev:
        net_device structure
    :type netdev: struct net_device \*

    :param card:
        card structure
    :type card: struct gelic_card \*

.. _`gelic_net_setup_netdev.description`:

Description
-----------

Returns 0 on success or <0 on failure

gelic_ether_setup_netdev initializes the net_device structure
and register it.

.. _`gelic_align`:

GELIC_ALIGN
===========

.. c:function::  GELIC_ALIGN()

    allocates net_device and card structure

.. _`gelic_align.description`:

Description
-----------

returns the card structure or NULL in case of errors

the card and net_device structures are linked to each other

.. _`ps3_gelic_driver_probe`:

ps3_gelic_driver_probe
======================

.. c:function:: int ps3_gelic_driver_probe(struct ps3_system_bus_device *dev)

    add a device to the control of this driver

    :param dev:
        *undescribed*
    :type dev: struct ps3_system_bus_device \*

.. _`ps3_gelic_driver_remove`:

ps3_gelic_driver_remove
=======================

.. c:function:: int ps3_gelic_driver_remove(struct ps3_system_bus_device *dev)

    remove a device from the control of this driver

    :param dev:
        *undescribed*
    :type dev: struct ps3_system_bus_device \*

.. This file was automatic generated / don't edit.

