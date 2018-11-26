.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/toshiba/spider_net.c

.. _`spider_net_read_reg`:

spider_net_read_reg
===================

.. c:function:: u32 spider_net_read_reg(struct spider_net_card *card, u32 reg)

    reads an SMMIO register of a card

    :param card:
        device structure
    :type card: struct spider_net_card \*

    :param reg:
        register to read from
    :type reg: u32

.. _`spider_net_read_reg.description`:

Description
-----------

returns the content of the specified SMMIO register.

.. _`spider_net_write_reg`:

spider_net_write_reg
====================

.. c:function:: void spider_net_write_reg(struct spider_net_card *card, u32 reg, u32 value)

    writes to an SMMIO register of a card

    :param card:
        device structure
    :type card: struct spider_net_card \*

    :param reg:
        register to write to
    :type reg: u32

    :param value:
        value to write into the specified SMMIO register
    :type value: u32

.. _`spider_net_write_phy`:

spider_net_write_phy
====================

.. c:function:: void spider_net_write_phy(struct net_device *netdev, int mii_id, int reg, int val)

    write to phy register

    :param netdev:
        adapter to be written to
    :type netdev: struct net_device \*

    :param mii_id:
        id of MII
    :type mii_id: int

    :param reg:
        PHY register
    :type reg: int

    :param val:
        value to be written to phy register
    :type val: int

.. _`spider_net_write_phy.description`:

Description
-----------

spider_net_write_phy_register writes to an arbitrary PHY
register via the spider GPCWOPCMD register. We assume the queue does
not run full (not more than 15 commands outstanding).

.. _`spider_net_read_phy`:

spider_net_read_phy
===================

.. c:function:: int spider_net_read_phy(struct net_device *netdev, int mii_id, int reg)

    read from phy register

    :param netdev:
        network device to be read from
    :type netdev: struct net_device \*

    :param mii_id:
        id of MII
    :type mii_id: int

    :param reg:
        PHY register
    :type reg: int

.. _`spider_net_read_phy.description`:

Description
-----------

Returns value read from PHY register

spider_net_write_phy reads from an arbitrary PHY
register via the spider GPCROPCMD register

.. _`spider_net_setup_aneg`:

spider_net_setup_aneg
=====================

.. c:function:: void spider_net_setup_aneg(struct spider_net_card *card)

    initial auto-negotiation setup

    :param card:
        device structure
    :type card: struct spider_net_card \*

.. _`spider_net_rx_irq_off`:

spider_net_rx_irq_off
=====================

.. c:function:: void spider_net_rx_irq_off(struct spider_net_card *card)

    switch off rx irq on this spider card

    :param card:
        device structure
    :type card: struct spider_net_card \*

.. _`spider_net_rx_irq_off.description`:

Description
-----------

switches off rx irq by masking them out in the GHIINTnMSK register

.. _`spider_net_rx_irq_on`:

spider_net_rx_irq_on
====================

.. c:function:: void spider_net_rx_irq_on(struct spider_net_card *card)

    switch on rx irq on this spider card

    :param card:
        device structure
    :type card: struct spider_net_card \*

.. _`spider_net_rx_irq_on.description`:

Description
-----------

switches on rx irq by enabling them in the GHIINTnMSK register

.. _`spider_net_set_promisc`:

spider_net_set_promisc
======================

