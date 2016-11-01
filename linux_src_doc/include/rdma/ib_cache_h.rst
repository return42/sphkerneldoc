.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/ib_cache.h

.. _`ib_get_cached_gid`:

ib_get_cached_gid
=================

.. c:function:: int ib_get_cached_gid(struct ib_device *device, u8 port_num, int index, union ib_gid *gid, struct ib_gid_attr *attr)

    Returns a cached GID table entry

    :param struct ib_device \*device:
        The device to query.

    :param u8 port_num:
        The port number of the device to query.

    :param int index:
        The index into the cached GID table to query.

    :param union ib_gid \*gid:
        The GID value found at the specified index.

    :param struct ib_gid_attr \*attr:
        The GID attribute found at the specified index (only in RoCE).
        NULL means ignore (output parameter).

.. _`ib_get_cached_gid.description`:

Description
-----------

ib_get_cached_gid() fetches the specified GID table entry stored in
the local software cache.

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

ib_find_cached_gid() searches for the specified GID value in
the local software cache.

.. _`ib_find_cached_gid_by_port`:

ib_find_cached_gid_by_port
==========================

.. c:function:: int ib_find_cached_gid_by_port(struct ib_device *device, const union ib_gid *gid, enum ib_gid_type gid_type, u8 port_num, struct net_device *ndev, u16 *index)

    Returns the GID table index where a specified GID value occurs

    :param struct ib_device \*device:
        The device to query.

    :param const union ib_gid \*gid:
        The GID value to search for.

    :param enum ib_gid_type gid_type:
        The GID type to search for.

    :param u8 port_num:
        The port number of the device where the GID value sould be
        searched.

    :param struct net_device \*ndev:
        In RoCE, the net device of the device. Null means ignore.

    :param u16 \*index:
        The index into the cached GID table where the GID was found.  This
        parameter may be NULL.

.. _`ib_find_cached_gid_by_port.description`:

Description
-----------

ib_find_cached_gid() searches for the specified GID value in
the local software cache.

.. _`ib_get_cached_pkey`:

ib_get_cached_pkey
==================

.. c:function:: int ib_get_cached_pkey(struct ib_device *device_handle, u8 port_num, int index, u16 *pkey)

    Returns a cached PKey table entry

    :param struct ib_device \*device_handle:
        *undescribed*

    :param u8 port_num:
        The port number of the device to query.

    :param int index:
        The index into the cached PKey table to query.

    :param u16 \*pkey:
        The PKey value found at the specified index.

.. _`ib_get_cached_pkey.description`:

Description
-----------

ib_get_cached_pkey() fetches the specified PKey table entry stored in
the local software cache.

.. _`ib_find_cached_pkey`:

ib_find_cached_pkey
===================

.. c:function:: int ib_find_cached_pkey(struct ib_device *device, u8 port_num, u16 pkey, u16 *index)

    Returns the PKey table index where a specified PKey value occurs.

    :param struct ib_device \*device:
        The device to query.

    :param u8 port_num:
        The port number of the device to search for the PKey.

    :param u16 pkey:
        The PKey value to search for.

    :param u16 \*index:
        The index into the cached PKey table where the PKey was found.

.. _`ib_find_cached_pkey.description`:

Description
-----------

ib_find_cached_pkey() searches the specified PKey table in
the local software cache.

.. _`ib_find_exact_cached_pkey`:

ib_find_exact_cached_pkey
=========================

.. c:function:: int ib_find_exact_cached_pkey(struct ib_device *device, u8 port_num, u16 pkey, u16 *index)

    Returns the PKey table index where a specified PKey value occurs. Comparison uses the FULL 16 bits (incl membership bit)

    :param struct ib_device \*device:
        The device to query.

    :param u8 port_num:
        The port number of the device to search for the PKey.

    :param u16 pkey:
        The PKey value to search for.

    :param u16 \*index:
        The index into the cached PKey table where the PKey was found.

.. _`ib_find_exact_cached_pkey.description`:

Description
-----------

ib_find_exact_cached_pkey() searches the specified PKey table in
the local software cache.

.. _`ib_get_cached_lmc`:

ib_get_cached_lmc
=================

.. c:function:: int ib_get_cached_lmc(struct ib_device *device, u8 port_num, u8 *lmc)

    Returns a cached lmc table entry

    :param struct ib_device \*device:
        The device to query.

    :param u8 port_num:
        The port number of the device to query.

    :param u8 \*lmc:
        The lmc value for the specified port for that device.

.. _`ib_get_cached_lmc.description`:

Description
-----------

ib_get_cached_lmc() fetches the specified lmc table entry stored in
the local software cache.

.. This file was automatic generated / don't edit.

