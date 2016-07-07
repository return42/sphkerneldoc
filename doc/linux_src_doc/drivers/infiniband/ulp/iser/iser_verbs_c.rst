.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/iser/iser_verbs.c

.. _`iser_create_device_ib_res`:

iser_create_device_ib_res
=========================

.. c:function:: int iser_create_device_ib_res(struct iser_device *device)

    creates Protection Domain (PD), Completion Queue (CQ), DMA Memory Region (DMA MR) with the device associated with the adapator.

    :param struct iser_device \*device:
        *undescribed*

.. _`iser_create_device_ib_res.description`:

Description
-----------

returns 0 on success, -1 on failure

.. _`iser_free_device_ib_res`:

iser_free_device_ib_res
=======================

.. c:function:: void iser_free_device_ib_res(struct iser_device *device)

    destroy/dealloc/dereg the DMA MR, CQ and PD created with the device associated with the adapator.

    :param struct iser_device \*device:
        *undescribed*

.. _`iser_alloc_fmr_pool`:

iser_alloc_fmr_pool
===================

.. c:function:: int iser_alloc_fmr_pool(struct ib_conn *ib_conn, unsigned cmds_max, unsigned int size)

    Creates FMR pool and page_vector

    :param struct ib_conn \*ib_conn:
        *undescribed*

    :param unsigned cmds_max:
        *undescribed*

    :param unsigned int size:
        *undescribed*

.. _`iser_alloc_fmr_pool.description`:

Description
-----------

returns 0 on success, or errno code on failure

.. _`iser_free_fmr_pool`:

iser_free_fmr_pool
==================

.. c:function:: void iser_free_fmr_pool(struct ib_conn *ib_conn)

    releases the FMR pool and page vec

    :param struct ib_conn \*ib_conn:
        *undescribed*

.. _`iser_alloc_fastreg_pool`:

iser_alloc_fastreg_pool
=======================

.. c:function:: int iser_alloc_fastreg_pool(struct ib_conn *ib_conn, unsigned cmds_max, unsigned int size)

    Creates pool of fast_reg descriptors for fast registration work requests. returns 0 on success, or errno code on failure

    :param struct ib_conn \*ib_conn:
        *undescribed*

    :param unsigned cmds_max:
        *undescribed*

    :param unsigned int size:
        *undescribed*

.. _`iser_free_fastreg_pool`:

iser_free_fastreg_pool
======================

.. c:function:: void iser_free_fastreg_pool(struct ib_conn *ib_conn)

    releases the pool of fast_reg descriptors

    :param struct ib_conn \*ib_conn:
        *undescribed*

.. _`iser_create_ib_conn_res`:

iser_create_ib_conn_res
=======================

.. c:function:: int iser_create_ib_conn_res(struct ib_conn *ib_conn)

    Queue-Pair (QP)

    :param struct ib_conn \*ib_conn:
        *undescribed*

.. _`iser_create_ib_conn_res.description`:

Description
-----------

returns 0 on success, -1 on failure

.. _`iser_device_find_by_ib_device`:

iser_device_find_by_ib_device
=============================

.. c:function:: struct iser_device *iser_device_find_by_ib_device(struct rdma_cm_id *cma_id)

    device for this device. If there's no such, create one.

    :param struct rdma_cm_id \*cma_id:
        *undescribed*

.. _`iser_conn_state_comp_exch`:

iser_conn_state_comp_exch
=========================

.. c:function:: int iser_conn_state_comp_exch(struct iser_conn *iser_conn, enum iser_conn_state comp, enum iser_conn_state exch)

    :param struct iser_conn \*iser_conn:
        *undescribed*

    :param enum iser_conn_state comp:
        *undescribed*

    :param enum iser_conn_state exch:
        *undescribed*

.. _`iser_free_ib_conn_res`:

iser_free_ib_conn_res
=====================

.. c:function:: void iser_free_ib_conn_res(struct iser_conn *iser_conn, bool destroy)

    release IB related resources

    :param struct iser_conn \*iser_conn:
        iser connection struct

    :param bool destroy:
        indicator if we need to try to release the
        iser device and memory regoins pool (only iscsi
        shutdown and DEVICE_REMOVAL will use this).

.. _`iser_free_ib_conn_res.description`:

Description
-----------

This routine is called with the iser state mutex held
so the cm_id removal is out of here. It is Safe to
be invoked multiple times.

.. _`iser_conn_release`:

iser_conn_release
=================

.. c:function:: void iser_conn_release(struct iser_conn *iser_conn)

    :param struct iser_conn \*iser_conn:
        *undescribed*

.. _`iser_conn_terminate`:

iser_conn_terminate
===================

.. c:function:: int iser_conn_terminate(struct iser_conn *iser_conn)

    Called with state mutex held

    :param struct iser_conn \*iser_conn:
        *undescribed*

.. _`iser_connect_error`:

iser_connect_error
==================

.. c:function:: void iser_connect_error(struct rdma_cm_id *cma_id)

    :param struct rdma_cm_id \*cma_id:
        *undescribed*

.. _`iser_addr_handler`:

iser_addr_handler
=================

.. c:function:: void iser_addr_handler(struct rdma_cm_id *cma_id)

    :param struct rdma_cm_id \*cma_id:
        *undescribed*

.. _`iser_route_handler`:

iser_route_handler
==================

.. c:function:: void iser_route_handler(struct rdma_cm_id *cma_id)

    :param struct rdma_cm_id \*cma_id:
        *undescribed*

.. _`iser_post_send`:

iser_post_send
==============

.. c:function:: int iser_post_send(struct ib_conn *ib_conn, struct iser_tx_desc *tx_desc, bool signal)

    Initiate a Send DTO operation

    :param struct ib_conn \*ib_conn:
        *undescribed*

    :param struct iser_tx_desc \*tx_desc:
        *undescribed*

    :param bool signal:
        *undescribed*

.. _`iser_post_send.description`:

Description
-----------

returns 0 on success, -1 on failure

.. This file was automatic generated / don't edit.

