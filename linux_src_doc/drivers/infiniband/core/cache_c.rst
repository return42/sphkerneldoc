.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/cache.c

.. _`add_modify_gid`:

add_modify_gid
==============

.. c:function:: int add_modify_gid(struct ib_gid_table *table, const union ib_gid *gid, const struct ib_gid_attr *attr)

    Add or modify GID table entry

    :param struct ib_gid_table \*table:
        GID table in which GID to be added or modified

    :param const union ib_gid \*gid:
        GID content

    :param const struct ib_gid_attr \*attr:
        Attributes of the GID

.. _`add_modify_gid.description`:

Description
-----------

Returns 0 on success or appropriate error code. It accepts zero
GID addition for non RoCE ports for HCA's who report them as valid
GID. However such zero GIDs are not added to the cache.

.. _`del_gid`:

del_gid
=======

.. c:function:: void del_gid(struct ib_device *ib_dev, u8 port, struct ib_gid_table *table, int ix)

    Delete GID table entry

    :param struct ib_device \*ib_dev:
        IB device whose GID entry to be deleted

    :param u8 port:
        Port number of the IB device

    :param struct ib_gid_table \*table:
        GID table of the IB device for a port

    :param int ix:
        GID entry index to delete

.. _`ib_find_cached_gid_by_port`:

ib_find_cached_gid_by_port
==========================

.. c:function:: int ib_find_cached_gid_by_port(struct ib_device *ib_dev, const union ib_gid *gid, enum ib_gid_type gid_type, u8 port, struct net_device *ndev, u16 *index)

    Returns the GID table index where a specified GID value occurs. It searches for the specified GID value in the local software cache.

    :param struct ib_device \*ib_dev:
        *undescribed*

    :param const union ib_gid \*gid:
        The GID value to search for.

    :param enum ib_gid_type gid_type:
        The GID type to search for.

    :param u8 port:
        *undescribed*

    :param struct net_device \*ndev:
        In RoCE, the net device of the device. Null means ignore.

    :param u16 \*index:
        The index into the cached GID table where the GID was found. This
        parameter may be NULL.

.. _`ib_cache_gid_find_by_filter`:

ib_cache_gid_find_by_filter
===========================

.. c:function:: int ib_cache_gid_find_by_filter(struct ib_device *ib_dev, const union ib_gid *gid, u8 port, bool (*filter)(const union ib_gid *, const struct ib_gid_attr *, void *), void *context, u16 *index)

    Returns the GID table index where a specified GID value occurs

    :param struct ib_device \*ib_dev:
        *undescribed*

    :param const union ib_gid \*gid:
        The GID value to search for.

    :param u8 port:
        *undescribed*

    :param bool (\*filter)(const union ib_gid \*, const struct ib_gid_attr \*, void \*):
        The filter function is executed on any matching GID in the table.
        If the filter function returns true, the corresponding index is returned,
        otherwise, we continue searching the GID table. It's guaranteed that
        while filter is executed, ndev field is valid and the structure won't
        change. filter is executed in an atomic context. filter must not be NULL.

    :param void \*context:
        *undescribed*

    :param u16 \*index:
        The index into the cached GID table where the GID was found. This
        parameter may be NULL.

.. _`ib_cache_gid_find_by_filter.description`:

Description
-----------

\ :c:func:`ib_cache_gid_find_by_filter`\  searches for the specified GID value
of which the filter function returns true in the port's GID table.
This function is only supported on RoCE ports.

.. _`ib_find_cached_gid`:

ib_find_cached_gid
==================

.. c:function:: int ib_find_cached_gid(struct ib_device *device, const union ib_gid *gid, enum ib_gid_type gid_type, struct net_device *ndev, u8 *port_num, u16 *index)

    Returns the port number and GID table index where a specified GID value occurs.

    :param struct ib_device \*device:
        The device to query.

    :param const union ib_gid \*gid:
        The GID value to search for.

    :param enum ib_gid_type gid_type:
        The GID type to search for.

    :param struct net_device \*ndev:
        In RoCE, the net device of the device. NULL means ignore.

    :param u8 \*port_num:
        The port number of the device where the GID value was found.

    :param u16 \*index:
        The index into the cached GID table where the GID was found.  This
        parameter may be NULL.

.. _`ib_find_cached_gid.description`:

Description
-----------

\ :c:func:`ib_find_cached_gid`\  searches for the specified GID value in
the local software cache.

.. This file was automatic generated / don't edit.

