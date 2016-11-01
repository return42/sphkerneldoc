.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-coex.h

.. _`iwl_bt_coex_cmd`:

struct iwl_bt_coex_cmd
======================

.. c:type:: struct iwl_bt_coex_cmd

    bt coex configuration command

.. _`iwl_bt_coex_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bt_coex_cmd {
        __le32 mode;
        __le32 enabled_modules;
    }

.. _`iwl_bt_coex_cmd.members`:

Members
-------

mode
    enum \ ``iwl_bt_coex_mode``\ 

enabled_modules
    enum \ ``iwl_bt_coex_enabled_modules``\ 

.. _`iwl_bt_coex_cmd.description`:

Description
-----------

The structure is used for the BT_COEX command.

.. _`iwl_bt_coex_corun_lut_update_cmd`:

struct iwl_bt_coex_corun_lut_update_cmd
=======================================

.. c:type:: struct iwl_bt_coex_corun_lut_update_cmd

    bt coex update the corun lut

.. _`iwl_bt_coex_corun_lut_update_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bt_coex_corun_lut_update_cmd {
        __le32 corun_lut20[BT_COEX_CORUN_LUT_SIZE];
        __le32 corun_lut40[BT_COEX_CORUN_LUT_SIZE];
    }

.. _`iwl_bt_coex_corun_lut_update_cmd.members`:

Members
-------

corun_lut20
    co-running 20 MHz LUT configuration

corun_lut40
    co-running 40 MHz LUT configuration

.. _`iwl_bt_coex_corun_lut_update_cmd.description`:

Description
-----------

The structure is used for the BT_COEX_UPDATE_CORUN_LUT command.

.. _`iwl_bt_coex_reduced_txp_update_cmd`:

struct iwl_bt_coex_reduced_txp_update_cmd
=========================================

.. c:type:: struct iwl_bt_coex_reduced_txp_update_cmd


.. _`iwl_bt_coex_reduced_txp_update_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bt_coex_reduced_txp_update_cmd {
        __le32 reduced_txp;
    }

.. _`iwl_bt_coex_reduced_txp_update_cmd.members`:

Members
-------

reduced_txp
    bit BT_REDUCED_TX_POWER_BIT to enable / disable, rest of the
    bits are the sta_id (value)

.. _`iwl_bt_coex_ci_cmd`:

struct iwl_bt_coex_ci_cmd
=========================

.. c:type:: struct iwl_bt_coex_ci_cmd

    bt coex channel inhibition command

.. _`iwl_bt_coex_ci_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bt_coex_ci_cmd {
        __le64 bt_primary_ci;
        __le32 primary_ch_phy_id;
        __le64 bt_secondary_ci;
        __le32 secondary_ch_phy_id;
    }

.. _`iwl_bt_coex_ci_cmd.members`:

Members
-------

bt_primary_ci
    *undescribed*

primary_ch_phy_id
    *undescribed*

bt_secondary_ci
    *undescribed*

secondary_ch_phy_id
    *undescribed*

.. _`iwl_bt_coex_ci_cmd.description`:

Description
-----------

Used for BT_COEX_CI command

.. _`iwl_bt_coex_profile_notif`:

struct iwl_bt_coex_profile_notif
================================

.. c:type:: struct iwl_bt_coex_profile_notif

    notification about BT coex

.. _`iwl_bt_coex_profile_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bt_coex_profile_notif {
        __le32 mbox_msg[4];
        __le32 msg_idx;
        __le32 bt_ci_compliance;
        __le32 primary_ch_lut;
        __le32 secondary_ch_lut;
        __le32 bt_activity_grading;
        u8 ttc_rrc_status;
        u8 reserved[3];
    }

.. _`iwl_bt_coex_profile_notif.members`:

Members
-------

mbox_msg
    message from BT to WiFi

msg_idx
    the index of the message

bt_ci_compliance
    enum \ ``iwl_bt_ci_compliance``\ 

primary_ch_lut
    LUT used for primary channel enum \ ``iwl_bt_coex_lut_type``\ 

secondary_ch_lut
    LUT used for secondary channel enume \ ``iwl_bt_coex_lut_type``\ 

bt_activity_grading
    the activity of BT enum \ ``iwl_bt_activity_grading``\ 

ttc_rrc_status
    is TTC or RRC enabled - one bit per PHY

.. This file was automatic generated / don't edit.

