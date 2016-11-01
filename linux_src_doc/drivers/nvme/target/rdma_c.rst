.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/target/rdma.c

.. _`nvmet_rdma_device_removal`:

nvmet_rdma_device_removal
=========================

.. c:function:: int nvmet_rdma_device_removal(struct rdma_cm_id *cm_id, struct nvmet_rdma_queue *queue)

    Handle RDMA device removal

    :param struct rdma_cm_id \*cm_id:
        *undescribed*

    :param struct nvmet_rdma_queue \*queue:
        nvmet rdma queue (cm id qp_context)

.. _`nvmet_rdma_device_removal.description`:

Description
-----------

DEVICE_REMOVAL event notifies us that the RDMA device is about
to unplug so we should take care of destroying our RDMA resources.
This event will be generated for each allocated cm_id.

Note that this event can be generated on a normal queue cm_id
and/or a device bound listener cm_id (where in this case
queue will be null).

we claim ownership on destroying the cm_id. For queues we move
the queue state to NVMET_RDMA_IN_DEVICE_REMOVAL and for port
we nullify the priv to prevent double cm_id destruction and destroying
the cm_id implicitely by returning a non-zero rc to the callout.

.. This file was automatic generated / don't edit.

