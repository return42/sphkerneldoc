.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-coex.h

.. _`iwl_bt_coex_flags`:

enum iwl_bt_coex_flags
======================

.. c:type:: enum iwl_bt_coex_flags

    flags for BT_COEX command

.. _`iwl_bt_coex_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_bt_coex_flags {
        BT_COEX_MODE_POS,
        BT_COEX_MODE_MSK,
        BT_COEX_DISABLE_OLD,
        BT_COEX_2W_OLD,
        BT_COEX_3W_OLD,
        BT_COEX_NW_OLD,
        BT_COEX_AUTO_OLD,
        BT_COEX_BT_OLD,
        BT_COEX_WIFI_OLD,
        BT_COEX_SYNC2SCO,
        BT_COEX_CORUNNING,
        BT_COEX_MPLUT,
        BT_COEX_TTC,
        BT_COEX_RRC
    };

.. _`iwl_bt_coex_flags.constants`:

Constants
---------

BT_COEX_MODE_POS
    *undescribed*

BT_COEX_MODE_MSK
    *undescribed*

BT_COEX_DISABLE_OLD
    *undescribed*

BT_COEX_2W_OLD
    *undescribed*

BT_COEX_3W_OLD
    *undescribed*

BT_COEX_NW_OLD
    *undescribed*

BT_COEX_AUTO_OLD
    *undescribed*

BT_COEX_BT_OLD
    Antenna is for BT (manufacuring tests)

BT_COEX_WIFI_OLD
    Antenna is for BT (manufacuring tests)

BT_COEX_SYNC2SCO
    *undescribed*

BT_COEX_CORUNNING
    *undescribed*

BT_COEX_MPLUT
    *undescribed*

BT_COEX_TTC
    *undescribed*

BT_COEX_RRC
    *undescribed*

.. _`iwl_bt_coex_flags.description`:

Description
-----------

The COEX_MODE must be set for each command. Even if it is not changed.

.. _`iwl_bt_reduced_tx_power`:

enum iwl_bt_reduced_tx_power
============================

.. c:type:: enum iwl_bt_reduced_tx_power

    allows to reduce txpower for WiFi frames.

.. _`iwl_bt_reduced_tx_power.definition`:

Definition
----------

.. code-block:: c

    enum iwl_bt_reduced_tx_power {
        BT_REDUCED_TX_POWER_CTL,
        BT_REDUCED_TX_POWER_DATA
    };

.. _`iwl_bt_reduced_tx_power.constants`:

Constants
---------

BT_REDUCED_TX_POWER_CTL
    reduce Tx power for control frames

BT_REDUCED_TX_POWER_DATA
    reduce Tx power for data frames

.. _`iwl_bt_reduced_tx_power.description`:

Description
-----------

This mechanism allows to have BT and WiFi run concurrently. Since WiFi
reduces its Tx power, it can work along with BT, hence reducing the amount
of WiFi frames being killed by BT.

.. _`iwl_bt_coex_cmd_old`:

struct iwl_bt_coex_cmd_old
==========================

.. c:type:: struct iwl_bt_coex_cmd_old

    bt coex configuration command

.. _`iwl_bt_coex_cmd_old.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bt_coex_cmd_old {
        __le32 flags;
        u8 max_kill;
        u8 bt_reduced_tx_power;
        u8 override_primary_lut;
        u8 override_secondary_lut;
        u8 bt4_antenna_isolation;
        u8 bt4_antenna_isolation_thr;
        u8 bt4_tx_tx_delta_freq_thr;
        u8 bt4_tx_rx_max_freq0;
        __le32 bt_prio_boost[BT_COEX_BOOST_SIZE];
        __le32 wifi_tx_prio_boost;
        __le32 wifi_rx_prio_boost;
        __le32 kill_ack_msk;
        __le32 kill_cts_msk;
        __le32 decision_lut[BT_COEX_MAX_LUT][BT_COEX_LUT_SIZE];
        __le32 bt4_multiprio_lut[BT_COEX_MULTI_PRIO_LUT_SIZE];
        __le32 bt4_corun_lut20[BT_COEX_CORUN_LUT_SIZE];
        __le32 bt4_corun_lut40[BT_COEX_CORUN_LUT_SIZE];
        __le32 valid_bit_msk;
    }

.. _`iwl_bt_coex_cmd_old.members`:

Members
-------

flags
    \ :c:type:`enum iwl_bt_coex_flags <iwl_bt_coex_flags>`\ 

max_kill
    *undescribed*

bt_reduced_tx_power
    enum \ ``iwl_bt_reduced_tx_power``\ 

