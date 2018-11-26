.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/dbg.h

.. _`iwl_fw_dump_desc`:

struct iwl_fw_dump_desc
=======================

.. c:type:: struct iwl_fw_dump_desc

    describes the dump

.. _`iwl_fw_dump_desc.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dump_desc {
        size_t len;
        struct iwl_fw_error_dump_trigger_desc trig_desc;
    }

.. _`iwl_fw_dump_desc.members`:

Members
-------

len
    length of trig_desc->data

trig_desc
    the description of the dump

.. _`iwl_fw_dbg_params`:

struct iwl_fw_dbg_params
========================

.. c:type:: struct iwl_fw_dbg_params

    register values to restore

.. _`iwl_fw_dbg_params.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_params {
        u32 in_sample;
        u32 out_ctrl;
    }

.. _`iwl_fw_dbg_params.members`:

Members
-------

in_sample
    DBGC_IN_SAMPLE value

out_ctrl
    DBGC_OUT_CTRL value

.. This file was automatic generated / don't edit.

