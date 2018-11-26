.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/commands.h

.. _`iwl_mvm_command_groups`:

enum iwl_mvm_command_groups
===========================

.. c:type:: enum iwl_mvm_command_groups

    command groups for the firmware

.. _`iwl_mvm_command_groups.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_command_groups {
        LEGACY_GROUP,
        LONG_GROUP,
        SYSTEM_GROUP,
        MAC_CONF_GROUP,
        PHY_OPS_GROUP,
        DATA_PATH_GROUP,
        NAN_GROUP,
        TOF_GROUP,
        PROT_OFFLOAD_GROUP,
        REGULATORY_AND_NVM_GROUP,
        DEBUG_GROUP
    };

.. _`iwl_mvm_command_groups.constants`:

Constants
---------

LEGACY_GROUP
    legacy group, uses command IDs from \ :c:type:`enum iwl_legacy_cmds <iwl_legacy_cmds>`\ 

LONG_GROUP
    legacy group with long header, also uses command IDs
    from \ :c:type:`enum iwl_legacy_cmds <iwl_legacy_cmds>`\ 

SYSTEM_GROUP
    system group, uses command IDs from
    \ :c:type:`enum iwl_system_subcmd_ids <iwl_system_subcmd_ids>`\ 

MAC_CONF_GROUP
    MAC configuration group, uses command IDs from
    \ :c:type:`enum iwl_mac_conf_subcmd_ids <iwl_mac_conf_subcmd_ids>`\ 

PHY_OPS_GROUP
    PHY operations group, uses command IDs from
    \ :c:type:`enum iwl_phy_ops_subcmd_ids <iwl_phy_ops_subcmd_ids>`\ 

DATA_PATH_GROUP
    data path group, uses command IDs from
    \ :c:type:`enum iwl_data_path_subcmd_ids <iwl_data_path_subcmd_ids>`\ 

NAN_GROUP
    NAN group, uses command IDs from \ :c:type:`enum iwl_nan_subcmd_ids <iwl_nan_subcmd_ids>`\ 

TOF_GROUP
    TOF group, uses command IDs from \ :c:type:`enum iwl_tof_subcmd_ids <iwl_tof_subcmd_ids>`\ 

PROT_OFFLOAD_GROUP
    protocol offload group, uses command IDs from
    \ :c:type:`enum iwl_prot_offload_subcmd_ids <iwl_prot_offload_subcmd_ids>`\ 

REGULATORY_AND_NVM_GROUP
    regulatory/NVM group, uses command IDs from
    \ :c:type:`enum iwl_regulatory_and_nvm_subcmd_ids <iwl_regulatory_and_nvm_subcmd_ids>`\ 

DEBUG_GROUP
    Debug group, uses command IDs from \ :c:type:`enum iwl_debug_cmds <iwl_debug_cmds>`\ 

.. _`iwl_legacy_cmds`:

enum iwl_legacy_cmds
====================

.. c:type:: enum iwl_legacy_cmds

    legacy group command IDs

.. _`iwl_legacy_cmds.definition`:

Definition
----------

.. code-block:: c

    enum iwl_legacy_cmds {
        MVM_ALIVE,
        REPLY_ERROR,
        ECHO_CMD,
        INIT_COMPLETE_NOTIF,
        PHY_CONTEXT_CMD,
        DBG_CFG,
        SCAN_ITERATION_COMPLETE_UMAC,
        SCAN_CFG_CMD,
        SCAN_REQ_UMAC,
        SCAN_ABORT_UMAC,
        SCAN_COMPLETE_UMAC,
        BA_WINDOW_STATUS_NOTIFICATION_ID,
        ADD_STA_KEY,
        ADD_STA,
        REMOVE_STA,
        FW_GET_ITEM_CMD,
        TX_CMD,
        TXPATH_FLUSH,
        MGMT_MCAST_KEY,
        SCD_QUEUE_CFG,
        WEP_KEY,
        SHARED_MEM_CFG,
        TDLS_CHANNEL_SWITCH_CMD,
        TDLS_CHANNEL_SWITCH_NOTIFICATION,
        TDLS_CONFIG_CMD,
        MAC_CONTEXT_CMD,
        TIME_EVENT_CMD,
        TIME_EVENT_NOTIFICATION,
        BINDING_CONTEXT_CMD,
        TIME_QUOTA_CMD,
        NON_QOS_TX_COUNTER_CMD,
        LEDS_CMD,
        LQ_CMD,
        FW_PAGING_BLOCK_CMD,
        SCAN_OFFLOAD_REQUEST_CMD,
        SCAN_OFFLOAD_ABORT_CMD,
        HOT_SPOT_CMD,
        SCAN_OFFLOAD_COMPLETE,
        SCAN_OFFLOAD_UPDATE_PROFILES_CMD,
        MATCH_FOUND_NOTIFICATION,
        SCAN_ITERATION_COMPLETE,
        PHY_CONFIGURATION_CMD,
        CALIB_RES_NOTIF_PHY_DB,
        PHY_DB_CMD,
        TOF_CMD,
        TOF_NOTIFICATION,
        POWER_TABLE_CMD,
        PSM_UAPSD_AP_MISBEHAVING_NOTIFICATION,
        LTR_CONFIG,
        REPLY_THERMAL_MNG_BACKOFF,
        DC2DC_CONFIG_CMD,
        NVM_ACCESS_CMD,
        BEACON_NOTIFICATION,
        BEACON_TEMPLATE_CMD,
        TX_ANT_CONFIGURATION_CMD,
        STATISTICS_CMD,
        STATISTICS_NOTIFICATION,
        EOSP_NOTIFICATION,
        REDUCE_TX_POWER_CMD,
        CARD_STATE_NOTIFICATION,
        MISSED_BEACONS_NOTIFICATION,
        MAC_PM_POWER_TABLE,
        MFUART_LOAD_NOTIFICATION,
        RSS_CONFIG_CMD,
        REPLY_RX_PHY_CMD,
        REPLY_RX_MPDU_CMD,
        FRAME_RELEASE,
        BA_NOTIF,
        MCC_UPDATE_CMD,
        MCC_CHUB_UPDATE_CMD,
        MARKER_CMD,
        BT_PROFILE_NOTIFICATION,
        BT_CONFIG,
        BT_COEX_UPDATE_REDUCED_TXP,
        BT_COEX_CI,
        REPLY_SF_CFG_CMD,
        REPLY_BEACON_FILTERING_CMD,
        DTS_MEASUREMENT_NOTIFICATION,
        LDBG_CONFIG_CMD,
        DEBUG_LOG_MSG,
        BCAST_FILTER_CMD,
        MCAST_FILTER_CMD,
        D3_CONFIG_CMD,
        PROT_OFFLOAD_CONFIG_CMD,
        OFFLOADS_QUERY_CMD,
        REMOTE_WAKE_CONFIG_CMD,
        D0I3_END_CMD,
        WOWLAN_PATTERNS,
        WOWLAN_CONFIGURATION,
        WOWLAN_TSC_RSC_PARAM,
        WOWLAN_TKIP_PARAM,
        WOWLAN_KEK_KCK_MATERIAL,
        WOWLAN_GET_STATUSES,
        SCAN_OFFLOAD_PROFILES_QUERY_CMD
    };

.. _`iwl_legacy_cmds.constants`:

Constants
---------

MVM_ALIVE
    Alive data from the firmware, as described in
    \ :c:type:`struct mvm_alive_resp_v3 <mvm_alive_resp_v3>`\  or \ :c:type:`struct mvm_alive_resp <mvm_alive_resp>`\ .

REPLY_ERROR
    Cause an error in the firmware, for testing purposes.

ECHO_CMD
    Send data to the device to have it returned immediately.

INIT_COMPLETE_NOTIF
    Notification that initialization is complete.

PHY_CONTEXT_CMD
    Add/modify/remove a PHY context, using \ :c:type:`struct iwl_phy_context_cmd <iwl_phy_context_cmd>`\ .

DBG_CFG
    Debug configuration command.

SCAN_ITERATION_COMPLETE_UMAC
    Firmware indicates a scan iteration completed, using
    \ :c:type:`struct iwl_umac_scan_iter_complete_notif <iwl_umac_scan_iter_complete_notif>`\ .

SCAN_CFG_CMD
    uses \ :c:type:`struct iwl_scan_config_v1 <iwl_scan_config_v1>`\  or \ :c:type:`struct iwl_scan_config <iwl_scan_config>`\ 

SCAN_REQ_UMAC
    uses \ :c:type:`struct iwl_scan_req_umac <iwl_scan_req_umac>`\ 

SCAN_ABORT_UMAC
    uses \ :c:type:`struct iwl_umac_scan_abort <iwl_umac_scan_abort>`\ 

SCAN_COMPLETE_UMAC
    uses \ :c:type:`struct iwl_umac_scan_complete <iwl_umac_scan_complete>`\ 

BA_WINDOW_STATUS_NOTIFICATION_ID
    uses \ :c:type:`struct iwl_ba_window_status_notif <iwl_ba_window_status_notif>`\ 

ADD_STA_KEY
    \ :c:type:`struct iwl_mvm_add_sta_key_cmd_v1 <iwl_mvm_add_sta_key_cmd_v1>`\  or
    \ :c:type:`struct iwl_mvm_add_sta_key_cmd <iwl_mvm_add_sta_key_cmd>`\ .

ADD_STA
    \ :c:type:`struct iwl_mvm_add_sta_cmd <iwl_mvm_add_sta_cmd>`\  or \ :c:type:`struct iwl_mvm_add_sta_cmd_v7 <iwl_mvm_add_sta_cmd_v7>`\ .

REMOVE_STA
    \ :c:type:`struct iwl_mvm_rm_sta_cmd <iwl_mvm_rm_sta_cmd>`\ 

FW_GET_ITEM_CMD
    uses \ :c:type:`struct iwl_fw_get_item_cmd <iwl_fw_get_item_cmd>`\ 

TX_CMD
    uses \ :c:type:`struct iwl_tx_cmd <iwl_tx_cmd>`\  or \ :c:type:`struct iwl_tx_cmd_gen2 <iwl_tx_cmd_gen2>`\  or     \ :c:type:`struct iwl_tx_cmd_gen3 <iwl_tx_cmd_gen3>`\ ,
    response in \ :c:type:`struct iwl_mvm_tx_resp <iwl_mvm_tx_resp>`\  or
    \ :c:type:`struct iwl_mvm_tx_resp_v3 <iwl_mvm_tx_resp_v3>`\ 

TXPATH_FLUSH
    \ :c:type:`struct iwl_tx_path_flush_cmd <iwl_tx_path_flush_cmd>`\ 

MGMT_MCAST_KEY
    \ :c:type:`struct iwl_mvm_mgmt_mcast_key_cmd <iwl_mvm_mgmt_mcast_key_cmd>`\  or
    \ :c:type:`struct iwl_mvm_mgmt_mcast_key_cmd_v1 <iwl_mvm_mgmt_mcast_key_cmd_v1>`\ 

SCD_QUEUE_CFG
    \ :c:type:`struct iwl_scd_txq_cfg_cmd <iwl_scd_txq_cfg_cmd>`\  for older hardware,     \ :c:type:`struct iwl_tx_queue_cfg_cmd <iwl_tx_queue_cfg_cmd>`\  with \ :c:type:`struct iwl_tx_queue_cfg_rsp <iwl_tx_queue_cfg_rsp>`\ 
    for newer (22000) hardware.

WEP_KEY
    uses \ :c:type:`struct iwl_mvm_wep_key_cmd <iwl_mvm_wep_key_cmd>`\ 

SHARED_MEM_CFG
    retrieve shared memory configuration - response in
    \ :c:type:`struct iwl_shared_mem_cfg <iwl_shared_mem_cfg>`\ 

TDLS_CHANNEL_SWITCH_CMD
    uses \ :c:type:`struct iwl_tdls_channel_switch_cmd <iwl_tdls_channel_switch_cmd>`\ 

TDLS_CHANNEL_SWITCH_NOTIFICATION
    uses \ :c:type:`struct iwl_tdls_channel_switch_notif <iwl_tdls_channel_switch_notif>`\ 

TDLS_CONFIG_CMD
    \ :c:type:`struct iwl_tdls_config_cmd <iwl_tdls_config_cmd>`\ , response in \ :c:type:`struct iwl_tdls_config_res <iwl_tdls_config_res>`\ 

MAC_CONTEXT_CMD
    \ :c:type:`struct iwl_mac_ctx_cmd <iwl_mac_ctx_cmd>`\ 

TIME_EVENT_CMD
    \ :c:type:`struct iwl_time_event_cmd <iwl_time_event_cmd>`\ , response in \ :c:type:`struct iwl_time_event_resp <iwl_time_event_resp>`\ 

TIME_EVENT_NOTIFICATION
    \ :c:type:`struct iwl_time_event_notif <iwl_time_event_notif>`\ 

BINDING_CONTEXT_CMD
    \ :c:type:`struct iwl_binding_cmd <iwl_binding_cmd>`\  or \ :c:type:`struct iwl_binding_cmd_v1 <iwl_binding_cmd_v1>`\ 

TIME_QUOTA_CMD
    \ :c:type:`struct iwl_time_quota_cmd <iwl_time_quota_cmd>`\ 

NON_QOS_TX_COUNTER_CMD
    command is \ :c:type:`struct iwl_nonqos_seq_query_cmd <iwl_nonqos_seq_query_cmd>`\ 

LEDS_CMD
    command is \ :c:type:`struct iwl_led_cmd <iwl_led_cmd>`\ 

LQ_CMD
    using \ :c:type:`struct iwl_lq_cmd <iwl_lq_cmd>`\ 

FW_PAGING_BLOCK_CMD
    \ :c:type:`struct iwl_fw_paging_cmd <iwl_fw_paging_cmd>`\ 

SCAN_OFFLOAD_REQUEST_CMD
    uses \ :c:type:`struct iwl_scan_req_lmac <iwl_scan_req_lmac>`\ 

SCAN_OFFLOAD_ABORT_CMD
    abort the scan - no further contents

HOT_SPOT_CMD
    uses \ :c:type:`struct iwl_hs20_roc_req <iwl_hs20_roc_req>`\ 

SCAN_OFFLOAD_COMPLETE
    notification, \ :c:type:`struct iwl_periodic_scan_complete <iwl_periodic_scan_complete>`\ 

SCAN_OFFLOAD_UPDATE_PROFILES_CMD
    update scan offload (scheduled scan) profiles/blacklist/etc.

MATCH_FOUND_NOTIFICATION
    scan match found

SCAN_ITERATION_COMPLETE
    uses \ :c:type:`struct iwl_lmac_scan_complete_notif <iwl_lmac_scan_complete_notif>`\ 

PHY_CONFIGURATION_CMD
    \ :c:type:`struct iwl_phy_cfg_cmd <iwl_phy_cfg_cmd>`\ 

CALIB_RES_NOTIF_PHY_DB
    \ :c:type:`struct iwl_calib_res_notif_phy_db <iwl_calib_res_notif_phy_db>`\ 

PHY_DB_CMD
    \ :c:type:`struct iwl_phy_db_cmd <iwl_phy_db_cmd>`\ 

TOF_CMD
    \ :c:type:`struct iwl_tof_config_cmd <iwl_tof_config_cmd>`\ 

TOF_NOTIFICATION
    \ :c:type:`struct iwl_tof_gen_resp_cmd <iwl_tof_gen_resp_cmd>`\ 

POWER_TABLE_CMD
    \ :c:type:`struct iwl_device_power_cmd <iwl_device_power_cmd>`\ 

PSM_UAPSD_AP_MISBEHAVING_NOTIFICATION
    \ :c:type:`struct iwl_uapsd_misbehaving_ap_notif <iwl_uapsd_misbehaving_ap_notif>`\ 

LTR_CONFIG
    \ :c:type:`struct iwl_ltr_config_cmd <iwl_ltr_config_cmd>`\ 

REPLY_THERMAL_MNG_BACKOFF
    Thermal throttling command

DC2DC_CONFIG_CMD
    Set/Get DC2DC frequency tune
    Command is \ :c:type:`struct iwl_dc2dc_config_cmd <iwl_dc2dc_config_cmd>`\ ,
    response is \ :c:type:`struct iwl_dc2dc_config_resp <iwl_dc2dc_config_resp>`\ 

NVM_ACCESS_CMD
    using \ :c:type:`struct iwl_nvm_access_cmd <iwl_nvm_access_cmd>`\ 

BEACON_NOTIFICATION
    \ :c:type:`struct iwl_extended_beacon_notif <iwl_extended_beacon_notif>`\ 

BEACON_TEMPLATE_CMD
    Uses one of \ :c:type:`struct iwl_mac_beacon_cmd_v6 <iwl_mac_beacon_cmd_v6>`\ ,
    \ :c:type:`struct iwl_mac_beacon_cmd_v7 <iwl_mac_beacon_cmd_v7>`\  or \ :c:type:`struct iwl_mac_beacon_cmd <iwl_mac_beacon_cmd>`\ 
    depending on the device version.

TX_ANT_CONFIGURATION_CMD
    \ :c:type:`struct iwl_tx_ant_cfg_cmd <iwl_tx_ant_cfg_cmd>`\ 

STATISTICS_CMD
    \ :c:type:`struct iwl_statistics_cmd <iwl_statistics_cmd>`\ 

STATISTICS_NOTIFICATION
    one of \ :c:type:`struct iwl_notif_statistics_v10 <iwl_notif_statistics_v10>`\ ,
    \ :c:type:`struct iwl_notif_statistics_v11 <iwl_notif_statistics_v11>`\ ,
    \ :c:type:`struct iwl_notif_statistics_cdb <iwl_notif_statistics_cdb>`\ 

EOSP_NOTIFICATION
    Notify that a service period ended,
    \ :c:type:`struct iwl_mvm_eosp_notification <iwl_mvm_eosp_notification>`\ 

REDUCE_TX_POWER_CMD
    \ :c:type:`struct iwl_dev_tx_power_cmd_v3 <iwl_dev_tx_power_cmd_v3>`\  or \ :c:type:`struct iwl_dev_tx_power_cmd_v4 <iwl_dev_tx_power_cmd_v4>`\ 
    or \ :c:type:`struct iwl_dev_tx_power_cmd <iwl_dev_tx_power_cmd>`\ 

CARD_STATE_NOTIFICATION
    Card state (RF/CT kill) notification,
    uses \ :c:type:`struct iwl_card_state_notif <iwl_card_state_notif>`\ 

MISSED_BEACONS_NOTIFICATION
    \ :c:type:`struct iwl_missed_beacons_notif <iwl_missed_beacons_notif>`\ 

MAC_PM_POWER_TABLE
    using \ :c:type:`struct iwl_mac_power_cmd <iwl_mac_power_cmd>`\ 

MFUART_LOAD_NOTIFICATION
    \ :c:type:`struct iwl_mfuart_load_notif <iwl_mfuart_load_notif>`\ 

RSS_CONFIG_CMD
    \ :c:type:`struct iwl_rss_config_cmd <iwl_rss_config_cmd>`\ 

REPLY_RX_PHY_CMD
    \ :c:type:`struct iwl_rx_phy_info <iwl_rx_phy_info>`\ 

REPLY_RX_MPDU_CMD
    \ :c:type:`struct iwl_rx_mpdu_res_start <iwl_rx_mpdu_res_start>`\  or \ :c:type:`struct iwl_rx_mpdu_desc <iwl_rx_mpdu_desc>`\ 

FRAME_RELEASE
    Frame release (reorder helper) notification, uses
    \ :c:type:`struct iwl_frame_release <iwl_frame_release>`\ 

BA_NOTIF
    BlockAck notification, uses \ :c:type:`struct iwl_mvm_compressed_ba_notif <iwl_mvm_compressed_ba_notif>`\ 
    or \ :c:type:`struct iwl_mvm_ba_notif <iwl_mvm_ba_notif>`\  depending on the HW

MCC_UPDATE_CMD
    using \ :c:type:`struct iwl_mcc_update_cmd <iwl_mcc_update_cmd>`\ 

MCC_CHUB_UPDATE_CMD
    using \ :c:type:`struct iwl_mcc_chub_notif <iwl_mcc_chub_notif>`\ 

MARKER_CMD
    trace marker command, uses \ :c:type:`struct iwl_mvm_markerwith <iwl_mvm_markerwith>`\  \ :c:type:`struct iwl_mvm_marker_rsp <iwl_mvm_marker_rsp>`\ 

BT_PROFILE_NOTIFICATION
    \ :c:type:`struct iwl_bt_coex_profile_notif <iwl_bt_coex_profile_notif>`\ 

BT_CONFIG
    \ :c:type:`struct iwl_bt_coex_cmd <iwl_bt_coex_cmd>`\ 

BT_COEX_UPDATE_REDUCED_TXP
    \ :c:type:`struct iwl_bt_coex_reduced_txp_update_cmd <iwl_bt_coex_reduced_txp_update_cmd>`\ 

BT_COEX_CI
    \ :c:type:`struct iwl_bt_coex_ci_cmd <iwl_bt_coex_ci_cmd>`\ 

REPLY_SF_CFG_CMD
    \ :c:type:`struct iwl_sf_cfg_cmd <iwl_sf_cfg_cmd>`\ 

REPLY_BEACON_FILTERING_CMD
    \ :c:type:`struct iwl_beacon_filter_cmd <iwl_beacon_filter_cmd>`\ 

DTS_MEASUREMENT_NOTIFICATION
    \ :c:type:`struct iwl_dts_measurement_notif_v1 <iwl_dts_measurement_notif_v1>`\  or
    \ :c:type:`struct iwl_dts_measurement_notif_v2 <iwl_dts_measurement_notif_v2>`\ 

LDBG_CONFIG_CMD
    configure continuous trace recording

DEBUG_LOG_MSG
    Debugging log data from firmware

BCAST_FILTER_CMD
    \ :c:type:`struct iwl_bcast_filter_cmd <iwl_bcast_filter_cmd>`\ 

MCAST_FILTER_CMD
    \ :c:type:`struct iwl_mcast_filter_cmd <iwl_mcast_filter_cmd>`\ 

D3_CONFIG_CMD
    \ :c:type:`struct iwl_d3_manager_config <iwl_d3_manager_config>`\ 

PROT_OFFLOAD_CONFIG_CMD
    Depending on firmware, uses one of&struct iwl_proto_offload_cmd_v1, \ :c:type:`struct iwl_proto_offload_cmd_v2 <iwl_proto_offload_cmd_v2>`\ ,
    \ :c:type:`struct iwl_proto_offload_cmd_v3_small <iwl_proto_offload_cmd_v3_small>`\ ,
    \ :c:type:`struct iwl_proto_offload_cmd_v3_large <iwl_proto_offload_cmd_v3_large>`\ 

OFFLOADS_QUERY_CMD
    No data in command, response in \ :c:type:`struct iwl_wowlan_status <iwl_wowlan_status>`\ 

REMOTE_WAKE_CONFIG_CMD
    \ :c:type:`struct iwl_wowlan_remote_wake_config <iwl_wowlan_remote_wake_config>`\ 

D0I3_END_CMD
    End D0i3/D3 state, no command data

WOWLAN_PATTERNS
    \ :c:type:`struct iwl_wowlan_patterns_cmd <iwl_wowlan_patterns_cmd>`\ 

WOWLAN_CONFIGURATION
    \ :c:type:`struct iwl_wowlan_config_cmd <iwl_wowlan_config_cmd>`\ 

WOWLAN_TSC_RSC_PARAM
    \ :c:type:`struct iwl_wowlan_rsc_tsc_params_cmd <iwl_wowlan_rsc_tsc_params_cmd>`\ 

WOWLAN_TKIP_PARAM
    \ :c:type:`struct iwl_wowlan_tkip_params_cmd <iwl_wowlan_tkip_params_cmd>`\ 

WOWLAN_KEK_KCK_MATERIAL
    \ :c:type:`struct iwl_wowlan_kek_kck_material_cmd <iwl_wowlan_kek_kck_material_cmd>`\ 

WOWLAN_GET_STATUSES
    response in \ :c:type:`struct iwl_wowlan_status <iwl_wowlan_status>`\ 

SCAN_OFFLOAD_PROFILES_QUERY_CMD
    No command data, response is \ :c:type:`struct iwl_scan_offload_profiles_query <iwl_scan_offload_profiles_query>`\ 

.. _`iwl_system_subcmd_ids`:

enum iwl_system_subcmd_ids
==========================

.. c:type:: enum iwl_system_subcmd_ids

    system group command IDs

.. _`iwl_system_subcmd_ids.definition`:

Definition
----------

.. code-block:: c

    enum iwl_system_subcmd_ids {
        SHARED_MEM_CFG_CMD,
        INIT_EXTENDED_CFG_CMD
    };

.. _`iwl_system_subcmd_ids.constants`:

Constants
---------

SHARED_MEM_CFG_CMD
    response in \ :c:type:`struct iwl_shared_mem_cfg <iwl_shared_mem_cfg>`\  or
    \ :c:type:`struct iwl_shared_mem_cfg_v2 <iwl_shared_mem_cfg_v2>`\ 

INIT_EXTENDED_CFG_CMD
    \ :c:type:`struct iwl_init_extended_cfg_cmd <iwl_init_extended_cfg_cmd>`\ 

.. This file was automatic generated / don't edit.

