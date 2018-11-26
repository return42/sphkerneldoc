.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/megaraid_sas.h

.. _`mr_priv_device`:

struct MR_PRIV_DEVICE
=====================

.. c:type:: struct MR_PRIV_DEVICE

    sdev private hostdata

.. _`mr_priv_device.definition`:

Definition
----------

.. code-block:: c

    struct MR_PRIV_DEVICE {
        bool is_tm_capable;
        bool tm_busy;
        atomic_t r1_ldio_hint;
        u8 interface_type;
        u8 task_abort_tmo;
        u8 target_reset_tmo;
    }

.. _`mr_priv_device.members`:

Members
-------

is_tm_capable
    firmware managed tm_capable flag

tm_busy
    TM request is in progress

r1_ldio_hint
    *undescribed*

interface_type
    *undescribed*

task_abort_tmo
    *undescribed*

target_reset_tmo
    *undescribed*

.. This file was automatic generated / don't edit.

