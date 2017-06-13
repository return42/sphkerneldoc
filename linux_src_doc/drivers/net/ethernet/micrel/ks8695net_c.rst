.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/micrel/ks8695net.c

.. _`rx_ring_desc`:

struct rx_ring_desc
===================

.. c:type:: struct rx_ring_desc

    Receive descriptor ring element

.. _`rx_ring_desc.definition`:

Definition
----------

.. code-block:: c

    struct rx_ring_desc {
        __le32 status;
        __le32 length;
        __le32 data_ptr;
        __le32 next_desc;
    }

.. _`rx_ring_desc.members`:

Members
-------

status
    The status of the descriptor element (E.g. who owns it)

length
    The number of bytes in the block pointed to by data_ptr

data_ptr
    The physical address of the data block to receive into

next_desc
    The physical address of the next descriptor element.

.. _`tx_ring_desc`:

struct tx_ring_desc
===================

.. c:type:: struct tx_ring_desc

    Transmit descriptor ring element

.. _`tx_ring_desc.definition`:

Definition
----------

.. code-block:: c

    struct tx_ring_desc {
        __le32 owner;
        __le32 status;
        __le32 data_ptr;
        __le32 next_desc;
    }

.. _`tx_ring_desc.members`:

Members
-------

owner
    Who owns the descriptor

status
    The number of bytes in the block pointed to by data_ptr

data_ptr
    The physical address of the data block to receive into

next_desc
    The physical address of the next descriptor element.

.. _`ks8695_skbuff`:

struct ks8695_skbuff
====================

.. c:type:: struct ks8695_skbuff

    sk_buff wrapper for rx/tx rings.

.. _`ks8695_skbuff.definition`:

Definition
----------

.. code-block:: c

    struct ks8695_skbuff {
        struct sk_buff *skb;
        dma_addr_t dma_ptr;
        u32 length;
    }

.. _`ks8695_skbuff.members`:

Members
-------

skb
    The buffer in the ring

dma_ptr
    The mapped DMA pointer of the buffer

length
    The number of bytes mapped to dma_ptr

.. _`ks8695_dtype`:

enum ks8695_dtype
=================

.. c:type:: enum ks8695_dtype

    Device type

.. _`ks8695_dtype.definition`:

Definition
----------

.. code-block:: c

    enum ks8695_dtype {
        KS8695_DTYPE_WAN,
        KS8695_DTYPE_LAN,
        KS8695_DTYPE_HPNA
    };

.. _`ks8695_dtype.constants`:

Constants
---------

KS8695_DTYPE_WAN
    This device is a WAN interface

KS8695_DTYPE_LAN
    This device is a LAN interface

KS8695_DTYPE_HPNA
    This device is an HPNA interface

.. _`ks8695_priv`:

struct ks8695_priv
==================

.. c:type:: struct ks8695_priv

    Private data for the KS8695 Ethernet

.. _`ks8695_priv.definition`:

Definition
----------

.. code-block:: c

    struct ks8695_priv {
        int in_suspend;
        struct net_device *ndev;
        struct device *dev;
        enum ks8695_dtype dtype;
        void __iomem *io_regs;
        struct napi_struct napi;
        const char *rx_irq_name;
        const char * *tx_irq_name;
        const char * * *link_irq_name;
        int rx_irq;
        int tx_irq;
        int link_irq;
        struct resource *regs_req;
        struct resource * *phyiface_req;
        void __iomem *phyiface_regs;
        void *ring_base;
        dma_addr_t ring_base_dma;
        struct tx_ring_desc *tx_ring;
        int tx_ring_used;
        int tx_ring_next_slot;
        dma_addr_t tx_ring_dma;
        struct ks8695_skbuff tx_buffers[MAX_TX_DESC];
        spinlock_t txq_lock;
        struct rx_ring_desc *rx_ring;
        dma_addr_t rx_ring_dma;
        struct ks8695_skbuff rx_buffers[MAX_RX_DESC];
        int next_rx_desc_read;
        spinlock_t rx_lock;
        int msg_enable;
    }

.. _`ks8695_priv.members`:

Members
-------

in_suspend
    Flag to indicate if we're suspending/resuming

ndev
    The net_device for this interface

dev
    The platform device object for this interface

dtype
    The type of this device

io_regs
    The ioremapped registers for this interface

