.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/target/target_core_user.c

.. _`queue_cmd_ring`:

queue_cmd_ring
==============

.. c:function:: sense_reason_t queue_cmd_ring(struct tcmu_cmd *tcmu_cmd, int *scsi_err)

    queue cmd to ring or internally

    :param struct tcmu_cmd \*tcmu_cmd:
        cmd to queue

    :param int \*scsi_err:
        TCM error code if failure (-1) returned.

.. _`queue_cmd_ring.return`:

Return
------

-1 we cannot queue internally or to the ring.
0 success
1 internally queued to wait for ring memory to free.

.. This file was automatic generated / don't edit.

