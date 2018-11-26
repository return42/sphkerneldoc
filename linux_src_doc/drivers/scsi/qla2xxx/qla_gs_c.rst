.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_gs.c

.. _`qla2x00_prep_ms_iocb`:

qla2x00_prep_ms_iocb
====================

.. c:function:: void *qla2x00_prep_ms_iocb(scsi_qla_host_t *vha, struct ct_arg *arg)

    Prepare common MS/CT IOCB fields for SNS CT query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param arg:
        CT arguments
    :type arg: struct ct_arg \*

.. _`qla2x00_prep_ms_iocb.description`:

Description
-----------

Returns a pointer to the \ ``vha``\ 's ms_iocb.

.. _`qla24xx_prep_ms_iocb`:

qla24xx_prep_ms_iocb
====================

.. c:function:: void *qla24xx_prep_ms_iocb(scsi_qla_host_t *vha, struct ct_arg *arg)

    Prepare common CT IOCB fields for SNS CT query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param arg:
        CT arguments
    :type arg: struct ct_arg \*

.. _`qla24xx_prep_ms_iocb.description`:

Description
-----------

Returns a pointer to the \ ``ha``\ 's ms_iocb.

.. _`qla2x00_prep_ct_req`:

qla2x00_prep_ct_req
===================

.. c:function:: struct ct_sns_req *qla2x00_prep_ct_req(struct ct_sns_pkt *p, uint16_t cmd, uint16_t rsp_size)

    Prepare common CT request fields for SNS query.

    :param p:
        CT request buffer
    :type p: struct ct_sns_pkt \*

    :param cmd:
        GS command
    :type cmd: uint16_t

    :param rsp_size:
        response size in bytes
    :type rsp_size: uint16_t

.. _`qla2x00_prep_ct_req.description`:

Description
-----------

Returns a pointer to the intitialized \ ``ct_req``\ .

.. _`qla2x00_ga_nxt`:

qla2x00_ga_nxt
==============

.. c:function:: int qla2x00_ga_nxt(scsi_qla_host_t *vha, fc_port_t *fcport)

    SNS scan for fabric devices via GA_NXT command.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param fcport:
        fcport entry to updated
    :type fcport: fc_port_t \*

.. _`qla2x00_ga_nxt.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_gid_pt`:

qla2x00_gid_pt
==============

.. c:function:: int qla2x00_gid_pt(scsi_qla_host_t *vha, sw_info_t *list)

    SNS scan for fabric devices via GID_PT command.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param list:
        switch info entries to populate
    :type list: sw_info_t \*

.. _`qla2x00_gid_pt.note`:

NOTE
----

Non-Nx_Ports are not requested.

Returns 0 on success.

.. _`qla2x00_gpn_id`:

qla2x00_gpn_id
==============

.. c:function:: int qla2x00_gpn_id(scsi_qla_host_t *vha, sw_info_t *list)

    SNS Get Port Name (GPN_ID) query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param list:
        switch info entries to populate
    :type list: sw_info_t \*

.. _`qla2x00_gpn_id.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_gnn_id`:

qla2x00_gnn_id
==============

.. c:function:: int qla2x00_gnn_id(scsi_qla_host_t *vha, sw_info_t *list)

    SNS Get Node Name (GNN_ID) query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param list:
        switch info entries to populate
    :type list: sw_info_t \*

.. _`qla2x00_gnn_id.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_rft_id`:

qla2x00_rft_id
==============

.. c:function:: int qla2x00_rft_id(scsi_qla_host_t *vha)

    SNS Register FC-4 TYPEs (RFT_ID) supported by the HBA.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_rft_id.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_rff_id`:

qla2x00_rff_id
==============

.. c:function:: int qla2x00_rff_id(scsi_qla_host_t *vha, u8 type)

    SNS Register FC-4 Features (RFF_ID) supported by the HBA.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param type:
        not used
    :type type: u8

.. _`qla2x00_rff_id.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_rnn_id`:

qla2x00_rnn_id
==============

.. c:function:: int qla2x00_rnn_id(scsi_qla_host_t *vha)

    SNS Register Node Name (RNN_ID) of the HBA.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_rnn_id.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_rsnn_nn`:

qla2x00_rsnn_nn
===============

