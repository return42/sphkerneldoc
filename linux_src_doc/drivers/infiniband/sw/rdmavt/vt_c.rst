.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/vt.c

.. _`rvt_alloc_device`:

rvt_alloc_device
================

.. c:function:: struct rvt_dev_info *rvt_alloc_device(size_t size, int nports)

    allocate rdi

    :param size:
        how big of a structure to allocate
    :type size: size_t

    :param nports:
        number of ports to allocate array slots for
    :type nports: int

.. _`rvt_alloc_device.description`:

Description
-----------

Use IB core device alloc to allocate space for the rdi which is assumed to be
inside of the ib_device. Any extra space that drivers require should be
included in size.

We also allocate a port array based on the number of ports.

.. _`rvt_alloc_device.return`:

Return
------

pointer to allocated rdi

.. _`rvt_dealloc_device`:

rvt_dealloc_device
==================

.. c:function:: void rvt_dealloc_device(struct rvt_dev_info *rdi)

    deallocate rdi

    :param rdi:
        structure to free
    :type rdi: struct rvt_dev_info \*

.. _`rvt_dealloc_device.description`:

Description
-----------

Free a structure allocated with \ :c:func:`rvt_alloc_device`\ 

.. _`rvt_query_port`:

rvt_query_port
==============

.. c:function:: int rvt_query_port(struct ib_device *ibdev, u8 port_num, struct ib_port_attr *props)

    Passes the query port call to the driver

    :param ibdev:
        Verbs IB dev
    :type ibdev: struct ib_device \*

    :param port_num:
        port number, 1 based from ib core
    :type port_num: u8

    :param props:
        structure to hold returned properties
    :type props: struct ib_port_attr \*

.. _`rvt_query_port.return`:

Return
------

0 on success

.. _`rvt_modify_port`:

rvt_modify_port
===============

.. c:function:: int rvt_modify_port(struct ib_device *ibdev, u8 port_num, int port_modify_mask, struct ib_port_modify *props)

    :param ibdev:
        Verbs IB dev
    :type ibdev: struct ib_device \*

    :param port_num:
        Port number, 1 based from ib core
    :type port_num: u8

    :param port_modify_mask:
        How to change the port
    :type port_modify_mask: int

    :param props:
        Structure to fill in
    :type props: struct ib_port_modify \*

.. _`rvt_modify_port.return`:

Return
------

0 on success

.. _`rvt_query_pkey`:

rvt_query_pkey
==============

.. c:function:: int rvt_query_pkey(struct ib_device *ibdev, u8 port_num, u16 index, u16 *pkey)

    Return a pkey from the table at a given index

    :param ibdev:
        Verbs IB dev
    :type ibdev: struct ib_device \*

    :param port_num:
        Port number, 1 based from ib core
    :type port_num: u8

    :param index:
        Index into pkey table
    :type index: u16

    :param pkey:
        returned pkey from the port pkey table
    :type pkey: u16 \*

.. _`rvt_query_pkey.return`:

Return
------

0 on failure pkey otherwise

.. _`rvt_query_gid`:

rvt_query_gid
=============

.. c:function:: int rvt_query_gid(struct ib_device *ibdev, u8 port_num, int guid_index, union ib_gid *gid)

    Return a gid from the table

    :param ibdev:
        Verbs IB dev
    :type ibdev: struct ib_device \*

    :param port_num:
        Port number, 1 based from ib core
    :type port_num: u8

    :param guid_index:
        Index in table
    :type guid_index: int

    :param gid:
        Gid to return
    :type gid: union ib_gid \*

.. _`rvt_query_gid.return`:

Return
------

0 on success

.. _`rvt_alloc_ucontext`:

rvt_alloc_ucontext
==================

.. c:function:: struct ib_ucontext *rvt_alloc_ucontext(struct ib_device *ibdev, struct ib_udata *udata)

    Allocate a user context

    :param ibdev:
        Verbs IB dev
    :type ibdev: struct ib_device \*

    :param udata:
        User data allocated
    :type udata: struct ib_udata \*

.. _`rvt_dealloc_ucontext`:

rvt_dealloc_ucontext
====================

.. c:function:: int rvt_dealloc_ucontext(struct ib_ucontext *context)

    Free a user context \ ``context``\  - Free this

    :param context:
        *undescribed*
    :type context: struct ib_ucontext \*

.. _`rvt_register_device`:

rvt_register_device
===================

.. c:function:: int rvt_register_device(struct rvt_dev_info *rdi, u32 driver_id)

    register a driver

    :param rdi:
        main dev structure for all of rdmavt operations
    :type rdi: struct rvt_dev_info \*

    :param driver_id:
        *undescribed*
    :type driver_id: u32

.. _`rvt_register_device.description`:

Description
-----------

It is up to drivers to allocate the rdi and fill in the appropriate
information.

.. _`rvt_register_device.return`:

Return
------

0 on success otherwise an errno.

.. _`rvt_unregister_device`:

rvt_unregister_device
=====================

.. c:function:: void rvt_unregister_device(struct rvt_dev_info *rdi)

    remove a driver

    :param rdi:
        rvt dev struct
    :type rdi: struct rvt_dev_info \*

.. _`rvt_init_port`:

rvt_init_port
=============

.. c:function:: int rvt_init_port(struct rvt_dev_info *rdi, struct rvt_ibport *port, int port_index, u16 *pkey_table)

    init internal data for driver port

    :param rdi:
        rvt dev strut
    :type rdi: struct rvt_dev_info \*

    :param port:
        rvt port
    :type port: struct rvt_ibport \*

    :param port_index:
        0 based index of ports, different from IB core port num
    :type port_index: int

    :param pkey_table:
        *undescribed*
    :type pkey_table: u16 \*

.. _`rvt_init_port.description`:

Description
-----------

Keep track of a list of ports. No need to have a detach port.
They persist until the driver goes away.

.. _`rvt_init_port.return`:

Return
------

always 0

.. This file was automatic generated / don't edit.