.. c:function:: void spider_net_set_promisc(struct spider_net_card *card)

    sets the unicast address or the promiscuous mode

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_set_promisc.description`:

Description
-----------

spider_net_set_promisc sets the unicast destination address filter and
thus either allows for non-promisc mode or promisc mode

.. _`spider_net_get_descr_status`:

spider_net_get_descr_status
===========================

.. c:function:: int spider_net_get_descr_status(struct spider_net_hw_descr *hwdescr)

    - returns the status of a descriptor

    :param hwdescr:
        *undescribed*
    :type hwdescr: struct spider_net_hw_descr \*

.. _`spider_net_get_descr_status.description`:

Description
-----------

returns the status as in the dmac_cmd_status field of the descriptor

.. _`spider_net_free_chain`:

spider_net_free_chain
=====================

.. c:function:: void spider_net_free_chain(struct spider_net_card *card, struct spider_net_descr_chain *chain)

    free descriptor chain

    :param card:
        card structure
    :type card: struct spider_net_card \*

    :param chain:
        address of chain
    :type chain: struct spider_net_descr_chain \*

.. _`spider_net_init_chain`:

spider_net_init_chain
=====================

.. c:function:: int spider_net_init_chain(struct spider_net_card *card, struct spider_net_descr_chain *chain)

    alloc and link descriptor chain

    :param card:
        card structure
    :type card: struct spider_net_card \*

    :param chain:
        address of chain
    :type chain: struct spider_net_descr_chain \*

.. _`spider_net_init_chain.description`:

Description
-----------

We manage a circular list that mirrors the hardware structure,
except that the hardware uses bus addresses.

Returns 0 on success, <0 on failure

.. _`spider_net_free_rx_chain_contents`:

spider_net_free_rx_chain_contents
=================================

.. c:function:: void spider_net_free_rx_chain_contents(struct spider_net_card *card)

    frees descr contents in rx chain

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_free_rx_chain_contents.description`:

Description
-----------

returns 0 on success, <0 on failure

.. _`spider_net_prepare_rx_descr`:

spider_net_prepare_rx_descr
===========================

.. c:function:: int spider_net_prepare_rx_descr(struct spider_net_card *card, struct spider_net_descr *descr)

    Reinitialize RX descriptor

    :param card:
        card structure
    :type card: struct spider_net_card \*

    :param descr:
        descriptor to re-init
    :type descr: struct spider_net_descr \*

.. _`spider_net_prepare_rx_descr.description`:

Description
-----------

Return 0 on success, <0 on failure.

Allocates a new rx skb, iommu-maps it and attaches it to the
descriptor. Mark the descriptor as activated, ready-to-use.

.. _`spider_net_enable_rxchtails`:

spider_net_enable_rxchtails
===========================

.. c:function:: void spider_net_enable_rxchtails(struct spider_net_card *card)

    sets RX dmac chain tail addresses

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_enable_rxchtails.description`:

Description
-----------

spider_net_enable_rxchtails sets the RX DMAC chain tail addresses in the
chip by writing to the appropriate register. DMA is enabled in
spider_net_enable_rxdmac.

.. _`spider_net_enable_rxdmac`:

spider_net_enable_rxdmac
========================

.. c:function:: void spider_net_enable_rxdmac(struct spider_net_card *card)

    enables a receive DMA controller

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_enable_rxdmac.description`:

Description
-----------

spider_net_enable_rxdmac enables the DMA controller by setting RX_DMA_EN
in the GDADMACCNTR register

.. _`spider_net_disable_rxdmac`:

spider_net_disable_rxdmac
=========================

.. c:function:: void spider_net_disable_rxdmac(struct spider_net_card *card)

    disables the receive DMA controller

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_disable_rxdmac.description`:

Description
-----------

spider_net_disable_rxdmac terminates processing on the DMA controller
by turing off the DMA controller, with the force-end flag set.

.. _`spider_net_refill_rx_chain`:

spider_net_refill_rx_chain
==========================

.. c:function:: void spider_net_refill_rx_chain(struct spider_net_card *card)

    refills descriptors/skbs in the rx chains

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_refill_rx_chain.refills-descriptors-in-the-rx-chain`:

refills descriptors in the rx chain
-----------------------------------

allocates skbs and iommu-maps them.

.. _`spider_net_alloc_rx_skbs`:

spider_net_alloc_rx_skbs
========================

