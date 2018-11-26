.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_mr.c

.. _`qlafx00_pci_config`:

qlafx00_pci_config
==================

.. c:function:: int qlafx00_pci_config(scsi_qla_host_t *vha)

    Setup ISPFx00 PCI configuration registers.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qlafx00_pci_config.description`:

Description
-----------

Returns 0 on success.

.. _`qlafx00_soc_cpu_reset`:

qlafx00_soc_cpu_reset
=====================

.. c:function:: void qlafx00_soc_cpu_reset(scsi_qla_host_t *vha)

    Perform warm reset of iSA(CPUs being reset on SOC).

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qlafx00_soft_reset`:

qlafx00_soft_reset
==================

.. c:function:: void qlafx00_soft_reset(scsi_qla_host_t *vha)

    Soft Reset ISPFx00.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qlafx00_soft_reset.description`:

Description
-----------

Returns 0 on success.

.. _`qlafx00_chip_diag`:

qlafx00_chip_diag
=================

.. c:function:: int qlafx00_chip_diag(scsi_qla_host_t *vha)

    Test ISPFx00 for proper operation.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qlafx00_chip_diag.description`:

Description
-----------

Returns 0 on success.

.. _`qlafx00_init_response_q_entries`:

qlafx00_init_response_q_entries
===============================

.. c:function:: void qlafx00_init_response_q_entries(struct rsp_que *rsp)

    Initializes response queue entries.

    :param rsp:
        response queue
    :type rsp: struct rsp_que \*

.. _`qlafx00_init_response_q_entries.description`:

Description
-----------

Beginning of request ring has initialization control block already built
by nvram config routine.

Returns 0 on success.

.. _`qlafx00_status_entry`:

qlafx00_status_entry
====================

.. c:function:: void qlafx00_status_entry(scsi_qla_host_t *vha, struct rsp_que *rsp, void *pkt)

    Process a Status IOCB entry.

    :param vha:
        SCSI driver HA context
    :type vha: scsi_qla_host_t \*

    :param rsp:
        response queue
    :type rsp: struct rsp_que \*

    :param pkt:
        Entry pointer
    :type pkt: void \*

.. _`qlafx00_status_cont_entry`:

qlafx00_status_cont_entry
=========================

.. c:function:: void qlafx00_status_cont_entry(struct rsp_que *rsp, sts_cont_entry_t *pkt)

    Process a Status Continuations entry.

    :param rsp:
        response queue
    :type rsp: struct rsp_que \*

    :param pkt:
        Entry pointer
    :type pkt: sts_cont_entry_t \*

.. _`qlafx00_status_cont_entry.description`:

Description
-----------

Extended sense data.

.. _`qlafx00_multistatus_entry`:

qlafx00_multistatus_entry
=========================

.. c:function:: void qlafx00_multistatus_entry(struct scsi_qla_host *vha, struct rsp_que *rsp, void *pkt)

    Process Multi response queue entries.

    :param vha:
        SCSI driver HA context
    :type vha: struct scsi_qla_host \*

    :param rsp:
        response queue
    :type rsp: struct rsp_que \*

    :param pkt:
        received packet
    :type pkt: void \*

.. _`qlafx00_error_entry`:

qlafx00_error_entry
===================

.. c:function:: void qlafx00_error_entry(scsi_qla_host_t *vha, struct rsp_que *rsp, struct sts_entry_fx00 *pkt)

    Process an error entry.

    :param vha:
        SCSI driver HA context
    :type vha: scsi_qla_host_t \*

    :param rsp:
        response queue
    :type rsp: struct rsp_que \*

    :param pkt:
        Entry pointer
    :type pkt: struct sts_entry_fx00 \*

.. _`qlafx00_process_response_queue`:

qlafx00_process_response_queue
==============================

.. c:function:: void qlafx00_process_response_queue(struct scsi_qla_host *vha, struct rsp_que *rsp)

    Process response queue entries.

    :param vha:
        SCSI driver HA context
    :type vha: struct scsi_qla_host \*

    :param rsp:
        response queue
    :type rsp: struct rsp_que \*

.. _`qlafx00_async_event`:

qlafx00_async_event
===================

.. c:function:: void qlafx00_async_event(scsi_qla_host_t *vha)

    Process aynchronous events.

    :param vha:
        SCSI driver HA context
    :type vha: scsi_qla_host_t \*

.. _`qlafx00_mbx_completion`:

qlafx00_mbx_completion
======================

.. c:function:: void qlafx00_mbx_completion(scsi_qla_host_t *vha, uint32_t mb0)

    Process mailbox command completions.

    :param vha:
        SCSI driver HA context
    :type vha: scsi_qla_host_t \*

    :param mb0:
        value to be written into mailbox register 0
    :type mb0: uint32_t

.. _`qlafx00_intr_handler`:

qlafx00_intr_handler
====================

.. c:function:: irqreturn_t qlafx00_intr_handler(int irq, void *dev_id)

    Process interrupts for the ISPFX00.

    :param irq:
        interrupt number
    :type irq: int

    :param dev_id:
        SCSI driver HA context
    :type dev_id: void \*

.. _`qlafx00_intr_handler.description`:

Description
-----------

Called by system whenever the host adapter generates an interrupt.

Returns handled flag.

.. _`qlafx00_start_scsi`:

qlafx00_start_scsi
==================

.. c:function:: int qlafx00_start_scsi(srb_t *sp)

    Send a SCSI command to the ISP

    :param sp:
        command to send to the ISP
    :type sp: srb_t \*

.. _`qlafx00_start_scsi.description`:

Description
-----------

Returns non-zero if a failure occurred, else zero.

.. This file was automatic generated / don't edit.

