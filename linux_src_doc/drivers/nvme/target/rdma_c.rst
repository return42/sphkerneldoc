.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/target/rdma.c

.. _`nvmet_rdma_device_removal`:

nvmet_rdma_device_removal
=========================

.. c:function:: int nvmet_rdma_device_removal(struct rdma_cm_id *cm_id, struct nvmet_rdma_queue *queue)

    Handle RDMA device removal

    :param struct rdma_cm_id \*cm_id:
        rdma_cm id, used for nvmet port

    :param struct nvmet_rdma_queue \*queue:
        nvmet rdma queue (cm id qp_context)

.. _`nvmet_rdma_device_removal.description`:

Description
-----------

DEVICE_REMOVAL event notifies us that the RDMA device is about
to unplug. Note that this event can be generated on a normal
queue cm_id and/or a device bound listener cm_id (where in this
case queue will be null).

We registered an ib_client to handle device removal for queues,
so we only need to handle the listening port cm_ids. In this case
we nullify the priv to prevent double cm_id destruction and destroying
the cm_id implicitely by returning a non-zero rc to the callout.

.. This file was automatic generated / don't edit.

