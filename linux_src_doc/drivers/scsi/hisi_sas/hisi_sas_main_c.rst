.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/hisi_sas/hisi_sas_main.c

.. _`hisi_sas_internal_task_abort`:

hisi_sas_internal_task_abort
============================

.. c:function:: int hisi_sas_internal_task_abort(struct hisi_hba *hisi_hba, struct domain_device *device, int abort_flag, int tag)

    - execute an internal abort command for single IO command or a device

    :param hisi_hba:
        host controller struct
    :type hisi_hba: struct hisi_hba \*

    :param device:
        domain device
    :type device: struct domain_device \*

    :param abort_flag:
        mode of operation, device or single IO
    :type abort_flag: int

    :param tag:
        tag of IO to be aborted (only relevant to single
        IO mode)
    :type tag: int

.. This file was automatic generated / don't edit.

