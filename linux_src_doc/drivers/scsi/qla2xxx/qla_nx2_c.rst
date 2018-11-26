.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_nx2.c

.. _`qla8044_lock_recovery`:

qla8044_lock_recovery
=====================

.. c:function:: int qla8044_lock_recovery(struct scsi_qla_host *vha)

    Recovers the idc_lock.

    :param vha:
        Pointer to adapter structure
    :type vha: struct scsi_qla_host \*

.. _`qla8044_lock_recovery.description`:

Description
-----------

Lock Recovery Register
5-2  Lock recovery owner: Function ID of driver doing lock recovery,
valid if bits 1..0 are set by driver doing lock recovery.
1-0  1 - Driver intends to force unlock the IDC lock.
2 - Driver is moving forward to unlock the IDC lock. Driver clears
this field after force unlocking the IDC lock.

Lock Recovery process
a. Read the IDC_LOCK_RECOVERY register. If the value in bits 1..0 is
greater than 0, then wait for the other driver to unlock otherwise
move to the next step.
b. Indicate intent to force-unlock by writing 1h to the IDC_LOCK_RECOVERY
register bits 1..0 and also set the function# in bits 5..2.
c. Read the IDC_LOCK_RECOVERY register again after a delay of 200ms.
Wait for the other driver to perform lock recovery if the function
number in bits 5..2 has changed, otherwise move to the next step.
d. Write a value of 2h to the IDC_LOCK_RECOVERY register bits 1..0
leaving your function# in bits 5..2.
e. Force unlock using the DRIVER_UNLOCK register and immediately clear
the IDC_LOCK_RECOVERY bits 5..0 by writing 0.

.. _`qla8044_need_reset_handler`:

qla8044_need_reset_handler
==========================

.. c:function:: void qla8044_need_reset_handler(struct scsi_qla_host *vha)

    Code to start reset sequence

    :param vha:
        pointer to adapter structure
    :type vha: struct scsi_qla_host \*

.. _`qla8044_need_reset_handler.note`:

Note
----

IDC lock must be held upon entry

.. _`qla8044_need_qsnt_handler`:

qla8044_need_qsnt_handler
=========================

.. c:function:: void qla8044_need_qsnt_handler(struct scsi_qla_host *vha)

    Code to start qsnt

    :param vha:
        pointer to adapter structure
    :type vha: struct scsi_qla_host \*

.. _`qla8044_check_temp`:

qla8044_check_temp
==================

.. c:function:: int qla8044_check_temp(struct scsi_qla_host *vha)

    Check the ISP82XX temperature.

    :param vha:
        adapter block pointer.
    :type vha: struct scsi_qla_host \*

.. _`qla8044_check_temp.note`:

Note
----

The caller should not hold the idc lock.

.. _`qla8044_check_fw_alive`:

qla8044_check_fw_alive
======================

.. c:function:: int qla8044_check_fw_alive(struct scsi_qla_host *vha)

    Check firmware health

    :param vha:
        Pointer to host adapter structure.
    :type vha: struct scsi_qla_host \*

.. _`qla8044_check_fw_alive.context`:

Context
-------

Interrupt

.. _`qla8044_intr_handler`:

qla8044_intr_handler
====================

.. c:function:: irqreturn_t qla8044_intr_handler(int irq, void *dev_id)

    Process interrupts for the ISP8044

    :param irq:
        interrupt number
    :type irq: int

    :param dev_id:
        SCSI driver HA context
    :type dev_id: void \*

.. _`qla8044_intr_handler.description`:

Description
-----------

Called by system whenever the host adapter generates an interrupt.

Returns handled flag.

.. This file was automatic generated / don't edit.

