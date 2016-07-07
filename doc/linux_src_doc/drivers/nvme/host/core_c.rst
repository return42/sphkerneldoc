.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/host/core.c

.. _`nvme_kill_queues`:

nvme_kill_queues
================

.. c:function:: void nvme_kill_queues(struct nvme_ctrl *ctrl)

    Ends all namespace queues

    :param struct nvme_ctrl \*ctrl:
        the dead controller that needs to end

.. _`nvme_kill_queues.description`:

Description
-----------

Call this function when the driver determines it is unable to get the
controller in a state capable of servicing IO.

.. This file was automatic generated / don't edit.

