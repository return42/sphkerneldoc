.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/runtime.h

.. _`iwl_fw_runtime`:

struct iwl_fw_runtime
=====================

.. c:type:: struct iwl_fw_runtime

    runtime data for firmware

.. _`iwl_fw_runtime.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_runtime {
        struct iwl_trans *trans;
        const struct iwl_fw *fw;
        struct device *dev;
        const struct iwl_fw_runtime_ops *ops;
        void *ops_ctx;
        unsigned long status;
        struct iwl_fw_paging fw_paging_db;
        u16 num_of_paging_blk;
        u16 num_of_pages_in_last_blk;
        enum iwl_ucode_type cur_fw_img;
        struct iwl_fwrt_shared_mem_cfg smem_cfg;
        struct dump;
    }

.. _`iwl_fw_runtime.members`:

Members
-------

trans
    *undescribed*

fw
    firmware image

dev
    device pointer

ops
    user ops

ops_ctx
    user ops context

status
    status flags

fw_paging_db
    paging database

num_of_paging_blk
    number of paging blocks

num_of_pages_in_last_blk
    number of pages in the last block

cur_fw_img
    current firmware image, must be maintained by
    the driver by calling \ :c:type:`struct iwl_fw_set_current_image <iwl_fw_set_current_image>`\ ()

smem_cfg
    saved firmware SMEM configuration

dump
    debug dump data

.. This file was automatic generated / don't edit.

