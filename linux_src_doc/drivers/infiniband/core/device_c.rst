.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/device.c

.. _`ib_alloc_device`:

ib_alloc_device
===============

.. c:function:: struct ib_device *ib_alloc_device(size_t size)

    allocate an IB device struct

    :param size_t size:
        size of structure to allocate

.. _`ib_alloc_device.description`:

Description
-----------

Low-level drivers should use \ :c:func:`ib_alloc_device`\  to allocate \ :c:type:`struct ib_device <ib_device>`\ .  \ ``size``\  is the size of the structure to be allocated,
including any private data used by the low-level driver.
\ :c:func:`ib_dealloc_device`\  must be used to free structures allocated with
\ :c:func:`ib_alloc_device`\ .

.. _`ib_dealloc_device`:

ib_dealloc_device
=================

.. c:function:: void ib_dealloc_device(struct ib_device *device)

    free an IB device struct

    :param struct ib_device \*device:
        structure to free

.. _`ib_dealloc_device.description`:

Description
-----------

Free a structure allocated with \ :c:func:`ib_alloc_device`\ .

.. _`__dev_new_index`:

__dev_new_index
===============

.. c:function:: u32 __dev_new_index( void)

    allocate an device index

    :param  void:
        no arguments

.. _`__dev_new_index.description`:

Description
-----------

Returns a suitable unique value for a new device interface
number.  It assumes that there are less than 2^32-1 ib devices
will be present in the system.

.. _`ib_register_device`:

ib_register_device
==================

.. c:function:: int ib_register_device(struct ib_device *device, int (*port_callback)(struct ib_device *, u8, struct kobject *))

    Register an IB device with IB core

    :param struct ib_device \*device:
        Device to register

    :param int (\*port_callback)(struct ib_device \*, u8, struct kobject \*):
        *undescribed*

.. _`ib_register_device.description`:

Description
-----------

Low-level drivers use \ :c:func:`ib_register_device`\  to register their
devices with the IB core.  All registered clients will receive a
callback for each device that is added. \ ``device``\  must be allocated
with \ :c:func:`ib_alloc_device`\ .

.. _`ib_unregister_device`:

ib_unregister_device
====================

.. c:function:: void ib_unregister_device(struct ib_device *device)

    Unregister an IB device

    :param struct ib_device \*device:
        Device to unregister

.. _`ib_unregister_device.description`:

Description
-----------

Unregister an IB device.  All clients will receive a remove callback.

.. _`ib_register_client`:

ib_register_client
==================

.. c:function:: int ib_register_client(struct ib_client *client)

    Register an IB client

    :param struct ib_client \*client:
        Client to register

.. _`ib_register_client.description`:

Description
-----------

Upper level users of the IB drivers can use \ :c:func:`ib_register_client`\  to
register callbacks for IB device addition and removal.  When an IB
device is added, each registered client's add method will be called
(in the order the clients were registered), and when a device is
removed, each client's remove method will be called (in the reverse
order that clients were registered).  In addition, when
\ :c:func:`ib_register_client`\  is called, the client will receive an add
callback for all devices already registered.

.. _`ib_unregister_client`:

ib_unregister_client
====================

.. c:function:: void ib_unregister_client(struct ib_client *client)

    Unregister an IB client

    :param struct ib_client \*client:
        Client to unregister

.. _`ib_unregister_client.description`:

Description
-----------

Upper level users use \ :c:func:`ib_unregister_client`\  to remove their client
registration.  When \ :c:func:`ib_unregister_client`\  is called, the client
will receive a remove callback for each IB device still registered.

.. _`ib_get_client_data`:

ib_get_client_data
==================

.. c:function:: void *ib_get_client_data(struct ib_device *device, struct ib_client *client)

    Get IB client context

    :param struct ib_device \*device:
        Device to get context for

    :param struct ib_client \*client:
        Client to get context for

.. _`ib_get_client_data.description`:

Description
-----------

ib_get_client_data() returns client context set with
\ :c:func:`ib_set_client_data`\ .

.. _`ib_set_client_data`:

ib_set_client_data
==================

.. c:function:: void ib_set_client_data(struct ib_device *device, struct ib_client *client, void *data)

    Set IB client context

    :param struct ib_device \*device:
        Device to set context for

    :param struct ib_client \*client:
        Client to set context for

    :param void \*data:
        Context to set

