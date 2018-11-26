.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/img.h

.. _`iwl_ucode_type`:

enum iwl_ucode_type
===================

.. c:type:: enum iwl_ucode_type


.. _`iwl_ucode_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_ucode_type {
        IWL_UCODE_REGULAR,
        IWL_UCODE_INIT,
        IWL_UCODE_WOWLAN,
        IWL_UCODE_REGULAR_USNIFFER,
        IWL_UCODE_TYPE_MAX
    };

.. _`iwl_ucode_type.constants`:

Constants
---------

IWL_UCODE_REGULAR
    Normal runtime ucode

IWL_UCODE_INIT
    Initial ucode

IWL_UCODE_WOWLAN
    Wake on Wireless enabled ucode

IWL_UCODE_REGULAR_USNIFFER
    Normal runtime ucode when using usniffer image

IWL_UCODE_TYPE_MAX
    *undescribed*

.. _`iwl_ucode_type.description`:

Description
-----------

The type of ucode.

.. _`iwl_fw_paging`:

struct iwl_fw_paging
====================

.. c:type:: struct iwl_fw_paging


.. _`iwl_fw_paging.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_paging {
        dma_addr_t fw_paging_phys;
        struct page *fw_paging_block;
        u32 fw_paging_size;
    }

.. _`iwl_fw_paging.members`:

Members
-------

fw_paging_phys
    page phy pointer

fw_paging_block
    pointer to the allocated block

fw_paging_size
    page size

.. _`iwl_fw_cscheme_list`:

struct iwl_fw_cscheme_list
==========================

.. c:type:: struct iwl_fw_cscheme_list

    a cipher scheme list

.. _`iwl_fw_cscheme_list.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_cscheme_list {
        u8 size;
        struct iwl_fw_cipher_scheme cs[];
    }

.. _`iwl_fw_cscheme_list.members`:

Members
-------

size
    a number of entries

cs
    cipher scheme entries

.. _`iwl_fw_type`:

enum iwl_fw_type
================

.. c:type:: enum iwl_fw_type

    iwlwifi firmware type

.. _`iwl_fw_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_fw_type {
        IWL_FW_DVM,
        IWL_FW_MVM
    };

.. _`iwl_fw_type.constants`:

Constants
---------

IWL_FW_DVM
    DVM firmware

IWL_FW_MVM
    MVM firmware

.. _`iwl_fw_dbg`:

struct iwl_fw_dbg
=================

.. c:type:: struct iwl_fw_dbg

    debug data

.. _`iwl_fw_dbg.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg {
        struct iwl_fw_dbg_dest_tlv_v1 *dest_tlv;
        u8 n_dest_reg;
        struct iwl_fw_dbg_conf_tlv *conf_tlv[FW_DBG_CONF_MAX];
        struct iwl_fw_dbg_trigger_tlv *trigger_tlv[FW_DBG_TRIGGER_MAX];
        size_t trigger_tlv_len[FW_DBG_TRIGGER_MAX];
        struct iwl_fw_dbg_mem_seg_tlv *mem_tlv;
        size_t n_mem_tlv;
        u32 dump_mask;
    }

.. _`iwl_fw_dbg.members`:

Members
-------

dest_tlv
    points to debug destination TLV (typically SRAM or DRAM)

n_dest_reg
    num of reg_ops in dest_tlv

conf_tlv
    array of pointers to configuration HCMDs

trigger_tlv
    array of pointers to triggers TLVs

trigger_tlv_len
    lengths of the \ ``dbg_trigger_tlv``\  entries

mem_tlv
    Runtime addresses to dump

n_mem_tlv
    number of runtime addresses

dump_mask
    bitmask of dump regions

.. _`iwl_fw`:

struct iwl_fw
=============

.. c:type:: struct iwl_fw

    variables associated with the firmware

.. _`iwl_fw.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw {
        u32 ucode_ver;
        char fw_version[ETHTOOL_FWVERS_LEN];
        struct fw_img img[IWL_UCODE_TYPE_MAX];
        size_t iml_len;
        u8 *iml;
        struct iwl_ucode_capabilities ucode_capa;
        bool enhance_sensitivity_table;
        u32 init_evtlog_ptr, init_evtlog_size, init_errlog_ptr;
        u32 inst_evtlog_ptr, inst_evtlog_size, inst_errlog_ptr;
        struct iwl_tlv_calib_ctrl default_calib[IWL_UCODE_TYPE_MAX];
        u32 phy_config;
        u8 valid_tx_ant;
        u8 valid_rx_ant;
        enum iwl_fw_type type;
        struct iwl_fw_cipher_scheme cs[IWL_UCODE_MAX_CS];
        u8 human_readable[FW_VER_HUMAN_READABLE_SZ];
        struct iwl_fw_dbg dbg;
    }

.. _`iwl_fw.members`:

Members
-------

ucode_ver
    ucode version from the ucode file

fw_version
    firmware version string

img
    ucode image like ucode_rt, ucode_init, ucode_wowlan.

iml_len
    length of the image loader image

iml
    image loader fw image

ucode_capa
    capabilities parsed from the ucode file.

enhance_sensitivity_table
    device can do enhanced sensitivity.

init_evtlog_ptr
    event log offset for init ucode.

init_evtlog_size
    event log size for init ucode.

init_errlog_ptr
    error log offfset for init ucode.

inst_evtlog_ptr
    event log offset for runtime ucode.

inst_evtlog_size
    event log size for runtime ucode.

inst_errlog_ptr
    error log offfset for runtime ucode.

default_calib
    *undescribed*

phy_config
    *undescribed*

valid_tx_ant
    *undescribed*

valid_rx_ant
    *undescribed*

type
    firmware type (&enum iwl_fw_type)

cs
    *undescribed*

human_readable
    human readable version
    we get the ALIVE from the uCode

dbg
    *undescribed*

.. This file was automatic generated / don't edit.

