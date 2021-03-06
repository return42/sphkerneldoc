.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/nvm-reg.h

.. _`iwl_regulatory_and_nvm_subcmd_ids`:

enum iwl_regulatory_and_nvm_subcmd_ids
======================================

.. c:type:: enum iwl_regulatory_and_nvm_subcmd_ids

    regulatory/NVM commands

.. _`iwl_regulatory_and_nvm_subcmd_ids.definition`:

Definition
----------

.. code-block:: c

    enum iwl_regulatory_and_nvm_subcmd_ids {
        NVM_ACCESS_COMPLETE,
        NVM_GET_INFO
    };

.. _`iwl_regulatory_and_nvm_subcmd_ids.constants`:

Constants
---------

NVM_ACCESS_COMPLETE
    \ :c:type:`struct iwl_nvm_access_complete_cmd <iwl_nvm_access_complete_cmd>`\ 

NVM_GET_INFO
    Command is \ :c:type:`struct iwl_nvm_get_info <iwl_nvm_get_info>`\ ,
    response is \ :c:type:`struct iwl_nvm_get_info_rsp <iwl_nvm_get_info_rsp>`\ 

.. _`iwl_nvm_access_op`:

enum iwl_nvm_access_op
======================

.. c:type:: enum iwl_nvm_access_op

    NVM access opcode

.. _`iwl_nvm_access_op.definition`:

Definition
----------

.. code-block:: c

    enum iwl_nvm_access_op {
        IWL_NVM_READ,
        IWL_NVM_WRITE
    };

.. _`iwl_nvm_access_op.constants`:

Constants
---------

IWL_NVM_READ
    read NVM

IWL_NVM_WRITE
    write NVM

.. _`iwl_nvm_access_target`:

enum iwl_nvm_access_target
==========================

.. c:type:: enum iwl_nvm_access_target

    target of the NVM_ACCESS_CMD

.. _`iwl_nvm_access_target.definition`:

Definition
----------

.. code-block:: c

    enum iwl_nvm_access_target {
        NVM_ACCESS_TARGET_CACHE,
        NVM_ACCESS_TARGET_OTP,
        NVM_ACCESS_TARGET_EEPROM
    };

.. _`iwl_nvm_access_target.constants`:

Constants
---------

NVM_ACCESS_TARGET_CACHE
    access the cache

NVM_ACCESS_TARGET_OTP
    access the OTP

NVM_ACCESS_TARGET_EEPROM
    access the EEPROM

.. _`iwl_nvm_section_type`:

enum iwl_nvm_section_type
=========================

.. c:type:: enum iwl_nvm_section_type

    section types for NVM_ACCESS_CMD

.. _`iwl_nvm_section_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_nvm_section_type {
        NVM_SECTION_TYPE_SW,
        NVM_SECTION_TYPE_REGULATORY,
        NVM_SECTION_TYPE_CALIBRATION,
        NVM_SECTION_TYPE_PRODUCTION,
        NVM_SECTION_TYPE_REGULATORY_SDP,
        NVM_SECTION_TYPE_MAC_OVERRIDE,
        NVM_SECTION_TYPE_PHY_SKU,
        NVM_MAX_NUM_SECTIONS
    };

.. _`iwl_nvm_section_type.constants`:

Constants
---------

NVM_SECTION_TYPE_SW
    software section

NVM_SECTION_TYPE_REGULATORY
    regulatory section

NVM_SECTION_TYPE_CALIBRATION
    calibration section

NVM_SECTION_TYPE_PRODUCTION
    production section

NVM_SECTION_TYPE_REGULATORY_SDP
    regulatory section used by 3168 series

NVM_SECTION_TYPE_MAC_OVERRIDE
    MAC override section

NVM_SECTION_TYPE_PHY_SKU
    PHY SKU section

NVM_MAX_NUM_SECTIONS
    number of sections

.. _`iwl_nvm_access_cmd`:

struct iwl_nvm_access_cmd
=========================

.. c:type:: struct iwl_nvm_access_cmd

    Request the device to send an NVM section

.. _`iwl_nvm_access_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_access_cmd {
        u8 op_code;
        u8 target;
        __le16 type;
        __le16 offset;
        __le16 length;
        u8 data[];
    }