.. _`ib_set_client_data.description`:

Description
-----------

ib_set_client_data() sets client context that can be retrieved with
\ :c:func:`ib_get_client_data`\ .

.. _`ib_register_event_handler`:

ib_register_event_handler
=========================

.. c:function:: void ib_register_event_handler(struct ib_event_handler *event_handler)

    Register an IB event handler

    :param struct ib_event_handler \*event_handler:
        Handler to register

.. _`ib_register_event_handler.description`:

Description
-----------

ib_register_event_handler() registers an event handler that will be
called back when asynchronous IB events occur (as defined in
chapter 11 of the InfiniBand Architecture Specification).  This
callback may occur in interrupt context.

.. _`ib_unregister_event_handler`:

ib_unregister_event_handler
===========================

.. c:function:: void ib_unregister_event_handler(struct ib_event_handler *event_handler)

    Unregister an event handler

    :param struct ib_event_handler \*event_handler:
        Handler to unregister

.. _`ib_unregister_event_handler.description`:

Description
-----------

Unregister an event handler registered with
\ :c:func:`ib_register_event_handler`\ .

.. _`ib_dispatch_event`:

ib_dispatch_event
=================

.. c:function:: void ib_dispatch_event(struct ib_event *event)

    Dispatch an asynchronous event

    :param struct ib_event \*event:
        Event to dispatch

.. _`ib_dispatch_event.description`:

Description
-----------

Low-level drivers must call \ :c:func:`ib_dispatch_event`\  to dispatch the
event to all registered event handlers when an asynchronous event
occurs.

.. _`ib_query_port`:

ib_query_port
=============

.. c:function:: int ib_query_port(struct ib_device *device, u8 port_num, struct ib_port_attr *port_attr)

    Query IB port attributes

    :param struct ib_device \*device:
        Device to query

    :param u8 port_num:
        Port number to query

    :param struct ib_port_attr \*port_attr:
        Port attributes

.. _`ib_query_port.description`:

Description
-----------

ib_query_port() returns the attributes of a port through the
\ ``port_attr``\  pointer.

.. _`ib_query_gid`:

ib_query_gid
============

.. c:function:: int ib_query_gid(struct ib_device *device, u8 port_num, int index, union ib_gid *gid, struct ib_gid_attr *attr)

    Get GID table entry

    :param struct ib_device \*device:
        Device to query

    :param u8 port_num:
        Port number to query

    :param int index:
        GID table index to query

    :param union ib_gid \*gid:
        Returned GID

    :param struct ib_gid_attr \*attr:
        Returned GID attributes related to this GID index (only in RoCE).
        NULL means ignore.

.. _`ib_query_gid.description`:

Description
-----------

ib_query_gid() fetches the specified GID table entry.

.. _`ib_enum_roce_netdev`:

ib_enum_roce_netdev
===================

.. c:function:: void ib_enum_roce_netdev(struct ib_device *ib_dev, roce_netdev_filter filter, void *filter_cookie, roce_netdev_callback cb, void *cookie)

    enumerate all RoCE ports

    :param struct ib_device \*ib_dev:
        IB device we want to query

    :param roce_netdev_filter filter:
        Should we call the callback?

    :param void \*filter_cookie:
        Cookie passed to filter

    :param roce_netdev_callback cb:
        Callback to call for each found RoCE ports

    :param void \*cookie:
        Cookie passed back to the callback

.. _`ib_enum_roce_netdev.description`:

Description
-----------

Enumerates all of the physical RoCE ports of ib_dev
which are related to netdevice and calls \ :c:func:`callback`\  on each
device for which \ :c:func:`filter`\  function returns non zero.

.. _`ib_enum_all_roce_netdevs`:

ib_enum_all_roce_netdevs
========================

.. c:function:: void ib_enum_all_roce_netdevs(roce_netdev_filter filter, void *filter_cookie, roce_netdev_callback cb, void *cookie)

    enumerate all RoCE devices

    :param roce_netdev_filter filter:
        Should we call the callback?

    :param void \*filter_cookie:
        Cookie passed to filter

    :param roce_netdev_callback cb:
        Callback to call for each found RoCE ports

    :param void \*cookie:
        Cookie passed back to the callback

.. _`ib_enum_all_roce_netdevs.description`:

Description
-----------

Enumerates all RoCE devices' physical ports which are related
to netdevices and calls \ :c:func:`callback`\  on each device for which
\ :c:func:`filter`\  function returns non zero.