napi
    Add support NAPI for Rx

rx_irq_name
    The textual name of the RX IRQ from the platform data

tx_irq_name
    The textual name of the TX IRQ from the platform data

link_irq_name
    The textual name of the link IRQ from the
    platform data if available

rx_irq
    The IRQ number for the RX IRQ

tx_irq
    The IRQ number for the TX IRQ

link_irq
    The IRQ number for the link IRQ if available

regs_req
    The resource request for the registers region

phyiface_req
    The resource request for the phy/switch region
    if available

phyiface_regs
    The ioremapped registers for the phy/switch if available

ring_base
    The base pointer of the dma coherent memory for the rings

ring_base_dma
    The DMA mapped equivalent of ring_base

tx_ring
    The pointer in ring_base of the TX ring

tx_ring_used
    The number of slots in the TX ring which are occupied

tx_ring_next_slot
    The next slot to fill in the TX ring

tx_ring_dma
    The DMA mapped equivalent of tx_ring

tx_buffers
    The sk_buff mappings for the TX ring

txq_lock
    A lock to protect the tx_buffers tx_ring_used etc variables

rx_ring
    The pointer in ring_base of the RX ring

rx_ring_dma
    The DMA mapped equivalent of rx_ring

rx_buffers
    The sk_buff mappings for the RX ring

next_rx_desc_read
    The next RX descriptor to read from on IRQ

rx_lock
    A lock to protect Rx irq function

msg_enable
    The flags for which messages to emit

.. _`ks8695_readreg`:

ks8695_readreg
==============

.. c:function:: u32 ks8695_readreg(struct ks8695_priv *ksp, int reg)

    Read from a KS8695 ethernet register

    :param struct ks8695_priv \*ksp:
        The device to read from

    :param int reg:
        The register to read

.. _`ks8695_writereg`:

ks8695_writereg
===============

.. c:function:: void ks8695_writereg(struct ks8695_priv *ksp, int reg, u32 value)

    Write to a KS8695 ethernet register

    :param struct ks8695_priv \*ksp:
        The device to write to

    :param int reg:
        The register to write

    :param u32 value:
        The value to write to the register

.. _`ks8695_port_type`:

ks8695_port_type
================

.. c:function:: const char *ks8695_port_type(struct ks8695_priv *ksp)

    Retrieve port-type as user-friendly string

    :param struct ks8695_priv \*ksp:
        The device to return the type for

.. _`ks8695_port_type.description`:

Description
-----------

Returns a string indicating which of the WAN, LAN or HPNA
ports this device is likely to represent.

.. _`ks8695_update_mac`:

ks8695_update_mac
=================

.. c:function:: void ks8695_update_mac(struct ks8695_priv *ksp)

    Update the MAC registers in the device

    :param struct ks8695_priv \*ksp:
        The device to update

.. _`ks8695_update_mac.description`:

Description
-----------

Updates the MAC registers in the KS8695 device from the address in the
net_device structure associated with this interface.

.. _`ks8695_refill_rxbuffers`:

ks8695_refill_rxbuffers
=======================

.. c:function:: void ks8695_refill_rxbuffers(struct ks8695_priv *ksp)

    Re-fill the RX buffer ring

    :param struct ks8695_priv \*ksp:
        The device to refill

.. _`ks8695_refill_rxbuffers.description`:

Description
-----------

Iterates the RX ring of the device looking for empty slots.
For each empty slot, we allocate and map a new SKB and give it
to the hardware.
This can be called from interrupt context safely.

.. _`ks8695_init_partial_multicast`:

ks8695_init_partial_multicast
=============================

.. c:function:: void ks8695_init_partial_multicast(struct ks8695_priv *ksp, struct net_device *ndev)

    Init the mcast addr registers

    :param struct ks8695_priv \*ksp:
        The device to initialise

    :param struct net_device \*ndev:
        *undescribed*

.. _`ks8695_init_partial_multicast.description`:

Description
-----------

This routine is a helper for ks8695_set_multicast - it writes
the additional-address registers in the KS8695 ethernet device
and cleans up any others left behind.

.. _`ks8695_tx_irq`:

ks8695_tx_irq
=============

.. c:function:: irqreturn_t ks8695_tx_irq(int irq, void *dev_id)

    Transmit IRQ handler

    :param int irq:
        The IRQ which went off (ignored)

    :param void \*dev_id:
        The net_device for the interrupt

