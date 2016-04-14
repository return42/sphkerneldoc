.. -*- coding: utf-8; mode: rst -*-

=====
dev.c
=====

.. _`dev_add_pack`:

dev_add_pack
============

.. c:function:: void dev_add_pack (struct packet_type *pt)

    add packet handler

    :param struct packet_type \*pt:
        packet type declaration


.. _`dev_add_pack.description`:

Description
-----------

Add a protocol handler to the networking stack. The passed :c:type:`struct packet_type <packet_type>`
is linked into kernel lists and may not be freed until it has been
removed from the kernel lists.

This call does not sleep therefore it can not
guarantee all CPU's that are in middle of receiving packets
will see the new packet type (until the next received packet).


.. _`__dev_remove_pack`:

__dev_remove_pack
=================

.. c:function:: void __dev_remove_pack (struct packet_type *pt)

    remove packet handler

    :param struct packet_type \*pt:
        packet type declaration


.. _`__dev_remove_pack.description`:

Description
-----------

Remove a protocol handler that was previously added to the kernel
protocol handlers by :c:func:`dev_add_pack`. The passed :c:type:`struct packet_type <packet_type>` is removed
from the kernel lists and can be freed or reused once this function
returns.::

     The packet type might still be in use by receivers

and must not be freed until after all the CPU's have gone
through a quiescent state.


.. _`dev_remove_pack`:

dev_remove_pack
===============

.. c:function:: void dev_remove_pack (struct packet_type *pt)

    remove packet handler

    :param struct packet_type \*pt:
        packet type declaration


.. _`dev_remove_pack.description`:

Description
-----------

Remove a protocol handler that was previously added to the kernel
protocol handlers by :c:func:`dev_add_pack`. The passed :c:type:`struct packet_type <packet_type>` is removed
from the kernel lists and can be freed or reused once this function
returns.

This call sleeps to guarantee that no CPU is looking at the packet
type after return.


.. _`dev_add_offload`:

dev_add_offload
===============

.. c:function:: void dev_add_offload (struct packet_offload *po)

    register offload handlers

    :param struct packet_offload \*po:
        protocol offload declaration


.. _`dev_add_offload.description`:

Description
-----------

Add protocol offload handlers to the networking stack. The passed
:c:type:`struct proto_offload <proto_offload>` is linked into kernel lists and may not be freed until
it has been removed from the kernel lists.

This call does not sleep therefore it can not
guarantee all CPU's that are in middle of receiving packets
will see the new offload handlers (until the next received packet).


.. _`__dev_remove_offload`:

__dev_remove_offload
====================

.. c:function:: void __dev_remove_offload (struct packet_offload *po)

    remove offload handler

    :param struct packet_offload \*po:
        packet offload declaration


.. _`__dev_remove_offload.description`:

Description
-----------

Remove a protocol offload handler that was previously added to the
kernel offload handlers by :c:func:`dev_add_offload`. The passed :c:type:`struct offload_type <offload_type>`
is removed from the kernel lists and can be freed or reused once this
function returns.::

     The packet type might still be in use by receivers

and must not be freed until after all the CPU's have gone
through a quiescent state.


.. _`dev_remove_offload`:

dev_remove_offload
==================

.. c:function:: void dev_remove_offload (struct packet_offload *po)

    remove packet offload handler

    :param struct packet_offload \*po:
        packet offload declaration


.. _`dev_remove_offload.description`:

Description
-----------

Remove a packet offload handler that was previously added to the kernel
offload handlers by :c:func:`dev_add_offload`. The passed :c:type:`struct offload_type <offload_type>` is
removed from the kernel lists and can be freed or reused once this
function returns.

This call sleeps to guarantee that no CPU is looking at the packet
type after return.


.. _`netdev_boot_setup_add`:

netdev_boot_setup_add
=====================

.. c:function:: int netdev_boot_setup_add (char *name, struct ifmap *map)

    add new setup entry

    :param char \*name:
        name of the device

    :param struct ifmap \*map:
        configured settings for the device


.. _`netdev_boot_setup_add.description`:

Description
-----------

Adds new setup entry to the dev_boot_setup list.  The function
returns 0 on error and 1 on success.  This is a generic routine to
all netdevices.


.. _`netdev_boot_setup_check`:

netdev_boot_setup_check
=======================

.. c:function:: int netdev_boot_setup_check (struct net_device *dev)

    check boot time settings

    :param struct net_device \*dev:
        the netdevice


.. _`netdev_boot_setup_check.description`:

Description
-----------

Check boot time settings for the device.
The found settings are set for the device to be used
later in the device probing.
Returns 0 if no settings found, 1 if they are.


.. _`netdev_boot_base`:

netdev_boot_base
================

.. c:function:: unsigned long netdev_boot_base (const char *prefix, int unit)

    get address from boot time settings

    :param const char \*prefix:
        prefix for network device

    :param int unit:
        id for network device


.. _`netdev_boot_base.description`:

Description
-----------

Check boot time settings for the base address of device.
The found settings are set for the device to be used
later in the device probing.
Returns 0 if no settings found.


.. _`dev_get_iflink`:

dev_get_iflink
==============

.. c:function:: int dev_get_iflink (const struct net_device *dev)

    get 'iflink' value of a interface

    :param const struct net_device \*dev:
        targeted interface


.. _`dev_get_iflink.description`:

Description
-----------

Indicates the ifindex the interface is linked to.
Physical interfaces have the same 'ifindex' and 'iflink' values.


.. _`dev_fill_metadata_dst`:

dev_fill_metadata_dst
=====================

.. c:function:: int dev_fill_metadata_dst (struct net_device *dev, struct sk_buff *skb)

    Retrieve tunnel egress information.

    :param struct net_device \*dev:
        targeted interface

    :param struct sk_buff \*skb:
        The packet.


.. _`dev_fill_metadata_dst.description`:

Description
-----------

For better visibility of tunnel traffic OVS needs to retrieve
egress tunnel information for a packet. Following API allows
user to get this info.


.. _`__dev_get_by_name`:

__dev_get_by_name
=================

.. c:function:: struct net_device *__dev_get_by_name (struct net *net, const char *name)

    find a device by its name

    :param struct net \*net:
        the applicable net namespace

    :param const char \*name:
        name to find


.. _`__dev_get_by_name.description`:

Description
-----------

Find an interface by name. Must be called under RTNL semaphore
or ``dev_base_lock``\ . If the name is found a pointer to the device
is returned. If the name is not found then ``NULL`` is returned. The
reference counters are not incremented so the caller must be
careful with locks.


.. _`dev_get_by_name_rcu`:

dev_get_by_name_rcu
===================

.. c:function:: struct net_device *dev_get_by_name_rcu (struct net *net, const char *name)

    find a device by its name

    :param struct net \*net:
        the applicable net namespace

    :param const char \*name:
        name to find


.. _`dev_get_by_name_rcu.description`:

Description
-----------

Find an interface by name.
If the name is found a pointer to the device is returned.
If the name is not found then ``NULL`` is returned.
The reference counters are not incremented so the caller must be
careful with locks. The caller must hold RCU lock.


.. _`dev_get_by_name`:

dev_get_by_name
===============

.. c:function:: struct net_device *dev_get_by_name (struct net *net, const char *name)

    find a device by its name

    :param struct net \*net:
        the applicable net namespace

    :param const char \*name:
        name to find


.. _`dev_get_by_name.description`:

Description
-----------

Find an interface by name. This can be called from any
context and does its own locking. The returned handle has
the usage count incremented and the caller must use :c:func:`dev_put` to
release it when it is no longer needed. ``NULL`` is returned if no
matching device is found.


.. _`__dev_get_by_index`:

__dev_get_by_index
==================

.. c:function:: struct net_device *__dev_get_by_index (struct net *net, int ifindex)

    find a device by its ifindex

    :param struct net \*net:
        the applicable net namespace

    :param int ifindex:
        index of device


.. _`__dev_get_by_index.description`:

Description
-----------

Search for an interface by index. Returns ``NULL`` if the device
is not found or a pointer to the device. The device has not
had its reference counter increased so the caller must be careful
about locking. The caller must hold either the RTNL semaphore
or ``dev_base_lock``\ .


.. _`dev_get_by_index_rcu`:

dev_get_by_index_rcu
====================

.. c:function:: struct net_device *dev_get_by_index_rcu (struct net *net, int ifindex)

    find a device by its ifindex

    :param struct net \*net:
        the applicable net namespace

    :param int ifindex:
        index of device


.. _`dev_get_by_index_rcu.description`:

Description
-----------

Search for an interface by index. Returns ``NULL`` if the device
is not found or a pointer to the device. The device has not
had its reference counter increased so the caller must be careful
about locking. The caller must hold RCU lock.


.. _`dev_get_by_index`:

dev_get_by_index
================

.. c:function:: struct net_device *dev_get_by_index (struct net *net, int ifindex)

    find a device by its ifindex

    :param struct net \*net:
        the applicable net namespace

    :param int ifindex:
        index of device


.. _`dev_get_by_index.description`:

Description
-----------

Search for an interface by index. Returns NULL if the device
is not found or a pointer to the device. The device returned has
had a reference added and the pointer is safe until the user calls
dev_put to indicate they have finished with it.


.. _`netdev_get_name`:

netdev_get_name
===============

.. c:function:: int netdev_get_name (struct net *net, char *name, int ifindex)

    get a netdevice name, knowing its ifindex.

    :param struct net \*net:
        network namespace

    :param char \*name:
        a pointer to the buffer where the name will be stored.

    :param int ifindex:
        the ifindex of the interface to get the name from.


.. _`netdev_get_name.description`:

Description
-----------

The use of :c:func:`raw_seqcount_begin` and :c:func:`cond_resched` before
retrying is required as we want to give the writers a chance
to complete when CONFIG_PREEMPT is not set.


.. _`dev_getbyhwaddr_rcu`:

dev_getbyhwaddr_rcu
===================

.. c:function:: struct net_device *dev_getbyhwaddr_rcu (struct net *net, unsigned short type, const char *ha)

    find a device by its hardware address

    :param struct net \*net:
        the applicable net namespace

    :param unsigned short type:
        media type of device

    :param const char \*ha:
        hardware address


.. _`dev_getbyhwaddr_rcu.description`:

Description
-----------

Search for an interface by MAC address. Returns NULL if the device
is not found or a pointer to the device.
The caller must hold RCU or RTNL.
The returned device has not had its ref count increased
and the caller must therefore be careful about locking


.. _`__dev_get_by_flags`:

__dev_get_by_flags
==================

.. c:function:: struct net_device *__dev_get_by_flags (struct net *net, unsigned short if_flags, unsigned short mask)

    find any device with given flags

    :param struct net \*net:
        the applicable net namespace

    :param unsigned short if_flags:
        IFF_\* values

    :param unsigned short mask:
        bitmask of bits in if_flags to check


.. _`__dev_get_by_flags.description`:

Description
-----------

Search for any interface with the given flags. Returns NULL if a device
is not found or a pointer to the device. Must be called inside
:c:func:`rtnl_lock`, and result refcount is unchanged.


.. _`dev_valid_name`:

dev_valid_name
==============

.. c:function:: bool dev_valid_name (const char *name)

    check if name is okay for network device

    :param const char \*name:
        name string


.. _`dev_valid_name.description`:

Description
-----------

Network device names need to be valid file names to
to allow sysfs to work.  We also disallow any kind of
whitespace.


.. _`__dev_alloc_name`:

__dev_alloc_name
================

.. c:function:: int __dev_alloc_name (struct net *net, const char *name, char *buf)

    allocate a name for a device

    :param struct net \*net:
        network namespace to allocate the device name in

    :param const char \*name:
        name format string

    :param char \*buf:
        scratch buffer and result name string


.. _`__dev_alloc_name.description`:

Description
-----------

Passed a format string - eg "lt\ ``d``\ " it will try and find a suitable
id. It scans list of devices to build up a free map, then chooses
the first empty slot. The caller must hold the dev_base or rtnl lock
while allocating the name and adding the device in order to avoid
duplicates.
Limited to bits_per_byte * page size devices (ie 32K on most platforms).
Returns the number of the unit assigned or a negative errno code.


.. _`dev_alloc_name`:

dev_alloc_name
==============

.. c:function:: int dev_alloc_name (struct net_device *dev, const char *name)

    allocate a name for a device

    :param struct net_device \*dev:
        device

    :param const char \*name:
        name format string


