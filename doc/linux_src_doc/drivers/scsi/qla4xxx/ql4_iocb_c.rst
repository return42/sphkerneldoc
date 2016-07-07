.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla4xxx/ql4_iocb.c

.. _`qla4xxx_get_req_pkt`:

qla4xxx_get_req_pkt
===================

.. c:function:: int qla4xxx_get_req_pkt(struct scsi_qla_host *ha, struct queue_entry **queue_entry)

    returns a valid entry in request queue.

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param struct queue_entry \*\*queue_entry:
        Pointer to pointer to queue entry structure

.. _`qla4xxx_get_req_pkt.this-routine-performs-the-following-tasks`:

This routine performs the following tasks
-----------------------------------------

- returns the current request_in pointer (if queue not full)
- advances the request_in pointer
- checks for queue full

.. _`qla4xxx_send_marker_iocb`:

qla4xxx_send_marker_iocb
========================

.. c:function:: int qla4xxx_send_marker_iocb(struct scsi_qla_host *ha, struct ddb_entry *ddb_entry, uint64_t lun, uint16_t mrkr_mod)

    issues marker iocb to HBA

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param struct ddb_entry \*ddb_entry:
        Pointer to device database entry

    :param uint64_t lun:
        SCSI LUN

    :param uint16_t mrkr_mod:
        *undescribed*

.. _`qla4xxx_send_marker_iocb.description`:

Description
-----------

This routine issues a marker IOCB.

.. _`qla4_82xx_queue_iocb`:

qla4_82xx_queue_iocb
====================

.. c:function:: void qla4_82xx_queue_iocb(struct scsi_qla_host *ha)

    Tell ISP it's got new request(s)

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

.. _`qla4_82xx_queue_iocb.description`:

Description
-----------

This routine notifies the ISP that one or more new request
queue entries have been placed on the request queue.

.. _`qla4_82xx_complete_iocb`:

qla4_82xx_complete_iocb
=======================

.. c:function:: void qla4_82xx_complete_iocb(struct scsi_qla_host *ha)

    Tell ISP we're done with response(s)

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

.. _`qla4_82xx_complete_iocb.description`:

Description
-----------

This routine notifies the ISP that one or more response/completion
queue entries have been processed by the driver.
This also clears the interrupt.

.. _`qla4xxx_queue_iocb`:

qla4xxx_queue_iocb
==================

.. c:function:: void qla4xxx_queue_iocb(struct scsi_qla_host *ha)

    Tell ISP it's got new request(s)

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

.. _`qla4xxx_queue_iocb.description`:

Description
-----------

This routine is notifies the ISP that one or more new request
queue entries have been placed on the request queue.

.. _`qla4xxx_complete_iocb`:

qla4xxx_complete_iocb
=====================

.. c:function:: void qla4xxx_complete_iocb(struct scsi_qla_host *ha)

    Tell ISP we're done with response(s)

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

.. _`qla4xxx_complete_iocb.description`:

Description
-----------

This routine is notifies the ISP that one or more response/completion
queue entries have been processed by the driver.
This also clears the interrupt.

.. _`qla4xxx_send_command_to_isp`:

qla4xxx_send_command_to_isp
===========================

.. c:function:: int qla4xxx_send_command_to_isp(struct scsi_qla_host *ha, struct srb *srb)

    issues command to HBA

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

    :param struct srb \*srb:
        pointer to SCSI Request Block to be sent to ISP

.. _`qla4xxx_send_command_to_isp.description`:

Description
-----------

This routine is called by qla4xxx_queuecommand to build an ISP
command and pass it to the ISP for execution.

.. This file was automatic generated / don't edit.

