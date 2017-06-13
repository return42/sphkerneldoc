.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/neterion/vxge/vxge-main.c

.. _`vxge_xmit`:

vxge_xmit
=========

.. c:function:: netdev_tx_t vxge_xmit(struct sk_buff *skb, struct net_device *dev)

    :param struct sk_buff \*skb:
        the socket buffer containing the Tx data.

    :param struct net_device \*dev:
        device pointer.

.. _`vxge_xmit.description`:

Description
-----------

This function is the Tx entry point of the driver. Neterion NIC supports
certain protocol assist features on Tx side, namely  CSO, S/G, LSO.

.. _`vxge_set_multicast`:

vxge_set_multicast
==================

.. c:function:: void vxge_set_multicast(struct net_device *dev)

    :param struct net_device \*dev:
        pointer to the device structure

.. _`vxge_set_multicast.description`:

Description
-----------

Entry point for multicast address enable/disable
This function is a driver entry point which gets called by the kernel
whenever multicast addresses must be enabled/disabled. This also gets
called to set/reset promiscuous mode. Depending on the deivce flag, we
determine, if multicast address must be enabled or if promiscuous mode
is to be disabled etc.

.. _`vxge_set_mac_addr`:

vxge_set_mac_addr
=================

.. c:function:: int vxge_set_mac_addr(struct net_device *dev, void *p)

    :param struct net_device \*dev:
        pointer to the device structure

    :param void \*p:
        *undescribed*

.. _`vxge_set_mac_addr.description`:

Description
-----------

Update entry "0" (default MAC addr)

.. _`vxge_poll_msix`:

vxge_poll_msix
==============

.. c:function:: int vxge_poll_msix(struct napi_struct *napi, int budget)

    Receive handler when Receive Polling is used.

    :param struct napi_struct \*napi:
        *undescribed*

    :param int budget:
        Number of packets budgeted to be processed in this iteration.

.. _`vxge_poll_msix.description`:

Description
-----------

This function comes into picture only if Receive side is being handled
through polling (called NAPI in linux). It mostly does what the normal
Rx interrupt handler does in terms of descriptor and packet processing
but not in an interrupt context. Also it will process a specified number
of packets at most in one iteration. This value is passed down by the
kernel as the function argument 'budget'.

.. _`vxge_netpoll`:

vxge_netpoll
============

.. c:function:: void vxge_netpoll(struct net_device *dev)

    netpoll event handler entry point

    :param struct net_device \*dev:
        pointer to the device structure.

.. _`vxge_netpoll.description`:

Description
-----------

This function will be called by upper layer to check for events on the
interface in situations where interrupts are disabled. It is used for
specific in-kernel networking tasks, such as remote consoles and kernel
debugging over the network (example netdump in RedHat).

.. _`adaptive_coalesce_tx_interrupts`:

adaptive_coalesce_tx_interrupts
===============================

.. c:function:: void adaptive_coalesce_tx_interrupts(struct vxge_fifo *fifo)

    Changes the interrupt coalescing if the interrupts are not within a range

    :param struct vxge_fifo \*fifo:
        pointer to transmit fifo structure

.. _`adaptive_coalesce_tx_interrupts.description`:

Description
-----------

The function changes boundary timer and restriction timer
value depends on the traffic

.. _`adaptive_coalesce_tx_interrupts.return-value`:

Return Value
------------

None

.. _`adaptive_coalesce_rx_interrupts`:

adaptive_coalesce_rx_interrupts
===============================

.. c:function:: void adaptive_coalesce_rx_interrupts(struct vxge_ring *ring)

    Changes the interrupt coalescing if the interrupts are not within a range

    :param struct vxge_ring \*ring:
        pointer to receive ring structure

.. _`adaptive_coalesce_rx_interrupts.description`:

Description
-----------

The function increases of decreases the packet counts within
the ranges of traffic utilization, if the interrupts due to this ring are
not within a fixed range.

.. _`adaptive_coalesce_rx_interrupts.return-value`:

Return Value
------------

Nothing

.. _`vxge_open`:

vxge_open
=========

.. c:function:: int vxge_open(struct net_device *dev)

    :param struct net_device \*dev:
        pointer to the device structure.

.. _`vxge_open.description`:

Description
-----------

This function is the open entry point of the driver. It mainly calls a
function to allocate Rx buffers and inserts them into the buffer
descriptors and then enables the Rx part of the NIC.

.. _`vxge_open.return-value`:

Return value
------------

'0' on success and an appropriate (-)ve integer as
defined in errno.h file on failure.

.. _`vxge_close`:

vxge_close
==========

.. c:function:: int vxge_close(struct net_device *dev)

    :param struct net_device \*dev:
        device pointer.

.. _`vxge_close.description`:

Description
-----------

This is the stop entry point of the driver. It needs to undo exactly
whatever was done by the open entry point, thus it's usually referred to
as the close function.Among other things this function mainly stops the
Rx side of the NIC and frees all the Rx buffers in the Rx rings.

