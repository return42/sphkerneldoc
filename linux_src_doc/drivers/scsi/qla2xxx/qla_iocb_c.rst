.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_iocb.c

.. _`qla2x00_get_cmd_direction`:

qla2x00_get_cmd_direction
=========================

.. c:function:: uint16_t qla2x00_get_cmd_direction(srb_t *sp)

    Determine control_flag data direction.

    :param sp:
        SCSI command
    :type sp: srb_t \*

.. _`qla2x00_get_cmd_direction.description`:

Description
-----------

Returns the proper CF\_\* direction based on CDB.

.. _`qla2x00_calc_iocbs_32`:

qla2x00_calc_iocbs_32
=====================

.. c:function:: uint16_t qla2x00_calc_iocbs_32(uint16_t dsds)

    Determine number of Command Type 2 and Continuation Type 0 IOCBs to allocate.

    :param dsds:
        number of data segment decriptors needed
    :type dsds: uint16_t

.. _`qla2x00_calc_iocbs_32.description`:

Description
-----------

Returns the number of IOCB entries needed to store \ ``dsds``\ .

.. _`qla2x00_calc_iocbs_64`:

qla2x00_calc_iocbs_64
=====================

.. c:function:: uint16_t qla2x00_calc_iocbs_64(uint16_t dsds)

    Determine number of Command Type 3 and Continuation Type 1 IOCBs to allocate.

    :param dsds:
        number of data segment decriptors needed
    :type dsds: uint16_t

.. _`qla2x00_calc_iocbs_64.description`:

Description
-----------

Returns the number of IOCB entries needed to store \ ``dsds``\ .

.. _`qla2x00_prep_cont_type0_iocb`:

qla2x00_prep_cont_type0_iocb
============================

.. c:function:: cont_entry_t *qla2x00_prep_cont_type0_iocb(struct scsi_qla_host *vha)

    Initialize a Continuation Type 0 IOCB.

    :param vha:
        HA context
    :type vha: struct scsi_qla_host \*

.. _`qla2x00_prep_cont_type0_iocb.description`:

Description
-----------

Returns a pointer to the Continuation Type 0 IOCB packet.

.. _`qla2x00_prep_cont_type1_iocb`:

qla2x00_prep_cont_type1_iocb
============================

.. c:function:: cont_a64_entry_t *qla2x00_prep_cont_type1_iocb(scsi_qla_host_t *vha, struct req_que *req)

    Initialize a Continuation Type 1 IOCB.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param req:
        request queue
    :type req: struct req_que \*

.. _`qla2x00_prep_cont_type1_iocb.description`:

Description
-----------

Returns a pointer to the continuation type 1 IOCB packet.

.. _`qla2x00_build_scsi_iocbs_64`:

qla2x00_build_scsi_iocbs_64
===========================

.. c:function:: void qla2x00_build_scsi_iocbs_64(srb_t *sp, cmd_entry_t *cmd_pkt, uint16_t tot_dsds)

    Build IOCB command utilizing 64bit capable IOCB types.

    :param sp:
        SRB command to process
    :type sp: srb_t \*

    :param cmd_pkt:
        Command type 3 IOCB
    :type cmd_pkt: cmd_entry_t \*

    :param tot_dsds:
        Total number of segments to transfer
    :type tot_dsds: uint16_t

.. _`qla2x00_start_scsi`:

qla2x00_start_scsi
==================

.. c:function:: int qla2x00_start_scsi(srb_t *sp)

    Send a SCSI command to the ISP

    :param sp:
        command to send to the ISP
    :type sp: srb_t \*

.. _`qla2x00_start_scsi.description`:

Description
-----------

Returns non-zero if a failure occurred, else zero.

.. _`qla2x00_start_iocbs`:

qla2x00_start_iocbs
===================

.. c:function:: void qla2x00_start_iocbs(struct scsi_qla_host *vha, struct req_que *req)

    Execute the IOCB command

    :param vha:
        HA context
    :type vha: struct scsi_qla_host \*

    :param req:
        request queue
    :type req: struct req_que \*

.. _`__qla2x00_marker`:

\__qla2x00_marker
=================