override_primary_lut
    enum \ ``iwl_bt_coex_lut_type``\ : BT_COEX_INVALID_LUT
    should be set by default

override_secondary_lut
    enum \ ``iwl_bt_coex_lut_type``\ : BT_COEX_INVALID_LUT
    should be set by default

bt4_antenna_isolation
    antenna isolation

bt4_antenna_isolation_thr
    antenna threshold value

bt4_tx_tx_delta_freq_thr
    TxTx delta frequency

bt4_tx_rx_max_freq0
    TxRx max frequency

bt_prio_boost
    BT priority boost registers

wifi_tx_prio_boost
    SW boost of wifi tx priority

wifi_rx_prio_boost
    SW boost of wifi rx priority

kill_ack_msk
    kill ACK mask. 1 - Tx ACK, 0 - kill Tx of ACK.

kill_cts_msk
    kill CTS mask. 1 - Tx CTS, 0 - kill Tx of CTS.

decision_lut
    PTA decision LUT, per Prio-Ch

bt4_multiprio_lut
    multi priority LUT configuration

bt4_corun_lut20
    co-running 20 MHz LUT configuration

bt4_corun_lut40
    co-running 40 MHz LUT configuration

valid_bit_msk
    enum \ ``iwl_bt_coex_valid_bit_msk``\ 

.. _`iwl_bt_coex_cmd_old.description`:

Description
-----------

The structure is used for the BT_COEX command.

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

.. _`iwl_bt_coex_prio_tbl_cmd`:

struct iwl_bt_coex_prio_tbl_cmd
===============================

.. c:type:: struct iwl_bt_coex_prio_tbl_cmd

    priority table for BT coex

.. _`iwl_bt_coex_prio_tbl_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bt_coex_prio_tbl_cmd {
        u8 prio_tbl[BT_COEX_PRIO_TBL_EVT_MAX];
    }

.. _`iwl_bt_coex_prio_tbl_cmd.members`:

Members
-------

.. _`iwl_bt_coex_ci_cmd_old`:

struct iwl_bt_coex_ci_cmd_old
=============================

.. c:type:: struct iwl_bt_coex_ci_cmd_old

    bt coex channel inhibition command

.. _`iwl_bt_coex_ci_cmd_old.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bt_coex_ci_cmd_old {
        __le64 bt_primary_ci;
        __le64 bt_secondary_ci;
        u8 co_run_bw_primary;
        u8 co_run_bw_secondary;
        u8 primary_ch_phy_id;
        u8 secondary_ch_phy_id;
    }

.. _`iwl_bt_coex_ci_cmd_old.members`:

Members
-------

bt_primary_ci
    *undescribed*

bt_secondary_ci
    *undescribed*

co_run_bw_primary
    *undescribed*

co_run_bw_secondary
    *undescribed*

primary_ch_phy_id
    *undescribed*

secondary_ch_phy_id
    *undescribed*

.. _`iwl_bt_coex_ci_cmd_old.description`:

Description
-----------

Used for BT_COEX_CI command

.. _`iwl_bt_coex_profile_notif_old`:

struct iwl_bt_coex_profile_notif_old
====================================

.. c:type:: struct iwl_bt_coex_profile_notif_old

    notification about BT coex

.. _`iwl_bt_coex_profile_notif_old.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bt_coex_profile_notif_old {
        __le32 mbox_msg[4];
        __le32 msg_idx;
        u8 bt_status;
        u8 bt_open_conn;
        u8 bt_traffic_load;
        u8 bt_agg_traffic_load;
        u8 bt_ci_compliance;
        u8 ttc_enabled;
        u8 rrc_enabled;
        u8 reserved;
        __le32 primary_ch_lut;
        __le32 secondary_ch_lut;
        __le32 bt_activity_grading;
    }

.. _`iwl_bt_coex_profile_notif_old.members`:

Members
-------

mbox_msg
    message from BT to WiFi

msg_idx
    the index of the message

bt_status
    0 - off, 1 - on

bt_open_conn
    number of BT connections open

bt_traffic_load
    load of BT traffic

bt_agg_traffic_load
    aggregated load of BT traffic

bt_ci_compliance
    0 - no CI compliance, 1 - CI compliant

ttc_enabled
    *undescribed*

rrc_enabled
    *undescribed*

reserved
    *undescribed*

primary_ch_lut
    LUT used for primary channel

secondary_ch_lut
    LUT used for secondary channel

bt_activity_grading
    the activity of BT enum \ ``iwl_bt_activity_grading``\ 

.. This file was automatic generated / don't edit.