.. _`dev_alloc_name.description`:

Description
-----------

Passed a format string - eg "lt\ ``d``\ " it will try and find a suitable
id. It scans list of devices to build up a free map, then chooses
the first empty slot. The caller must hold the dev_base or rtnl lock
while allocating the name and adding the device in order to avoid
duplicates.
Limited to bits_per_byte * page size devices (ie 32K on most platforms).
Returns the number of the unit assigned or a negative errno code.


.. _`dev_change_name`:

dev_change_name
===============

.. c:function:: int dev_change_name (struct net_device *dev, const char *newname)

    change name of a device

    :param struct net_device \*dev:
        device

    :param const char \*newname:
        name (or format string) must be at least IFNAMSIZ


.. _`dev_change_name.description`:

Description
-----------

Change name of a device, can pass format strings "eth\ ``d``\ ".
for wildcarding.


.. _`dev_set_alias`:

dev_set_alias
=============

.. c:function:: int dev_set_alias (struct net_device *dev, const char *alias, size_t len)

    change ifalias of a device

    :param struct net_device \*dev:
        device

    :param const char \*alias:
        name up to IFALIASZ

    :param size_t len:
        limit of bytes to copy from info


.. _`dev_set_alias.description`:

Description
-----------

Set ifalias for a device,


.. _`netdev_features_change`:

netdev_features_change
======================

.. c:function:: void netdev_features_change (struct net_device *dev)

    device changes features

    :param struct net_device \*dev:
        device to cause notification


.. _`netdev_features_change.description`:

Description
-----------

Called to indicate a device has changed features.


.. _`netdev_state_change`:

netdev_state_change
===================

.. c:function:: void netdev_state_change (struct net_device *dev)

    device changes state

    :param struct net_device \*dev:
        device to cause notification


.. _`netdev_state_change.description`:

Description
-----------

Called to indicate a device has changed state. This function calls
the notifier chains for netdev_chain and sends a NEWLINK message
to the routing socket.


.. _`netdev_notify_peers`:

netdev_notify_peers
===================

.. c:function:: void netdev_notify_peers (struct net_device *dev)

    notify network peers about existence of @dev

    :param struct net_device \*dev:
        network device


.. _`netdev_notify_peers.description`:

Description
-----------

Generate traffic such that interested network peers are aware of
``dev``\ , such as by generating a gratuitous ARP. This may be used when
a device wants to inform the rest of the network about some sort of
reconfiguration such as a failover event or virtual machine
migration.


.. _`dev_open`:

dev_open
========

.. c:function:: int dev_open (struct net_device *dev)

    prepare an interface for use.

    :param struct net_device \*dev:
        device to open


.. _`dev_open.description`:

Description
-----------

Takes a device from down to up state. The device's private open
function is invoked and then the multicast lists are loaded. Finally
the device is moved into the up state and a ``NETDEV_UP`` message is
sent to the netdev notifier chain.

Calling this function on an active interface is a nop. On a failure
a negative errno code is returned.


.. _`dev_close`:

dev_close
=========

.. c:function:: int dev_close (struct net_device *dev)

    shutdown an interface.

    :param struct net_device \*dev:
        device to shutdown


.. _`dev_close.description`:

Description
-----------

This function moves an active device into down state. A
``NETDEV_GOING_DOWN`` is sent to the netdev notifier chain. The device
is then deactivated and finally a ``NETDEV_DOWN`` is sent to the notifier
chain.


.. _`dev_disable_lro`:

dev_disable_lro
===============

.. c:function:: void dev_disable_lro (struct net_device *dev)

    disable Large Receive Offload on a device

    :param struct net_device \*dev:
        device


.. _`dev_disable_lro.description`:

Description
-----------

Disable Large Receive Offload (LRO) on a net device.  Must be
called under RTNL.  This is needed if received packets may be
forwarded to another interface.


.. _`register_netdevice_notifier`:

register_netdevice_notifier
===========================

.. c:function:: int register_netdevice_notifier (struct notifier_block *nb)

    register a network notifier block

    :param struct notifier_block \*nb:
        notifier


.. _`register_netdevice_notifier.description`:

Description
-----------

Register a notifier to be called when network device events occur.
The notifier passed is linked into the kernel structures and must
not be reused until it has been unregistered. A negative errno code
is returned on a failure.

When registered all registration and up events are replayed
to the new notifier to allow device to have a race free
view of the network device list.


.. _`unregister_netdevice_notifier`:

unregister_netdevice_notifier
=============================

.. c:function:: int unregister_netdevice_notifier (struct notifier_block *nb)

    unregister a network notifier block

    :param struct notifier_block \*nb:
        notifier


.. _`unregister_netdevice_notifier.description`:

Description
-----------

Unregister a notifier previously registered by
:c:func:`register_netdevice_notifier`. The notifier is unlinked into the
kernel structures and may then be reused. A negative errno code
is returned on a failure.

After unregistering unregister and down device events are synthesized
for all devices on the device list to the removed notifier to remove
the need for special case cleanup code.


.. _`call_netdevice_notifiers_info`:

call_netdevice_notifiers_info
=============================

.. c:function:: int call_netdevice_notifiers_info (unsigned long val, struct net_device *dev, struct netdev_notifier_info *info)

    call all network notifier blocks

    :param unsigned long val:
        value passed unmodified to notifier function

    :param struct net_device \*dev:
        net_device pointer passed unmodified to notifier function

    :param struct netdev_notifier_info \*info:
        notifier information data


.. _`call_netdevice_notifiers_info.description`:

Description
-----------

Call all network notifier blocks.  Parameters and return value
are as for :c:func:`raw_notifier_call_chain`.


.. _`call_netdevice_notifiers`:

call_netdevice_notifiers
========================

.. c:function:: int call_netdevice_notifiers (unsigned long val, struct net_device *dev)

    call all network notifier blocks

    :param unsigned long val:
        value passed unmodified to notifier function

    :param struct net_device \*dev:
        net_device pointer passed unmodified to notifier function


.. _`call_netdevice_notifiers.description`:

Description
-----------

Call all network notifier blocks.  Parameters and return value
are as for :c:func:`raw_notifier_call_chain`.


.. _`dev_forward_skb`:

dev_forward_skb
===============

