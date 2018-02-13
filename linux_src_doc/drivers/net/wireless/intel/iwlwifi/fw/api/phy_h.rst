.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/phy.h

.. _`iwl_phy_ops_subcmd_ids`:

enum iwl_phy_ops_subcmd_ids
===========================

.. c:type:: enum iwl_phy_ops_subcmd_ids

    PHY group commands

.. _`iwl_phy_ops_subcmd_ids.definition`:

Definition
----------

.. code-block:: c

    enum iwl_phy_ops_subcmd_ids {
        CMD_DTS_MEASUREMENT_TRIGGER_WIDE,
        CTDP_CONFIG_CMD,
        TEMP_REPORTING_THRESHOLDS_CMD,
        GEO_TX_POWER_LIMIT,
        CT_KILL_NOTIFICATION,
        DTS_MEASUREMENT_NOTIF_WIDE
    };

.. _`iwl_phy_ops_subcmd_ids.constants`:

Constants
---------

CMD_DTS_MEASUREMENT_TRIGGER_WIDE
    Uses either \ :c:type:`struct iwl_dts_measurement_cmd <iwl_dts_measurement_cmd>`\  or
    \ :c:type:`struct iwl_ext_dts_measurement_cmd <iwl_ext_dts_measurement_cmd>`\ 

CTDP_CONFIG_CMD
    \ :c:type:`struct iwl_mvm_ctdp_cmd <iwl_mvm_ctdp_cmd>`\ 

TEMP_REPORTING_THRESHOLDS_CMD
    \ :c:type:`struct temp_report_ths_cmd <temp_report_ths_cmd>`\ 

GEO_TX_POWER_LIMIT
    \ :c:type:`struct iwl_geo_tx_power_profiles_cmd <iwl_geo_tx_power_profiles_cmd>`\ 

CT_KILL_NOTIFICATION
    \ :c:type:`struct ct_kill_notif <ct_kill_notif>`\ 

DTS_MEASUREMENT_NOTIF_WIDE
    \ :c:type:`struct iwl_dts_measurement_notif_v1 <iwl_dts_measurement_notif_v1>`\  or
    \ :c:type:`struct iwl_dts_measurement_notif_v2 <iwl_dts_measurement_notif_v2>`\ 

.. _`iwl_dts_measurement_cmd`:

struct iwl_dts_measurement_cmd
==============================

.. c:type:: struct iwl_dts_measurement_cmd

    request DTS temp and/or voltage measurements

.. _`iwl_dts_measurement_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dts_measurement_cmd {
        __le32 flags;
    }

.. _`iwl_dts_measurement_cmd.members`:

Members
-------

flags
    indicates which measurements we want as specified in
    \ :c:type:`enum iwl_dts_measurement_flags <iwl_dts_measurement_flags>`\ 

.. _`iwl_dts_control_measurement_mode`:

enum iwl_dts_control_measurement_mode
=====================================

.. c:type:: enum iwl_dts_control_measurement_mode

    DTS measurement type

.. _`iwl_dts_control_measurement_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_dts_control_measurement_mode {
        DTS_AUTOMATIC,
        DTS_REQUEST_READ,
        DTS_OVER_WRITE,
        DTS_DIRECT_WITHOUT_MEASURE
    };

.. _`iwl_dts_control_measurement_mode.constants`:

Constants
---------

DTS_AUTOMATIC
    Automatic mode (full SW control). Provide temperature read
    back (latest value. Not waiting for new value). Use automatic
    SW DTS configuration.

DTS_REQUEST_READ
    Request DTS read. Configure DTS with manual settings,
    trigger DTS reading and provide read back temperature read
    when available.

DTS_OVER_WRITE
    over-write the DTS temperatures in the SW until next read

DTS_DIRECT_WITHOUT_MEASURE
    DTS returns its latest temperature result,
    without measurement trigger.

.. _`iwl_dts_used`:

enum iwl_dts_used
=================

.. c:type:: enum iwl_dts_used

    DTS to use or used for measurement in the DTS request

.. _`iwl_dts_used.definition`:

Definition
----------

.. code-block:: c

    enum iwl_dts_used {
        DTS_USE_TOP,
        DTS_USE_CHAIN_A,
        DTS_USE_CHAIN_B,
        DTS_USE_CHAIN_C,
        XTAL_TEMPERATURE
    };

.. _`iwl_dts_used.constants`:

Constants
---------

DTS_USE_TOP
    Top

DTS_USE_CHAIN_A
    chain A

DTS_USE_CHAIN_B
    chain B

DTS_USE_CHAIN_C
    chain C

XTAL_TEMPERATURE
    read temperature from xtal

.. _`iwl_dts_bit_mode`:

enum iwl_dts_bit_mode
=====================

.. c:type:: enum iwl_dts_bit_mode

    bit-mode to use in DTS request read mode

