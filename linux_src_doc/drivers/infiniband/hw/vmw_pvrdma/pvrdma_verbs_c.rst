.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_verbs.c

.. _`pvrdma_query_device`:

pvrdma_query_device
===================

.. c:function:: int pvrdma_query_device(struct ib_device *ibdev, struct ib_device_attr *props, struct ib_udata *uhw)

    query device

    :param ibdev:
        the device to query
    :type ibdev: struct ib_device \*

    :param props:
        the device properties
    :type props: struct ib_device_attr \*

    :param uhw:
        user data
    :type uhw: struct ib_udata \*

.. _`pvrdma_query_port`:

pvrdma_query_port
=================

.. c:function:: int pvrdma_query_port(struct ib_device *ibdev, u8 port, struct ib_port_attr *props)

    query device port attributes

    :param ibdev:
        the device to query
    :type ibdev: struct ib_device \*

    :param port:
        the port number
    :type port: u8

    :param props:
        the device properties
    :type props: struct ib_port_attr \*

.. _`pvrdma_query_gid`:

pvrdma_query_gid
================

.. c:function:: int pvrdma_query_gid(struct ib_device *ibdev, u8 port, int index, union ib_gid *gid)

    query device gid

    :param ibdev:
        the device to query
    :type ibdev: struct ib_device \*

    :param port:
        the port number
    :type port: u8

    :param index:
        the index
    :type index: int

    :param gid:
        the device gid value
    :type gid: union ib_gid \*

.. _`pvrdma_query_pkey`:

pvrdma_query_pkey
=================

.. c:function:: int pvrdma_query_pkey(struct ib_device *ibdev, u8 port, u16 index, u16 *pkey)

    query device port's P_Key table

    :param ibdev:
        the device to query
    :type ibdev: struct ib_device \*

    :param port:
        the port number
    :type port: u8

    :param index:
        the index
    :type index: u16

    :param pkey:
        the device P_Key value
    :type pkey: u16 \*

.. _`pvrdma_modify_port`:

pvrdma_modify_port
==================

.. c:function:: int pvrdma_modify_port(struct ib_device *ibdev, u8 port, int mask, struct ib_port_modify *props)

    modify device port attributes

    :param ibdev:
        the device to modify
    :type ibdev: struct ib_device \*

    :param port:
        the port number
    :type port: u8

    :param mask:
        attributes to modify
    :type mask: int

    :param props:
        the device properties
    :type props: struct ib_port_modify \*

.. _`pvrdma_alloc_ucontext`:

pvrdma_alloc_ucontext
=====================

.. c:function:: struct ib_ucontext *pvrdma_alloc_ucontext(struct ib_device *ibdev, struct ib_udata *udata)

    allocate ucontext

    :param ibdev:
        the IB device
    :type ibdev: struct ib_device \*

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`pvrdma_dealloc_ucontext`:

pvrdma_dealloc_ucontext
=======================

.. c:function:: int pvrdma_dealloc_ucontext(struct ib_ucontext *ibcontext)

    deallocate ucontext

    :param ibcontext:
        the ucontext
    :type ibcontext: struct ib_ucontext \*

.. _`pvrdma_mmap`:

pvrdma_mmap
===========

.. c:function:: int pvrdma_mmap(struct ib_ucontext *ibcontext, struct vm_area_struct *vma)

    create mmap region

    :param ibcontext:
        the user context
    :type ibcontext: struct ib_ucontext \*

    :param vma:
        the VMA
    :type vma: struct vm_area_struct \*

.. _`pvrdma_alloc_pd`:

pvrdma_alloc_pd
===============

.. c:function:: struct ib_pd *pvrdma_alloc_pd(struct ib_device *ibdev, struct ib_ucontext *context, struct ib_udata *udata)

    allocate protection domain

    :param ibdev:
        the IB device
    :type ibdev: struct ib_device \*

    :param context:
        user context
    :type context: struct ib_ucontext \*

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`pvrdma_dealloc_pd`:

pvrdma_dealloc_pd
=================

.. c:function:: int pvrdma_dealloc_pd(struct ib_pd *pd)

    deallocate protection domain

    :param pd:
        the protection domain to be released
    :type pd: struct ib_pd \*

.. _`pvrdma_create_ah`:

pvrdma_create_ah
================

.. c:function:: struct ib_ah *pvrdma_create_ah(struct ib_pd *pd, struct rdma_ah_attr *ah_attr, struct ib_udata *udata)

    create an address handle

    :param pd:
        the protection domain
    :type pd: struct ib_pd \*

    :param ah_attr:
        the attributes of the AH
    :type ah_attr: struct rdma_ah_attr \*

    :param udata:
        user data blob
    :type udata: struct ib_udata \*

.. _`pvrdma_destroy_ah`:

pvrdma_destroy_ah
=================

.. c:function:: int pvrdma_destroy_ah(struct ib_ah *ah)

    destroy an address handle

    :param ah:
        the address handle to destroyed
    :type ah: struct ib_ah \*

.. This file was automatic generated / don't edit.

