.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/ib_cache.h

.. _`ib_get_cached_pkey`:

ib_get_cached_pkey
==================

.. c:function:: int ib_get_cached_pkey(struct ib_device *device_handle, u8 port_num, int index, u16 *pkey)

    Returns a cached PKey table entry

    :param device_handle:
        *undescribed*
    :type device_handle: struct ib_device \*

    :param port_num:
        The port number of the device to query.
    :type port_num: u8

    :param index:
        The index into the cached PKey table to query.
    :type index: int

    :param pkey:
        The PKey value found at the specified index.
    :type pkey: u16 \*

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

    :param device:
        The device to query.
    :type device: struct ib_device \*

    :param port_num:
        The port number of the device to search for the PKey.
    :type port_num: u8

    :param pkey:
        The PKey value to search for.
    :type pkey: u16

    :param index:
        The index into the cached PKey table where the PKey was found.
    :type index: u16 \*

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

    :param device:
        The device to query.
    :type device: struct ib_device \*

    :param port_num:
        The port number of the device to search for the PKey.
    :type port_num: u8

    :param pkey:
        The PKey value to search for.
    :type pkey: u16

    :param index:
        The index into the cached PKey table where the PKey was found.
    :type index: u16 \*

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

    :param device:
        The device to query.
    :type device: struct ib_device \*

    :param port_num:
        The port number of the device to query.
    :type port_num: u8

    :param lmc:
        The lmc value for the specified port for that device.
    :type lmc: u8 \*

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

    :param device:
        The device to query.
    :type device: struct ib_device \*

    :param port_num:
        The port number of the device to query.
    :type port_num: u8

    :param port_active:
        *undescribed*
    :type port_active: enum ib_port_state \*

.. _`ib_get_cached_port_state.description`:

Description
-----------

\ :c:func:`ib_get_cached_port_state`\  fetches the specified port_state table entry stored in
the local software cache.

.. This file was automatic generated / don't edit.