.. _`ks8695_tx_irq.description`:

Description
-----------

Process the TX ring, clearing out any transmitted slots.
Allows the net_device to pass us new packets once slots are
freed.

.. _`ks8695_get_rx_enable_bit`:

ks8695_get_rx_enable_bit
========================

.. c:function:: u32 ks8695_get_rx_enable_bit(struct ks8695_priv *ksp)

    Get rx interrupt enable/status bit

    :param struct ks8695_priv \*ksp:
        Private data for the KS8695 Ethernet

.. _`ks8695_get_rx_enable_bit.for-ks8695-document`:

For KS8695 document
-------------------

Interrupt Enable Register (offset 0xE204)
Bit29 : WAN MAC Receive Interrupt Enable
Bit16 : LAN MAC Receive Interrupt Enable
Interrupt Status Register (Offset 0xF208)

.. _`ks8695_get_rx_enable_bit.bit29`:

Bit29
-----

WAN MAC Receive Status

.. _`ks8695_get_rx_enable_bit.bit16`:

Bit16
-----

LAN MAC Receive Status
So, this Rx interrupt enable/status bit number is equal
as Rx IRQ number.

.. _`ks8695_rx_irq`:

ks8695_rx_irq
=============

.. c:function:: irqreturn_t ks8695_rx_irq(int irq, void *dev_id)

    Receive IRQ handler

    :param int irq:
        The IRQ which went off (ignored)

    :param void \*dev_id:
        The net_device for the interrupt

.. _`ks8695_rx_irq.description`:

Description
-----------

Inform NAPI that packet reception needs to be scheduled

.. _`ks8695_rx`:

ks8695_rx
=========

.. c:function:: int ks8695_rx(struct ks8695_priv *ksp, int budget)

    Receive packets called by NAPI poll method

    :param struct ks8695_priv \*ksp:
        Private data for the KS8695 Ethernet

    :param int budget:
        Number of packets allowed to process

.. _`ks8695_poll`:

ks8695_poll
===========

.. c:function:: int ks8695_poll(struct napi_struct *napi, int budget)

    Receive packet by NAPI poll method

    :param struct napi_struct \*napi:
        *undescribed*

    :param int budget:
        The remaining number packets for network subsystem

.. _`ks8695_poll.description`:

Description
-----------

Invoked by the network core when it requests for new
packets from the driver

.. _`ks8695_link_irq`:

ks8695_link_irq
===============

.. c:function:: irqreturn_t ks8695_link_irq(int irq, void *dev_id)

    Link change IRQ handler

    :param int irq:
        The IRQ which went off (ignored)

    :param void \*dev_id:
        The net_device for the interrupt

.. _`ks8695_link_irq.description`:

Description
-----------

The WAN interface can generate an IRQ when the link changes,
report this to the net layer and the user.

.. _`ks8695_reset`:

ks8695_reset
============

.. c:function:: void ks8695_reset(struct ks8695_priv *ksp)

    Reset a KS8695 ethernet interface

    :param struct ks8695_priv \*ksp:
        The interface to reset

.. _`ks8695_reset.description`:

Description
-----------

Perform an engine reset of the interface and re-program it
with sensible defaults.

.. _`ks8695_shutdown`:

ks8695_shutdown
===============

.. c:function:: void ks8695_shutdown(struct ks8695_priv *ksp)

    Shut down a KS8695 ethernet interface

    :param struct ks8695_priv \*ksp:
        The interface to shut down

.. _`ks8695_shutdown.description`:

Description
-----------

This disables packet RX/TX, cleans up IRQs, drains the rings,
and basically places the interface into a clean shutdown
state.

.. _`ks8695_setup_irq`:

ks8695_setup_irq
================

.. c:function:: int ks8695_setup_irq(int irq, const char *irq_name, irq_handler_t handler, struct net_device *ndev)

    IRQ setup helper function

    :param int irq:
        The IRQ number to claim

    :param const char \*irq_name:
        The name to give the IRQ claimant

    :param irq_handler_t handler:
        The function to call to handle the IRQ

    :param struct net_device \*ndev:
        The net_device to pass in as the dev_id argument to the handler

.. _`ks8695_setup_irq.description`:

Description
-----------

Return 0 on success.

.. _`ks8695_init_net`:

ks8695_init_net
===============

.. c:function:: int ks8695_init_net(struct ks8695_priv *ksp)

    Initialise a KS8695 ethernet interface

    :param struct ks8695_priv \*ksp:
        The interface to initialise

.. _`ks8695_init_net.description`:

Description
-----------

This routine fills the RX ring, initialises the DMA engines,
allocates the IRQs and then starts the packet TX and RX
engines.

.. _`ks8695_release_device`:

ks8695_release_device
=====================

.. c:function:: void ks8695_release_device(struct ks8695_priv *ksp)

    HW resource release for KS8695 e-net

    :param struct ks8695_priv \*ksp:
        The device to be freed

.. _`ks8695_release_device.description`:

Description
-----------

This unallocates io memory regions, dma-coherent regions etc
which were allocated in ks8695_probe.

.. _`ks8695_get_msglevel`:

ks8695_get_msglevel
===================

.. c:function:: u32 ks8695_get_msglevel(struct net_device *ndev)

    Get the messages enabled for emission

    :param struct net_device \*ndev:
        The network device to read from

.. _`ks8695_set_msglevel`:

ks8695_set_msglevel
===================

.. c:function:: void ks8695_set_msglevel(struct net_device *ndev, u32 value)

    Set the messages enabled for emission

    :param struct net_device \*ndev:
        The network device to configure

    :param u32 value:
        The messages to set for emission

.. _`ks8695_wan_get_link_ksettings`:

ks8695_wan_get_link_ksettings
=============================

.. c:function:: int ks8695_wan_get_link_ksettings(struct net_device *ndev, struct ethtool_link_ksettings *cmd)

    Get device-specific settings.

    :param struct net_device \*ndev:
        The network device to read settings from

    :param struct ethtool_link_ksettings \*cmd:
        The ethtool structure to read into

.. _`ks8695_wan_set_link_ksettings`:

ks8695_wan_set_link_ksettings
=============================

.. c:function:: int ks8695_wan_set_link_ksettings(struct net_device *ndev, const struct ethtool_link_ksettings *cmd)

    Set device-specific settings.

    :param struct net_device \*ndev:
        The network device to configure

    :param const struct ethtool_link_ksettings \*cmd:
        The settings to configure

.. _`ks8695_wan_nwayreset`:

ks8695_wan_nwayreset
====================

.. c:function:: int ks8695_wan_nwayreset(struct net_device *ndev)

    Restart the autonegotiation on the port.

    :param struct net_device \*ndev:
        The network device to restart autoneotiation on

.. _`ks8695_wan_get_pause`:

ks8695_wan_get_pause
====================

.. c:function:: void ks8695_wan_get_pause(struct net_device *ndev, struct ethtool_pauseparam *param)

    Retrieve network pause/flow-control advertising

    :param struct net_device \*ndev:
        The device to retrieve settings from

    :param struct ethtool_pauseparam \*param:
        The structure to fill out with the information

.. _`ks8695_get_drvinfo`:

ks8695_get_drvinfo
==================

.. c:function:: void ks8695_get_drvinfo(struct net_device *ndev, struct ethtool_drvinfo *info)

    Retrieve driver information

    :param struct net_device \*ndev:
        The network device to retrieve info about

    :param struct ethtool_drvinfo \*info:
        The info structure to fill out.

.. _`ks8695_set_mac`:

ks8695_set_mac
==============

.. c:function:: int ks8695_set_mac(struct net_device *ndev, void *addr)

    Update MAC in net dev and HW

    :param struct net_device \*ndev:
        The network device to update

    :param void \*addr:
        The new MAC address to set

.. _`ks8695_set_multicast`:

ks8695_set_multicast
====================

.. c:function:: void ks8695_set_multicast(struct net_device *ndev)

    Set up the multicast behaviour of the interface

    :param struct net_device \*ndev:
        The net_device to configure

.. _`ks8695_set_multicast.description`:

Description
-----------

This routine, called by the net layer, configures promiscuity
and multicast reception behaviour for the interface.

.. _`ks8695_timeout`:

ks8695_timeout
==============

.. c:function:: void ks8695_timeout(struct net_device *ndev)

    Handle a network tx/rx timeout.

    :param struct net_device \*ndev:
        The net_device which timed out.