.. _`iwl_nvm_access_cmd.members`:

Members
-------

op_code
    \ :c:type:`enum iwl_nvm_access_op <iwl_nvm_access_op>`\ 

target
    \ :c:type:`enum iwl_nvm_access_target <iwl_nvm_access_target>`\ 

type
    \ :c:type:`enum iwl_nvm_section_type <iwl_nvm_section_type>`\ 

offset
    offset in bytes into the section

length
    in bytes, to read/write

data
    if write operation, the data to write. On read its empty

.. _`iwl_nvm_access_resp`:

struct iwl_nvm_access_resp
==========================

.. c:type:: struct iwl_nvm_access_resp

    response to NVM_ACCESS_CMD

.. _`iwl_nvm_access_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_access_resp {
        __le16 offset;
        __le16 length;
        __le16 type;
        __le16 status;
        u8 data[];
    }

.. _`iwl_nvm_access_resp.members`:

Members
-------

offset
    offset in bytes into the section

length
    in bytes, either how much was written or read

type
    NVM_SECTION_TYPE\_\*

status
    0 for success, fail otherwise

data
    if read operation, the data returned. Empty on write.

.. _`iwl_nvm_info_general_flags`:

enum iwl_nvm_info_general_flags
===============================

.. c:type:: enum iwl_nvm_info_general_flags

    flags in NVM_GET_INFO resp

.. _`iwl_nvm_info_general_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_nvm_info_general_flags {
        NVM_GENERAL_FLAGS_EMPTY_OTP
    };

.. _`iwl_nvm_info_general_flags.constants`:

Constants
---------

NVM_GENERAL_FLAGS_EMPTY_OTP
    1 if OTP is empty

.. _`iwl_nvm_get_info_general`:

struct iwl_nvm_get_info_general
===============================

.. c:type:: struct iwl_nvm_get_info_general

    general NVM data

.. _`iwl_nvm_get_info_general.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_get_info_general {
        __le32 flags;
        __le16 nvm_version;
        u8 board_type;
        u8 n_hw_addrs;
    }

.. _`iwl_nvm_get_info_general.members`:

Members
-------

flags
    bit 0: 1 - empty, 0 - non-empty

nvm_version
    nvm version

board_type
    board type

n_hw_addrs
    number of reserved MAC addresses

.. _`iwl_nvm_mac_sku_flags`:

enum iwl_nvm_mac_sku_flags
==========================

.. c:type:: enum iwl_nvm_mac_sku_flags

    flags in \ :c:type:`struct iwl_nvm_get_info_sku <iwl_nvm_get_info_sku>`\ 

.. _`iwl_nvm_mac_sku_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_nvm_mac_sku_flags {
        NVM_MAC_SKU_FLAGS_BAND_2_4_ENABLED,
        NVM_MAC_SKU_FLAGS_BAND_5_2_ENABLED,
        NVM_MAC_SKU_FLAGS_802_11N_ENABLED,
        NVM_MAC_SKU_FLAGS_802_11AC_ENABLED,
        NVM_MAC_SKU_FLAGS_802_11AX_ENABLED,
        NVM_MAC_SKU_FLAGS_MIMO_DISABLED,
        NVM_MAC_SKU_FLAGS_WAPI_ENABLED,
        NVM_MAC_SKU_FLAGS_REG_CHECK_ENABLED,
        NVM_MAC_SKU_FLAGS_API_LOCK_ENABLED
    };

.. _`iwl_nvm_mac_sku_flags.constants`:

Constants
---------

NVM_MAC_SKU_FLAGS_BAND_2_4_ENABLED
    true if 2.4 band enabled

NVM_MAC_SKU_FLAGS_BAND_5_2_ENABLED
    true if 5.2 band enabled

NVM_MAC_SKU_FLAGS_802_11N_ENABLED
    true if 11n enabled

NVM_MAC_SKU_FLAGS_802_11AC_ENABLED
    true if 11ac enabled

NVM_MAC_SKU_FLAGS_802_11AX_ENABLED
    true if 11ax enabled

NVM_MAC_SKU_FLAGS_MIMO_DISABLED
    true if MIMO disabled

