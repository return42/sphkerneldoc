.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla4xxx/ql4_83xx.c

.. _`qla4_83xx_need_reset_handler`:

qla4_83xx_need_reset_handler
============================

.. c:function:: void qla4_83xx_need_reset_handler(struct scsi_qla_host *ha)

    Code to start reset sequence

    :param struct scsi_qla_host \*ha:
        pointer to adapter structure

.. _`qla4_83xx_need_reset_handler.note`:

Note
----

IDC lock must be held upon entry

.. _`qla4_83xx_poll_reg`:

qla4_83xx_poll_reg
==================

.. c:function:: int qla4_83xx_poll_reg(struct scsi_qla_host *ha, uint32_t addr, int duration, uint32_t test_mask, uint32_t test_result)

    Poll the given CRB addr for duration msecs till value read ANDed with test_mask is equal to test_result.

    :param struct scsi_qla_host \*ha:
        Pointer to adapter structure

    :param uint32_t addr:
        CRB register address

    :param int duration:
        Poll for total of "duration" msecs

    :param uint32_t test_mask:
        Mask value read with "test_mask"

    :param uint32_t test_result:
        Compare (value\ :c:type:`struct test_mask <test_mask>`) with test_result.

.. _`qla4_83xx_read_reset_template`:

qla4_83xx_read_reset_template
=============================

.. c:function:: void qla4_83xx_read_reset_template(struct scsi_qla_host *ha)

    Read Reset Template from Flash

    :param struct scsi_qla_host \*ha:
        Pointer to adapter structure

.. _`qla4_83xx_read_write_crb_reg`:

qla4_83xx_read_write_crb_reg
============================

.. c:function:: void qla4_83xx_read_write_crb_reg(struct scsi_qla_host *ha, uint32_t raddr, uint32_t waddr)

    Read from raddr and write value to waddr.

    :param struct scsi_qla_host \*ha:
        Pointer to adapter structure

    :param uint32_t raddr:
        CRB address to read from

    :param uint32_t waddr:
        CRB address to write to

.. _`qla4_83xx_rmw_crb_reg`:

qla4_83xx_rmw_crb_reg
=====================

.. c:function:: void qla4_83xx_rmw_crb_reg(struct scsi_qla_host *ha, uint32_t raddr, uint32_t waddr, struct qla4_83xx_rmw *p_rmw_hdr)

    Read Modify Write crb register

    :param struct scsi_qla_host \*ha:
        Pointer to adapter structure

    :param uint32_t raddr:
        CRB address to read from

    :param uint32_t waddr:
        CRB address to write to

    :param struct qla4_83xx_rmw \*p_rmw_hdr:
        header with shift/or/xor values.

.. _`qla4_83xx_rmw_crb_reg.description`:

Description
-----------

This function read value from raddr, AND with test_mask,
Shift Left,Right/OR/XOR with values RMW header and write value to waddr.

.. _`qla4_83xx_process_reset_template`:

qla4_83xx_process_reset_template
================================

.. c:function:: void qla4_83xx_process_reset_template(struct scsi_qla_host *ha, char *p_buff)

    Process reset template.

    :param struct scsi_qla_host \*ha:
        Pointer to adapter structure

    :param char \*p_buff:
        Common reset entry header.

.. _`qla4_83xx_process_reset_template.description`:

Description
-----------

Process all entries in reset template till entry with SEQ_END opcode,
which indicates end of the reset template processing. Each entry has a
Reset Entry header, entry opcode/command, with size of the entry, number
of entries in sub-sequence and delay in microsecs or timeout in millisecs.

.. _`qla4_83xx_isp_reset`:

qla4_83xx_isp_reset
===================

.. c:function:: int qla4_83xx_isp_reset(struct scsi_qla_host *ha)

    Resets ISP and aborts all outstanding commands.

    :param struct scsi_qla_host \*ha:
        pointer to host adapter structure.

.. _`qla4_83xx_eport_init`:

qla4_83xx_eport_init
====================

.. c:function:: void qla4_83xx_eport_init(struct scsi_qla_host *ha)

    Initialize EPort.

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4_83xx_eport_init.description`:

Description
-----------

If EPort hardware is in reset state before disabling pause, there would be
serious hardware wedging issues. To prevent this perform eport init everytime
before disabling pause frames.

.. _`qla4_83xx_is_detached`:

qla4_83xx_is_detached
=====================

.. c:function:: int qla4_83xx_is_detached(struct scsi_qla_host *ha)

    Check if we are marked invisible.

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. This file was automatic generated / don't edit.

