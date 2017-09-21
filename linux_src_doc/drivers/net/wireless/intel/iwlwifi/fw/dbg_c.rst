.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/dbg.c

.. _`iwl_fw_dump_ptrs`:

struct iwl_fw_dump_ptrs
=======================

.. c:type:: struct iwl_fw_dump_ptrs

    set of pointers needed for the fw-error-dump

.. _`iwl_fw_dump_ptrs.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dump_ptrs {
        struct iwl_trans_dump_data *trans_ptr;
        void *fwrt_ptr;
        u32 fwrt_len;
    }

.. _`iwl_fw_dump_ptrs.members`:

Members
-------

trans_ptr
    pointer to struct \ ``iwl_trans_dump_data``\  which contains the
    transport's data.

fwrt_ptr
    pointer to the buffer coming from fwrt

fwrt_len
    length of the valid data in fwrt_ptr

.. This file was automatic generated / don't edit.

