.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_fsf.c

.. _`zfcp_fsf_req_free`:

zfcp_fsf_req_free
=================

.. c:function:: void zfcp_fsf_req_free(struct zfcp_fsf_req *req)

    free memory used by fsf request

    :param req:
        *undescribed*
    :type req: struct zfcp_fsf_req \*

.. _`zfcp_fsf_req_complete`:

zfcp_fsf_req_complete
=====================

.. c:function:: void zfcp_fsf_req_complete(struct zfcp_fsf_req *req)

    process completion of a FSF request

    :param req:
        *undescribed*
    :type req: struct zfcp_fsf_req \*

.. _`zfcp_fsf_req_complete.description`:

Description
-----------

When a request has been completed either from the FCP adapter,
or it has been dismissed due to a queue shutdown, this function
is called to process the completion status and trigger further
events related to the FSF request.

.. _`zfcp_fsf_req_dismiss_all`:

zfcp_fsf_req_dismiss_all
========================

.. c:function:: void zfcp_fsf_req_dismiss_all(struct zfcp_adapter *adapter)

    dismiss all fsf requests

    :param adapter:
        pointer to struct zfcp_adapter
    :type adapter: struct zfcp_adapter \*

.. _`zfcp_fsf_req_dismiss_all.description`:

Description
-----------

Never ever call this without shutting down the adapter first.
Otherwise the adapter would continue using and corrupting s390 storage.
Included \ :c:func:`BUG_ON`\  call to ensure this is done.
ERP is supposed to be the only user of this function.

.. _`zfcp_fsf_status_read`:

zfcp_fsf_status_read
====================

.. c:function:: int zfcp_fsf_status_read(struct zfcp_qdio *qdio)

    send status read request

    :param qdio:
        *undescribed*
    :type qdio: struct zfcp_qdio \*

.. _`zfcp_fsf_status_read.return`:

Return
------

0 on success, ERROR otherwise

.. _`zfcp_fsf_abort_fcp_cmnd`:

zfcp_fsf_abort_fcp_cmnd
=======================

.. c:function:: struct zfcp_fsf_req *zfcp_fsf_abort_fcp_cmnd(struct scsi_cmnd *scmnd)

    abort running SCSI command

    :param scmnd:
        The SCSI command to abort
    :type scmnd: struct scsi_cmnd \*

.. _`zfcp_fsf_abort_fcp_cmnd.return`:

Return
------

pointer to struct zfcp_fsf_req

.. _`zfcp_fsf_send_ct`:

zfcp_fsf_send_ct
================

.. c:function:: int zfcp_fsf_send_ct(struct zfcp_fc_wka_port *wka_port, struct zfcp_fsf_ct_els *ct, mempool_t *pool, unsigned int timeout)

    initiate a Generic Service request (FC-GS)

    :param wka_port:
        *undescribed*
    :type wka_port: struct zfcp_fc_wka_port \*

    :param ct:
        pointer to struct zfcp_send_ct with data for request
    :type ct: struct zfcp_fsf_ct_els \*

    :param pool:
        if non-null this mempool is used to allocate struct zfcp_fsf_req
    :type pool: mempool_t \*

    :param timeout:
        *undescribed*
    :type timeout: unsigned int

.. _`zfcp_fsf_send_els`:

zfcp_fsf_send_els
=================

.. c:function:: int zfcp_fsf_send_els(struct zfcp_adapter *adapter, u32 d_id, struct zfcp_fsf_ct_els *els, unsigned int timeout)

    initiate an ELS command (FC-FS)

    :param adapter:
        *undescribed*
    :type adapter: struct zfcp_adapter \*

    :param d_id:
        *undescribed*
    :type d_id: u32

    :param els:
        pointer to struct zfcp_send_els with data for the command
    :type els: struct zfcp_fsf_ct_els \*

    :param timeout:
        *undescribed*
    :type timeout: unsigned int

.. _`zfcp_fsf_exchange_port_data`:

zfcp_fsf_exchange_port_data
===========================

.. c:function:: int zfcp_fsf_exchange_port_data(struct zfcp_erp_action *erp_action)

    request information about local port

    :param erp_action:
        ERP action for the adapter for which port data is requested
    :type erp_action: struct zfcp_erp_action \*

.. _`zfcp_fsf_exchange_port_data.return`:

Return
------

0 on success, error otherwise

.. _`zfcp_fsf_exchange_port_data_sync`:

zfcp_fsf_exchange_port_data_sync
================================

.. c:function:: int zfcp_fsf_exchange_port_data_sync(struct zfcp_qdio *qdio, struct fsf_qtcb_bottom_port *data)

    request information about local port

    :param qdio:
        pointer to struct zfcp_qdio
    :type qdio: struct zfcp_qdio \*

    :param data:
        pointer to struct fsf_qtcb_bottom_port
    :type data: struct fsf_qtcb_bottom_port \*

.. _`zfcp_fsf_exchange_port_data_sync.return`:

Return
------

0 on success, error otherwise

.. _`zfcp_fsf_open_port`:

zfcp_fsf_open_port
==================

