.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_trigger_diag.c

.. _`_mpt3sas_raise_sigio`:

\_mpt3sas_raise_sigio
=====================

.. c:function:: void _mpt3sas_raise_sigio(struct MPT3SAS_ADAPTER *ioc, struct SL_WH_TRIGGERS_EVENT_DATA_T *event_data)

    notifiy app

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param event_data:
        ?
    :type event_data: struct SL_WH_TRIGGERS_EVENT_DATA_T \*

.. _`mpt3sas_process_trigger_data`:

mpt3sas_process_trigger_data
============================

.. c:function:: void mpt3sas_process_trigger_data(struct MPT3SAS_ADAPTER *ioc, struct SL_WH_TRIGGERS_EVENT_DATA_T *event_data)

    process the event data for the trigger

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param event_data:
        ?
    :type event_data: struct SL_WH_TRIGGERS_EVENT_DATA_T \*

.. _`mpt3sas_trigger_master`:

mpt3sas_trigger_master
======================

.. c:function:: void mpt3sas_trigger_master(struct MPT3SAS_ADAPTER *ioc, u32 trigger_bitmask)

    Master trigger handler

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param trigger_bitmask:
        *undescribed*
    :type trigger_bitmask: u32

.. _`mpt3sas_trigger_event`:

mpt3sas_trigger_event
=====================

.. c:function:: void mpt3sas_trigger_event(struct MPT3SAS_ADAPTER *ioc, u16 event, u16 log_entry_qualifier)

    Event trigger handler

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param event:
        ?
    :type event: u16

    :param log_entry_qualifier:
        ?
    :type log_entry_qualifier: u16

.. _`mpt3sas_trigger_scsi`:

mpt3sas_trigger_scsi
====================

.. c:function:: void mpt3sas_trigger_scsi(struct MPT3SAS_ADAPTER *ioc, u8 sense_key, u8 asc, u8 ascq)

    SCSI trigger handler

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param sense_key:
        ?
    :type sense_key: u8

    :param asc:
        ?
    :type asc: u8

    :param ascq:
        ?
    :type ascq: u8

.. _`mpt3sas_trigger_mpi`:

mpt3sas_trigger_mpi
===================

.. c:function:: void mpt3sas_trigger_mpi(struct MPT3SAS_ADAPTER *ioc, u16 ioc_status, u32 loginfo)

    MPI trigger handler

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param ioc_status:
        ?
    :type ioc_status: u16

    :param loginfo:
        ?
    :type loginfo: u32

.. This file was automatic generated / don't edit.

