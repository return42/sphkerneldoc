.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/cache.c

.. _`free_gid_work`:

free_gid_work
=============

.. c:function:: void free_gid_work(struct work_struct *work)

    Release reference to the GID entry

    :param work:
        Work structure to refer to GID entry which needs to be
        deleted.
    :type work: struct work_struct \*

.. _`free_gid_work.description`:

Description
-----------

\ :c:func:`free_gid_work`\  frees the entry from the HCA's hardware table
if provider supports it. It releases reference to netdevice.

.. _`del_gid`:

del_gid
=======

.. c:function:: void del_gid(struct ib_device *ib_dev, u8 port, struct ib_gid_table *table, int ix)

    Delete GID table entry

    :param ib_dev:
        IB device whose GID entry to be deleted
    :type ib_dev: struct ib_device \*

    :param port:
        Port number of the IB device
    :type port: u8

    :param table:
        GID table of the IB device for a port
    :type table: struct ib_gid_table \*

    :param ix:
        GID entry index to delete
    :type ix: int

.. _`add_modify_gid`:

add_modify_gid
==============

.. c:function:: int add_modify_gid(struct ib_gid_table *table, const struct ib_gid_attr *attr)

    Add or modify GID table entry

    :param table:
        GID table in which GID to be added or modified
    :type table: struct ib_gid_table \*

    :param attr:
        Attributes of the GID
    :type attr: const struct ib_gid_attr \*

.. _`add_modify_gid.description`:

Description
-----------

Returns 0 on success or appropriate error code. It accepts zero
GID addition for non RoCE ports for HCA's who report them as valid
GID. However such zero GIDs are not added to the cache.

.. _`rdma_find_gid_by_port`:

rdma_find_gid_by_port
=====================

.. c:function:: const struct ib_gid_attr *rdma_find_gid_by_port(struct ib_device *ib_dev, const union ib_gid *gid, enum ib_gid_type gid_type, u8 port, struct net_device *ndev)

    Returns the GID entry attributes when it finds a valid GID entry for given search parameters. It searches for the specified GID value in the local software cache.

    :param ib_dev:
        *undescribed*
    :type ib_dev: struct ib_device \*

    :param gid:
        The GID value to search for.
    :type gid: const union ib_gid \*

    :param gid_type:
        The GID type to search for.
    :type gid_type: enum ib_gid_type

    :param port:
        *undescribed*
    :type port: u8

    :param ndev:
        In RoCE, the net device of the device. NULL means ignore.
    :type ndev: struct net_device \*

.. _`rdma_find_gid_by_port.description`:

Description
-----------

Returns sgid attributes if the GID is found with valid reference or
returns ERR_PTR for the error.
The caller must invoke \ :c:func:`rdma_put_gid_attr`\  to release the reference.

.. _`rdma_find_gid_by_filter`:

rdma_find_gid_by_filter
=======================

.. c:function:: const struct ib_gid_attr *rdma_find_gid_by_filter(struct ib_device *ib_dev, const union ib_gid *gid, u8 port, bool (*filter)(const union ib_gid *gid, const struct ib_gid_attr *, void *), void *context)

    Returns the GID table attribute where a specified GID value occurs

    :param ib_dev:
        *undescribed*
    :type ib_dev: struct ib_device \*

    :param gid:
        The GID value to search for.
    :type gid: const union ib_gid \*

    :param port:
        The port number of the device where the GID value could be
        searched.
    :type port: u8

    :param bool (\*filter)(const union ib_gid \*gid, const struct ib_gid_attr \*, void \*):
        The filter function is executed on any matching GID in the table.
        If the filter function returns true, the corresponding index is returned,
        otherwise, we continue searching the GID table. It's guaranteed that
        while filter is executed, ndev field is valid and the structure won't
        change. filter is executed in an atomic context. filter must not be NULL.

    :param context:
        *undescribed*
    :type context: void \*

.. _`rdma_find_gid_by_filter.description`:

Description
-----------

\ :c:func:`rdma_find_gid_by_filter`\  searches for the specified GID value
of which the filter function returns true in the port's GID table.

.. _`rdma_query_gid`:

rdma_query_gid
==============

.. c:function:: int rdma_query_gid(struct ib_device *device, u8 port_num, int index, union ib_gid *gid)

    Read the GID content from the GID software cache

    :param device:
        Device to query the GID
    :type device: struct ib_device \*

    :param port_num:
        Port number of the device
    :type port_num: u8

    :param index:
        Index of the GID table entry to read
    :type index: int

    :param gid:
        Pointer to GID where to store the entry's GID
    :type gid: union ib_gid \*