.. c:function:: int dev_forward_skb (struct net_device *dev, struct sk_buff *skb)

    loopback an skb to another netif

    :param struct net_device \*dev:
        destination network device

    :param struct sk_buff \*skb:
        buffer to forward


.. _`dev_forward_skb.description`:

Description
-----------

return values::

        NET_RX_SUCCESS        (no congestion)
        NET_RX_DROP     (packet was dropped, but freed)

dev_forward_skb can be used for injecting an skb from the
start_xmit function of one device into the receive queue
of another device.

The receiving device may be in another namespace, so
we have to clear all information in the skb that could
impact namespace isolation.


.. _`netif_setup_tc`:

netif_setup_tc
==============

.. c:function:: void netif_setup_tc (struct net_device *dev, unsigned int txq)

    Handle tc mappings on real_num_tx_queues change

    :param struct net_device \*dev:
        Network device

    :param unsigned int txq:
        number of queues available


.. _`netif_setup_tc.description`:

Description
-----------

If real_num_tx_queues is changed the tc mappings may no longer be
valid. To resolve this verify the tc mapping remains valid and if
not NULL the mapping. With no priorities mapping to this
offset/count pair it will no longer be used. In the worst case TC0
is invalid nothing can be done so disable priority mappings. If is
expected that drivers will fix this mapping if they can before
calling netif_set_real_num_tx_queues.


.. _`netif_set_real_num_rx_queues`:

netif_set_real_num_rx_queues
============================

.. c:function:: int netif_set_real_num_rx_queues (struct net_device *dev, unsigned int rxq)

    set actual number of RX queues used

    :param struct net_device \*dev:
        Network device

    :param unsigned int rxq:
        Actual number of RX queues


.. _`netif_set_real_num_rx_queues.description`:

Description
-----------

This must be called either with the rtnl_lock held or before
registration of the net device.  Returns 0 on success, or a
negative error code.  If called before registration, it always
succeeds.


.. _`netif_get_num_default_rss_queues`:

netif_get_num_default_rss_queues
================================

.. c:function:: int netif_get_num_default_rss_queues ( void)

    default number of RSS queues

    :param void:
        no arguments


.. _`netif_get_num_default_rss_queues.description`:

Description
-----------


This routine should set an upper limit on the number of RSS queues
used by default by multiqueue devices.


.. _`netif_wake_subqueue`:

netif_wake_subqueue
===================

.. c:function:: void netif_wake_subqueue (struct net_device *dev, u16 queue_index)

    allow sending packets on subqueue

    :param struct net_device \*dev:
        network device

    :param u16 queue_index:
        sub queue index


.. _`netif_wake_subqueue.description`:

Description
-----------

Resume individual transmit queue of a device with multiple transmit queues.


.. _`netif_device_detach`:

netif_device_detach
===================

.. c:function:: void netif_device_detach (struct net_device *dev)

    mark device as removed

    :param struct net_device \*dev:
        network device


.. _`netif_device_detach.description`:

Description
-----------

Mark device as removed from system and therefore no longer available.


.. _`netif_device_attach`:

netif_device_attach
===================

.. c:function:: void netif_device_attach (struct net_device *dev)

    mark device as attached

    :param struct net_device \*dev:
        network device


.. _`netif_device_attach.description`:

Description
-----------

Mark device as attached from system and restart if needed.


.. _`skb_mac_gso_segment`:

skb_mac_gso_segment
===================

.. c:function:: struct sk_buff *skb_mac_gso_segment (struct sk_buff *skb, netdev_features_t features)

    mac layer segmentation handler.

    :param struct sk_buff \*skb:
        buffer to segment

    :param netdev_features_t features:
        features for the output path (see dev->features)


.. _`__skb_gso_segment`:

__skb_gso_segment
=================

.. c:function:: struct sk_buff *__skb_gso_segment (struct sk_buff *skb, netdev_features_t features, bool tx_path)

    Perform segmentation on skb.

    :param struct sk_buff \*skb:
        buffer to segment

    :param netdev_features_t features:
        features for the output path (see dev->features)

    :param bool tx_path:
        whether it is called in TX path


.. _`__skb_gso_segment.description`:

Description
-----------

This function segments the given skb and returns a list of segments.

It may return NULL if the skb requires no segmentation.  This is
only possible when GSO is used for verifying header integrity.

Segmentation preserves SKB_SGO_CB_OFFSET bytes of previous skb cb.


.. _`dev_loopback_xmit`:

dev_loopback_xmit
=================

.. c:function:: int dev_loopback_xmit (struct net *net, struct sock *sk, struct sk_buff *skb)

    loop back @skb

    :param struct net \*net:
        network namespace this loopback is happening in

    :param struct sock \*sk:
        sk needed to be a netfilter okfn

    :param struct sk_buff \*skb:
        buffer to transmit


.. _`__dev_queue_xmit`:

__dev_queue_xmit
================

.. c:function:: int __dev_queue_xmit (struct sk_buff *skb, void *accel_priv)

    transmit a buffer

    :param struct sk_buff \*skb:
        buffer to transmit

    :param void \*accel_priv:
        private data used for L2 forwarding offload


.. _`__dev_queue_xmit.description`:

Description
-----------

Queue a buffer for transmission to a network device. The caller must
have set the device and priority and built the buffer before calling
this function. The function can be called from an interrupt.

A negative errno code is returned on a failure. A success does not
guarantee the frame will be transmitted as it may be dropped due
to congestion or traffic shaping.

-----------------------------------------------------------------------------------
I notice this method can also return errors from the queue disciplines,
including NET_XMIT_DROP, which is a positive value.  So, errors can also
be positive.

Regardless of the return value, the skb is consumed, so it is currently
difficult to retry a send to this method.  (You can bump the ref count
before sending to hold a reference for retry if you are careful.)

When calling this method, interrupts MUST be enabled.  This is because
the BH enable code must have IRQs enabled so that it will not deadlock.
--BLG


.. _`rps_may_expire_flow`:

rps_may_expire_flow
===================

.. c:function:: bool rps_may_expire_flow (struct net_device *dev, u16 rxq_index, u32 flow_id, u16 filter_id)

    check whether an RFS hardware filter may be removed

    :param struct net_device \*dev:
        Device on which the filter was set

    :param u16 rxq_index:
        RX queue index

    :param u32 flow_id:
        Flow ID passed to :c:func:`ndo_rx_flow_steer`

    :param u16 filter_id:
        Filter ID returned by :c:func:`ndo_rx_flow_steer`


