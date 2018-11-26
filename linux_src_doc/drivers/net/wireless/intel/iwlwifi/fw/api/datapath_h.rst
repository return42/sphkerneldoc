.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/datapath.h

.. _`iwl_data_path_subcmd_ids`:

enum iwl_data_path_subcmd_ids
=============================

.. c:type:: enum iwl_data_path_subcmd_ids

    data path group commands

.. _`iwl_data_path_subcmd_ids.definition`:

Definition
----------

.. code-block:: c

    enum iwl_data_path_subcmd_ids {
        DQA_ENABLE_CMD,
        UPDATE_MU_GROUPS_CMD,
        TRIGGER_RX_QUEUES_NOTIF_CMD,
        STA_HE_CTXT_CMD,
        RFH_QUEUE_CONFIG_CMD,
        TLC_MNG_CONFIG_CMD,
        HE_AIR_SNIFFER_CONFIG_CMD,
        TLC_MNG_UPDATE_NOTIF,
        STA_PM_NOTIF,
        MU_GROUP_MGMT_NOTIF,
        RX_QUEUES_NOTIFICATION
    };

.. _`iwl_data_path_subcmd_ids.constants`:

Constants
---------

DQA_ENABLE_CMD
    \ :c:type:`struct iwl_dqa_enable_cmd <iwl_dqa_enable_cmd>`\ 

UPDATE_MU_GROUPS_CMD
    \ :c:type:`struct iwl_mu_group_mgmt_cmd <iwl_mu_group_mgmt_cmd>`\ 

TRIGGER_RX_QUEUES_NOTIF_CMD
    \ :c:type:`struct iwl_rxq_sync_cmd <iwl_rxq_sync_cmd>`\ 

STA_HE_CTXT_CMD
    \ :c:type:`struct iwl_he_sta_context_cmd <iwl_he_sta_context_cmd>`\ 

RFH_QUEUE_CONFIG_CMD
    \ :c:type:`struct iwl_rfh_queue_config <iwl_rfh_queue_config>`\ 

TLC_MNG_CONFIG_CMD
    \ :c:type:`struct iwl_tlc_config_cmd <iwl_tlc_config_cmd>`\ 

HE_AIR_SNIFFER_CONFIG_CMD
    \ :c:type:`struct iwl_he_monitor_cmd <iwl_he_monitor_cmd>`\ 

TLC_MNG_UPDATE_NOTIF
    \ :c:type:`struct iwl_tlc_update_notif <iwl_tlc_update_notif>`\ 

STA_PM_NOTIF
    \ :c:type:`struct iwl_mvm_pm_state_notification <iwl_mvm_pm_state_notification>`\ 

MU_GROUP_MGMT_NOTIF
    \ :c:type:`struct iwl_mu_group_mgmt_notif <iwl_mu_group_mgmt_notif>`\ 

RX_QUEUES_NOTIFICATION
    \ :c:type:`struct iwl_rxq_sync_notification <iwl_rxq_sync_notification>`\ 

.. _`iwl_mu_group_mgmt_cmd`:

struct iwl_mu_group_mgmt_cmd
============================

.. c:type:: struct iwl_mu_group_mgmt_cmd

    VHT MU-MIMO group configuration

.. _`iwl_mu_group_mgmt_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mu_group_mgmt_cmd {
        __le32 reserved;
        __le32 membership_status[2];
        __le32 user_position[4];
    }

.. _`iwl_mu_group_mgmt_cmd.members`:

Members
-------

reserved
    reserved

membership_status
    a bitmap of MU groups

user_position
    the position of station in a group. If the station is in the
    group then bits (group \* 2) is the position -1

.. _`iwl_mu_group_mgmt_notif`:

struct iwl_mu_group_mgmt_notif
==============================

.. c:type:: struct iwl_mu_group_mgmt_notif

    VHT MU-MIMO group id notification

.. _`iwl_mu_group_mgmt_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mu_group_mgmt_notif {
        __le32 membership_status[2];
        __le32 user_position[4];
    }

.. _`iwl_mu_group_mgmt_notif.members`:

Members
-------

membership_status
    a bitmap of MU groups

user_position
    the position of station in a group. If the station is in the
    group then bits (group \* 2) is the position -1

.. This file was automatic generated / don't edit.

