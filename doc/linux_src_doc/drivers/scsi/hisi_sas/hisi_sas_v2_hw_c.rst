.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/hisi_sas/hisi_sas_v2_hw.c

.. _`get_free_slot_v2_hw`:

get_free_slot_v2_hw
===================

.. c:function:: int get_free_slot_v2_hw(struct hisi_hba *hisi_hba, int *q, int *s)

    Slots are allocated from queues in a round-robin fashion.

    :param struct hisi_hba \*hisi_hba:
        *undescribed*

    :param int \*q:
        *undescribed*

    :param int \*s:
        *undescribed*

.. _`get_free_slot_v2_hw.description`:

Description
-----------

The callpath to this function and upto writing the write
queue pointer should be safe from interruption.

.. _`interrupt_init_v2_hw`:

interrupt_init_v2_hw
====================

.. c:function:: int interrupt_init_v2_hw(struct hisi_hba *hisi_hba)

    to map in all mbigen interrupts, even if they are not used.

    :param struct hisi_hba \*hisi_hba:
        *undescribed*

.. This file was automatic generated / don't edit.