.. c:function:: int spider_net_alloc_rx_skbs(struct spider_net_card *card)

    Allocates rx skbs in rx descriptor chains

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_alloc_rx_skbs.description`:

Description
-----------

Returns 0 on success, <0 on failure.

.. _`spider_net_get_multicast_hash`:

spider_net_get_multicast_hash
=============================

.. c:function:: u8 spider_net_get_multicast_hash(struct net_device *netdev, __u8 *addr)

    generates hash for multicast filter table

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param addr:
        multicast address
    :type addr: __u8 \*

.. _`spider_net_get_multicast_hash.description`:

Description
-----------

returns the hash value.

spider_net_get_multicast_hash calculates a hash value for a given multicast
address, that is used to set the multicast filter tables

.. _`spider_net_set_multi`:

spider_net_set_multi
====================

.. c:function:: void spider_net_set_multi(struct net_device *netdev)

    sets multicast addresses and promisc flags

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`spider_net_set_multi.description`:

Description
-----------

spider_net_set_multi configures multicast addresses as needed for the
netdev interface. It also sets up multicast, allmulti and promisc
flags appropriately

.. _`spider_net_prepare_tx_descr`:

spider_net_prepare_tx_descr
===========================

.. c:function:: int spider_net_prepare_tx_descr(struct spider_net_card *card, struct sk_buff *skb)

    fill tx descriptor with skb data

    :param card:
        card structure
    :type card: struct spider_net_card \*

    :param skb:
        packet to use
    :type skb: struct sk_buff \*

.. _`spider_net_prepare_tx_descr.description`:

Description
-----------

returns 0 on success, <0 on failure.

fills out the descriptor structure with skb data and len. Copies data,
if needed (32bit DMA!)

.. _`spider_net_release_tx_chain`:

spider_net_release_tx_chain
===========================

.. c:function:: int spider_net_release_tx_chain(struct spider_net_card *card, int brutal)

    processes sent tx descriptors

    :param card:
        adapter structure
    :type card: struct spider_net_card \*

    :param brutal:
        if set, don't care about whether descriptor seems to be in use
    :type brutal: int

.. _`spider_net_release_tx_chain.description`:

Description
-----------

returns 0 if the tx ring is empty, otherwise 1.

spider_net_release_tx_chain releases the tx descriptors that spider has
finished with (if non-brutal) or simply release tx descriptors (if brutal).
If some other context is calling this function, we return 1 so that we're
scheduled again (if we were scheduled) and will not lose initiative.

.. _`spider_net_kick_tx_dma`:

spider_net_kick_tx_dma
======================

.. c:function:: void spider_net_kick_tx_dma(struct spider_net_card *card)

    enables TX DMA processing

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_kick_tx_dma.description`:

Description
-----------

This routine will start the transmit DMA running if
it is not already running. This routine ned only be
called when queueing a new packet to an empty tx queue.
Writes the current tx chain head as start address
of the tx descriptor chain and enables the transmission
DMA engine.

.. _`spider_net_xmit`:

spider_net_xmit
===============

.. c:function:: netdev_tx_t spider_net_xmit(struct sk_buff *skb, struct net_device *netdev)

    transmits a frame over the device

    :param skb:
        packet to send out
    :type skb: struct sk_buff \*

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`spider_net_xmit.description`:

Description
-----------

returns NETDEV_TX_OK on success, NETDEV_TX_BUSY on failure

.. _`spider_net_cleanup_tx_ring`:

spider_net_cleanup_tx_ring
==========================

.. c:function:: void spider_net_cleanup_tx_ring(struct timer_list *t)

    cleans up the TX ring

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`spider_net_cleanup_tx_ring.description`:

Description
-----------

spider_net_cleanup_tx_ring is called by either the tx_timer
or from the NAPI polling routine.
This routine releases resources associted with transmitted
packets, including updating the queue tail pointer.

.. _`spider_net_do_ioctl`:

spider_net_do_ioctl
===================

.. c:function:: int spider_net_do_ioctl(struct net_device *netdev, struct ifreq *ifr, int cmd)

    called for device ioctls

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

    :param ifr:
        request parameter structure for ioctl
    :type ifr: struct ifreq \*

    :param cmd:
        command code for ioctl
    :type cmd: int

.. _`spider_net_do_ioctl.description`:

Description
-----------

returns 0 on success, <0 on failure. Currently, we have no special ioctls.
-EOPNOTSUPP is returned, if an unknown ioctl was requested

.. _`spider_net_pass_skb_up`:

spider_net_pass_skb_up
======================