.. _`rps_may_expire_flow.description`:

Description
-----------

Drivers that implement :c:func:`ndo_rx_flow_steer` should periodically call
this function for each installed filter and remove the filters for
which it returns ``true``\ .


.. _`netif_rx`:

netif_rx
========

.. c:function:: int netif_rx (struct sk_buff *skb)

    post buffer to the network code

    :param struct sk_buff \*skb:
        buffer to post


.. _`netif_rx.description`:

Description
-----------

This function receives a packet from a device driver and queues it for
the upper (protocol) levels to process.  It always succeeds. The buffer
may be dropped during processing for congestion control or by the
protocol layers.

return values:
NET_RX_SUCCESS        (no congestion)
NET_RX_DROP     (packet was dropped)


.. _`netdev_rx_handler_register`:

netdev_rx_handler_register
==========================

.. c:function:: int netdev_rx_handler_register (struct net_device *dev, rx_handler_func_t *rx_handler, void *rx_handler_data)

    register receive handler

    :param struct net_device \*dev:
        device to register a handler for

    :param rx_handler_func_t \*rx_handler:
        receive handler to register

    :param void \*rx_handler_data:
        data pointer that is used by rx handler


.. _`netdev_rx_handler_register.description`:

Description
-----------

Register a receive handler for a device. This handler will then be
called from __netif_receive_skb. A negative errno code is returned
on a failure.

The caller must hold the rtnl_mutex.

For a general description of rx_handler, see enum rx_handler_result.


.. _`netdev_rx_handler_unregister`:

netdev_rx_handler_unregister
============================

.. c:function:: void netdev_rx_handler_unregister (struct net_device *dev)

    unregister receive handler

    :param struct net_device \*dev:
        device to unregister a handler from


.. _`netdev_rx_handler_unregister.description`:

Description
-----------

Unregister a receive handler from a device.

The caller must hold the rtnl_mutex.


.. _`netif_receive_skb`:

netif_receive_skb
=================

.. c:function:: int netif_receive_skb (struct sk_buff *skb)

    process receive buffer from network

    :param struct sk_buff \*skb:
        buffer to process


.. _`netif_receive_skb.description`:

Description
-----------

:c:func:`netif_receive_skb` is the main receive data processing function.
It always succeeds. The buffer may be dropped during processing
for congestion control or by the protocol layers.

This function may only be called from softirq context and interrupts
should be enabled.

Return values (usually ignored):
NET_RX_SUCCESS: no congestion
NET_RX_DROP: packet was dropped


.. _`__napi_schedule`:

__napi_schedule
===============

.. c:function:: void __napi_schedule (struct napi_struct *n)

    schedule for receive

    :param struct napi_struct \*n:
        entry to schedule


.. _`__napi_schedule.description`:

Description
-----------

The entry's receive function will be scheduled to run.
Consider using :c:func:`__napi_schedule_irqoff` if hard irqs are masked.


.. _`__napi_schedule_irqoff`:

__napi_schedule_irqoff
======================

.. c:function:: void __napi_schedule_irqoff (struct napi_struct *n)

    schedule for receive

    :param struct napi_struct \*n:
        entry to schedule


.. _`__napi_schedule_irqoff.description`:

Description
-----------

Variant of :c:func:`__napi_schedule` assuming hard irqs are masked


.. _`netdev_has_upper_dev`:

netdev_has_upper_dev
====================

.. c:function:: bool netdev_has_upper_dev (struct net_device *dev, struct net_device *upper_dev)

    Check if device is linked to an upper device

    :param struct net_device \*dev:
        device

    :param struct net_device \*upper_dev:
        upper device to check


.. _`netdev_has_upper_dev.description`:

Description
-----------

Find out if a device is linked to specified upper device and return true
in case it is. Note that this checks only immediate upper device,
not through a complete stack of devices. The caller must hold the RTNL lock.


.. _`netdev_has_any_upper_dev`:

netdev_has_any_upper_dev
========================

.. c:function:: bool netdev_has_any_upper_dev (struct net_device *dev)

    Check if device is linked to some device

    :param struct net_device \*dev:
        device


.. _`netdev_has_any_upper_dev.description`:

Description
-----------

Find out if a device is linked to an upper device and return true in case
it is. The caller must hold the RTNL lock.


.. _`netdev_master_upper_dev_get`:

netdev_master_upper_dev_get
===========================

.. c:function:: struct net_device *netdev_master_upper_dev_get (struct net_device *dev)

    Get master upper device

    :param struct net_device \*dev:
        device


.. _`netdev_master_upper_dev_get.description`:

Description
-----------

Find a master upper device and return pointer to it or NULL in case
it's not there. The caller must hold the RTNL lock.


.. _`netdev_upper_get_next_dev_rcu`:

netdev_upper_get_next_dev_rcu
=============================

.. c:function:: struct net_device *netdev_upper_get_next_dev_rcu (struct net_device *dev, struct list_head **iter)

    Get the next dev from upper list

    :param struct net_device \*dev:
        device

    :param struct list_head \*\*iter:
        list_head ** of the current position


.. _`netdev_upper_get_next_dev_rcu.description`:

Description
-----------

Gets the next device from the dev's upper list, starting from iter
position. The caller must hold RCU read lock.


.. _`netdev_all_upper_get_next_dev_rcu`:

netdev_all_upper_get_next_dev_rcu
=================================

.. c:function:: struct net_device *netdev_all_upper_get_next_dev_rcu (struct net_device *dev, struct list_head **iter)

    Get the next dev from upper list

    :param struct net_device \*dev:
        device

    :param struct list_head \*\*iter:
        list_head ** of the current position


.. _`netdev_all_upper_get_next_dev_rcu.description`:

Description
-----------

Gets the next device from the dev's upper list, starting from iter
position. The caller must hold RCU read lock.


.. _`netdev_lower_get_next_private`:

netdev_lower_get_next_private
=============================

.. c:function:: void *netdev_lower_get_next_private (struct net_device *dev, struct list_head **iter)

    Get the next ->private from the lower neighbour list

    :param struct net_device \*dev:
        device

    :param struct list_head \*\*iter:
        list_head ** of the current position


.. _`netdev_lower_get_next_private.description`:

Description
-----------

Gets the next netdev_adjacent->private from the dev's lower neighbour
list, starting from iter position. The caller must hold either hold the
RTNL lock or its own locking that guarantees that the neighbour lower
list will remain unchanged.


.. _`netdev_lower_get_next_private_rcu`:

netdev_lower_get_next_private_rcu
=================================

.. c:function:: void *netdev_lower_get_next_private_rcu (struct net_device *dev, struct list_head **iter)

    Get the next ->private from the lower neighbour list, RCU variant

    :param struct net_device \*dev:
        device

    :param struct list_head \*\*iter:
        list_head ** of the current position


.. _`netdev_lower_get_next_private_rcu.description`:

Description
-----------

Gets the next netdev_adjacent->private from the dev's lower neighbour
list, starting from iter position. The caller must hold RCU read lock.


.. _`netdev_lower_get_next`:

netdev_lower_get_next
=====================

.. c:function:: void *netdev_lower_get_next (struct net_device *dev, struct list_head **iter)

    Get the next device from the lower neighbour list

    :param struct net_device \*dev:
        device

    :param struct list_head \*\*iter:
        list_head ** of the current position


.. _`netdev_lower_get_next.description`:

Description
-----------

Gets the next netdev_adjacent from the dev's lower neighbour
list, starting from iter position. The caller must hold RTNL lock or
its own locking that guarantees that the neighbour lower
list will remain unchanged.


.. _`netdev_lower_get_first_private_rcu`:

netdev_lower_get_first_private_rcu
==================================

.. c:function:: void *netdev_lower_get_first_private_rcu (struct net_device *dev)

    Get the first ->private from the lower neighbour list, RCU variant

    :param struct net_device \*dev:
        device


.. _`netdev_lower_get_first_private_rcu.description`:

Description
-----------

Gets the first netdev_adjacent->private from the dev's lower neighbour
list. The caller must hold RCU read lock.


.. _`netdev_master_upper_dev_get_rcu`:

netdev_master_upper_dev_get_rcu
===============================

.. c:function:: struct net_device *netdev_master_upper_dev_get_rcu (struct net_device *dev)

    Get master upper device

    :param struct net_device \*dev:
        device


.. _`netdev_master_upper_dev_get_rcu.description`:

Description
-----------

Find a master upper device and return pointer to it or NULL in case
it's not there. The caller must hold the RCU read lock.


.. _`netdev_upper_dev_link`:

netdev_upper_dev_link
=====================

.. c:function:: int netdev_upper_dev_link (struct net_device *dev, struct net_device *upper_dev)

    Add a link to the upper device

    :param struct net_device \*dev:
        device

    :param struct net_device \*upper_dev:
        new upper device


.. _`netdev_upper_dev_link.description`:

Description
-----------

Adds a link to device which is upper to this one. The caller must hold
the RTNL lock. On a failure a negative errno code is returned.
On success the reference counts are adjusted and the function
returns zero.


.. _`netdev_master_upper_dev_link`:

netdev_master_upper_dev_link
============================

.. c:function:: int netdev_master_upper_dev_link (struct net_device *dev, struct net_device *upper_dev, void *upper_priv, void *upper_info)

    Add a master link to the upper device

    :param struct net_device \*dev:
        device

    :param struct net_device \*upper_dev:
        new upper device

    :param void \*upper_priv:
        upper device private

    :param void \*upper_info:
        upper info to be passed down via notifier


.. _`netdev_master_upper_dev_link.description`:

Description
-----------

Adds a link to device which is upper to this one. In this case, only
one master upper device can be linked, although other non-master devices
might be linked as well. The caller must hold the RTNL lock.
On a failure a negative errno code is returned. On success the reference
counts are adjusted and the function returns zero.


.. _`netdev_upper_dev_unlink`:

netdev_upper_dev_unlink
=======================

.. c:function:: void netdev_upper_dev_unlink (struct net_device *dev, struct net_device *upper_dev)

    Removes a link to upper device

    :param struct net_device \*dev:
        device

    :param struct net_device \*upper_dev:
        new upper device


.. _`netdev_upper_dev_unlink.description`:

Description
-----------

Removes a link to device which is upper to this one. The caller must hold
the RTNL lock.


.. _`netdev_bonding_info_change`:

netdev_bonding_info_change
==========================

.. c:function:: void netdev_bonding_info_change (struct net_device *dev, struct netdev_bonding_info *bonding_info)

    Dispatch event about slave change

    :param struct net_device \*dev:
        device

    :param struct netdev_bonding_info \*bonding_info:
        info to dispatch


.. _`netdev_bonding_info_change.description`:

Description
-----------

Send NETDEV_BONDING_INFO to netdev notifiers with info.
The caller must hold the RTNL lock.


.. _`netdev_lower_state_changed`:

netdev_lower_state_changed
==========================

.. c:function:: void netdev_lower_state_changed (struct net_device *lower_dev, void *lower_state_info)

    Dispatch event about lower device state change

    :param struct net_device \*lower_dev:
        device

    :param void \*lower_state_info:
        state to dispatch


.. _`netdev_lower_state_changed.description`:

Description
-----------

Send NETDEV_CHANGELOWERSTATE to netdev notifiers with info.
The caller must hold the RTNL lock.


.. _`dev_set_promiscuity`:

dev_set_promiscuity
===================

.. c:function:: int dev_set_promiscuity (struct net_device *dev, int inc)

    update promiscuity count on a device

    :param struct net_device \*dev:
        device

    :param int inc:
        modifier


.. _`dev_set_promiscuity.description`:

Description
-----------

Add or remove promiscuity from a device. While the count in the device
remains above zero the interface remains promiscuous. Once it hits zero
the device reverts back to normal filtering operation. A negative inc
value is used to drop promiscuity on the device.
Return 0 if successful or a negative errno code on error.


.. _`dev_set_allmulti`:

dev_set_allmulti
================

.. c:function:: int dev_set_allmulti (struct net_device *dev, int inc)

    update allmulti count on a device

    :param struct net_device \*dev:
        device

    :param int inc:
        modifier


.. _`dev_set_allmulti.description`:

Description
-----------

Add or remove reception of all multicast frames to a device. While the
count in the device remains above zero the interface remains listening
to all interfaces. Once it hits zero the device reverts back to normal
filtering operation. A negative ``inc`` value is used to drop the counter
when releasing a resource needing all multicasts.
Return 0 if successful or a negative errno code on error.


