.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_trigger_diag.h

.. _`sl_wh_event_trigger_t`:

struct SL_WH_EVENT_TRIGGER_T
============================

.. c:type:: struct SL_WH_EVENT_TRIGGER_T

    Definition of an event trigger element

.. _`sl_wh_event_trigger_t.definition`:

Definition
----------

.. code-block:: c

    struct SL_WH_EVENT_TRIGGER_T {
        uint16_t EventValue;
        uint16_t LogEntryQualifier;
    }

.. _`sl_wh_event_trigger_t.members`:

Members
-------

EventValue
    Event Code to trigger on

LogEntryQualifier
    Type of FW event that logged (Log Entry Added Event only)

.. _`sl_wh_event_trigger_t.description`:

Description
-----------

Defines an event that should induce a DIAG_TRIGGER driver event if observed.

.. _`sl_wh_event_triggers_t`:

struct SL_WH_EVENT_TRIGGERS_T
=============================

.. c:type:: struct SL_WH_EVENT_TRIGGERS_T

    Structure passed to/from sysfs containing a list of Event Triggers to be monitored for.

.. _`sl_wh_event_triggers_t.definition`:

Definition
----------

.. code-block:: c

    struct SL_WH_EVENT_TRIGGERS_T {
        uint32_t ValidEntries;
        struct SL_WH_EVENT_TRIGGER_T EventTriggerEntry[NUM_VALID_ENTRIES];
    }

.. _`sl_wh_event_triggers_t.members`:

Members
-------

ValidEntries
    Number of \_SL_WH_EVENT_TRIGGER_T structures contained in this
    structure.

EventTriggerEntry
    List of Event trigger elements.

.. _`sl_wh_event_triggers_t.description`:

Description
-----------

This binary structure is transferred via sysfs to get/set Event Triggers
in the Linux Driver.

.. _`sl_wh_scsi_trigger_t`:

struct SL_WH_SCSI_TRIGGER_T
===========================

.. c:type:: struct SL_WH_SCSI_TRIGGER_T

    Definition of a SCSI trigger element

.. _`sl_wh_scsi_trigger_t.definition`:

Definition
----------

.. code-block:: c

    struct SL_WH_SCSI_TRIGGER_T {
        U8 ASCQ;
        U8 ASC;
        U8 SenseKey;
        U8 Reserved;
    }

.. _`sl_wh_scsi_trigger_t.members`:

Members
-------

ASCQ
    Additional Sense Code Qualifier.  Can be specific or 0xFF for
    wildcard.

ASC
    Additional Sense Code.  Can be specific or 0xFF for wildcard

SenseKey
    SCSI Sense Key

Reserved
    *undescribed*

.. _`sl_wh_scsi_trigger_t.description`:

Description
-----------

Defines a sense key (single or many variants) that should induce a
DIAG_TRIGGER driver event if observed.

.. _`sl_wh_scsi_triggers_t`:

struct SL_WH_SCSI_TRIGGERS_T
============================

.. c:type:: struct SL_WH_SCSI_TRIGGERS_T

    Structure passed to/from sysfs containing a list of SCSI sense codes that should trigger a DIAG_SERVICE event when observed.

.. _`sl_wh_scsi_triggers_t.definition`:

Definition
----------

.. code-block:: c

    struct SL_WH_SCSI_TRIGGERS_T {
        uint32_t ValidEntries;
        struct SL_WH_SCSI_TRIGGER_T SCSITriggerEntry[NUM_VALID_ENTRIES];
    }

.. _`sl_wh_scsi_triggers_t.members`:

Members
-------

ValidEntries
    Number of \_SL_WH_SCSI_TRIGGER_T structures contained in this
    structure.

SCSITriggerEntry
    List of SCSI Sense Code trigger elements.

.. _`sl_wh_scsi_triggers_t.description`:

Description
-----------

This binary structure is transferred via sysfs to get/set SCSI Sense Code
Triggers in the Linux Driver.

.. _`sl_wh_mpi_trigger_t`:

struct SL_WH_MPI_TRIGGER_T
==========================

.. c:type:: struct SL_WH_MPI_TRIGGER_T

    Definition of an MPI trigger element

.. _`sl_wh_mpi_trigger_t.definition`:

Definition
----------

.. code-block:: c

    struct SL_WH_MPI_TRIGGER_T {
        uint16_t IOCStatus;
        uint16_t Reserved;
        uint32_t IocLogInfo;
    }

.. _`sl_wh_mpi_trigger_t.members`:

Members
-------

IOCStatus
    MPI IOCStatus

Reserved
    *undescribed*

IocLogInfo
    MPI IocLogInfo.  Can be specific or 0xFFFFFFFF for wildcard

.. _`sl_wh_mpi_trigger_t.description`:

Description
-----------

Defines a MPI IOCStatus/IocLogInfo pair that should induce a DIAG_TRIGGER
driver event if observed.

.. _`sl_wh_mpi_triggers_t`:

struct SL_WH_MPI_TRIGGERS_T
===========================

.. c:type:: struct SL_WH_MPI_TRIGGERS_T

    Structure passed to/from sysfs containing a list of MPI IOCStatus/IocLogInfo pairs that should trigger a DIAG_SERVICE event when observed.

.. _`sl_wh_mpi_triggers_t.definition`:

Definition
----------

.. code-block:: c

    struct SL_WH_MPI_TRIGGERS_T {
        uint32_t ValidEntries;
        struct SL_WH_MPI_TRIGGER_T MPITriggerEntry[NUM_VALID_ENTRIES];
    }

.. _`sl_wh_mpi_triggers_t.members`:

Members
-------

ValidEntries
    Number of \_SL_WH_MPI_TRIGGER_T structures contained in this
    structure.

MPITriggerEntry
    List of MPI IOCStatus/IocLogInfo trigger elements.

.. _`sl_wh_mpi_triggers_t.description`:

Description
-----------

This binary structure is transferred via sysfs to get/set MPI Error Triggers
in the Linux Driver.

.. _`sl_wh_triggers_event_data_t`:

struct SL_WH_TRIGGERS_EVENT_DATA_T
==================================

.. c:type:: struct SL_WH_TRIGGERS_EVENT_DATA_T

    event data for trigger

.. _`sl_wh_triggers_event_data_t.definition`:

Definition
----------

.. code-block:: c

    struct SL_WH_TRIGGERS_EVENT_DATA_T {
        uint32_t trigger_type;
        union u;
    }

.. _`sl_wh_triggers_event_data_t.members`:

Members
-------

trigger_type
    trigger type (see MPT3SAS_TRIGGER_XXXX)

u
    trigger condition that caused trigger to be sent

.. This file was automatic generated / don't edit.

