.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla4xxx/ql4_isr.c

.. _`qla4xxx_copy_sense`:

qla4xxx_copy_sense
==================

.. c:function:: void qla4xxx_copy_sense(struct scsi_qla_host *ha, struct status_entry *sts_entry, struct srb *srb)

    copy sense data into cmd sense buffer

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param struct status_entry \*sts_entry:
        Pointer to status entry structure.

    :param struct srb \*srb:
        Pointer to srb structure.

.. _`qla4xxx_status_cont_entry`:

qla4xxx_status_cont_entry
=========================

.. c:function:: void qla4xxx_status_cont_entry(struct scsi_qla_host *ha, struct status_cont_entry *sts_cont)

    Process a Status Continuations entry.

    :param struct scsi_qla_host \*ha:
        SCSI driver HA context

    :param struct status_cont_entry \*sts_cont:
        Entry pointer

.. _`qla4xxx_status_cont_entry.description`:

Description
-----------

Extended sense data.

.. _`qla4xxx_status_entry`:

qla4xxx_status_entry
====================

.. c:function:: void qla4xxx_status_entry(struct scsi_qla_host *ha, struct status_entry *sts_entry)

    processes status IOCBs

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param struct status_entry \*sts_entry:
        Pointer to status entry structure.

.. _`qla4xxx_passthru_status_entry`:

qla4xxx_passthru_status_entry
=============================

.. c:function:: void qla4xxx_passthru_status_entry(struct scsi_qla_host *ha, struct passthru_status *sts_entry)

    processes passthru status IOCBs (0x3C)

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param struct passthru_status \*sts_entry:
        Pointer to status entry structure.

.. _`qla4xxx_process_response_queue`:

qla4xxx_process_response_queue
==============================

.. c:function:: void qla4xxx_process_response_queue(struct scsi_qla_host *ha)

    process response queue completions

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_process_response_queue.description`:

Description
-----------

This routine process response queue completions in interrupt context.
Hardware_lock locked upon entry

.. _`qla4_83xx_loopback_in_progress`:

qla4_83xx_loopback_in_progress
==============================

.. c:function:: int qla4_83xx_loopback_in_progress(struct scsi_qla_host *ha)

    Is loopback in progress?

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_isr_decode_mailbox`:

qla4xxx_isr_decode_mailbox
==========================

.. c:function:: void qla4xxx_isr_decode_mailbox(struct scsi_qla_host *ha, uint32_t mbox_status)

    decodes mailbox status

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param uint32_t mbox_status:
        *undescribed*

.. _`qla4xxx_isr_decode_mailbox.description`:

Description
-----------

This routine decodes the mailbox status during the ISR.
Hardware_lock locked upon entry. runs in interrupt context.

.. _`qla4_82xx_interrupt_service_routine`:

qla4_82xx_interrupt_service_routine
===================================

.. c:function:: void qla4_82xx_interrupt_service_routine(struct scsi_qla_host *ha, uint32_t intr_status)

    isr

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

    :param uint32_t intr_status:
        *undescribed*

.. _`qla4_82xx_interrupt_service_routine.description`:

Description
-----------

This is the main interrupt service routine.
hardware_lock locked upon entry. runs in interrupt context.

.. _`qla4xxx_interrupt_service_routine`:

qla4xxx_interrupt_service_routine
=================================

.. c:function:: void qla4xxx_interrupt_service_routine(struct scsi_qla_host *ha, uint32_t intr_status)

    isr

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

    :param uint32_t intr_status:
        *undescribed*

.. _`qla4xxx_interrupt_service_routine.description`:

Description
-----------

This is the main interrupt service routine.
hardware_lock locked upon entry. runs in interrupt context.

.. _`qla4_82xx_spurious_interrupt`:

qla4_82xx_spurious_interrupt
============================

.. c:function:: void qla4_82xx_spurious_interrupt(struct scsi_qla_host *ha, uint8_t reqs_count)

    processes spurious interrupt

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

    :param uint8_t reqs_count:
        .

.. _`qla4xxx_intr_handler`:

qla4xxx_intr_handler
====================

.. c:function:: irqreturn_t qla4xxx_intr_handler(int irq, void *dev_id)

    hardware interrupt handler.

    :param int irq:
        Unused

    :param void \*dev_id:
        Pointer to host adapter structure

.. _`qla4_82xx_intr_handler`:

qla4_82xx_intr_handler
======================

.. c:function:: irqreturn_t qla4_82xx_intr_handler(int irq, void *dev_id)

    hardware interrupt handler.

    :param int irq:
        Unused

    :param void \*dev_id:
        Pointer to host adapter structure

.. _`qla4_83xx_intr_handler`:

qla4_83xx_intr_handler
======================

.. c:function:: irqreturn_t qla4_83xx_intr_handler(int irq, void *dev_id)

    hardware interrupt handler.

    :param int irq:
        Unused

    :param void \*dev_id:
        Pointer to host adapter structure

.. _`qla4_8xxx_default_intr_handler`:

qla4_8xxx_default_intr_handler
==============================

.. c:function:: irqreturn_t qla4_8xxx_default_intr_handler(int irq, void *dev_id)

    hardware interrupt handler.

    :param int irq:
        Unused

    :param void \*dev_id:
        Pointer to host adapter structure

.. _`qla4_8xxx_default_intr_handler.description`:

Description
-----------

This interrupt handler is called directly for MSI-X, and
called indirectly for MSI.

.. _`qla4xxx_process_aen`:

qla4xxx_process_aen
===================

.. c:function:: void qla4xxx_process_aen(struct scsi_qla_host *ha, uint8_t process_aen)

    processes AENs generated by firmware

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

    :param uint8_t process_aen:
        type of AENs to process

.. _`qla4xxx_process_aen.description`:

Description
-----------

Processes specific types of Asynchronous Events generated by firmware.
The type of AENs to process is specified by process_aen and can be
PROCESS_ALL_AENS         0
FLUSH_DDB_CHANGED_AENS   1
RELOGIN_DDB_CHANGED_AENS 2

.. This file was automatic generated / don't edit.