.. c:function:: void spider_net_pass_skb_up(struct spider_net_descr *descr, struct spider_net_card *card)

    takes an skb from a descriptor and passes it on

    :param descr:
        descriptor to process
    :type descr: struct spider_net_descr \*

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_pass_skb_up.description`:

Description
-----------

Fills out skb structure and passes the data to the stack.
The descriptor state is not changed.

.. _`spider_net_resync_head_ptr`:

spider_net_resync_head_ptr
==========================

.. c:function:: void spider_net_resync_head_ptr(struct spider_net_card *card)

    Advance head ptr past empty descrs

    :param card:
        *undescribed*
    :type card: struct spider_net_card \*

.. _`spider_net_resync_head_ptr.description`:

Description
-----------

If the driver fails to keep up and empty the queue, then the
hardware wil run out of room to put incoming packets. This
will cause the hardware to skip descrs that are full (instead
of halting/retrying). Thus, once the driver runs, it wil need
to "catch up" to where the hardware chain pointer is at.

.. _`spider_net_decode_one_descr`:

spider_net_decode_one_descr
===========================

.. c:function:: int spider_net_decode_one_descr(struct spider_net_card *card)

    processes an RX descriptor

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_decode_one_descr.description`:

Description
-----------

Returns 1 if a packet has been sent to the stack, otherwise 0.

Processes an RX descriptor by iommu-unmapping the data buffer
and passing the packet up to the stack. This function is called
in softirq context, e.g. either bottom half from interrupt or
NAPI polling context.

.. _`spider_net_poll`:

spider_net_poll
===============

.. c:function:: int spider_net_poll(struct napi_struct *napi, int budget)

    NAPI poll function called by the stack to return packets

    :param napi:
        *undescribed*
    :type napi: struct napi_struct \*

    :param budget:
        number of packets we can pass to the stack at most
    :type budget: int

.. _`spider_net_poll.description`:

Description
-----------

returns 0 if no more packets available to the driver/stack. Returns 1,
if the quota is exceeded, but the driver has still packets.

spider_net_poll returns all packets from the rx descriptors to the stack
(using netif_receive_skb). If all/enough packets are up, the driver
reenables interrupts and returns 0. If not, 1 is returned.

.. _`spider_net_set_mac`:

spider_net_set_mac
==================

.. c:function:: int spider_net_set_mac(struct net_device *netdev, void *p)

    sets the MAC of an interface

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

    :param p:
        *undescribed*
    :type p: void \*

.. _`spider_net_set_mac.description`:

Description
-----------

Returns 0 on success, <0 on failure. Currently, we don't support this
and will always return EOPNOTSUPP.

.. _`spider_net_link_reset`:

spider_net_link_reset
=====================

.. c:function:: void spider_net_link_reset(struct net_device *netdev)

    :param netdev:
        net device structure
    :type netdev: struct net_device \*

.. _`spider_net_link_reset.description`:

Description
-----------

This is called when the PHY_LINK signal is asserted. For the blade this is
not connected so we should never get here.

.. _`spider_net_handle_error_irq`:

spider_net_handle_error_irq
===========================

.. c:function:: void spider_net_handle_error_irq(struct spider_net_card *card, u32 status_reg, u32 error_reg1, u32 error_reg2)

    handles errors raised by an interrupt

    :param card:
        card structure
    :type card: struct spider_net_card \*

    :param status_reg:
        interrupt status register 0 (GHIINT0STS)
    :type status_reg: u32

    :param error_reg1:
        *undescribed*
    :type error_reg1: u32

    :param error_reg2:
        *undescribed*
    :type error_reg2: u32

.. _`spider_net_handle_error_irq.description`:

Description
-----------

spider_net_handle_error_irq treats or ignores all error conditions
found when an interrupt is presented

.. _`spider_net_interrupt`:

spider_net_interrupt
====================

.. c:function:: irqreturn_t spider_net_interrupt(int irq, void *ptr)

    interrupt handler for spider_net

    :param irq:
        interrupt number
    :type irq: int

    :param ptr:
        pointer to net_device
    :type ptr: void \*

.. _`spider_net_interrupt.description`:

Description
-----------

returns IRQ_HANDLED, if interrupt was for driver, or IRQ_NONE, if no
interrupt found raised by card.

This is the interrupt handler, that turns off
interrupts for this device and makes the stack poll the driver

.. _`spider_net_poll_controller`:

spider_net_poll_controller
==========================

.. c:function:: void spider_net_poll_controller(struct net_device *netdev)

    artificial interrupt for netconsole etc.

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`spider_net_poll_controller.description`:

Description
-----------

see Documentation/networking/netconsole.txt

.. _`spider_net_enable_interrupts`:

spider_net_enable_interrupts
============================

.. c:function:: void spider_net_enable_interrupts(struct spider_net_card *card)

    enable interrupts

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_enable_interrupts.description`:

Description
-----------

spider_net_enable_interrupt enables several interrupts

.. _`spider_net_disable_interrupts`:

spider_net_disable_interrupts
=============================

.. c:function:: void spider_net_disable_interrupts(struct spider_net_card *card)

    disable interrupts

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_disable_interrupts.description`:

Description
-----------

spider_net_disable_interrupts disables all the interrupts

.. _`spider_net_init_card`:

spider_net_init_card
====================

.. c:function:: void spider_net_init_card(struct spider_net_card *card)

    initializes the card

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_init_card.description`:

Description
-----------

spider_net_init_card initializes the card so that other registers can
be used

.. _`spider_net_enable_card`:

spider_net_enable_card
======================

.. c:function:: void spider_net_enable_card(struct spider_net_card *card)

    enables the card by setting all kinds of regs

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_enable_card.description`:

Description
-----------

spider_net_enable_card sets a lot of SMMIO registers to enable the device

.. _`spider_net_download_firmware`:

spider_net_download_firmware
============================

.. c:function:: int spider_net_download_firmware(struct spider_net_card *card, const void *firmware_ptr)

    loads firmware into the adapter

    :param card:
        card structure
    :type card: struct spider_net_card \*

    :param firmware_ptr:
        pointer to firmware data
    :type firmware_ptr: const void \*

.. _`spider_net_download_firmware.description`:

Description
-----------

spider_net_download_firmware loads the firmware data into the
adapter. It assumes the length etc. to be allright.

.. _`spider_net_init_firmware`:

spider_net_init_firmware
========================

.. c:function:: int spider_net_init_firmware(struct spider_net_card *card)

    reads in firmware parts

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_init_firmware.description`:

Description
-----------

Returns 0 on success, <0 on failure

spider_net_init_firmware opens the sequencer firmware and does some basic
checks. This function opens and releases the firmware structure. A call
to download the firmware is performed before the release.

Firmware format
===============
spider_fw.bin is expected to be a file containing 6\*1024\*4 bytes, 4k being
the program for each sequencer. Use the command
tail -q -n +2 Seq_code1_0x088.txt Seq_code2_0x090.txt              \
Seq_code3_0x098.txt Seq_code4_0x0A0.txt Seq_code5_0x0A8.txt   \
Seq_code6_0x0B0.txt \| xxd -r -p -c4 > spider_fw.bin

to generate spider_fw.bin, if you have sequencer programs with something

.. _`spider_net_init_firmware.like-the-following-contents-for-each-sequencer`:

like the following contents for each sequencer
----------------------------------------------

<ONE LINE COMMENT>
<FIRST 4-BYTES-WORD FOR SEQUENCER>
<SECOND 4-BYTES-WORD FOR SEQUENCER>
...
<1024th 4-BYTES-WORD FOR SEQUENCER>

.. _`spider_net_open`:

spider_net_open
===============

.. c:function:: int spider_net_open(struct net_device *netdev)

    called upon ifonfig up

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`spider_net_open.description`:

Description
-----------

returns 0 on success, <0 on failure

spider_net_open allocates all the descriptors and memory needed for
operation, sets up multicast list and enables interrupts

.. _`spider_net_link_phy`:

spider_net_link_phy
===================

.. c:function:: void spider_net_link_phy(struct timer_list *t)

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`spider_net_setup_phy`:

spider_net_setup_phy
====================

.. c:function:: int spider_net_setup_phy(struct spider_net_card *card)

    setup PHY

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_setup_phy.description`:

Description
-----------

returns 0 on success, <0 on failure

spider_net_setup_phy is used as part of spider_net_probe.

.. _`spider_net_workaround_rxramfull`:

spider_net_workaround_rxramfull
===============================

