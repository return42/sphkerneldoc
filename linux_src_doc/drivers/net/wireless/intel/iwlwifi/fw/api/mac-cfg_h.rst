.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/mac-cfg.h

.. _`iwl_mac_conf_subcmd_ids`:

enum iwl_mac_conf_subcmd_ids
============================

.. c:type:: enum iwl_mac_conf_subcmd_ids

    mac configuration command IDs

.. _`iwl_mac_conf_subcmd_ids.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mac_conf_subcmd_ids {
        LOW_LATENCY_CMD,
        PROBE_RESPONSE_DATA_NOTIF,
        CHANNEL_SWITCH_NOA_NOTIF
    };

.. _`iwl_mac_conf_subcmd_ids.constants`:

Constants
---------

LOW_LATENCY_CMD
    \ :c:type:`struct iwl_mac_low_latency_cmd <iwl_mac_low_latency_cmd>`\ 

PROBE_RESPONSE_DATA_NOTIF
    \ :c:type:`struct iwl_probe_resp_data_notif <iwl_probe_resp_data_notif>`\ 

CHANNEL_SWITCH_NOA_NOTIF
    \ :c:type:`struct iwl_channel_switch_noa_notif <iwl_channel_switch_noa_notif>`\ 

.. _`iwl_p2p_noa_attr`:

struct iwl_p2p_noa_attr
=======================

.. c:type:: struct iwl_p2p_noa_attr

    NOA attr contained in probe resp FW notification

.. _`iwl_p2p_noa_attr.definition`:

Definition
----------

.. code-block:: c

    struct iwl_p2p_noa_attr {
        u8 id;
        u8 len_low;
        u8 len_high;
        u8 idx;
        u8 ctwin;
        struct ieee80211_p2p_noa_desc desc[IWL_P2P_NOA_DESC_COUNT];
        u8 reserved;
    }

.. _`iwl_p2p_noa_attr.members`:

Members
-------

id
    attribute id

len_low
    length low half

len_high
    length high half

idx
    instance of NoA timing

ctwin
    GO's ct window and pwer save capability

desc
    NoA descriptor

reserved
    reserved for alignment purposes

.. _`iwl_probe_resp_data_notif`:

struct iwl_probe_resp_data_notif
================================

.. c:type:: struct iwl_probe_resp_data_notif

    notification with NOA and CSA counter

.. _`iwl_probe_resp_data_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_probe_resp_data_notif {
        __le32 mac_id;
        __le32 noa_active;
        struct iwl_p2p_noa_attr noa_attr;
        u8 csa_counter;
        u8 reserved[3];
    }

.. _`iwl_probe_resp_data_notif.members`:

Members
-------

mac_id
    the mac which should send the probe response

noa_active
    notifies if the noa attribute should be handled

noa_attr
    P2P NOA attribute

csa_counter
    current csa counter

reserved
    reserved for alignment purposes

.. _`iwl_channel_switch_noa_notif`:

struct iwl_channel_switch_noa_notif
===================================

.. c:type:: struct iwl_channel_switch_noa_notif

    Channel switch NOA notification

.. _`iwl_channel_switch_noa_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_channel_switch_noa_notif {
        __le32 id_and_color;
    }

.. _`iwl_channel_switch_noa_notif.members`:

Members
-------

id_and_color
    ID and color of the MAC

.. _`iwl_mac_low_latency_cmd`:

struct iwl_mac_low_latency_cmd
==============================

.. c:type:: struct iwl_mac_low_latency_cmd

    set/clear mac to 'low-latency mode'

.. _`iwl_mac_low_latency_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_low_latency_cmd {
        __le32 mac_id;
        u8 low_latency_rx;
        u8 low_latency_tx;
        __le16 reserved;
    }

.. _`iwl_mac_low_latency_cmd.members`:

Members
-------

mac_id
    MAC ID to whom to apply the low-latency configurations

low_latency_rx
    1/0 to set/clear Rx low latency direction

low_latency_tx
    1/0 to set/clear Tx low latency direction

reserved
    reserved for alignment purposes

.. This file was automatic generated / don't edit.