.. _`dev_get_flags`:

dev_get_flags
=============

.. c:function:: unsigned int dev_get_flags (const struct net_device *dev)

    get flags reported to userspace

    :param const struct net_device \*dev:
        device


.. _`dev_get_flags.description`:

Description
-----------

Get the combination of flag bits exported through APIs to userspace.


.. _`dev_change_flags`:

dev_change_flags
================

.. c:function:: int dev_change_flags (struct net_device *dev, unsigned int flags)

    change device settings

    :param struct net_device \*dev:
        device

    :param unsigned int flags:
        device state flags


.. _`dev_change_flags.description`:

Description
-----------

Change settings on device based state flags. The flags are
in the userspace exported format.


.. _`dev_set_mtu`:

dev_set_mtu
===========

.. c:function:: int dev_set_mtu (struct net_device *dev, int new_mtu)

    Change maximum transfer unit

    :param struct net_device \*dev:
        device

    :param int new_mtu:
        new transfer unit


.. _`dev_set_mtu.description`:

Description
-----------

Change the maximum transfer size of the network device.


.. _`dev_set_group`:

dev_set_group
=============

.. c:function:: void dev_set_group (struct net_device *dev, int new_group)

    Change group this device belongs to

    :param struct net_device \*dev:
        device

    :param int new_group:
        group this device should belong to


.. _`dev_set_mac_address`:

dev_set_mac_address
===================

.. c:function:: int dev_set_mac_address (struct net_device *dev, struct sockaddr *sa)

    Change Media Access Control Address

    :param struct net_device \*dev:
        device

    :param struct sockaddr \*sa:
        new address


.. _`dev_set_mac_address.description`:

Description
-----------

Change the hardware (MAC) address of the device


.. _`dev_change_carrier`:

dev_change_carrier
==================

.. c:function:: int dev_change_carrier (struct net_device *dev, bool new_carrier)

    Change device carrier

    :param struct net_device \*dev:
        device

    :param bool new_carrier:
        new value


.. _`dev_change_carrier.description`:

Description
-----------

Change device carrier


.. _`dev_get_phys_port_id`:

dev_get_phys_port_id
====================

.. c:function:: int dev_get_phys_port_id (struct net_device *dev, struct netdev_phys_item_id *ppid)

    Get device physical port ID

    :param struct net_device \*dev:
        device

    :param struct netdev_phys_item_id \*ppid:
        port ID


.. _`dev_get_phys_port_id.description`:

Description
-----------

Get device physical port ID


.. _`dev_get_phys_port_name`:

dev_get_phys_port_name
======================

.. c:function:: int dev_get_phys_port_name (struct net_device *dev, char *name, size_t len)

    Get device physical port name

    :param struct net_device \*dev:
        device

    :param char \*name:
        port name

    :param size_t len:
        limit of bytes to copy to name


.. _`dev_get_phys_port_name.description`:

Description
-----------

Get device physical port name


.. _`dev_change_proto_down`:

dev_change_proto_down
=====================

.. c:function:: int dev_change_proto_down (struct net_device *dev, bool proto_down)

    update protocol port state information

    :param struct net_device \*dev:
        device

    :param bool proto_down:
        new value


.. _`dev_change_proto_down.description`:

Description
-----------

This info can be used by switch drivers to set the phys state of the
port.


.. _`dev_new_index`:

dev_new_index
=============

.. c:function:: int dev_new_index (struct net *net)

    allocate an ifindex

    :param struct net \*net:
        the applicable net namespace


.. _`dev_new_index.description`:

Description
-----------

Returns a suitable unique value for a new device interface
number.  The caller must hold the rtnl semaphore or the
dev_base_lock to be sure it remains unique.


.. _`netdev_update_features`:

netdev_update_features
======================

.. c:function:: void netdev_update_features (struct net_device *dev)

    recalculate device features

    :param struct net_device \*dev:
        the device to check


.. _`netdev_update_features.description`:

Description
-----------

Recalculate dev->features set and send notifications if it
has changed. Should be called after driver or hardware dependent
conditions might have changed that influence the features.


.. _`netdev_change_features`:

netdev_change_features
======================

.. c:function:: void netdev_change_features (struct net_device *dev)

    recalculate device features

    :param struct net_device \*dev:
        the device to check


.. _`netdev_change_features.description`:

Description
-----------

Recalculate dev->features set and send notifications even
if they have not changed. Should be called instead of
:c:func:`netdev_update_features` if also dev->vlan_features might
have changed to allow the changes to be propagated to stacked
VLAN devices.


.. _`netif_stacked_transfer_operstate`:

netif_stacked_transfer_operstate
================================

.. c:function:: void netif_stacked_transfer_operstate (const struct net_device *rootdev, struct net_device *dev)

    transfer operstate

    :param const struct net_device \*rootdev:
        the root or lower level device to transfer state from

    :param struct net_device \*dev:
        the device to transfer operstate to


.. _`netif_stacked_transfer_operstate.description`:

Description
-----------

Transfer operational state from root to device. This is normally
called when a stacking relationship exists between the root
device and the device(a leaf device).


.. _`register_netdevice`:

register_netdevice
==================

.. c:function:: int register_netdevice (struct net_device *dev)

    register a network device

    :param struct net_device \*dev:
        device to register


.. _`register_netdevice.description`:

Description
-----------

Take a completed network device structure and add it to the kernel
interfaces. A ``NETDEV_REGISTER`` message is sent to the netdev notifier
chain. 0 is returned on success. A negative errno code is returned
on a failure to set up the device, or if the name is a duplicate.

Callers must hold the rtnl semaphore. You may want
:c:func:`register_netdev` instead of this.

BUGS:
The locking appears insufficient to guarantee two parallel registers
will not get the same name.


.. _`init_dummy_netdev`:

init_dummy_netdev
=================

.. c:function:: int init_dummy_netdev (struct net_device *dev)

    init a dummy network device for NAPI

    :param struct net_device \*dev:
        device to init


.. _`init_dummy_netdev.description`:

Description
-----------

This takes a network device structure and initialize the minimum
amount of fields so it can be used to schedule NAPI polls without
registering a full blown interface. This is to be used by drivers
that need to tie several hardware interfaces to a single NAPI
poll scheduler due to HW limitations.


