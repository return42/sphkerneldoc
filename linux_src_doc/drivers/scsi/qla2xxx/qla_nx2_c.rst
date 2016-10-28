.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_nx2.c

.. _`qla8044_need_reset_handler`:

qla8044_need_reset_handler
==========================

.. c:function:: void qla8044_need_reset_handler(struct scsi_qla_host *vha)

    Code to start reset sequence

    :param struct scsi_qla_host \*vha:
        *undescribed*

.. _`qla8044_need_reset_handler.note`:

Note
----

IDC lock must be held upon entry

.. _`qla8044_need_qsnt_handler`:

qla8044_need_qsnt_handler
=========================

.. c:function:: void qla8044_need_qsnt_handler(struct scsi_qla_host *vha)

    Code to start qsnt

    :param struct scsi_qla_host \*vha:
        *undescribed*

.. _`qla8044_check_temp`:

qla8044_check_temp
==================

.. c:function:: int qla8044_check_temp(struct scsi_qla_host *vha)

    Check the ISP82XX temperature.

    :param struct scsi_qla_host \*vha:
        *undescribed*

.. _`qla8044_check_temp.note`:

Note
----

The caller should not hold the idc lock.

.. _`qla8044_check_fw_alive`:

qla8044_check_fw_alive
======================

.. c:function:: int qla8044_check_fw_alive(struct scsi_qla_host *vha)

    Check firmware health

    :param struct scsi_qla_host \*vha:
        *undescribed*

.. _`qla8044_check_fw_alive.context`:

Context
-------

Interrupt

.. _`qla8044_intr_handler`:

qla8044_intr_handler
====================

.. c:function:: irqreturn_t qla8044_intr_handler(int irq, void *dev_id)

    Process interrupts for the ISP8044

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        SCSI driver HA context

.. _`qla8044_intr_handler.description`:

Description
-----------

Called by system whenever the host adapter generates an interrupt.

Returns handled flag.

.. This file was automatic generated / don't edit.

