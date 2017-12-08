.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/paging.h

.. _`iwl_fw_paging_cmd`:

struct iwl_fw_paging_cmd
========================

.. c:type:: struct iwl_fw_paging_cmd

    paging layout

.. _`iwl_fw_paging_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_paging_cmd {
        __le32 flags;
        __le32 block_size;
        __le32 block_num;
        __le32 device_phy_addr[NUM_OF_FW_PAGING_BLOCKS];
    }

.. _`iwl_fw_paging_cmd.members`:

Members
-------

flags
    various flags for the command

block_size
    the block size in powers of 2

block_num
    number of blocks specified in the command.

device_phy_addr
    virtual addresses from device side

.. _`iwl_fw_paging_cmd.description`:

Description
-----------

Send to FW the paging layout in the driver.

.. This file was automatic generated / don't edit.