.. _`register_netdev`:

register_netdev
===============

.. c:function:: int register_netdev (struct net_device *dev)

    register a network device

    :param struct net_device \*dev:
        device to register


.. _`register_netdev.description`:

Description
-----------

Take a completed network device structure and add it to the kernel
interfaces. A ``NETDEV_REGISTER`` message is sent to the netdev notifier
chain. 0 is returned on success. A negative errno code is returned
on a failure to set up the device, or if the name is a duplicate.

This is a wrapper around register_netdevice that takes the rtnl semaphore
and expands the device name if you passed a format string to
alloc_netdev.


.. _`netdev_wait_allrefs`:

netdev_wait_allrefs
===================

.. c:function:: void netdev_wait_allrefs (struct net_device *dev)

    wait until all references are gone.

    :param struct net_device \*dev:
        target net_device


.. _`netdev_wait_allrefs.description`:

Description
-----------

This is called when unregistering network devices.

Any protocol or device that holds a reference should register
for netdevice notification, and cleanup and put back the
reference if they receive an UNREGISTER event.
We can get stuck here if buggy protocols don't correctly
call dev_put.


.. _`dev_get_stats`:

dev_get_stats
=============

.. c:function:: struct rtnl_link_stats64 *dev_get_stats (struct net_device *dev, struct rtnl_link_stats64 *storage)

    get network device statistics

    :param struct net_device \*dev:
        device to get statistics from

    :param struct rtnl_link_stats64 \*storage:
        place to store stats


.. _`dev_get_stats.description`:

Description
-----------

Get network statistics from device. Return ``storage``\ .
The device driver may provide its own method by setting
dev->netdev_ops->get_stats64 or dev->netdev_ops->get_stats;
otherwise the internal statistics structure is used.


.. _`alloc_netdev_mqs`:

alloc_netdev_mqs
================

.. c:function:: struct net_device *alloc_netdev_mqs (int sizeof_priv, const char *name, unsigned char name_assign_type, void (*setup) (struct net_device *, unsigned int txqs, unsigned int rxqs)

    allocate network device

    :param int sizeof_priv:
        size of private data to allocate space for

    :param const char \*name:
        device name format string

    :param unsigned char name_assign_type:
        origin of device name

    :param void (\*setup) (struct net_device \*):
        callback to initialize device

    :param unsigned int txqs:
        the number of TX subqueues to allocate

    :param unsigned int rxqs:
        the number of RX subqueues to allocate


.. _`alloc_netdev_mqs.description`:

Description
-----------

Allocates a struct net_device with private data area for driver use
and performs basic initialization.  Also allocates subqueue structs
for each queue on the device.


.. _`free_netdev`:

free_netdev
===========

.. c:function:: void free_netdev (struct net_device *dev)

    free network device

    :param struct net_device \*dev:
        device


.. _`free_netdev.description`:

Description
-----------

This function does the last stage of destroying an allocated device
interface. The reference to the device object is released.
If this is the last reference then it will be freed.
Must be called in process context.


.. _`synchronize_net`:

synchronize_net
===============

.. c:function:: void synchronize_net ( void)

    Synchronize with packet receive processing

    :param void:
        no arguments


.. _`synchronize_net.description`:

Description
-----------


Wait for packets currently being received to be done.
Does not block later packets from starting.


.. _`unregister_netdevice_queue`:

unregister_netdevice_queue
==========================

.. c:function:: void unregister_netdevice_queue (struct net_device *dev, struct list_head *head)

    remove device from the kernel

    :param struct net_device \*dev:
        device

    :param struct list_head \*head:
        list


.. _`unregister_netdevice_queue.description`:

Description
-----------

This function shuts down a device interface and removes it
from the kernel tables.
If head not NULL, device is queued to be unregistered later.

Callers must hold the rtnl semaphore.  You may want
:c:func:`unregister_netdev` instead of this.


.. _`unregister_netdevice_many`:

unregister_netdevice_many
=========================

.. c:function:: void unregister_netdevice_many (struct list_head *head)

    unregister many devices

    :param struct list_head \*head:
        list of devices


.. _`unregister_netdevice_many.description`:

Description
-----------

Note: As most callers use a stack allocated list_head,
we force a :c:func:`list_del` to make sure stack wont be corrupted later.


.. _`unregister_netdev`:

unregister_netdev
=================

.. c:function:: void unregister_netdev (struct net_device *dev)

    remove device from the kernel

    :param struct net_device \*dev:
        device


.. _`unregister_netdev.description`:

Description
-----------

This function shuts down a device interface and removes it
from the kernel tables.

This is just a wrapper for unregister_netdevice that takes
the rtnl semaphore.  In general you want to use this and not
unregister_netdevice.


.. _`dev_change_net_namespace`:

dev_change_net_namespace
========================

.. c:function:: int dev_change_net_namespace (struct net_device *dev, struct net *net, const char *pat)

    move device to different nethost namespace

    :param struct net_device \*dev:
        device

    :param struct net \*net:
        network namespace

    :param const char \*pat:
        If not NULL name pattern to try if the current device name
        is already taken in the destination network namespace.


.. _`dev_change_net_namespace.description`:

Description
-----------

This function shuts down a device interface and moves it
to a new network namespace. On success 0 is returned, on
a failure a netagive errno code is returned.

Callers must hold the rtnl semaphore.


.. _`netdev_increment_features`:

netdev_increment_features
=========================

.. c:function:: netdev_features_t netdev_increment_features (netdev_features_t all, netdev_features_t one, netdev_features_t mask)

    increment feature set by one

    :param netdev_features_t all:
        current feature set

    :param netdev_features_t one:
        new feature set

    :param netdev_features_t mask:
        mask feature set


.. _`netdev_increment_features.description`:

Description
-----------

Computes a new feature set after adding a device with feature set
``one`` to the master device with current feature set ``all``\ .  Will not
enable anything that is off in ``mask``\ . Returns the new feature set.


.. _`netdev_drivername`:

netdev_drivername
=================

.. c:function:: const char *netdev_drivername (const struct net_device *dev)

    network driver for the device

    :param const struct net_device \*dev:
        network device


.. _`netdev_drivername.description`:

Description
-----------

Determine network driver for device.

