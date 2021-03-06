.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_netdev.c

.. _`fm10k_setup_tx_resources`:

fm10k_setup_tx_resources
========================

.. c:function:: int fm10k_setup_tx_resources(struct fm10k_ring *tx_ring)

    allocate Tx resources (Descriptors)

    :param tx_ring:
        tx descriptor ring (for a specific queue) to setup
    :type tx_ring: struct fm10k_ring \*

.. _`fm10k_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`fm10k_setup_all_tx_resources`:

fm10k_setup_all_tx_resources
============================

.. c:function:: int fm10k_setup_all_tx_resources(struct fm10k_intfc *interface)

    allocate all queues Tx resources

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_setup_all_tx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`fm10k_setup_rx_resources`:

fm10k_setup_rx_resources
========================

.. c:function:: int fm10k_setup_rx_resources(struct fm10k_ring *rx_ring)

    allocate Rx resources (Descriptors)

    :param rx_ring:
        rx descriptor ring (for a specific queue) to setup
    :type rx_ring: struct fm10k_ring \*

.. _`fm10k_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`fm10k_setup_all_rx_resources`:

fm10k_setup_all_rx_resources
============================

.. c:function:: int fm10k_setup_all_rx_resources(struct fm10k_intfc *interface)

    allocate all queues Rx resources

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_setup_all_rx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`fm10k_clean_tx_ring`:

fm10k_clean_tx_ring
===================

.. c:function:: void fm10k_clean_tx_ring(struct fm10k_ring *tx_ring)

    Free Tx Buffers

    :param tx_ring:
        ring to be cleaned
    :type tx_ring: struct fm10k_ring \*

.. _`fm10k_free_tx_resources`:

fm10k_free_tx_resources
=======================

.. c:function:: void fm10k_free_tx_resources(struct fm10k_ring *tx_ring)

    Free Tx Resources per Queue

    :param tx_ring:
        Tx descriptor ring for a specific queue
    :type tx_ring: struct fm10k_ring \*

.. _`fm10k_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`fm10k_clean_all_tx_rings`:

fm10k_clean_all_tx_rings
========================

.. c:function:: void fm10k_clean_all_tx_rings(struct fm10k_intfc *interface)

    Free Tx Buffers for all queues

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_free_all_tx_resources`:

fm10k_free_all_tx_resources
===========================

.. c:function:: void fm10k_free_all_tx_resources(struct fm10k_intfc *interface)

    Free Tx Resources for All Queues

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_free_all_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`fm10k_clean_rx_ring`:

fm10k_clean_rx_ring
===================

.. c:function:: void fm10k_clean_rx_ring(struct fm10k_ring *rx_ring)

    Free Rx Buffers per Queue

    :param rx_ring:
        ring to free buffers from
    :type rx_ring: struct fm10k_ring \*

.. _`fm10k_free_rx_resources`:

fm10k_free_rx_resources
=======================

.. c:function:: void fm10k_free_rx_resources(struct fm10k_ring *rx_ring)

    Free Rx Resources

    :param rx_ring:
        ring to clean the resources from
    :type rx_ring: struct fm10k_ring \*

.. _`fm10k_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`fm10k_clean_all_rx_rings`:

fm10k_clean_all_rx_rings
========================

.. c:function:: void fm10k_clean_all_rx_rings(struct fm10k_intfc *interface)

    Free Rx Buffers for all queues

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_free_all_rx_resources`:

fm10k_free_all_rx_resources
===========================

.. c:function:: void fm10k_free_all_rx_resources(struct fm10k_intfc *interface)

    Free Rx Resources for All Queues

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_free_all_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`fm10k_request_glort_range`:

fm10k_request_glort_range
=========================

.. c:function:: void fm10k_request_glort_range(struct fm10k_intfc *interface)

    Request GLORTs for use in configuring rules

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_request_glort_range.description`:

Description
-----------

This function allocates a range of glorts for this interface to use.

.. _`fm10k_free_udp_port_info`:

fm10k_free_udp_port_info
========================

.. c:function:: void fm10k_free_udp_port_info(struct fm10k_intfc *interface)

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_free_udp_port_info.description`:

Description
-----------

This function frees both geneve_port and vxlan_port structures

.. _`fm10k_restore_udp_port_info`:

fm10k_restore_udp_port_info
===========================

