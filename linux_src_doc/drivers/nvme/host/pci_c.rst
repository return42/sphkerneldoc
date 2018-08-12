.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/host/pci.c

.. _`nvme_submit_cmd`:

nvme_submit_cmd
===============

.. c:function:: void nvme_submit_cmd(struct nvme_queue *nvmeq, struct nvme_command *cmd)

    Copy a command into a queue and ring the doorbell

    :param struct nvme_queue \*nvmeq:
        The queue to use

    :param struct nvme_command \*cmd:
        The command to send

.. _`nvme_dif_remap`:

nvme_dif_remap
==============

.. c:function:: void nvme_dif_remap(struct request *req, void (*dif_swap)(u32 p, u32 v, struct t10_pi_tuple *pi))

    remaps ref tags to bip seed and physical lba

    :param struct request \*req:
        *undescribed*

    :param void (\*dif_swap)(u32 p, u32 v, struct t10_pi_tuple \*pi):
        *undescribed*

.. _`nvme_dif_remap.description`:

Description
-----------

The virtual start sector is the one that was originally submitted by the
block layer. Due to partitioning, MD/DM cloning, etc. the actual physical
start sector may be different. Remap protection information to match the
physical LBA on writes, and back to the original seed on reads.

Type 0 and 3 do not have a ref tag, so no remapping required.

.. _`nvme_suspend_queue`:

nvme_suspend_queue
==================

.. c:function:: int nvme_suspend_queue(struct nvme_queue *nvmeq)

    put queue into suspended state \ ``nvmeq``\  - queue to suspend

    :param struct nvme_queue \*nvmeq:
        *undescribed*

.. This file was automatic generated / don't edit.

