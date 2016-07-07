.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_iocb.c

.. _`qla2x00_get_cmd_direction`:

qla2x00_get_cmd_direction
=========================

.. c:function:: uint16_t qla2x00_get_cmd_direction(srb_t *sp)

    Determine control_flag data direction.

    :param srb_t \*sp:
        *undescribed*

.. _`qla2x00_get_cmd_direction.description`:

Description
-----------

Returns the proper CF\_\* direction based on CDB.

.. _`qla2x00_calc_iocbs_32`:

qla2x00_calc_iocbs_32
=====================

.. c:function:: uint16_t qla2x00_calc_iocbs_32(uint16_t dsds)

    Determine number of Command Type 2 and Continuation Type 0 IOCBs to allocate.

    :param uint16_t dsds:
        number of data segment decriptors needed

.. _`qla2x00_calc_iocbs_32.description`:

Description
-----------

Returns the number of IOCB entries needed to store \ ``dsds``\ .

.. _`qla2x00_calc_iocbs_64`:

qla2x00_calc_iocbs_64
=====================

.. c:function:: uint16_t qla2x00_calc_iocbs_64(uint16_t dsds)

    Determine number of Command Type 3 and Continuation Type 1 IOCBs to allocate.

    :param uint16_t dsds:
        number of data segment decriptors needed

.. _`qla2x00_calc_iocbs_64.description`:

Description
-----------

Returns the number of IOCB entries needed to store \ ``dsds``\ .

.. _`qla2x00_prep_cont_type0_iocb`:

qla2x00_prep_cont_type0_iocb
============================

.. c:function:: cont_entry_t *qla2x00_prep_cont_type0_iocb(struct scsi_qla_host *vha)

    Initialize a Continuation Type 0 IOCB.

    :param struct scsi_qla_host \*vha:
        *undescribed*

.. _`qla2x00_prep_cont_type0_iocb.description`:

Description
-----------

Returns a pointer to the Continuation Type 0 IOCB packet.

.. _`qla2x00_prep_cont_type1_iocb`:

qla2x00_prep_cont_type1_iocb
============================

.. c:function:: cont_a64_entry_t *qla2x00_prep_cont_type1_iocb(scsi_qla_host_t *vha, struct req_que *req)

    Initialize a Continuation Type 1 IOCB.

    :param scsi_qla_host_t \*vha:
        *undescribed*

    :param struct req_que \*req:
        *undescribed*

.. _`qla2x00_prep_cont_type1_iocb.description`:

Description
-----------

Returns a pointer to the continuation type 1 IOCB packet.

.. _`qla2x00_build_scsi_iocbs_64`:

qla2x00_build_scsi_iocbs_64
===========================

.. c:function:: void qla2x00_build_scsi_iocbs_64(srb_t *sp, cmd_entry_t *cmd_pkt, uint16_t tot_dsds)

    Build IOCB command utilizing 64bit capable IOCB types.

    :param srb_t \*sp:
        SRB command to process

    :param cmd_entry_t \*cmd_pkt:
        Command type 3 IOCB

    :param uint16_t tot_dsds:
        Total number of segments to transfer

.. _`qla2x00_start_scsi`:

qla2x00_start_scsi
==================

.. c:function:: int qla2x00_start_scsi(srb_t *sp)

    Send a SCSI command to the ISP

    :param srb_t \*sp:
        command to send to the ISP

.. _`qla2x00_start_scsi.description`:

Description
-----------

Returns non-zero if a failure occurred, else zero.

.. _`qla2x00_start_iocbs`:

qla2x00_start_iocbs
===================

.. c:function:: void qla2x00_start_iocbs(struct scsi_qla_host *vha, struct req_que *req)

    Execute the IOCB command

    :param struct scsi_qla_host \*vha:
        *undescribed*

    :param struct req_que \*req:
        *undescribed*

.. _`__qla2x00_marker`:

__qla2x00_marker
================

.. c:function:: int __qla2x00_marker(struct scsi_qla_host *vha, struct req_que *req, struct rsp_que *rsp, uint16_t loop_id, uint64_t lun, uint8_t type)

    Send a marker IOCB to the firmware.

    :param struct scsi_qla_host \*vha:
        *undescribed*

    :param struct req_que \*req:
        *undescribed*

    :param struct rsp_que \*rsp:
        *undescribed*

    :param uint16_t loop_id:
        loop ID

    :param uint64_t lun:
        LUN

    :param uint8_t type:
        marker modifier

.. _`__qla2x00_marker.description`:

Description
-----------

Can be called from both normal and interrupt context.

Returns non-zero if a failure occurred, else zero.

.. _`qla24xx_build_scsi_iocbs`:

qla24xx_build_scsi_iocbs
========================

.. c:function:: void qla24xx_build_scsi_iocbs(srb_t *sp, struct cmd_type_7 *cmd_pkt, uint16_t tot_dsds)

    Build IOCB command utilizing Command Type 7 IOCB types.

    :param srb_t \*sp:
        SRB command to process

    :param struct cmd_type_7 \*cmd_pkt:
        Command type 3 IOCB

    :param uint16_t tot_dsds:
        Total number of segments to transfer

.. _`qla24xx_build_scsi_crc_2_iocbs`:

qla24xx_build_scsi_crc_2_iocbs
==============================

.. c:function:: int qla24xx_build_scsi_crc_2_iocbs(srb_t *sp, struct cmd_type_crc_2 *cmd_pkt, uint16_t tot_dsds, uint16_t tot_prot_dsds, uint16_t fw_prot_opts)

    Build IOCB command utilizing Command Type 6 IOCB types.

    :param srb_t \*sp:
        SRB command to process

    :param struct cmd_type_crc_2 \*cmd_pkt:
        Command type 3 IOCB

    :param uint16_t tot_dsds:
        Total number of segments to transfer

    :param uint16_t tot_prot_dsds:
        *undescribed*

    :param uint16_t fw_prot_opts:
        *undescribed*

.. _`qla24xx_start_scsi`:

qla24xx_start_scsi
==================

.. c:function:: int qla24xx_start_scsi(srb_t *sp)

    Send a SCSI command to the ISP

    :param srb_t \*sp:
        command to send to the ISP

.. _`qla24xx_start_scsi.description`:

Description
-----------

Returns non-zero if a failure occurred, else zero.

.. _`qla24xx_dif_start_scsi`:

qla24xx_dif_start_scsi
======================

.. c:function:: int qla24xx_dif_start_scsi(srb_t *sp)

    Send a SCSI command to the ISP

    :param srb_t \*sp:
        command to send to the ISP

.. _`qla24xx_dif_start_scsi.description`:

Description
-----------

Returns non-zero if a failure occurred, else zero.

.. This file was automatic generated / don't edit.

