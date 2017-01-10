.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/hisi_sas/hisi_sas_v1_hw.c

.. _`get_free_slot_v1_hw`:

get_free_slot_v1_hw
===================

.. c:function:: int get_free_slot_v1_hw(struct hisi_hba *hisi_hba, u32 dev_id, int *q, int *s)

    Slots are allocated from queues in a round-robin fashion.

    :param struct hisi_hba \*hisi_hba:
        *undescribed*

    :param u32 dev_id:
        *undescribed*

    :param int \*q:
        *undescribed*

    :param int \*s:
        *undescribed*

.. _`get_free_slot_v1_hw.description`:

Description
-----------

The callpath to this function and upto writing the write
queue pointer should be safe from interruption.

.. This file was automatic generated / don't edit.