.. _`ib_enum_all_devs`:

ib_enum_all_devs
================

.. c:function:: int ib_enum_all_devs(nldev_callback nldev_cb, struct sk_buff *skb, struct netlink_callback *cb)

    enumerate all ib_devices

    :param nldev_callback nldev_cb:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct netlink_callback \*cb:
        Callback to call for each found ib_device

.. _`ib_enum_all_devs.description`:

Description
-----------

Enumerates all ib_devices and calls \ :c:func:`callback`\  on each device.

.. _`ib_query_pkey`:

ib_query_pkey
=============

.. c:function:: int ib_query_pkey(struct ib_device *device, u8 port_num, u16 index, u16 *pkey)

    Get P_Key table entry

    :param struct ib_device \*device:
        Device to query

    :param u8 port_num:
        Port number to query

    :param u16 index:
        P_Key table index to query

    :param u16 \*pkey:
        Returned P_Key

.. _`ib_query_pkey.description`:

Description
-----------

ib_query_pkey() fetches the specified P_Key table entry.

.. _`ib_modify_device`:

ib_modify_device
================

.. c:function:: int ib_modify_device(struct ib_device *device, int device_modify_mask, struct ib_device_modify *device_modify)

    Change IB device attributes

    :param struct ib_device \*device:
        Device to modify

    :param int device_modify_mask:
        Mask of attributes to change

    :param struct ib_device_modify \*device_modify:
        New attribute values

.. _`ib_modify_device.description`:

Description
-----------

ib_modify_device() changes a device's attributes as specified by
the \ ``device_modify_mask``\  and \ ``device_modify``\  structure.

.. _`ib_modify_port`:

ib_modify_port
==============

.. c:function:: int ib_modify_port(struct ib_device *device, u8 port_num, int port_modify_mask, struct ib_port_modify *port_modify)

    Modifies the attributes for the specified port.

    :param struct ib_device \*device:
        The device to modify.

    :param u8 port_num:
        The number of the port to modify.

    :param int port_modify_mask:
        Mask used to specify which attributes of the port
        to change.

    :param struct ib_port_modify \*port_modify:
        New attribute values for the port.

.. _`ib_modify_port.description`:

Description
-----------

ib_modify_port() changes a port's attributes as specified by the
\ ``port_modify_mask``\  and \ ``port_modify``\  structure.

.. _`ib_find_gid`:

ib_find_gid
===========

.. c:function:: int ib_find_gid(struct ib_device *device, union ib_gid *gid, enum ib_gid_type gid_type, struct net_device *ndev, u8 *port_num, u16 *index)

    Returns the port number and GID table index where a specified GID value occurs.

    :param struct ib_device \*device:
        The device to query.

    :param union ib_gid \*gid:
        The GID value to search for.

    :param enum ib_gid_type gid_type:
        Type of GID.

    :param struct net_device \*ndev:
        The ndev related to the GID to search for.

    :param u8 \*port_num:
        The port number of the device where the GID value was found.

    :param u16 \*index:
        The index into the GID table where the GID was found.  This
        parameter may be NULL.

.. _`ib_find_pkey`:

ib_find_pkey
============

.. c:function:: int ib_find_pkey(struct ib_device *device, u8 port_num, u16 pkey, u16 *index)

    Returns the PKey table index where a specified PKey value occurs.

    :param struct ib_device \*device:
        The device to query.

    :param u8 port_num:
        The port number of the device to search for the PKey.

    :param u16 pkey:
        The PKey value to search for.

    :param u16 \*index:
        The index into the PKey table where the PKey was found.

.. _`ib_get_net_dev_by_params`:

ib_get_net_dev_by_params
========================

.. c:function:: struct net_device *ib_get_net_dev_by_params(struct ib_device *dev, u8 port, u16 pkey, const union ib_gid *gid, const struct sockaddr *addr)

    Return the appropriate net_dev for a received CM request

    :param struct ib_device \*dev:
        An RDMA device on which the request has been received.

    :param u8 port:
        Port number on the RDMA device.

    :param u16 pkey:
        The Pkey the request came on.

    :param const union ib_gid \*gid:
        A GID that the net_dev uses to communicate.

    :param const struct sockaddr \*addr:
        Contains the IP address that the request specified as its
        destination.

.. This file was automatic generated / don't edit.

