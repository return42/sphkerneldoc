.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_verbs.c

.. _`pvrdma_query_device`:

pvrdma_query_device
===================

.. c:function:: int pvrdma_query_device(struct ib_device *ibdev, struct ib_device_attr *props, struct ib_udata *uhw)

    query device

    :param struct ib_device \*ibdev:
        the device to query

    :param struct ib_device_attr \*props:
        the device properties

    :param struct ib_udata \*uhw:
        user data

.. _`pvrdma_query_port`:

pvrdma_query_port
=================

.. c:function:: int pvrdma_query_port(struct ib_device *ibdev, u8 port, struct ib_port_attr *props)

    query device port attributes

    :param struct ib_device \*ibdev:
        the device to query

    :param u8 port:
        the port number

    :param struct ib_port_attr \*props:
        the device properties

.. _`pvrdma_query_gid`:

pvrdma_query_gid
================

.. c:function:: int pvrdma_query_gid(struct ib_device *ibdev, u8 port, int index, union ib_gid *gid)

    query device gid

    :param struct ib_device \*ibdev:
        the device to query

    :param u8 port:
        the port number

    :param int index:
        the index

    :param union ib_gid \*gid:
        the device gid value

.. _`pvrdma_query_pkey`:

pvrdma_query_pkey
=================

.. c:function:: int pvrdma_query_pkey(struct ib_device *ibdev, u8 port, u16 index, u16 *pkey)

    query device port's P_Key table

    :param struct ib_device \*ibdev:
        the device to query

    :param u8 port:
        the port number

    :param u16 index:
        the index

    :param u16 \*pkey:
        the device P_Key value

.. _`pvrdma_modify_port`:

pvrdma_modify_port
==================

.. c:function:: int pvrdma_modify_port(struct ib_device *ibdev, u8 port, int mask, struct ib_port_modify *props)

    modify device port attributes

    :param struct ib_device \*ibdev:
        the device to modify

    :param u8 port:
        the port number

    :param int mask:
        attributes to modify

    :param struct ib_port_modify \*props:
        the device properties

.. _`pvrdma_alloc_ucontext`:

pvrdma_alloc_ucontext
=====================

.. c:function:: struct ib_ucontext *pvrdma_alloc_ucontext(struct ib_device *ibdev, struct ib_udata *udata)

    allocate ucontext

    :param struct ib_device \*ibdev:
        the IB device

    :param struct ib_udata \*udata:
        user data

.. _`pvrdma_dealloc_ucontext`:

pvrdma_dealloc_ucontext
=======================

.. c:function:: int pvrdma_dealloc_ucontext(struct ib_ucontext *ibcontext)

    deallocate ucontext

    :param struct ib_ucontext \*ibcontext:
        the ucontext

.. _`pvrdma_mmap`:

pvrdma_mmap
===========

.. c:function:: int pvrdma_mmap(struct ib_ucontext *ibcontext, struct vm_area_struct *vma)

    create mmap region

    :param struct ib_ucontext \*ibcontext:
        the user context

    :param struct vm_area_struct \*vma:
        the VMA

.. _`pvrdma_alloc_pd`:

pvrdma_alloc_pd
===============

.. c:function:: struct ib_pd *pvrdma_alloc_pd(struct ib_device *ibdev, struct ib_ucontext *context, struct ib_udata *udata)

    allocate protection domain

    :param struct ib_device \*ibdev:
        the IB device

    :param struct ib_ucontext \*context:
        user context

    :param struct ib_udata \*udata:
        user data

.. _`pvrdma_dealloc_pd`:

pvrdma_dealloc_pd
=================

.. c:function:: int pvrdma_dealloc_pd(struct ib_pd *pd)

    deallocate protection domain

    :param struct ib_pd \*pd:
        the protection domain to be released

.. _`pvrdma_create_ah`:

pvrdma_create_ah
================

.. c:function:: struct ib_ah *pvrdma_create_ah(struct ib_pd *pd, struct rdma_ah_attr *ah_attr, struct ib_udata *udata)

    create an address handle

    :param struct ib_pd \*pd:
        the protection domain

    :param struct rdma_ah_attr \*ah_attr:
        the attributes of the AH

    :param struct ib_udata \*udata:
        user data blob

.. _`pvrdma_destroy_ah`:

pvrdma_destroy_ah
=================

.. c:function:: int pvrdma_destroy_ah(struct ib_ah *ah)

    destroy an address handle

    :param struct ib_ah \*ah:
        the address handle to destroyed

.. This file was automatic generated / don't edit.