.. _`rdma_query_gid.description`:

Description
-----------

\ :c:func:`rdma_query_gid`\  only reads the GID entry content for requested device,
port and index. It reads for IB, RoCE and iWarp link layers.  It doesn't
hold any reference to the GID table entry in the HCA or software cache.

Returns 0 on success or appropriate error code.

.. _`rdma_find_gid`:

rdma_find_gid
=============

.. c:function:: const struct ib_gid_attr *rdma_find_gid(struct ib_device *device, const union ib_gid *gid, enum ib_gid_type gid_type, struct net_device *ndev)

    Returns SGID attributes if the matching GID is found.

    :param device:
        The device to query.
    :type device: struct ib_device \*

    :param gid:
        The GID value to search for.
    :type gid: const union ib_gid \*

    :param gid_type:
        The GID type to search for.
    :type gid_type: enum ib_gid_type

    :param ndev:
        In RoCE, the net device of the device. NULL means ignore.
    :type ndev: struct net_device \*

.. _`rdma_find_gid.description`:

Description
-----------

\ :c:func:`rdma_find_gid`\  searches for the specified GID value in the software cache.

Returns GID attributes if a valid GID is found or returns ERR_PTR for the
error. The caller must invoke \ :c:func:`rdma_put_gid_attr`\  to release the reference.

.. _`rdma_get_gid_attr`:

rdma_get_gid_attr
=================

.. c:function:: const struct ib_gid_attr *rdma_get_gid_attr(struct ib_device *device, u8 port_num, int index)

    Returns GID attributes for a port of a device at a requested gid_index, if a valid GID entry exists.

    :param device:
        The device to query.
    :type device: struct ib_device \*

    :param port_num:
        The port number on the device where the GID value
        is to be queried.
    :type port_num: u8

    :param index:
        Index of the GID table entry whose attributes are to
        be queried.
    :type index: int

.. _`rdma_get_gid_attr.description`:

Description
-----------

\ :c:func:`rdma_get_gid_attr`\  acquires reference count of gid attributes from the
cached GID table. Caller must invoke \ :c:func:`rdma_put_gid_attr`\  to release
reference to gid attribute regardless of link layer.

Returns pointer to valid gid attribute or ERR_PTR for the appropriate error
code.

.. _`rdma_put_gid_attr`:

rdma_put_gid_attr
=================

.. c:function:: void rdma_put_gid_attr(const struct ib_gid_attr *attr)

    Release reference to the GID attribute

    :param attr:
        Pointer to the GID attribute whose reference
        needs to be released.
    :type attr: const struct ib_gid_attr \*

.. _`rdma_put_gid_attr.description`:

Description
-----------

\ :c:func:`rdma_put_gid_attr`\  must be used to release reference whose
reference is acquired using \ :c:func:`rdma_get_gid_attr`\  or any APIs
which returns a pointer to the ib_gid_attr regardless of link layer
of IB or RoCE.

.. _`rdma_hold_gid_attr`:

rdma_hold_gid_attr
==================

.. c:function:: void rdma_hold_gid_attr(const struct ib_gid_attr *attr)

    Get reference to existing GID attribute

    :param attr:
        Pointer to the GID attribute whose reference
        needs to be taken.
    :type attr: const struct ib_gid_attr \*

.. _`rdma_hold_gid_attr.description`:

Description
-----------

Increase the reference count to a GID attribute to keep it from being
freed. Callers are required to already be holding a reference to attribute.

.. _`rdma_read_gid_attr_ndev_rcu`:

rdma_read_gid_attr_ndev_rcu
===========================

.. c:function:: struct net_device *rdma_read_gid_attr_ndev_rcu(const struct ib_gid_attr *attr)

    Read GID attribute netdevice which must be in UP state.

    :param attr:
        Pointer to the GID attribute
    :type attr: const struct ib_gid_attr \*

.. _`rdma_read_gid_attr_ndev_rcu.description`:

Description
-----------

Returns pointer to netdevice if the netdevice was attached to GID and
netdevice is in UP state. Caller must hold RCU lock as this API
reads the netdev flags which can change while netdevice migrates to
different net namespace. Returns ERR_PTR with error code otherwise.

.. This file was automatic generated / don't edit.