.. _`iwl_dts_bit_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_dts_bit_mode {
        DTS_BIT6_MODE,
        DTS_BIT8_MODE
    };

.. _`iwl_dts_bit_mode.constants`:

Constants
---------

DTS_BIT6_MODE
    bit 6 mode

DTS_BIT8_MODE
    bit 8 mode

.. _`iwl_ext_dts_measurement_cmd`:

struct iwl_ext_dts_measurement_cmd
==================================

.. c:type:: struct iwl_ext_dts_measurement_cmd

    request extended DTS temp measurements

.. _`iwl_ext_dts_measurement_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_ext_dts_measurement_cmd {
        __le32 control_mode;
        __le32 temperature;
        __le32 sensor;
        __le32 avg_factor;
        __le32 bit_mode;
        __le32 step_duration;
    }

.. _`iwl_ext_dts_measurement_cmd.members`:

Members
-------

control_mode
    see \ :c:type:`enum iwl_dts_control_measurement_mode <iwl_dts_control_measurement_mode>`\ 

temperature
    used when over write DTS mode is selected

sensor
    set temperature sensor to use. See \ :c:type:`enum iwl_dts_used <iwl_dts_used>`\ 

avg_factor
    average factor to DTS in request DTS read mode

bit_mode
    value defines the DTS bit mode to use. See \ :c:type:`enum iwl_dts_bit_mode <iwl_dts_bit_mode>`\ 

step_duration
    step duration for the DTS

.. _`iwl_dts_measurement_notif_v1`:

struct iwl_dts_measurement_notif_v1
===================================

.. c:type:: struct iwl_dts_measurement_notif_v1

    measurements notification

.. _`iwl_dts_measurement_notif_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dts_measurement_notif_v1 {
        __le32 temp;
        __le32 voltage;
    }

.. _`iwl_dts_measurement_notif_v1.members`:

Members
-------

temp
    the measured temperature

voltage
    the measured voltage

.. _`iwl_dts_measurement_notif_v2`:

struct iwl_dts_measurement_notif_v2
===================================

.. c:type:: struct iwl_dts_measurement_notif_v2

    measurements notification

.. _`iwl_dts_measurement_notif_v2.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dts_measurement_notif_v2 {
        __le32 temp;
        __le32 voltage;
        __le32 threshold_idx;
    }

.. _`iwl_dts_measurement_notif_v2.members`:

Members
-------

temp
    the measured temperature

voltage
    the measured voltage

threshold_idx
    the trip index that was crossed

.. _`ct_kill_notif`:

struct ct_kill_notif
====================

.. c:type:: struct ct_kill_notif

    CT-kill entry notification

.. _`ct_kill_notif.definition`:

Definition
----------

.. code-block:: c

    struct ct_kill_notif {
        __le16 temperature;
        __le16 reserved;
    }

.. _`ct_kill_notif.members`:

Members
-------

temperature
    the current temperature in celsius

reserved
    reserved

.. _`iwl_mvm_ctdp_cmd_operation`:

enum iwl_mvm_ctdp_cmd_operation
===============================

.. c:type:: enum iwl_mvm_ctdp_cmd_operation

    CTDP command operations

.. _`iwl_mvm_ctdp_cmd_operation.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_ctdp_cmd_operation {
        CTDP_CMD_OPERATION_START,
        CTDP_CMD_OPERATION_STOP,
        CTDP_CMD_OPERATION_REPORT
    };

.. _`iwl_mvm_ctdp_cmd_operation.constants`:

Constants
---------

CTDP_CMD_OPERATION_START
    update the current budget

CTDP_CMD_OPERATION_STOP
    stop ctdp

CTDP_CMD_OPERATION_REPORT
    get the average budget

.. _`iwl_mvm_ctdp_cmd`:

struct iwl_mvm_ctdp_cmd
=======================

.. c:type:: struct iwl_mvm_ctdp_cmd

    track and manage the FW power consumption budget

.. _`iwl_mvm_ctdp_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_ctdp_cmd {
        __le32 operation;
        __le32 budget;
        __le32 window_size;
    }

.. _`iwl_mvm_ctdp_cmd.members`:

Members
-------

operation
    see \ :c:type:`enum iwl_mvm_ctdp_cmd_operation <iwl_mvm_ctdp_cmd_operation>`\ 

budget
    the budget in milliwatt

window_size
    defined in API but not used

.. _`temp_report_ths_cmd`:

struct temp_report_ths_cmd
==========================

.. c:type:: struct temp_report_ths_cmd

    set temperature thresholds

.. _`temp_report_ths_cmd.definition`:

Definition
----------

.. code-block:: c

    struct temp_report_ths_cmd {
        __le32 num_temps;
        __le16 thresholds[IWL_MAX_DTS_TRIPS];
    }

.. _`temp_report_ths_cmd.members`:

Members
-------

num_temps
    number of temperature thresholds passed

thresholds
    array with the thresholds to be configured

.. This file was automatic generated / don't edit.

