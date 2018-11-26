.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/host/pci.c

.. _`nvme_submit_cmd`:

nvme_submit_cmd
===============

.. c:function:: void nvme_submit_cmd(struct nvme_queue *nvmeq, struct nvme_command *cmd)

    Copy a command into a queue and ring the doorbell

    :param nvmeq:
        The queue to use
    :type nvmeq: struct nvme_queue \*

    :param cmd:
        The command to send
    :type cmd: struct nvme_command \*

.. _`nvme_suspend_queue`:

nvme_suspend_queue
==================

.. c:function:: int nvme_suspend_queue(struct nvme_queue *nvmeq)

    put queue into suspended state

    :param nvmeq:
        queue to suspend
    :type nvmeq: struct nvme_queue \*

.. This file was automatic generated / don't edit.

