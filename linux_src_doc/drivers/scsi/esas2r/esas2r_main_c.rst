.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/esas2r/esas2r_main.c

.. _`esas2r_check_active_queue`:

esas2r_check_active_queue
=========================

.. c:function:: int esas2r_check_active_queue(struct esas2r_adapter *a, struct esas2r_request **abort_request, struct scsi_cmnd *cmd, struct list_head *queue)

    to abort.

    :param a:
        *undescribed*
    :type a: struct esas2r_adapter \*

    :param abort_request:
        *undescribed*
    :type abort_request: struct esas2r_request \*\*

    :param cmd:
        *undescribed*
    :type cmd: struct scsi_cmnd \*

    :param queue:
        *undescribed*
    :type queue: struct list_head \*

.. _`esas2r_check_active_queue.description`:

Description
-----------

\ ``param``\  [in] a
\ ``param``\  [in] abort_request
\ ``param``\  [in] cmd
t
\ ``return``\  0 on failure, 1 if command was not found, 2 if command was found

.. This file was automatic generated / don't edit.