.. c:function:: int qla2x00_rsnn_nn(scsi_qla_host_t *vha)

    SNS Register Symbolic Node Name (RSNN_NN) of the HBA.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_rsnn_nn.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_prep_sns_cmd`:

qla2x00_prep_sns_cmd
====================

.. c:function:: struct sns_cmd_pkt *qla2x00_prep_sns_cmd(scsi_qla_host_t *vha, uint16_t cmd, uint16_t scmd_len, uint16_t data_size)

    Prepare common SNS command request fields for query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param cmd:
        GS command
    :type cmd: uint16_t

    :param scmd_len:
        Subcommand length
    :type scmd_len: uint16_t

    :param data_size:
        response size in bytes
    :type data_size: uint16_t

.. _`qla2x00_prep_sns_cmd.description`:

Description
-----------

Returns a pointer to the \ ``ha``\ 's sns_cmd.

.. _`qla2x00_sns_ga_nxt`:

qla2x00_sns_ga_nxt
==================

.. c:function:: int qla2x00_sns_ga_nxt(scsi_qla_host_t *vha, fc_port_t *fcport)

    SNS scan for fabric devices via GA_NXT command.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param fcport:
        fcport entry to updated
    :type fcport: fc_port_t \*

.. _`qla2x00_sns_ga_nxt.description`:

Description
-----------

This command uses the old Exectute SNS Command mailbox routine.

Returns 0 on success.

.. _`qla2x00_sns_gid_pt`:

qla2x00_sns_gid_pt
==================

.. c:function:: int qla2x00_sns_gid_pt(scsi_qla_host_t *vha, sw_info_t *list)

    SNS scan for fabric devices via GID_PT command.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param list:
        switch info entries to populate
    :type list: sw_info_t \*

.. _`qla2x00_sns_gid_pt.description`:

Description
-----------

This command uses the old Exectute SNS Command mailbox routine.

.. _`qla2x00_sns_gid_pt.note`:

NOTE
----

Non-Nx_Ports are not requested.

Returns 0 on success.

.. _`qla2x00_sns_gpn_id`:

qla2x00_sns_gpn_id
==================

.. c:function:: int qla2x00_sns_gpn_id(scsi_qla_host_t *vha, sw_info_t *list)

    SNS Get Port Name (GPN_ID) query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param list:
        switch info entries to populate
    :type list: sw_info_t \*

.. _`qla2x00_sns_gpn_id.description`:

Description
-----------

This command uses the old Exectute SNS Command mailbox routine.

Returns 0 on success.

.. _`qla2x00_sns_gnn_id`:

qla2x00_sns_gnn_id
==================

.. c:function:: int qla2x00_sns_gnn_id(scsi_qla_host_t *vha, sw_info_t *list)

    SNS Get Node Name (GNN_ID) query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param list:
        switch info entries to populate
    :type list: sw_info_t \*

.. _`qla2x00_sns_gnn_id.description`:

Description
-----------

This command uses the old Exectute SNS Command mailbox routine.

Returns 0 on success.

.. _`qla2x00_sns_rft_id`:

qla2x00_sns_rft_id
==================

.. c:function:: int qla2x00_sns_rft_id(scsi_qla_host_t *vha)

    SNS Register FC-4 TYPEs (RFT_ID) supported by the HBA.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_sns_rft_id.description`:

Description
-----------

This command uses the old Exectute SNS Command mailbox routine.

Returns 0 on success.

.. _`qla2x00_sns_rnn_id`:

qla2x00_sns_rnn_id
==================

.. c:function:: int qla2x00_sns_rnn_id(scsi_qla_host_t *vha)

    SNS Register Node Name (RNN_ID) of the HBA.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_sns_rnn_id.description`:

Description
-----------

This command uses the old Exectute SNS Command mailbox routine.

Returns 0 on success.

.. _`qla2x00_mgmt_svr_login`:

qla2x00_mgmt_svr_login
======================

.. c:function:: int qla2x00_mgmt_svr_login(scsi_qla_host_t *vha)

    Login to fabric Management Service.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_mgmt_svr_login.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_prep_ms_fdmi_iocb`:

qla2x00_prep_ms_fdmi_iocb
=========================

