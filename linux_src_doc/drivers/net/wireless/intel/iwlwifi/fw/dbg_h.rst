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

.. This file was automatic generated / don't edit.

