.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla4xxx/ql4_83xx.c

.. _`qla4_83xx_need_reset_handler`:

qla4_83xx_need_reset_handler
============================

.. c:function:: void qla4_83xx_need_reset_handler(struct scsi_qla_host *ha)

    Code to start reset sequence

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4_83xx_need_reset_handler.note`:

Note
----

IDC lock must be held upon entry

.. _`qla4_83xx_poll_reg`:

qla4_83xx_poll_reg
==================

.. c:function:: int qla4_83xx_poll_reg(struct scsi_qla_host *ha, uint32_t addr, int duration, uint32_t test_mask, uint32_t test_result)

    Poll the given CRB addr for duration msecs till value read ANDed with test_mask is equal to test_result.

    :param ha:
        Pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param addr:
        CRB register address
    :type addr: uint32_t

    :param duration:
        Poll for total of "duration" msecs
    :type duration: int

    :param test_mask:
        Mask value read with "test_mask"
    :type test_mask: uint32_t

    :param test_result:
        Compare (value&test_mask) with test_result.
    :type test_result: uint32_t

.. _`qla4_83xx_read_reset_template`:

qla4_83xx_read_reset_template
=============================

.. c:function:: void qla4_83xx_read_reset_template(struct scsi_qla_host *ha)

    Read Reset Template from Flash

    :param ha:
        Pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4_83xx_read_write_crb_reg`:

qla4_83xx_read_write_crb_reg
============================

.. c:function:: void qla4_83xx_read_write_crb_reg(struct scsi_qla_host *ha, uint32_t raddr, uint32_t waddr)

    Read from raddr and write value to waddr.

    :param ha:
        Pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param raddr:
        CRB address to read from
    :type raddr: uint32_t

    :param waddr:
        CRB address to write to
    :type waddr: uint32_t

.. _`qla4_83xx_rmw_crb_reg`:

qla4_83xx_rmw_crb_reg
=====================

.. c:function:: void qla4_83xx_rmw_crb_reg(struct scsi_qla_host *ha, uint32_t raddr, uint32_t waddr, struct qla4_83xx_rmw *p_rmw_hdr)

    Read Modify Write crb register

    :param ha:
        Pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param raddr:
        CRB address to read from
    :type raddr: uint32_t

    :param waddr:
        CRB address to write to
    :type waddr: uint32_t

    :param p_rmw_hdr:
        header with shift/or/xor values.
    :type p_rmw_hdr: struct qla4_83xx_rmw \*

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

    :param ha:
        Pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param p_buff:
        Common reset entry header.
    :type p_buff: char \*

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

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4_83xx_eport_init`:

qla4_83xx_eport_init
====================

.. c:function:: void qla4_83xx_eport_init(struct scsi_qla_host *ha)

    Initialize EPort.

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

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

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. This file was automatic generated / don't edit.