.. c:function:: void *qla2x00_prep_ms_fdmi_iocb(scsi_qla_host_t *vha, uint32_t req_size, uint32_t rsp_size)

    Prepare common MS IOCB fields for FDMI query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param req_size:
        request size in bytes
    :type req_size: uint32_t

    :param rsp_size:
        response size in bytes
    :type rsp_size: uint32_t

.. _`qla2x00_prep_ms_fdmi_iocb.description`:

Description
-----------

Returns a pointer to the \ ``ha``\ 's ms_iocb.

.. _`qla24xx_prep_ms_fdmi_iocb`:

qla24xx_prep_ms_fdmi_iocb
=========================

.. c:function:: void *qla24xx_prep_ms_fdmi_iocb(scsi_qla_host_t *vha, uint32_t req_size, uint32_t rsp_size)

    Prepare common MS IOCB fields for FDMI query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param req_size:
        request size in bytes
    :type req_size: uint32_t

    :param rsp_size:
        response size in bytes
    :type rsp_size: uint32_t

.. _`qla24xx_prep_ms_fdmi_iocb.description`:

Description
-----------

Returns a pointer to the \ ``ha``\ 's ms_iocb.

.. _`qla2x00_prep_ct_fdmi_req`:

qla2x00_prep_ct_fdmi_req
========================

.. c:function:: struct ct_sns_req *qla2x00_prep_ct_fdmi_req(struct ct_sns_pkt *p, uint16_t cmd, uint16_t rsp_size)

    Prepare common CT request fields for SNS query.

    :param p:
        CT request buffer
    :type p: struct ct_sns_pkt \*

    :param cmd:
        GS command
    :type cmd: uint16_t

    :param rsp_size:
        response size in bytes
    :type rsp_size: uint16_t

.. _`qla2x00_prep_ct_fdmi_req.description`:

Description
-----------

Returns a pointer to the intitialized \ ``ct_req``\ .

.. _`qla2x00_fdmi_rhba`:

qla2x00_fdmi_rhba
=================

.. c:function:: int qla2x00_fdmi_rhba(scsi_qla_host_t *vha)

    perform RHBA FDMI registration

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_fdmi_rhba.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_fdmi_rpa`:

qla2x00_fdmi_rpa
================

.. c:function:: int qla2x00_fdmi_rpa(scsi_qla_host_t *vha)

    perform RPA registration

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_fdmi_rpa.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_fdmiv2_rhba`:

qla2x00_fdmiv2_rhba
===================

.. c:function:: int qla2x00_fdmiv2_rhba(scsi_qla_host_t *vha)

    perform RHBA FDMI v2 registration

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_fdmiv2_rhba.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_fdmi_dhba`:

qla2x00_fdmi_dhba
=================

.. c:function:: int qla2x00_fdmi_dhba(scsi_qla_host_t *vha)

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_fdmi_dhba.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_fdmiv2_rpa`:

qla2x00_fdmiv2_rpa
==================

.. c:function:: int qla2x00_fdmiv2_rpa(scsi_qla_host_t *vha)

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_fdmiv2_rpa.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_fdmi_register`:

qla2x00_fdmi_register
=====================

.. c:function:: int qla2x00_fdmi_register(scsi_qla_host_t *vha)

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

.. _`qla2x00_fdmi_register.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_gfpn_id`:

qla2x00_gfpn_id
===============

.. c:function:: int qla2x00_gfpn_id(scsi_qla_host_t *vha, sw_info_t *list)

    SNS Get Fabric Port Name (GFPN_ID) query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param list:
        switch info entries to populate
    :type list: sw_info_t \*

.. _`qla2x00_gfpn_id.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_gpsc`:

qla2x00_gpsc
============

.. c:function:: int qla2x00_gpsc(scsi_qla_host_t *vha, sw_info_t *list)

    FCS Get Port Speed Capabilities (GPSC) query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param list:
        switch info entries to populate
    :type list: sw_info_t \*

.. _`qla2x00_gpsc.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_gff_id`:

qla2x00_gff_id
==============

.. c:function:: void qla2x00_gff_id(scsi_qla_host_t *vha, sw_info_t *list)

    SNS Get FC-4 Features (GFF_ID) query.

    :param vha:
        HA context
    :type vha: scsi_qla_host_t \*

    :param list:
        switch info entries to populate
    :type list: sw_info_t \*

.. This file was automatic generated / don't edit.

