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
        CHANNEL_SWITCH_NOA_NOTIF
    };

.. _`iwl_mac_conf_subcmd_ids.constants`:

Constants
---------

LOW_LATENCY_CMD
    \ :c:type:`struct iwl_mac_low_latency_cmd <iwl_mac_low_latency_cmd>`\ 

CHANNEL_SWITCH_NOA_NOTIF
    \ :c:type:`struct iwl_channel_switch_noa_notif <iwl_channel_switch_noa_notif>`\ 

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