.. c:function:: int zfcp_fsf_open_port(struct zfcp_erp_action *erp_action)

    create and send open port request

    :param erp_action:
        pointer to struct zfcp_erp_action
    :type erp_action: struct zfcp_erp_action \*

.. _`zfcp_fsf_open_port.return`:

Return
------

0 on success, error otherwise

.. _`zfcp_fsf_close_port`:

zfcp_fsf_close_port
===================

.. c:function:: int zfcp_fsf_close_port(struct zfcp_erp_action *erp_action)

    create and send close port request

    :param erp_action:
        pointer to struct zfcp_erp_action
    :type erp_action: struct zfcp_erp_action \*

.. _`zfcp_fsf_close_port.return`:

Return
------

0 on success, error otherwise

.. _`zfcp_fsf_open_wka_port`:

zfcp_fsf_open_wka_port
======================

.. c:function:: int zfcp_fsf_open_wka_port(struct zfcp_fc_wka_port *wka_port)

    create and send open wka-port request

    :param wka_port:
        pointer to struct zfcp_fc_wka_port
    :type wka_port: struct zfcp_fc_wka_port \*

.. _`zfcp_fsf_open_wka_port.return`:

Return
------

0 on success, error otherwise

.. _`zfcp_fsf_close_wka_port`:

zfcp_fsf_close_wka_port
=======================

.. c:function:: int zfcp_fsf_close_wka_port(struct zfcp_fc_wka_port *wka_port)

    create and send close wka port request

    :param wka_port:
        WKA port to open
    :type wka_port: struct zfcp_fc_wka_port \*

.. _`zfcp_fsf_close_wka_port.return`:

Return
------

0 on success, error otherwise

.. _`zfcp_fsf_close_physical_port`:

zfcp_fsf_close_physical_port
============================

.. c:function:: int zfcp_fsf_close_physical_port(struct zfcp_erp_action *erp_action)

    close physical port

    :param erp_action:
        pointer to struct zfcp_erp_action
    :type erp_action: struct zfcp_erp_action \*

.. _`zfcp_fsf_close_physical_port.return`:

Return
------

0 on success

.. _`zfcp_fsf_open_lun`:

zfcp_fsf_open_lun
=================

.. c:function:: int zfcp_fsf_open_lun(struct zfcp_erp_action *erp_action)

    open LUN

    :param erp_action:
        pointer to struct zfcp_erp_action
    :type erp_action: struct zfcp_erp_action \*

.. _`zfcp_fsf_open_lun.return`:

Return
------

0 on success, error otherwise

.. _`zfcp_fsf_close_lun`:

zfcp_fsf_close_lun
==================

.. c:function:: int zfcp_fsf_close_lun(struct zfcp_erp_action *erp_action)

    close LUN

    :param erp_action:
        pointer to erp_action triggering the "close LUN"
    :type erp_action: struct zfcp_erp_action \*

.. _`zfcp_fsf_close_lun.return`:

Return
------

0 on success, error otherwise

.. _`zfcp_fsf_fcp_handler_common`:

zfcp_fsf_fcp_handler_common
===========================

.. c:function:: void zfcp_fsf_fcp_handler_common(struct zfcp_fsf_req *req, struct scsi_device *sdev)

    FCP response handler common to I/O and TMF.

    :param req:
        Pointer to FSF request.
    :type req: struct zfcp_fsf_req \*

    :param sdev:
        Pointer to SCSI device as request context.
    :type sdev: struct scsi_device \*

.. _`zfcp_fsf_fcp_cmnd`:

zfcp_fsf_fcp_cmnd
=================

.. c:function:: int zfcp_fsf_fcp_cmnd(struct scsi_cmnd *scsi_cmnd)

    initiate an FCP command (for a SCSI command)

    :param scsi_cmnd:
        scsi command to be sent
    :type scsi_cmnd: struct scsi_cmnd \*

.. _`zfcp_fsf_fcp_task_mgmt`:

zfcp_fsf_fcp_task_mgmt
======================

.. c:function:: struct zfcp_fsf_req *zfcp_fsf_fcp_task_mgmt(struct scsi_device *sdev, u8 tm_flags)

    Send SCSI task management command (TMF).

    :param sdev:
        Pointer to SCSI device to send the task management command to.
    :type sdev: struct scsi_device \*

    :param tm_flags:
        Unsigned byte for task management flags.
    :type tm_flags: u8

.. _`zfcp_fsf_fcp_task_mgmt.return`:

Return
------

On success pointer to struct zfcp_fsf_req, \ ``NULL``\  otherwise.

.. _`zfcp_fsf_reqid_check`:

zfcp_fsf_reqid_check
====================

.. c:function:: void zfcp_fsf_reqid_check(struct zfcp_qdio *qdio, int sbal_idx)

    validate req_id contained in SBAL returned by QDIO

    :param qdio:
        *undescribed*
    :type qdio: struct zfcp_qdio \*

    :param sbal_idx:
        response queue index of SBAL to be processed
    :type sbal_idx: int

.. This file was automatic generated / don't edit.