.. c:function:: void fm10k_restore_udp_port_info(struct fm10k_intfc *interface)

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_restore_udp_port_info.description`:

Description
-----------

This function restores the value in the tunnel_cfg register(s) after reset

.. _`fm10k_udp_tunnel_add`:

fm10k_udp_tunnel_add
====================

.. c:function:: void fm10k_udp_tunnel_add(struct net_device *dev, struct udp_tunnel_info *ti)

    :param dev:
        network interface device structure
    :type dev: struct net_device \*

    :param ti:
        Tunnel endpoint information
    :type ti: struct udp_tunnel_info \*

.. _`fm10k_udp_tunnel_add.description`:

Description
-----------

This function is called when a new UDP tunnel port has been added.
Due to hardware restrictions, only one port per type can be offloaded at
once.

.. _`fm10k_udp_tunnel_del`:

fm10k_udp_tunnel_del
====================

.. c:function:: void fm10k_udp_tunnel_del(struct net_device *dev, struct udp_tunnel_info *ti)

    :param dev:
        network interface device structure
    :type dev: struct net_device \*

    :param ti:
        Tunnel end point information
    :type ti: struct udp_tunnel_info \*

.. _`fm10k_udp_tunnel_del.description`:

Description
-----------

This function is called when a new UDP tunnel port is deleted. The freed
port will be removed from the list, then we reprogram the offloaded port
based on the head of the list.

.. _`fm10k_open`:

fm10k_open
==========

.. c:function:: int fm10k_open(struct net_device *netdev)

    Called when a network interface is made active

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`fm10k_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`fm10k_close`:

fm10k_close
===========

.. c:function:: int fm10k_close(struct net_device *netdev)

    Disables a network interface

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`fm10k_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`fm10k_tx_timeout`:

fm10k_tx_timeout
================

.. c:function:: void fm10k_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`fm10k_host_mbx_ready`:

fm10k_host_mbx_ready
====================

.. c:function:: bool fm10k_host_mbx_ready(struct fm10k_intfc *interface)

    Check PF interface's mailbox readiness

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_host_mbx_ready.description`:

Description
-----------

This function checks if the PF interface's mailbox is ready before queueing
mailbox messages for transmission. This will prevent filling the TX mailbox
queue when the receiver is not ready. VF interfaces are exempt from this
check since it will block all PF-VF mailbox messages from being sent from
the VF to the PF at initialization.

.. _`fm10k_queue_vlan_request`:

fm10k_queue_vlan_request
========================

.. c:function:: int fm10k_queue_vlan_request(struct fm10k_intfc *interface, u32 vid, u8 vsi, bool set)

    Queue a VLAN update request

    :param interface:
        the fm10k interface structure
    :type interface: struct fm10k_intfc \*

    :param vid:
        the VLAN vid
    :type vid: u32

    :param vsi:
        VSI index number
    :type vsi: u8

    :param set:
        whether to set or clear
    :type set: bool

.. _`fm10k_queue_vlan_request.description`:

Description
-----------

This function queues up a VLAN update. For VFs, this must be sent to the
managing PF over the mailbox. For PFs, we'll use the same handling so that
it's similar to the VF. This avoids storming the PF<->VF mailbox with too
many VLAN updates during reset.

.. _`fm10k_queue_mac_request`:

fm10k_queue_mac_request
=======================

.. c:function:: int fm10k_queue_mac_request(struct fm10k_intfc *interface, u16 glort, const unsigned char *addr, u16 vid, bool set)

    Queue a MAC update request

    :param interface:
        the fm10k interface structure
    :type interface: struct fm10k_intfc \*

    :param glort:
        the target glort for this update
    :type glort: u16

    :param addr:
        the address to update
    :type addr: const unsigned char \*

    :param vid:
        the vid to update
    :type vid: u16

    :param set:
        whether to add or remove
    :type set: bool

.. _`fm10k_queue_mac_request.description`:

Description
-----------

This function queues up a MAC request for sending to the switch manager.
A separate thread monitors the queue and sends updates to the switch
manager. Return 0 on success, and negative error code on failure.

.. _`fm10k_clear_macvlan_queue`:

fm10k_clear_macvlan_queue
=========================

.. c:function:: void fm10k_clear_macvlan_queue(struct fm10k_intfc *interface, u16 glort, bool vlans)

    Cancel pending updates for a given glort

    :param interface:
        the fm10k interface structure
    :type interface: struct fm10k_intfc \*

    :param glort:
        the target glort to clear
    :type glort: u16

    :param vlans:
        true to clear VLAN messages, false to ignore them
    :type vlans: bool

.. _`fm10k_clear_macvlan_queue.description`:

Description
-----------

Cancel any outstanding MAC/VLAN requests for a given glort. This is
expected to be called when a logical port goes down.

.. _`fm10k_get_stats64`:

fm10k_get_stats64
=================

.. c:function:: void fm10k_get_stats64(struct net_device *netdev, struct rtnl_link_stats64 *stats)

    Get System Network Statistics

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param stats:
        storage space for 64bit statistics
    :type stats: struct rtnl_link_stats64 \*

.. _`fm10k_get_stats64.description`:

Description
-----------

Obtain 64bit statistics in a way that is safe for both 32bit and 64bit
architectures.

.. This file was automatic generated / don't edit.