.. c:function:: void spider_net_workaround_rxramfull(struct spider_net_card *card)

    work around firmware bug

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_workaround_rxramfull.description`:

Description
-----------

no return value

.. _`spider_net_stop`:

spider_net_stop
===============

.. c:function:: int spider_net_stop(struct net_device *netdev)

    called upon ifconfig down

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`spider_net_stop.description`:

Description
-----------

always returns 0

.. _`spider_net_tx_timeout_task`:

spider_net_tx_timeout_task
==========================

.. c:function:: void spider_net_tx_timeout_task(struct work_struct *work)

    task scheduled by the watchdog timeout function (to be called not under interrupt status)

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`spider_net_tx_timeout_task.description`:

Description
-----------

called as task when tx hangs, resets interface (if interface is up)

.. _`spider_net_tx_timeout`:

spider_net_tx_timeout
=====================

.. c:function:: void spider_net_tx_timeout(struct net_device *netdev)

    called when the tx timeout watchdog kicks in.

    :param netdev:
        interface device structure
    :type netdev: struct net_device \*

.. _`spider_net_tx_timeout.description`:

Description
-----------

called, if tx hangs. Schedules a task that resets the interface

.. _`spider_net_setup_netdev_ops`:

spider_net_setup_netdev_ops
===========================

.. c:function:: void spider_net_setup_netdev_ops(struct net_device *netdev)

    initialization of net_device operations

    :param netdev:
        net_device structure
    :type netdev: struct net_device \*

.. _`spider_net_setup_netdev_ops.description`:

Description
-----------

fills out function pointers in the net_device structure

.. _`spider_net_setup_netdev`:

spider_net_setup_netdev
=======================

.. c:function:: int spider_net_setup_netdev(struct spider_net_card *card)

    initialization of net_device

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_setup_netdev.description`:

Description
-----------

Returns 0 on success or <0 on failure

spider_net_setup_netdev initializes the net_device structure

.. _`spider_net_alloc_card`:

spider_net_alloc_card
=====================

.. c:function:: struct spider_net_card *spider_net_alloc_card( void)

    allocates net_device and card structure

    :param void:
        no arguments
    :type void: 

.. _`spider_net_alloc_card.description`:

Description
-----------

returns the card structure or NULL in case of errors

the card and net_device structures are linked to each other

.. _`spider_net_undo_pci_setup`:

spider_net_undo_pci_setup
=========================

.. c:function:: void spider_net_undo_pci_setup(struct spider_net_card *card)

    releases PCI ressources

    :param card:
        card structure
    :type card: struct spider_net_card \*

.. _`spider_net_undo_pci_setup.description`:

Description
-----------

spider_net_undo_pci_setup releases the mapped regions

.. _`spider_net_setup_pci_dev`:

spider_net_setup_pci_dev
========================

.. c:function:: struct spider_net_card *spider_net_setup_pci_dev(struct pci_dev *pdev)

    sets up the device in terms of PCI operations

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

.. _`spider_net_setup_pci_dev.description`:

Description
-----------

Returns the card structure or NULL if any errors occur

spider_net_setup_pci_dev initializes pdev and together with the
functions called in spider_net_open configures the device so that
data can be transferred over it
The net_device structure is attached to the card structure, if the
function returns without error.

.. _`spider_net_probe`:

spider_net_probe
================

.. c:function:: int spider_net_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    initialization of a device

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param ent:
        entry in the device id list
    :type ent: const struct pci_device_id \*

.. _`spider_net_probe.description`:

Description
-----------

Returns 0 on success, <0 on failure

spider_net_probe initializes pdev and registers a net_device
structure for it. After that, the device can be ifconfig'ed up

.. _`spider_net_remove`:

spider_net_remove
=================

.. c:function:: void spider_net_remove(struct pci_dev *pdev)

    removal of a device

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

.. _`spider_net_remove.description`:

Description
-----------

Returns 0 on success, <0 on failure

spider_net_remove is called to remove the device and unregisters the
net_device

.. _`spider_net_init`:

spider_net_init
===============

.. c:function:: int spider_net_init( void)

    init function when the driver is loaded

    :param void:
        no arguments
    :type void: 

.. _`spider_net_init.description`:

Description
-----------

spider_net_init registers the device driver

.. _`spider_net_cleanup`:

spider_net_cleanup
==================

.. c:function:: void __exit spider_net_cleanup( void)

    exit function when driver is unloaded

    :param void:
        no arguments
    :type void: 

.. _`spider_net_cleanup.description`:

Description
-----------

spider_net_cleanup unregisters the device driver

.. This file was automatic generated / don't edit.