NVM_MAC_SKU_FLAGS_WAPI_ENABLED
    true if WAPI enabled

NVM_MAC_SKU_FLAGS_REG_CHECK_ENABLED
    true if regulatory checker enabled

NVM_MAC_SKU_FLAGS_API_LOCK_ENABLED
    true if API lock enabled

.. _`iwl_nvm_get_info_sku`:

struct iwl_nvm_get_info_sku
===========================

.. c:type:: struct iwl_nvm_get_info_sku

    mac information

.. _`iwl_nvm_get_info_sku.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_get_info_sku {
        __le32 mac_sku_flags;
    }

.. _`iwl_nvm_get_info_sku.members`:

Members
-------

mac_sku_flags
    flags for SKU, see \ :c:type:`enum iwl_nvm_mac_sku_flags <iwl_nvm_mac_sku_flags>`\ 

.. _`iwl_nvm_get_info_phy`:

struct iwl_nvm_get_info_phy
===========================

.. c:type:: struct iwl_nvm_get_info_phy

    phy information

.. _`iwl_nvm_get_info_phy.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_get_info_phy {
        __le32 tx_chains;
        __le32 rx_chains;
    }

.. _`iwl_nvm_get_info_phy.members`:

Members
-------

tx_chains
    BIT 0 chain A, BIT 1 chain B

rx_chains
    BIT 0 chain A, BIT 1 chain B

.. _`iwl_nvm_get_info_regulatory`:

struct iwl_nvm_get_info_regulatory
==================================

.. c:type:: struct iwl_nvm_get_info_regulatory

    regulatory information

.. _`iwl_nvm_get_info_regulatory.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_get_info_regulatory {
        __le32 lar_enabled;
        __le16 channel_profile[IWL_NUM_CHANNELS];
        __le16 reserved;
    }

.. _`iwl_nvm_get_info_regulatory.members`:

Members
-------

lar_enabled
    is LAR enabled

channel_profile
    regulatory data of this channel

reserved
    reserved

.. _`iwl_nvm_get_info_rsp`:

struct iwl_nvm_get_info_rsp
===========================

.. c:type:: struct iwl_nvm_get_info_rsp

    response to get NVM data

.. _`iwl_nvm_get_info_rsp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_get_info_rsp {
        struct iwl_nvm_get_info_general general;
        struct iwl_nvm_get_info_sku mac_sku;
        struct iwl_nvm_get_info_phy phy_sku;
        struct iwl_nvm_get_info_regulatory regulatory;
    }

.. _`iwl_nvm_get_info_rsp.members`:

Members
-------

general
    general NVM data

mac_sku
    data relating to MAC sku

phy_sku
    data relating to PHY sku

regulatory
    regulatory data

.. _`iwl_nvm_access_complete_cmd`:

struct iwl_nvm_access_complete_cmd
==================================

.. c:type:: struct iwl_nvm_access_complete_cmd

    NVM_ACCESS commands are completed

.. _`iwl_nvm_access_complete_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_access_complete_cmd {
        __le32 reserved;
    }

.. _`iwl_nvm_access_complete_cmd.members`:

Members
-------

reserved
    reserved

.. _`iwl_mcc_update_cmd`:

struct iwl_mcc_update_cmd
=========================

.. c:type:: struct iwl_mcc_update_cmd

    Request the device to update geographic regulatory profile according to the given MCC (Mobile Country Code). The MCC is two letter-code, ascii upper case[A-Z] or '00' for world domain. 'ZZ' MCC will be used to switch to NVM default profile; in this case, the MCC in the cmd response will be the relevant MCC in the NVM.

.. _`iwl_mcc_update_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mcc_update_cmd {
        __le16 mcc;
        u8 source_id;
        u8 reserved;
        __le32 key;
        u8 reserved2[20];
    }

.. _`iwl_mcc_update_cmd.members`:

Members
-------

mcc
    given mobile country code

source_id
    the source from where we got the MCC, see iwl_mcc_source

reserved
    reserved for alignment

key
    integrity key for MCC API OEM testing

reserved2
    reserved

.. _`iwl_geo_information`:

enum iwl_geo_information
========================

.. c:type:: enum iwl_geo_information

    geographic information.

.. _`iwl_geo_information.definition`:

Definition
----------

.. code-block:: c

    enum iwl_geo_information {
        GEO_NO_INFO,
        GEO_WMM_ETSI_5GHZ_INFO
    };

.. _`iwl_geo_information.constants`:

Constants
---------

GEO_NO_INFO
    no special info for this geo profile.

GEO_WMM_ETSI_5GHZ_INFO
    this geo profile limits the WMM params
    for the 5 GHz band.

.. _`iwl_mcc_update_resp_v3`:

struct iwl_mcc_update_resp_v3
=============================

.. c:type:: struct iwl_mcc_update_resp_v3

    response to MCC_UPDATE_CMD. Contains the new channel control profile map, if changed, and the new MCC (mobile country code). The new MCC may be different than what was requested in MCC_UPDATE_CMD.

.. _`iwl_mcc_update_resp_v3.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mcc_update_resp_v3 {
        __le32 status;
        __le16 mcc;
        u8 cap;
        u8 source_id;
        __le16 time;
        __le16 geo_info;
        __le32 n_channels;
        __le32 channels[0];
    }

.. _`iwl_mcc_update_resp_v3.members`:

Members
-------

status
    see \ :c:type:`enum iwl_mcc_update_status <iwl_mcc_update_status>`\ 

mcc
    the new applied MCC

cap
    capabilities for all channels which matches the MCC

source_id
    the MCC source, see iwl_mcc_source

time
    time elapsed from the MCC test start (in units of 30 seconds)

geo_info
    geographic specific profile information
    see \ :c:type:`enum iwl_geo_information <iwl_geo_information>`\ .

n_channels
    number of channels in \ ``channels_data``\ .

channels
    channel control data map, DWORD for each channel. Only the first
    16bits are used.

.. _`iwl_mcc_update_resp`:

struct iwl_mcc_update_resp
==========================

.. c:type:: struct iwl_mcc_update_resp

    response to MCC_UPDATE_CMD. Contains the new channel control profile map, if changed, and the new MCC (mobile country code). The new MCC may be different than what was requested in MCC_UPDATE_CMD.

.. _`iwl_mcc_update_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mcc_update_resp {
        __le32 status;
        __le16 mcc;
        __le16 cap;
        __le16 time;
        __le16 geo_info;
        u8 source_id;
        u8 reserved[3];
        __le32 n_channels;
        __le32 channels[0];
    }

.. _`iwl_mcc_update_resp.members`:

Members
-------

status
    see \ :c:type:`enum iwl_mcc_update_status <iwl_mcc_update_status>`\ 

mcc
    the new applied MCC

cap
    capabilities for all channels which matches the MCC

time
    time elapsed from the MCC test start (in units of 30 seconds)

geo_info
    geographic specific profile information
    see \ :c:type:`enum iwl_geo_information <iwl_geo_information>`\ .

source_id
    the MCC source, see iwl_mcc_source

reserved
    for four bytes alignment.

n_channels
    number of channels in \ ``channels_data``\ .

channels
    channel control data map, DWORD for each channel. Only the first
    16bits are used.

.. _`iwl_mcc_chub_notif`:

struct iwl_mcc_chub_notif
=========================

.. c:type:: struct iwl_mcc_chub_notif

    chub notifies of mcc change (MCC_CHUB_UPDATE_CMD = 0xc9) The Chub (Communication Hub, CommsHUB) is a HW component that connects to the cellular and connectivity cores that gets updates of the mcc, and notifies the ucode directly of any mcc change. The ucode requests the driver to request the device to update geographic regulatory  profile according to the given MCC (Mobile Country Code). The MCC is two letter-code, ascii upper case[A-Z] or '00' for world domain. 'ZZ' MCC will be used to switch to NVM default profile; in this case, the MCC in the cmd response will be the relevant MCC in the NVM.

.. _`iwl_mcc_chub_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mcc_chub_notif {
        __le16 mcc;
        u8 source_id;
        u8 reserved1;
    }

.. _`iwl_mcc_chub_notif.members`:

Members
-------

mcc
    given mobile country code

source_id
    identity of the change originator, see iwl_mcc_source

reserved1
    reserved for alignment

.. This file was automatic generated / don't edit.

