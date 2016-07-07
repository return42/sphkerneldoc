.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_netdev.c

.. _`fm10k_setup_tx_resources`:

fm10k_setup_tx_resources
========================

.. c:function:: int fm10k_setup_tx_resources(struct fm10k_ring *tx_ring)

    allocate Tx resources (Descriptors)

    :param struct fm10k_ring \*tx_ring:
        tx descriptor ring (for a specific queue) to setup

.. _`fm10k_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`fm10k_setup_all_tx_resources`:

fm10k_setup_all_tx_resources
============================

.. c:function:: int fm10k_setup_all_tx_resources(struct fm10k_intfc *interface)

    allocate all queues Tx resources

    :param struct fm10k_intfc \*interface:
        board private structure

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

    :param struct fm10k_ring \*rx_ring:
        rx descriptor ring (for a specific queue) to setup

.. _`fm10k_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`fm10k_setup_all_rx_resources`:

fm10k_setup_all_rx_resources
============================

.. c:function:: int fm10k_setup_all_rx_resources(struct fm10k_intfc *interface)

    allocate all queues Rx resources

    :param struct fm10k_intfc \*interface:
        board private structure

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

    :param struct fm10k_ring \*tx_ring:
        ring to be cleaned

.. _`fm10k_free_tx_resources`:

fm10k_free_tx_resources
=======================

.. c:function:: void fm10k_free_tx_resources(struct fm10k_ring *tx_ring)

    Free Tx Resources per Queue

    :param struct fm10k_ring \*tx_ring:
        Tx descriptor ring for a specific queue

.. _`fm10k_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`fm10k_clean_all_tx_rings`:

fm10k_clean_all_tx_rings
========================

.. c:function:: void fm10k_clean_all_tx_rings(struct fm10k_intfc *interface)

    Free Tx Buffers for all queues

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_free_all_tx_resources`:

fm10k_free_all_tx_resources
===========================

.. c:function:: void fm10k_free_all_tx_resources(struct fm10k_intfc *interface)

    Free Tx Resources for All Queues

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_free_all_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`fm10k_clean_rx_ring`:

fm10k_clean_rx_ring
===================

.. c:function:: void fm10k_clean_rx_ring(struct fm10k_ring *rx_ring)

    Free Rx Buffers per Queue

    :param struct fm10k_ring \*rx_ring:
        ring to free buffers from

.. _`fm10k_free_rx_resources`:

fm10k_free_rx_resources
=======================

.. c:function:: void fm10k_free_rx_resources(struct fm10k_ring *rx_ring)

    Free Rx Resources

    :param struct fm10k_ring \*rx_ring:
        ring to clean the resources from

.. _`fm10k_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`fm10k_clean_all_rx_rings`:

fm10k_clean_all_rx_rings
========================

.. c:function:: void fm10k_clean_all_rx_rings(struct fm10k_intfc *interface)

    Free Rx Buffers for all queues

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_free_all_rx_resources`:

fm10k_free_all_rx_resources
===========================

.. c:function:: void fm10k_free_all_rx_resources(struct fm10k_intfc *interface)

    Free Rx Resources for All Queues

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_free_all_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`fm10k_request_glort_range`:

fm10k_request_glort_range
=========================

.. c:function:: void fm10k_request_glort_range(struct fm10k_intfc *interface)

    Request GLORTs for use in configuring rules

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_request_glort_range.description`:

Description
-----------

This function allocates a range of glorts for this interface to use.

.. _`fm10k_del_vxlan_port_all`:

fm10k_del_vxlan_port_all
========================

.. c:function:: void fm10k_del_vxlan_port_all(struct fm10k_intfc *interface)

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_del_vxlan_port_all.description`:

Description
-----------

This function frees the entire vxlan_port list

.. _`fm10k_restore_vxlan_port`:

fm10k_restore_vxlan_port
========================

.. c:function:: void fm10k_restore_vxlan_port(struct fm10k_intfc *interface)

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_restore_vxlan_port.description`:

Description
-----------

This function restores the value in the tunnel_cfg register after reset

.. _`fm10k_add_vxlan_port`:

fm10k_add_vxlan_port
====================

.. c:function:: void fm10k_add_vxlan_port(struct net_device *dev, sa_family_t sa_family, __be16 port)

    :param struct net_device \*dev:
        *undescribed*

    :param sa_family_t sa_family:
        Address family of new port

    :param __be16 port:
        port number used for VXLAN

.. _`fm10k_add_vxlan_port.description`:

Description
-----------

This function is called when a new VXLAN interface has added a new port
number to the range that is currently in use for VXLAN.  The new port
number is always added to the tail so that the port number list should
match the order in which the ports were allocated.  The head of the list
is always used as the VXLAN port number for offloads.

.. _`fm10k_del_vxlan_port`:

fm10k_del_vxlan_port
====================

.. c:function:: void fm10k_del_vxlan_port(struct net_device *dev, sa_family_t sa_family, __be16 port)

    :param struct net_device \*dev:
        *undescribed*

    :param sa_family_t sa_family:
        Address family of freed port

    :param __be16 port:
        port number used for VXLAN

.. _`fm10k_del_vxlan_port.description`:

Description
-----------

This function is called when a new VXLAN interface has freed a port
number from the range that is currently in use for VXLAN.  The freed
port is removed from the list and the new head is used to determine
the port number for offloads.

.. _`fm10k_open`:

fm10k_open
==========

.. c:function:: int fm10k_open(struct net_device *netdev)

    Called when a network interface is made active

    :param struct net_device \*netdev:
        network interface device structure

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

    :param struct net_device \*netdev:
        network interface device structure

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

    :param struct net_device \*netdev:
        network interface device structure

.. _`fm10k_get_stats64`:

fm10k_get_stats64
=================

.. c:function:: struct rtnl_link_stats64 *fm10k_get_stats64(struct net_device *netdev, struct rtnl_link_stats64 *stats)

    Get System Network Statistics

    :param struct net_device \*netdev:
        network interface device structure

    :param struct rtnl_link_stats64 \*stats:
        storage space for 64bit statistics

.. _`fm10k_get_stats64.description`:

Description
-----------

Returns 64bit statistics, for use in the ndo_get_stats64 callback. This
function replaces fm10k_get_stats for kernels which support it.

.. This file was automatic generated / don't edit.

