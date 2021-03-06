.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/tehuti/tehuti.c

.. _`bdx_fifo_init`:

bdx_fifo_init
=============

.. c:function:: int bdx_fifo_init(struct bdx_priv *priv, struct fifo *f, int fsz_type, u16 reg_CFG0, u16 reg_CFG1, u16 reg_RPTR, u16 reg_WPTR)

    create TX/RX descriptor fifo for host-NIC communication.

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

    :param f:
        fifo to initialize
    :type f: struct fifo \*

    :param fsz_type:
        fifo size type: 0-4KB, 1-8KB, 2-16KB, 3-32KB
    :type fsz_type: int

    :param reg_CFG0:
        *undescribed*
    :type reg_CFG0: u16

    :param reg_CFG1:
        *undescribed*
    :type reg_CFG1: u16

    :param reg_RPTR:
        *undescribed*
    :type reg_RPTR: u16

    :param reg_WPTR:
        *undescribed*
    :type reg_WPTR: u16

.. _`bdx_fifo_init.description`:

Description
-----------

1K extra space is allocated at the end of the fifo to simplify
processing of descriptors that wraps around fifo's end

Returns 0 on success, negative value on failure

.. _`bdx_fifo_free`:

bdx_fifo_free
=============

.. c:function:: void bdx_fifo_free(struct bdx_priv *priv, struct fifo *f)

    free all resources used by fifo

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

    :param f:
        fifo to release
    :type f: struct fifo \*

.. _`bdx_link_changed`:

bdx_link_changed
================

.. c:function:: void bdx_link_changed(struct bdx_priv *priv)

    notifies OS about hw link state.

    :param priv:
        hw adapter structure
    :type priv: struct bdx_priv \*

.. _`bdx_isr_napi`:

bdx_isr_napi
============

.. c:function:: irqreturn_t bdx_isr_napi(int irq, void *dev)

    Interrupt Service Routine for Bordeaux NIC

    :param irq:
        interrupt number
    :type irq: int

    :param dev:
        network device
    :type dev: void \*

.. _`bdx_isr_napi.description`:

Description
-----------

Return IRQ_NONE if it was not our interrupt, IRQ_HANDLED - otherwise

It reads ISR register to know interrupt reasons, and proceed them one by one.

.. _`bdx_isr_napi.reasons-of-interest-are`:

Reasons of interest are
-----------------------

RX_DESC - new packet has arrived and RXD fifo holds its descriptor
RX_FREE - number of free Rx buffers in RXF fifo gets low
TX_FREE - packet was transmited and RXF fifo holds its descriptor

.. _`bdx_fw_load`:

bdx_fw_load
===========

.. c:function:: int bdx_fw_load(struct bdx_priv *priv)

    loads firmware to NIC

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

.. _`bdx_fw_load.description`:

Description
-----------

Firmware is loaded via TXD fifo, so it must be initialized first.
Firware must be loaded once per NIC not per PCI device provided by NIC (NIC
can have few of them). So all drivers use semaphore register to choose one
that will actually load FW to NIC.

.. _`bdx_hw_start`:

bdx_hw_start
============

.. c:function:: int bdx_hw_start(struct bdx_priv *priv)

    inits registers and starts HW's Rx and Tx engines

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

.. _`bdx_close`:

bdx_close
=========

.. c:function:: int bdx_close(struct net_device *ndev)

    Disables a network interface

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

.. _`bdx_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`bdx_open`:

bdx_open
========

.. c:function:: int bdx_open(struct net_device *ndev)

    Called when a network interface is made active

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

.. _`bdx_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`__bdx_vlan_rx_vid`:

\__bdx_vlan_rx_vid
==================

.. c:function:: void __bdx_vlan_rx_vid(struct net_device *ndev, uint16_t vid, int enable)

    private helper for adding/killing VLAN vid

    :param ndev:
        network device
    :type ndev: struct net_device \*

    :param vid:
        VLAN vid
    :type vid: uint16_t

    :param enable:
        *undescribed*
    :type enable: int

.. _`__bdx_vlan_rx_vid.description`:

Description
-----------

Passes VLAN filter table to hardware

.. _`bdx_vlan_rx_add_vid`:

bdx_vlan_rx_add_vid
===================

.. c:function:: int bdx_vlan_rx_add_vid(struct net_device *ndev, __be16 proto, u16 vid)

    kernel hook for adding VLAN vid to hw filtering table

    :param ndev:
        network device
    :type ndev: struct net_device \*

    :param proto:
        *undescribed*
    :type proto: __be16

    :param vid:
        VLAN vid to add
    :type vid: u16

.. _`bdx_vlan_rx_kill_vid`:

bdx_vlan_rx_kill_vid
====================

