.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_dbf.c

.. _`zfcp_dbf_hba_fsf_res`:

zfcp_dbf_hba_fsf_res
====================

.. c:function:: void zfcp_dbf_hba_fsf_res(char *tag, int level, struct zfcp_fsf_req *req)

    trace event for fsf responses

    :param char \*tag:
        tag indicating which kind of unsolicited status has been received

    :param int level:
        *undescribed*

    :param struct zfcp_fsf_req \*req:
        request for which a response was received

.. _`zfcp_dbf_hba_fsf_uss`:

zfcp_dbf_hba_fsf_uss
====================

.. c:function:: void zfcp_dbf_hba_fsf_uss(char *tag, struct zfcp_fsf_req *req)

    trace event for an unsolicited status buffer

    :param char \*tag:
        tag indicating which kind of unsolicited status has been received

    :param struct zfcp_fsf_req \*req:
        request providing the unsolicited status

.. _`zfcp_dbf_hba_bit_err`:

zfcp_dbf_hba_bit_err
====================

.. c:function:: void zfcp_dbf_hba_bit_err(char *tag, struct zfcp_fsf_req *req)

    trace event for bit error conditions

    :param char \*tag:
        tag indicating which kind of unsolicited status has been received

    :param struct zfcp_fsf_req \*req:
        request which caused the bit_error condition

.. _`zfcp_dbf_hba_def_err`:

zfcp_dbf_hba_def_err
====================

.. c:function:: void zfcp_dbf_hba_def_err(struct zfcp_adapter *adapter, u64 req_id, u16 scount, void **pl)

    trace event for deferred error messages

    :param struct zfcp_adapter \*adapter:
        pointer to struct zfcp_adapter

    :param u64 req_id:
        request id which caused the deferred error message

    :param u16 scount:
        number of sbals incl. the signaling sbal

    :param void \*\*pl:
        array of all involved sbals

.. _`zfcp_dbf_hba_basic`:

zfcp_dbf_hba_basic
==================

.. c:function:: void zfcp_dbf_hba_basic(char *tag, struct zfcp_adapter *adapter)

    trace event for basic adapter events

    :param char \*tag:
        *undescribed*

    :param struct zfcp_adapter \*adapter:
        pointer to struct zfcp_adapter

.. _`zfcp_dbf_rec_trig`:

zfcp_dbf_rec_trig
=================

.. c:function:: void zfcp_dbf_rec_trig(char *tag, struct zfcp_adapter *adapter, struct zfcp_port *port, struct scsi_device *sdev, u8 want, u8 need)

    trace event related to triggered recovery

    :param char \*tag:
        identifier for event

    :param struct zfcp_adapter \*adapter:
        adapter on which the erp_action should run

    :param struct zfcp_port \*port:
        remote port involved in the erp_action

    :param struct scsi_device \*sdev:
        scsi device involved in the erp_action

    :param u8 want:
        wanted erp_action

    :param u8 need:
        required erp_action

.. _`zfcp_dbf_rec_trig.description`:

Description
-----------

The adapter->erp_lock has to be held.

.. _`zfcp_dbf_rec_run`:

zfcp_dbf_rec_run
================

.. c:function:: void zfcp_dbf_rec_run(char *tag, struct zfcp_erp_action *erp)

    trace event related to running recovery

    :param char \*tag:
        identifier for event

    :param struct zfcp_erp_action \*erp:
        erp_action running

.. _`zfcp_dbf_rec_run_wka`:

zfcp_dbf_rec_run_wka
====================

.. c:function:: void zfcp_dbf_rec_run_wka(char *tag, struct zfcp_fc_wka_port *wka_port, u64 req_id)

    trace wka port event with info like running recovery

    :param char \*tag:
        identifier for event

    :param struct zfcp_fc_wka_port \*wka_port:
        well known address port

    :param u64 req_id:
        request ID to correlate with potential HBA trace record

.. _`zfcp_dbf_san_req`:

zfcp_dbf_san_req
================

.. c:function:: void zfcp_dbf_san_req(char *tag, struct zfcp_fsf_req *fsf, u32 d_id)

    trace event for issued SAN request

    :param char \*tag:
        identifier for event

    :param struct zfcp_fsf_req \*fsf:
        *undescribed*

    :param u32 d_id:
        *undescribed*

.. _`zfcp_dbf_san_req.d_id`:

d_id
----

destination ID

.. _`zfcp_dbf_san_res`:

zfcp_dbf_san_res
================

.. c:function:: void zfcp_dbf_san_res(char *tag, struct zfcp_fsf_req *fsf)

    trace event for received SAN request

    :param char \*tag:
        identifier for event

    :param struct zfcp_fsf_req \*fsf:
        *undescribed*

.. _`zfcp_dbf_san_in_els`:

zfcp_dbf_san_in_els
===================

.. c:function:: void zfcp_dbf_san_in_els(char *tag, struct zfcp_fsf_req *fsf)

    trace event for incoming ELS

    :param char \*tag:
        identifier for event

    :param struct zfcp_fsf_req \*fsf:
        *undescribed*

.. _`zfcp_dbf_scsi`:

zfcp_dbf_scsi
=============

.. c:function:: void zfcp_dbf_scsi(char *tag, int level, struct scsi_cmnd *sc, struct zfcp_fsf_req *fsf)

    trace event for scsi commands

    :param char \*tag:
        identifier for event

    :param int level:
        *undescribed*

    :param struct scsi_cmnd \*sc:
        pointer to struct scsi_cmnd

    :param struct zfcp_fsf_req \*fsf:
        pointer to struct zfcp_fsf_req

.. _`zfcp_dbf_adapter_register`:

zfcp_dbf_adapter_register
=========================

.. c:function:: int zfcp_dbf_adapter_register(struct zfcp_adapter *adapter)

    registers debug feature for an adapter

    :param struct zfcp_adapter \*adapter:
        pointer to adapter for which debug features should be registered

.. _`zfcp_dbf_adapter_register.return`:

Return
------

-ENOMEM on error, 0 otherwise

.. _`zfcp_dbf_adapter_unregister`:

zfcp_dbf_adapter_unregister
===========================

.. c:function:: void zfcp_dbf_adapter_unregister(struct zfcp_adapter *adapter)

    unregisters debug feature for an adapter

    :param struct zfcp_adapter \*adapter:
        pointer to adapter for which debug features should be unregistered

.. This file was automatic generated / don't edit.

