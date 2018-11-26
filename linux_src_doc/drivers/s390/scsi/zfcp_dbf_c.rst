.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_dbf.c

.. _`zfcp_dbf_hba_fsf_res`:

zfcp_dbf_hba_fsf_res
====================

.. c:function:: void zfcp_dbf_hba_fsf_res(char *tag, int level, struct zfcp_fsf_req *req)

    trace event for fsf responses

    :param tag:
        tag indicating which kind of unsolicited status has been received
    :type tag: char \*

    :param level:
        *undescribed*
    :type level: int

    :param req:
        request for which a response was received
    :type req: struct zfcp_fsf_req \*

.. _`zfcp_dbf_hba_fsf_uss`:

zfcp_dbf_hba_fsf_uss
====================

.. c:function:: void zfcp_dbf_hba_fsf_uss(char *tag, struct zfcp_fsf_req *req)

    trace event for an unsolicited status buffer

    :param tag:
        tag indicating which kind of unsolicited status has been received
    :type tag: char \*

    :param req:
        request providing the unsolicited status
    :type req: struct zfcp_fsf_req \*

.. _`zfcp_dbf_hba_bit_err`:

zfcp_dbf_hba_bit_err
====================

.. c:function:: void zfcp_dbf_hba_bit_err(char *tag, struct zfcp_fsf_req *req)

    trace event for bit error conditions

    :param tag:
        tag indicating which kind of unsolicited status has been received
    :type tag: char \*

    :param req:
        request which caused the bit_error condition
    :type req: struct zfcp_fsf_req \*

.. _`zfcp_dbf_hba_def_err`:

zfcp_dbf_hba_def_err
====================

.. c:function:: void zfcp_dbf_hba_def_err(struct zfcp_adapter *adapter, u64 req_id, u16 scount, void **pl)

    trace event for deferred error messages

    :param adapter:
        pointer to struct zfcp_adapter
    :type adapter: struct zfcp_adapter \*

    :param req_id:
        request id which caused the deferred error message
    :type req_id: u64

    :param scount:
        number of sbals incl. the signaling sbal
    :type scount: u16

    :param pl:
        array of all involved sbals
    :type pl: void \*\*

.. _`zfcp_dbf_hba_basic`:

zfcp_dbf_hba_basic
==================

.. c:function:: void zfcp_dbf_hba_basic(char *tag, struct zfcp_adapter *adapter)

    trace event for basic adapter events

    :param tag:
        *undescribed*
    :type tag: char \*

    :param adapter:
        pointer to struct zfcp_adapter
    :type adapter: struct zfcp_adapter \*

.. _`zfcp_dbf_rec_trig`:

zfcp_dbf_rec_trig
=================

.. c:function:: void zfcp_dbf_rec_trig(char *tag, struct zfcp_adapter *adapter, struct zfcp_port *port, struct scsi_device *sdev, u8 want, u8 need)

    trace event related to triggered recovery

    :param tag:
        identifier for event
    :type tag: char \*

    :param adapter:
        adapter on which the erp_action should run
    :type adapter: struct zfcp_adapter \*

    :param port:
        remote port involved in the erp_action
    :type port: struct zfcp_port \*

    :param sdev:
        scsi device involved in the erp_action
    :type sdev: struct scsi_device \*

    :param want:
        wanted erp_action
    :type want: u8

    :param need:
        required erp_action
    :type need: u8

.. _`zfcp_dbf_rec_trig.description`:

Description
-----------

The adapter->erp_lock has to be held.

.. _`zfcp_dbf_rec_trig_lock`:

zfcp_dbf_rec_trig_lock
======================

.. c:function:: void zfcp_dbf_rec_trig_lock(char *tag, struct zfcp_adapter *adapter, struct zfcp_port *port, struct scsi_device *sdev, u8 want, u8 need)

    trace event related to triggered recovery with lock

    :param tag:
        identifier for event
    :type tag: char \*

    :param adapter:
        adapter on which the erp_action should run
    :type adapter: struct zfcp_adapter \*

    :param port:
        remote port involved in the erp_action
    :type port: struct zfcp_port \*

    :param sdev:
        scsi device involved in the erp_action
    :type sdev: struct scsi_device \*

    :param want:
        wanted erp_action
    :type want: u8

    :param need:
        required erp_action
    :type need: u8

.. _`zfcp_dbf_rec_trig_lock.description`:

Description
-----------

The adapter->erp_lock must not be held.

.. _`zfcp_dbf_rec_run_lvl`:

zfcp_dbf_rec_run_lvl
====================

.. c:function:: void zfcp_dbf_rec_run_lvl(int level, char *tag, struct zfcp_erp_action *erp)

    trace event related to running recovery

    :param level:
        trace level to be used for event
    :type level: int

    :param tag:
        identifier for event
    :type tag: char \*

    :param erp:
        erp_action running
    :type erp: struct zfcp_erp_action \*

