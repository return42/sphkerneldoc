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
        CHANNEL_SWITCH_NOA_NOTIF
    };

.. _`iwl_mac_conf_subcmd_ids.constants`:

Constants
---------

CHANNEL_SWITCH_NOA_NOTIF
    &struct iwl_channel_switch_noa_notif

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

.. This file was automatic generated / don't edit.

