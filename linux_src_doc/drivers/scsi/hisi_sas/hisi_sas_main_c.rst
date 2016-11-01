.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/hisi_sas/hisi_sas_main.c

.. _`hisi_sas_internal_task_abort`:

hisi_sas_internal_task_abort
============================

.. c:function:: int hisi_sas_internal_task_abort(struct hisi_hba *hisi_hba, struct domain_device *device, int abort_flag, int tag)

    - execute an internal abort command for single IO command or a device

    :param struct hisi_hba \*hisi_hba:
        host controller struct

    :param struct domain_device \*device:
        domain device

    :param int abort_flag:
        mode of operation, device or single IO

    :param int tag:
        tag of IO to be aborted (only relevant to single
        IO mode)

.. This file was automatic generated / don't edit.