.. _`vxge_close.return-value`:

Return value
------------

'0' on success and an appropriate (-)ve integer as
defined in errno.h file on failure.

.. _`vxge_change_mtu`:

vxge_change_mtu
===============

.. c:function:: int vxge_change_mtu(struct net_device *dev, int new_mtu)

    :param struct net_device \*dev:
        net device pointer.

    :param int new_mtu:
        the new MTU size for the device.

.. _`vxge_change_mtu.description`:

Description
-----------

A driver entry point to change MTU size for the device. Before changing
the MTU the device must be stopped.

.. _`vxge_get_stats64`:

vxge_get_stats64
================

.. c:function:: void vxge_get_stats64(struct net_device *dev, struct rtnl_link_stats64 *net_stats)

    :param struct net_device \*dev:
        pointer to the device structure

    :param struct rtnl_link_stats64 \*net_stats:
        *undescribed*

.. _`vxge_ioctl`:

vxge_ioctl
==========

.. c:function:: int vxge_ioctl(struct net_device *dev, struct ifreq *rq, int cmd)

    :param struct net_device \*dev:
        Device pointer.

    :param struct ifreq \*rq:
        *undescribed*

    :param int cmd:
        This is used to distinguish between the different commands that
        can be passed to the IOCTL functions.

.. _`vxge_ioctl.description`:

Description
-----------

Entry point for the Ioctl.

.. _`vxge_tx_watchdog`:

vxge_tx_watchdog
================

.. c:function:: void vxge_tx_watchdog(struct net_device *dev)

    :param struct net_device \*dev:
        pointer to net device structure

.. _`vxge_tx_watchdog.description`:

Description
-----------

Watchdog for transmit side.
This function is triggered if the Tx Queue is stopped
for a pre-defined amount of time when the Interface is still up.

.. _`vxge_vlan_rx_add_vid`:

vxge_vlan_rx_add_vid
====================

.. c:function:: int vxge_vlan_rx_add_vid(struct net_device *dev, __be16 proto, u16 vid)

    :param struct net_device \*dev:
        net device pointer.

    :param __be16 proto:
        vlan protocol

    :param u16 vid:
        vid

.. _`vxge_vlan_rx_add_vid.description`:

Description
-----------

Add the vlan id to the devices vlan id table

.. _`vxge_vlan_rx_kill_vid`:

vxge_vlan_rx_kill_vid
=====================

.. c:function:: int vxge_vlan_rx_kill_vid(struct net_device *dev, __be16 proto, u16 vid)

    :param struct net_device \*dev:
        net device pointer.

    :param __be16 proto:
        vlan protocol

    :param u16 vid:
        vid

.. _`vxge_vlan_rx_kill_vid.description`:

Description
-----------

Remove the vlan id from the device's vlan id table

.. _`vxge_pm_suspend`:

vxge_pm_suspend
===============

.. c:function:: int vxge_pm_suspend(struct pci_dev *pdev, pm_message_t state)

    vxge power management suspend entry point

    :param struct pci_dev \*pdev:
        *undescribed*

    :param pm_message_t state:
        *undescribed*

.. _`vxge_pm_resume`:

vxge_pm_resume
==============

.. c:function:: int vxge_pm_resume(struct pci_dev *pdev)

    vxge power management resume entry point

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`vxge_io_error_detected`:

vxge_io_error_detected
======================

.. c:function:: pci_ers_result_t vxge_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        Pointer to PCI device

    :param pci_channel_state_t state:
        The current pci connection state

.. _`vxge_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`vxge_io_slot_reset`:

vxge_io_slot_reset
==================

.. c:function:: pci_ers_result_t vxge_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`vxge_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot.
At this point, the card has exprienced a hard reset,
followed by fixups by BIOS, and has its config space
set up identically to what it was at cold boot.

.. _`vxge_io_resume`:

vxge_io_resume
==============

.. c:function:: void vxge_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`vxge_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells
us that its OK to resume normal operation.

.. _`vxge_probe`:

vxge_probe
==========

.. c:function:: int vxge_probe(struct pci_dev *pdev, const struct pci_device_id *pre)

    :param struct pci_dev \*pdev:
        structure containing the PCI related information of the device.

    :param const struct pci_device_id \*pre:
        List of PCI devices supported by the driver listed in vxge_id_table.

.. _`vxge_probe.description`:

Description
-----------

This function is called when a new PCI device gets detected and initializes
it.

.. _`vxge_probe.return-value`:

Return value
------------

returns 0 on success and negative on failure.

.. _`vxge_remove`:

vxge_remove
===========

.. c:function:: void vxge_remove(struct pci_dev *pdev)

    Free the PCI device

    :param struct pci_dev \*pdev:
        structure containing the PCI related information of the device.

.. _`vxge_remove.description`:

Description
-----------

This function is called by the Pci subsystem to release a
PCI device and free up all resource held up by the device.

.. This file was automatic generated / don't edit.

