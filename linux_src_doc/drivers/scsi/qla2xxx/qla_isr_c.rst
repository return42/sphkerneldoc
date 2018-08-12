.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_isr.c

.. _`qla2100_intr_handler`:

qla2100_intr_handler
====================

.. c:function:: irqreturn_t qla2100_intr_handler(int irq, void *dev_id)

    Process interrupts for the ISP2100 and ISP2200.

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        SCSI driver HA context

.. _`qla2100_intr_handler.description`:

Description
-----------

Called by system whenever the host adapter generates an interrupt.

Returns handled flag.

.. _`qla2300_intr_handler`:

qla2300_intr_handler
====================

.. c:function:: irqreturn_t qla2300_intr_handler(int irq, void *dev_id)

    Process interrupts for the ISP23xx and ISP63xx.

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        SCSI driver HA context

.. _`qla2300_intr_handler.description`:

Description
-----------

Called by system whenever the host adapter generates an interrupt.

Returns handled flag.

.. _`qla2x00_mbx_completion`:

qla2x00_mbx_completion
======================

.. c:function:: void qla2x00_mbx_completion(scsi_qla_host_t *vha, uint16_t mb0)

    Process mailbox command completions.

    :param scsi_qla_host_t \*vha:
        SCSI driver HA context

    :param uint16_t mb0:
        Mailbox0 register

.. _`qla2x00_async_event`:

qla2x00_async_event
===================

.. c:function:: void qla2x00_async_event(scsi_qla_host_t *vha, struct rsp_que *rsp, uint16_t *mb)

    Process aynchronous events.

    :param scsi_qla_host_t \*vha:
        SCSI driver HA context

    :param struct rsp_que \*rsp:
        response queue

    :param uint16_t \*mb:
        Mailbox registers (0 - 3)

.. _`qla2x00_process_completed_request`:

qla2x00_process_completed_request
=================================

.. c:function:: void qla2x00_process_completed_request(struct scsi_qla_host *vha, struct req_que *req, uint32_t index)

    Process a Fast Post response.

    :param struct scsi_qla_host \*vha:
        SCSI driver HA context

    :param struct req_que \*req:
        request queue

    :param uint32_t index:
        SRB index

.. _`qla2x00_process_response_queue`:

qla2x00_process_response_queue
==============================

.. c:function:: void qla2x00_process_response_queue(struct rsp_que *rsp)

    Process response queue entries.

    :param struct rsp_que \*rsp:
        response queue

.. _`qla2x00_status_entry`:

qla2x00_status_entry
====================

.. c:function:: void qla2x00_status_entry(scsi_qla_host_t *vha, struct rsp_que *rsp, void *pkt)

    Process a Status IOCB entry.

    :param scsi_qla_host_t \*vha:
        SCSI driver HA context

    :param struct rsp_que \*rsp:
        response queue

    :param void \*pkt:
        Entry pointer

.. _`qla2x00_status_cont_entry`:

qla2x00_status_cont_entry
=========================

.. c:function:: void qla2x00_status_cont_entry(struct rsp_que *rsp, sts_cont_entry_t *pkt)

    Process a Status Continuations entry.

    :param struct rsp_que \*rsp:
        response queue

    :param sts_cont_entry_t \*pkt:
        Entry pointer

.. _`qla2x00_status_cont_entry.description`:

Description
-----------

Extended sense data.

.. _`qla2x00_error_entry`:

qla2x00_error_entry
===================

.. c:function:: int qla2x00_error_entry(scsi_qla_host_t *vha, struct rsp_que *rsp, sts_entry_t *pkt)

    Process an error entry.

    :param scsi_qla_host_t \*vha:
        SCSI driver HA context

    :param struct rsp_que \*rsp:
        response queue

    :param sts_entry_t \*pkt:
        Entry pointer
        return : 1=allow further error analysis. 0=no additional error analysis.

.. _`qla24xx_mbx_completion`:

qla24xx_mbx_completion
======================

.. c:function:: void qla24xx_mbx_completion(scsi_qla_host_t *vha, uint16_t mb0)

    Process mailbox command completions.

    :param scsi_qla_host_t \*vha:
        SCSI driver HA context

    :param uint16_t mb0:
        Mailbox0 register

.. _`qla24xx_process_response_queue`:

qla24xx_process_response_queue
==============================

.. c:function:: void qla24xx_process_response_queue(struct scsi_qla_host *vha, struct rsp_que *rsp)

    Process response queue entries.

    :param struct scsi_qla_host \*vha:
        SCSI driver HA context

    :param struct rsp_que \*rsp:
        response queue

.. _`qla24xx_intr_handler`:

qla24xx_intr_handler
====================

.. c:function:: irqreturn_t qla24xx_intr_handler(int irq, void *dev_id)

    Process interrupts for the ISP23xx and ISP24xx.

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        SCSI driver HA context

.. _`qla24xx_intr_handler.description`:

Description
-----------

Called by system whenever the host adapter generates an interrupt.

Returns handled flag.

.. This file was automatic generated / don't edit.