.. c:function:: int bdx_vlan_rx_kill_vid(struct net_device *ndev, __be16 proto, u16 vid)

    kernel hook for killing VLAN vid in hw filtering table

    :param ndev:
        network device
    :type ndev: struct net_device \*

    :param proto:
        *undescribed*
    :type proto: __be16

    :param vid:
        VLAN vid to kill
    :type vid: u16

.. _`bdx_change_mtu`:

bdx_change_mtu
==============

.. c:function:: int bdx_change_mtu(struct net_device *ndev, int new_mtu)

    Change the Maximum Transfer Unit

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

    :param new_mtu:
        new value for maximum frame size
    :type new_mtu: int

.. _`bdx_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`bdx_rx_init`:

bdx_rx_init
===========

.. c:function:: int bdx_rx_init(struct bdx_priv *priv)

    initialize RX all related HW and SW resources

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

.. _`bdx_rx_init.description`:

Description
-----------

Returns 0 on success, negative value on failure

It creates rxf and rxd fifos, update relevant HW registers, preallocate
skb for rx. It assumes that Rx is desabled in HW
funcs are grouped for better cache usage

RxD fifo is smaller than RxF fifo by design. Upon high load, RxD will be
filled and packets will be dropped by nic without getting into host or
cousing interrupt. Anyway, in that condition, host has no chance to process
all packets, but dropping in nic is cheaper, since it takes 0 cpu cycles

.. _`bdx_rx_free_skbs`:

bdx_rx_free_skbs
================

.. c:function:: void bdx_rx_free_skbs(struct bdx_priv *priv, struct rxf_fifo *f)

    frees and unmaps all skbs allocated for the fifo

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

    :param f:
        RXF fifo
    :type f: struct rxf_fifo \*

.. _`bdx_rx_free`:

bdx_rx_free
===========

.. c:function:: void bdx_rx_free(struct bdx_priv *priv)

    release all Rx resources

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

.. _`bdx_rx_free.description`:

Description
-----------

It assumes that Rx is desabled in HW

.. _`bdx_rx_alloc_skbs`:

bdx_rx_alloc_skbs
=================

.. c:function:: void bdx_rx_alloc_skbs(struct bdx_priv *priv, struct rxf_fifo *f)

    fill rxf fifo with new skbs

    :param priv:
        nic's private structure
    :type priv: struct bdx_priv \*

    :param f:
        RXF fifo that needs skbs
    :type f: struct rxf_fifo \*

.. _`bdx_rx_alloc_skbs.description`:

Description
-----------

It allocates skbs, build rxf descs and push it (rxf descr) into rxf fifo.
skb's virtual and physical addresses are stored in skb db.
To calculate free space, func uses cached values of RPTR and WPTR
When needed, it also updates RPTR and WPTR.

.. _`bdx_rx_receive`:

bdx_rx_receive
==============

.. c:function:: int bdx_rx_receive(struct bdx_priv *priv, struct rxd_fifo *f, int budget)

    receives full packets from RXD fifo and pass them to OS

    :param priv:
        nic's private structure
    :type priv: struct bdx_priv \*

    :param f:
        RXF fifo that needs skbs
    :type f: struct rxd_fifo \*

    :param budget:
        maximum number of packets to receive
    :type budget: int

.. _`bdx_rx_receive.note`:

NOTE
----

a special treatment is given to non-continuous descriptors
that start near the end, wraps around and continue at the beginning. a second
part is copied right after the first, and then descriptor is interpreted as
normal. fifo has an extra space to allow such operations

.. _`__bdx_tx_db_ptr_next`:

\__bdx_tx_db_ptr_next
=====================

.. c:function:: void __bdx_tx_db_ptr_next(struct txdb *db, struct tx_map **pptr)

    helper function, increment read/write pointer + wrap

    :param db:
        tx data base
    :type db: struct txdb \*

    :param pptr:
        read or write pointer
    :type pptr: struct tx_map \*\*

.. _`bdx_tx_db_inc_rptr`:

bdx_tx_db_inc_rptr
==================

.. c:function:: void bdx_tx_db_inc_rptr(struct txdb *db)

    increment read pointer

    :param db:
        tx data base
    :type db: struct txdb \*

.. _`bdx_tx_db_inc_wptr`:

bdx_tx_db_inc_wptr
==================

.. c:function:: void bdx_tx_db_inc_wptr(struct txdb *db)

    increment write pointer

    :param db:
        tx data base
    :type db: struct txdb \*

.. _`bdx_tx_db_init`:

bdx_tx_db_init
==============

.. c:function:: int bdx_tx_db_init(struct txdb *d, int sz_type)

    creates and initializes tx db

    :param d:
        tx data base
    :type d: struct txdb \*

    :param sz_type:
        size of tx fifo
    :type sz_type: int

.. _`bdx_tx_db_init.description`:

Description
-----------

Returns 0 on success, error code otherwise

.. _`bdx_tx_db_close`:

bdx_tx_db_close
===============

.. c:function:: void bdx_tx_db_close(struct txdb *d)

    closes tx db and frees all memory

    :param d:
        tx data base
    :type d: struct txdb \*

.. _`bdx_tx_map_skb`:

bdx_tx_map_skb
==============

.. c:function:: void bdx_tx_map_skb(struct bdx_priv *priv, struct sk_buff *skb, struct txd_desc *txdd)

    creates and stores dma mappings for skb's data blocks

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

    :param skb:
        socket buffer to map
    :type skb: struct sk_buff \*

    :param txdd:
        TX descriptor to use
    :type txdd: struct txd_desc \*

.. _`bdx_tx_map_skb.description`:

Description
-----------

It makes dma mappings for skb's data blocks and writes them to PBL of
new tx descriptor. It also stores them in the tx db, so they could be
unmaped after data was sent. It is reponsibility of a caller to make
sure that there is enough space in the tx db. Last element holds pointer
to skb itself and marked with zero length

.. _`bdx_tx_space`:

bdx_tx_space
============

.. c:function:: int bdx_tx_space(struct bdx_priv *priv)

    calculates available space in TX fifo

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

.. _`bdx_tx_space.description`:

Description
-----------

Returns available space in TX fifo in bytes

.. _`bdx_tx_transmit`:

bdx_tx_transmit
===============

.. c:function:: netdev_tx_t bdx_tx_transmit(struct sk_buff *skb, struct net_device *ndev)

    send packet to NIC

    :param skb:
        packet to send
    :type skb: struct sk_buff \*

    :param ndev:
        network device assigned to NIC
    :type ndev: struct net_device \*

.. _`bdx_tx_transmit.return-codes`:

Return codes
------------

o NETDEV_TX_OK everything ok.
o NETDEV_TX_BUSY Cannot transmit packet, try later
Usually a bug, means queue start/stop flow control is broken in
the driver. Note: the driver must NOT put the skb in its DMA ring.

.. _`bdx_tx_cleanup`:

bdx_tx_cleanup
==============

.. c:function:: void bdx_tx_cleanup(struct bdx_priv *priv)

    clean TXF fifo, run in the context of IRQ.

    :param priv:
        bdx adapter
    :type priv: struct bdx_priv \*

.. _`bdx_tx_cleanup.description`:

Description
-----------

It scans TXF fifo for descriptors, frees DMA mappings and reports to OS
that those packets were sent

.. _`bdx_tx_free_skbs`:

bdx_tx_free_skbs
================

.. c:function:: void bdx_tx_free_skbs(struct bdx_priv *priv)

    frees all skbs from TXD fifo. It gets called when OS stops this dev, eg upon "ifconfig down" or rmmod

    :param priv:
        *undescribed*
    :type priv: struct bdx_priv \*

.. _`bdx_tx_push_desc`:

bdx_tx_push_desc
================

.. c:function:: void bdx_tx_push_desc(struct bdx_priv *priv, void *data, int size)

    push descriptor to TxD fifo

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

    :param data:
        desc's data
    :type data: void \*

    :param size:
        desc's size
    :type size: int

.. _`bdx_tx_push_desc.description`:

Description
-----------

Pushes desc to TxD fifo and overlaps it if needed.

.. _`bdx_tx_push_desc.note`:

NOTE
----

this func does not check for available space. this is responsibility
of the caller. Neither does it check that data size is smaller than
fifo size.

.. _`bdx_tx_push_desc_safe`:

bdx_tx_push_desc_safe
=====================

.. c:function:: void bdx_tx_push_desc_safe(struct bdx_priv *priv, void *data, int size)

    push descriptor to TxD fifo in a safe way

    :param priv:
        NIC private structure
    :type priv: struct bdx_priv \*

    :param data:
        desc's data
    :type data: void \*

    :param size:
        desc's size
    :type size: int

.. _`bdx_tx_push_desc_safe.note`:

NOTE
----

this func does check for available space and, if necessary, waits for
NIC to read existing data before writing new one.

.. _`bdx_probe`:

bdx_probe
=========

.. c:function:: int bdx_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param ent:
        entry in bdx_pci_tbl
    :type ent: const struct pci_device_id \*

.. _`bdx_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

bdx_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

functions and their order used as explained in
/usr/src/linux/Documentation/DMA-{API,mapping}.txt

.. _`bdx_remove`:

bdx_remove
==========

.. c:function:: void bdx_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`bdx_remove.description`:

Description
-----------

bdx_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. This file was automatic generated / don't edit.