.. _`ks8695_timeout.description`:

Description
-----------

A network transaction timed out, reset the device.

.. _`ks8695_start_xmit`:

ks8695_start_xmit
=================

.. c:function:: int ks8695_start_xmit(struct sk_buff *skb, struct net_device *ndev)

    Start a packet transmission

    :param struct sk_buff \*skb:
        The packet to transmit

    :param struct net_device \*ndev:
        The network device to send the packet on

.. _`ks8695_start_xmit.description`:

Description
-----------

This routine, called by the net layer, takes ownership of the
sk_buff and adds it to the TX ring. It then kicks the TX DMA
engine to ensure transmission begins.

.. _`ks8695_stop`:

ks8695_stop
===========

.. c:function:: int ks8695_stop(struct net_device *ndev)

    Stop (shutdown) a KS8695 ethernet interface

    :param struct net_device \*ndev:
        The net_device to stop

.. _`ks8695_stop.description`:

Description
-----------

This disables the TX queue and cleans up a KS8695 ethernet
device.

.. _`ks8695_open`:

ks8695_open
===========

.. c:function:: int ks8695_open(struct net_device *ndev)

    Open (bring up) a KS8695 ethernet interface

    :param struct net_device \*ndev:
        The net_device to open

.. _`ks8695_open.description`:

Description
-----------

This resets, configures the MAC, initialises the RX ring and
DMA engines and starts the TX queue for a KS8695 ethernet
device.

.. _`ks8695_init_switch`:

ks8695_init_switch
==================

.. c:function:: void ks8695_init_switch(struct ks8695_priv *ksp)

    Init LAN switch to known good defaults.

    :param struct ks8695_priv \*ksp:
        The device to initialise

.. _`ks8695_init_switch.description`:

Description
-----------

This initialises the LAN switch in the KS8695 to a known-good
set of defaults.

.. _`ks8695_init_wan_phy`:

ks8695_init_wan_phy
===================

.. c:function:: void ks8695_init_wan_phy(struct ks8695_priv *ksp)

    Initialise the WAN PHY to sensible defaults

    :param struct ks8695_priv \*ksp:
        The device to initialise

.. _`ks8695_init_wan_phy.description`:

Description
-----------

This initialises a KS8695's WAN phy to sensible values for
autonegotiation etc.

.. _`ks8695_probe`:

ks8695_probe
============

.. c:function:: int ks8695_probe(struct platform_device *pdev)

    Probe and initialise a KS8695 ethernet interface

    :param struct platform_device \*pdev:
        The platform device to probe

.. _`ks8695_probe.description`:

Description
-----------

Initialise a KS8695 ethernet device from platform data.

This driver requires at least one IORESOURCE_MEM for the
registers and two IORESOURCE_IRQ for the RX and TX IRQs
respectively. It can optionally take an additional
IORESOURCE_MEM for the switch or phy in the case of the lan or
wan ports, and an IORESOURCE_IRQ for the link IRQ for the wan
port.

.. _`ks8695_drv_suspend`:

ks8695_drv_suspend
==================

.. c:function:: int ks8695_drv_suspend(struct platform_device *pdev, pm_message_t state)

    Suspend a KS8695 ethernet platform device.

    :param struct platform_device \*pdev:
        The device to suspend

    :param pm_message_t state:
        The suspend state

.. _`ks8695_drv_suspend.description`:

Description
-----------

This routine detaches and shuts down a KS8695 ethernet device.

.. _`ks8695_drv_resume`:

ks8695_drv_resume
=================

.. c:function:: int ks8695_drv_resume(struct platform_device *pdev)

    Resume a KS8695 ethernet platform device.

    :param struct platform_device \*pdev:
        The device to resume

.. _`ks8695_drv_resume.description`:

Description
-----------

This routine re-initialises and re-attaches a KS8695 ethernet
device.

.. _`ks8695_drv_remove`:

ks8695_drv_remove
=================

.. c:function:: int ks8695_drv_remove(struct platform_device *pdev)

    Remove a KS8695 net device on driver unload.

    :param struct platform_device \*pdev:
        The platform device to remove

.. _`ks8695_drv_remove.description`:

Description
-----------

This unregisters and releases a KS8695 ethernet device.

.. This file was automatic generated / don't edit.

