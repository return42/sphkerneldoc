.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-fw.h

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
        struct iwl_fw_cipher_scheme cs;
    }

.. _`iwl_fw_cscheme_list.members`:

Members
-------

size
    a number of entries

cs
    cipher scheme entries

.. _`iwl_gscan_capabilities`:

struct iwl_gscan_capabilities
=============================

.. c:type:: struct iwl_gscan_capabilities

    gscan capabilities supported by FW

.. _`iwl_gscan_capabilities.definition`:

Definition
----------

.. code-block:: c

    struct iwl_gscan_capabilities {
        u32 max_scan_cache_size;
        u32 max_scan_buckets;
        u32 max_ap_cache_per_scan;
        u32 max_rssi_sample_size;
        u32 max_scan_reporting_threshold;
        u32 max_hotlist_aps;
        u32 max_significant_change_aps;
        u32 max_bssid_history_entries;
        u32 max_hotlist_ssids;
        u32 max_number_epno_networks;
        u32 max_number_epno_networks_by_ssid;
        u32 max_number_of_white_listed_ssid;
        u32 max_number_of_black_listed_ssid;
    }

.. _`iwl_gscan_capabilities.members`:

Members
-------

max_scan_cache_size
    total space allocated for scan results (in bytes).

max_scan_buckets
    maximum number of channel buckets.

max_ap_cache_per_scan
    maximum number of APs that can be stored per scan.

max_rssi_sample_size
    number of RSSI samples used for averaging RSSI.

max_scan_reporting_threshold
    max possible report threshold. in percentage.

max_hotlist_aps
    maximum number of entries for hotlist APs.

max_significant_change_aps
    maximum number of entries for significant
    change APs.

max_bssid_history_entries
    number of BSSID/RSSI entries that the device can
    hold.

max_hotlist_ssids
    maximum number of entries for hotlist SSIDs.

max_number_epno_networks
    max number of epno entries.

max_number_epno_networks_by_ssid
    max number of epno entries if ssid is
    specified.

max_number_of_white_listed_ssid
    max number of white listed SSIDs.

max_number_of_black_listed_ssid
    max number of black listed SSIDs.

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
        char fw_version;
        struct fw_img img;
        struct iwl_ucode_capabilities ucode_capa;
        bool enhance_sensitivity_table;
        u32 init_evtlog_ptr;
        u32 init_evtlog_size;
        u32 init_errlog_ptr;
        u32 inst_evtlog_ptr;
        u32 inst_evtlog_size;
        u32 inst_errlog_ptr;
        struct iwl_tlv_calib_ctrl default_calib;
        u32 phy_config;
        u8 valid_tx_ant;
        u8 valid_rx_ant;
        enum iwl_fw_type type;
        struct iwl_fw_cipher_scheme cs;
        u8 human_readable;
        u32 sdio_adma_addr;
        struct iwl_fw_dbg_dest_tlv *dbg_dest_tlv;
        struct iwl_fw_dbg_conf_tlv  *dbg_conf_tlv;
        size_t dbg_conf_tlv_len;
        struct iwl_fw_dbg_trigger_tlv  *dbg_trigger_tlv;
        struct iwl_fw_dbg_mem_seg_tlv *dbg_mem_tlv;
        size_t n_dbg_mem_tlv;
        size_t dbg_trigger_tlv_len;
        u8 dbg_dest_reg_num;
        struct iwl_gscan_capabilities gscan_capa;
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

sdio_adma_addr
    the default address to set for the ADMA in SDIO mode until
    we get the ALIVE from the uCode

dbg_dest_tlv
    points to the destination TLV for debug

dbg_conf_tlv
    array of pointers to configuration TLVs for debug

dbg_conf_tlv_len
    lengths of the \ ``dbg_conf_tlv``\  entries

dbg_trigger_tlv
    array of pointers to triggers TLVs

dbg_mem_tlv
    *undescribed*

n_dbg_mem_tlv
    *undescribed*

dbg_trigger_tlv_len
    lengths of the \ ``dbg_trigger_tlv``\  entries

dbg_dest_reg_num
    num of reg_ops in \ ``dbg_dest_tlv``\ 

gscan_capa
    *undescribed*

.. This file was automatic generated / don't edit.