.. _`zfcp_dbf_rec_run`:

zfcp_dbf_rec_run
================

.. c:function:: void zfcp_dbf_rec_run(char *tag, struct zfcp_erp_action *erp)

    trace event related to running recovery

    :param tag:
        identifier for event
    :type tag: char \*

    :param erp:
        erp_action running
    :type erp: struct zfcp_erp_action \*

.. _`zfcp_dbf_rec_run_wka`:

zfcp_dbf_rec_run_wka
====================

.. c:function:: void zfcp_dbf_rec_run_wka(char *tag, struct zfcp_fc_wka_port *wka_port, u64 req_id)

    trace wka port event with info like running recovery

    :param tag:
        identifier for event
    :type tag: char \*

    :param wka_port:
        well known address port
    :type wka_port: struct zfcp_fc_wka_port \*

    :param req_id:
        request ID to correlate with potential HBA trace record
    :type req_id: u64

.. _`zfcp_dbf_san_req`:

zfcp_dbf_san_req
================

.. c:function:: void zfcp_dbf_san_req(char *tag, struct zfcp_fsf_req *fsf, u32 d_id)

    trace event for issued SAN request

    :param tag:
        identifier for event
    :type tag: char \*

    :param fsf:
        *undescribed*
    :type fsf: struct zfcp_fsf_req \*

    :param d_id:
        *undescribed*
    :type d_id: u32

.. _`zfcp_dbf_san_req.d_id`:

d_id
----

destination ID

.. _`zfcp_dbf_san_res`:

zfcp_dbf_san_res
================

.. c:function:: void zfcp_dbf_san_res(char *tag, struct zfcp_fsf_req *fsf)

    trace event for received SAN request

    :param tag:
        identifier for event
    :type tag: char \*

    :param fsf:
        *undescribed*
    :type fsf: struct zfcp_fsf_req \*

.. _`zfcp_dbf_san_in_els`:

zfcp_dbf_san_in_els
===================

.. c:function:: void zfcp_dbf_san_in_els(char *tag, struct zfcp_fsf_req *fsf)

    trace event for incoming ELS

    :param tag:
        identifier for event
    :type tag: char \*

    :param fsf:
        *undescribed*
    :type fsf: struct zfcp_fsf_req \*

.. _`zfcp_dbf_scsi_common`:

zfcp_dbf_scsi_common
====================

.. c:function:: void zfcp_dbf_scsi_common(char *tag, int level, struct scsi_device *sdev, struct scsi_cmnd *sc, struct zfcp_fsf_req *fsf)

    Common trace event helper for scsi.

    :param tag:
        Identifier for event.
    :type tag: char \*

    :param level:
        trace level of event.
    :type level: int

    :param sdev:
        Pointer to SCSI device as context for this event.
    :type sdev: struct scsi_device \*

    :param sc:
        Pointer to SCSI command, or NULL with task management function (TMF).
    :type sc: struct scsi_cmnd \*

    :param fsf:
        Pointer to FSF request, or NULL.
    :type fsf: struct zfcp_fsf_req \*

.. _`zfcp_dbf_scsi_eh`:

zfcp_dbf_scsi_eh
================

.. c:function:: void zfcp_dbf_scsi_eh(char *tag, struct zfcp_adapter *adapter, unsigned int scsi_id, int ret)

    Trace event for special cases of scsi_eh callbacks.

    :param tag:
        Identifier for event.
    :type tag: char \*

    :param adapter:
        Pointer to zfcp adapter as context for this event.
    :type adapter: struct zfcp_adapter \*

    :param scsi_id:
        SCSI ID/target to indicate scope of task management function (TMF).
    :type scsi_id: unsigned int

    :param ret:
        Return value of calling function.
    :type ret: int

.. _`zfcp_dbf_scsi_eh.this-scsi-trace-variant-does-not-depend-on-any-of`:

This SCSI trace variant does not depend on any of
-------------------------------------------------

scsi_cmnd, zfcp_fsf_req, scsi_device.

.. _`zfcp_dbf_adapter_register`:

zfcp_dbf_adapter_register
=========================

.. c:function:: int zfcp_dbf_adapter_register(struct zfcp_adapter *adapter)

    registers debug feature for an adapter

    :param adapter:
        pointer to adapter for which debug features should be registered
    :type adapter: struct zfcp_adapter \*

.. _`zfcp_dbf_adapter_register.return`:

Return
------

-ENOMEM on error, 0 otherwise

.. _`zfcp_dbf_adapter_unregister`:

zfcp_dbf_adapter_unregister
===========================

.. c:function:: void zfcp_dbf_adapter_unregister(struct zfcp_adapter *adapter)

    unregisters debug feature for an adapter

    :param adapter:
        pointer to adapter for which debug features should be unregistered
    :type adapter: struct zfcp_adapter \*

.. This file was automatic generated / don't edit.

