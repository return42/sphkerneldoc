.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/phy-ctxt.h

.. _`iwl_phy_context_cmd`:

struct iwl_phy_context_cmd
==========================

.. c:type:: struct iwl_phy_context_cmd

    config of the PHY context ( PHY_CONTEXT_CMD = 0x8 )

.. _`iwl_phy_context_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_phy_context_cmd {
        __le32 id_and_color;
        __le32 action;
        __le32 apply_time;
        __le32 tx_param_color;
        struct iwl_fw_channel_info ci;
        __le32 txchain_info;
        __le32 rxchain_info;
        __le32 acquisition_data;
        __le32 dsp_cfg_flags;
    }

.. _`iwl_phy_context_cmd.members`:

Members
-------

id_and_color
    ID and color of the relevant Binding

action
    action to perform, one of FW_CTXT_ACTION\_\*

apply_time
    0 means immediate apply and context switch.
    other value means apply new params after X usecs

tx_param_color
    ???

ci
    channel info

txchain_info
    ???

rxchain_info
    ???

acquisition_data
    ???

dsp_cfg_flags
    set to 0

.. This file was automatic generated / don't edit.

