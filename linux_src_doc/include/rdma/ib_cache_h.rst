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

\ :c:func:`ib_get_cached_gid`\  fetches the specified GID table entry stored in
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

\ :c:func:`ib_get_cached_pkey`\  fetches the specified PKey table entry stored in
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

\ :c:func:`ib_find_cached_pkey`\  searches the specified PKey table in
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

\ :c:func:`ib_find_exact_cached_pkey`\  searches the specified PKey table in
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

\ :c:func:`ib_get_cached_lmc`\  fetches the specified lmc table entry stored in
the local software cache.

.. _`ib_get_cached_port_state`:

ib_get_cached_port_state
========================

.. c:function:: int ib_get_cached_port_state(struct ib_device *device, u8 port_num, enum ib_port_state *port_active)

    Returns a cached port state table entry

    :param struct ib_device \*device:
        The device to query.

    :param u8 port_num:
        The port number of the device to query.

    :param enum ib_port_state \*port_active:
        *undescribed*

.. _`ib_get_cached_port_state.description`:

Description
-----------

\ :c:func:`ib_get_cached_port_state`\  fetches the specified port_state table entry stored in
the local software cache.

.. This file was automatic generated / don't edit.