.. c:function:: int __qla2x00_marker(struct scsi_qla_host *vha, struct req_que *req, struct rsp_que *rsp, uint16_t loop_id, uint64_t lun, uint8_t type)

    Send a marker IOCB to the firmware.

    :param vha:
        HA context
    :type vha: struct scsi_qla_host \*

    :param req:
        request queue
    :type req: struct req_que \*

    :param rsp:
        response queue
    :type rsp: struct rsp_que \*

    :param loop_id:
        loop ID
    :type loop_id: uint16_t

    :param lun:
        LUN
    :type lun: uint64_t

    :param type:
        marker modifier
    :type type: uint8_t

.. _`__qla2x00_marker.description`:

Description
-----------

Can be called from both normal and interrupt context.

Returns non-zero if a failure occurred, else zero.

.. _`qla24xx_build_scsi_iocbs`:

qla24xx_build_scsi_iocbs
========================

.. c:function:: void qla24xx_build_scsi_iocbs(srb_t *sp, struct cmd_type_7 *cmd_pkt, uint16_t tot_dsds, struct req_que *req)

    Build IOCB command utilizing Command Type 7 IOCB types.

    :param sp:
        SRB command to process
    :type sp: srb_t \*

    :param cmd_pkt:
        Command type 3 IOCB
    :type cmd_pkt: struct cmd_type_7 \*

    :param tot_dsds:
        Total number of segments to transfer
    :type tot_dsds: uint16_t

    :param req:
        pointer to request queue
    :type req: struct req_que \*

.. _`qla24xx_build_scsi_crc_2_iocbs`:

qla24xx_build_scsi_crc_2_iocbs
==============================

.. c:function:: int qla24xx_build_scsi_crc_2_iocbs(srb_t *sp, struct cmd_type_crc_2 *cmd_pkt, uint16_t tot_dsds, uint16_t tot_prot_dsds, uint16_t fw_prot_opts)

    Build IOCB command utilizing Command Type 6 IOCB types.

    :param sp:
        SRB command to process
    :type sp: srb_t \*

    :param cmd_pkt:
        Command type 3 IOCB
    :type cmd_pkt: struct cmd_type_crc_2 \*

    :param tot_dsds:
        Total number of segments to transfer
    :type tot_dsds: uint16_t

    :param tot_prot_dsds:
        Total number of segments with protection information
    :type tot_prot_dsds: uint16_t

    :param fw_prot_opts:
        Protection options to be passed to firmware
    :type fw_prot_opts: uint16_t

.. _`qla24xx_start_scsi`:

qla24xx_start_scsi
==================

.. c:function:: int qla24xx_start_scsi(srb_t *sp)

    Send a SCSI command to the ISP

    :param sp:
        command to send to the ISP
    :type sp: srb_t \*

.. _`qla24xx_start_scsi.description`:

Description
-----------

Returns non-zero if a failure occurred, else zero.

.. _`qla24xx_dif_start_scsi`:

qla24xx_dif_start_scsi
======================

.. c:function:: int qla24xx_dif_start_scsi(srb_t *sp)

    Send a SCSI command to the ISP

    :param sp:
        command to send to the ISP
    :type sp: srb_t \*

.. _`qla24xx_dif_start_scsi.description`:

Description
-----------

Returns non-zero if a failure occurred, else zero.

.. _`qla2xxx_start_scsi_mq`:

qla2xxx_start_scsi_mq
=====================

.. c:function:: int qla2xxx_start_scsi_mq(srb_t *sp)

    Send a SCSI command to the ISP

    :param sp:
        command to send to the ISP
    :type sp: srb_t \*

.. _`qla2xxx_start_scsi_mq.description`:

Description
-----------

Returns non-zero if a failure occurred, else zero.

.. _`qla2xxx_dif_start_scsi_mq`:

qla2xxx_dif_start_scsi_mq
=========================

.. c:function:: int qla2xxx_dif_start_scsi_mq(srb_t *sp)

    Send a SCSI command to the ISP

    :param sp:
        command to send to the ISP
    :type sp: srb_t \*

.. _`qla2xxx_dif_start_scsi_mq.description`:

Description
-----------

Returns non-zero if a failure occurred, else zero.

.. This file was automatic generated / don't edit.

