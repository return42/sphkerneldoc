.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/srp/ib_srp.c

.. _`srp_destroy_fr_pool`:

srp_destroy_fr_pool
===================

.. c:function:: void srp_destroy_fr_pool(struct srp_fr_pool *pool)

    free the resources owned by a pool

    :param struct srp_fr_pool \*pool:
        Fast registration pool to be destroyed.

.. _`srp_create_fr_pool`:

srp_create_fr_pool
==================

.. c:function:: struct srp_fr_pool *srp_create_fr_pool(struct ib_device *device, struct ib_pd *pd, int pool_size, int max_page_list_len)

    allocate and initialize a pool for fast registration

    :param struct ib_device \*device:
        IB device to allocate fast registration descriptors for.

    :param struct ib_pd \*pd:
        Protection domain associated with the FR descriptors.

    :param int pool_size:
        Number of descriptors to allocate.

    :param int max_page_list_len:
        Maximum fast registration work request page list length.

.. _`srp_fr_pool_get`:

srp_fr_pool_get
===============

.. c:function:: struct srp_fr_desc *srp_fr_pool_get(struct srp_fr_pool *pool)

    obtain a descriptor suitable for fast registration

    :param struct srp_fr_pool \*pool:
        Pool to obtain descriptor from.

.. _`srp_fr_pool_put`:

srp_fr_pool_put
===============

.. c:function:: void srp_fr_pool_put(struct srp_fr_pool *pool, struct srp_fr_desc **desc, int n)

    put an FR descriptor back in the free list

    :param struct srp_fr_pool \*pool:
        Pool the descriptor was allocated from.

    :param struct srp_fr_desc \*\*desc:
        Pointer to an array of fast registration descriptor pointers.

    :param int n:
        Number of descriptors to put back.

.. _`srp_fr_pool_put.note`:

Note
----

The caller must already have queued an invalidation request for
desc->mr->rkey before calling this function.

.. _`srp_destroy_qp`:

srp_destroy_qp
==============

.. c:function:: void srp_destroy_qp(struct srp_rdma_ch *ch)

    destroy an RDMA queue pair

    :param struct srp_rdma_ch \*ch:
        SRP RDMA channel.

.. _`srp_destroy_qp.description`:

Description
-----------

Drain the qp before destroying it.  This avoids that the receive
completion handler can access the queue pair while it is
being destroyed.

.. _`srp_del_scsi_host_attr`:

srp_del_scsi_host_attr
======================

.. c:function:: void srp_del_scsi_host_attr(struct Scsi_Host *shost)

    Remove attributes defined in the host template.

    :param struct Scsi_Host \*shost:
        SCSI host whose attributes to remove from sysfs.

.. _`srp_del_scsi_host_attr.note`:

Note
----

Any attributes defined in the host template and that did not exist
before invocation of this function will be ignored.

.. _`srp_connected_ch`:

srp_connected_ch
================

.. c:function:: int srp_connected_ch(struct srp_target_port *target)

    number of connected channels

    :param struct srp_target_port \*target:
        SRP target port.

.. _`srp_claim_req`:

srp_claim_req
=============

.. c:function:: struct scsi_cmnd *srp_claim_req(struct srp_rdma_ch *ch, struct srp_request *req, struct scsi_device *sdev, struct scsi_cmnd *scmnd)

    Take ownership of the scmnd associated with a request.

    :param struct srp_rdma_ch \*ch:
        SRP RDMA channel.

    :param struct srp_request \*req:
        SRP request.

    :param struct scsi_device \*sdev:
        If not NULL, only take ownership for this SCSI device.

    :param struct scsi_cmnd \*scmnd:
        If NULL, take ownership of \ ``req``\ ->scmnd. If not NULL, only take
        ownership of \ ``req``\ ->scmnd if it equals \ ``scmnd``\ .

.. _`srp_claim_req.return-value`:

Return value
------------

Either NULL or a pointer to the SCSI command the caller became owner of.

.. _`srp_free_req`:

srp_free_req
============

.. c:function:: void srp_free_req(struct srp_rdma_ch *ch, struct srp_request *req, struct scsi_cmnd *scmnd, s32 req_lim_delta)

    Unmap data and adjust ch->req_lim.

    :param struct srp_rdma_ch \*ch:
        SRP RDMA channel.

    :param struct srp_request \*req:
        Request to be freed.

    :param struct scsi_cmnd \*scmnd:
        SCSI command associated with \ ``req``\ .

    :param s32 req_lim_delta:
        Amount to be added to \ ``target``\ ->req_lim.

.. _`srp_map_data`:

srp_map_data
============

.. c:function:: int srp_map_data(struct scsi_cmnd *scmnd, struct srp_rdma_ch *ch, struct srp_request *req)

    map SCSI data buffer onto an SRP request

    :param struct scsi_cmnd \*scmnd:
        SCSI command to map

    :param struct srp_rdma_ch \*ch:
        SRP RDMA channel

    :param struct srp_request \*req:
        SRP request

.. _`srp_map_data.description`:

Description
-----------

Returns the length in bytes of the SRP_CMD IU or a negative value if
mapping failed.

.. _`srp_tl_err_work`:

srp_tl_err_work
===============

.. c:function:: void srp_tl_err_work(struct work_struct *work)

    handle a transport layer error

    :param struct work_struct \*work:
        Work structure embedded in an SRP target port.

.. _`srp_tl_err_work.note`:

Note
----

This function may get invoked before the rport has been created,
hence the target->rport test.

.. _`srp_change_queue_depth`:

srp_change_queue_depth
======================

.. c:function:: int srp_change_queue_depth(struct scsi_device *sdev, int qdepth)

    setting device queue depth

    :param struct scsi_device \*sdev:
        scsi device struct

    :param int qdepth:
        requested queue depth

.. _`srp_change_queue_depth.description`:

Description
-----------

Returns queue depth.

.. _`srp_conn_unique`:

srp_conn_unique
===============

.. c:function:: bool srp_conn_unique(struct srp_host *host, struct srp_target_port *target)

    check whether the connection to a target is unique

    :param struct srp_host \*host:
        SRP host.

    :param struct srp_target_port \*target:
        SRP target port.

.. This file was automatic generated / don't edit.

