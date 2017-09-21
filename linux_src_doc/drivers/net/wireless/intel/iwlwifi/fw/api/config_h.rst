.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/config.h

.. _`iwl_calib_ctrl`:

struct iwl_calib_ctrl
=====================

.. c:type:: struct iwl_calib_ctrl

    Calibration control struct. Sent as part of the phy configuration command.

.. _`iwl_calib_ctrl.definition`:

Definition
----------

.. code-block:: c

    struct iwl_calib_ctrl {
        __le32 flow_trigger;
        __le32 event_trigger;
    }

.. _`iwl_calib_ctrl.members`:

Members
-------

flow_trigger
    bitmap for which calibrations to perform according to
    flow triggers, using \ :c:type:`enum iwl_calib_cfg <iwl_calib_cfg>`\ 

event_trigger
    bitmap for which calibrations to perform according to
    event triggers, using \ :c:type:`enum iwl_calib_cfg <iwl_calib_cfg>`\ 

.. _`iwl_phy_cfg_cmd`:

struct iwl_phy_cfg_cmd
======================

.. c:type:: struct iwl_phy_cfg_cmd

    Phy configuration command

.. _`iwl_phy_cfg_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_phy_cfg_cmd {
        __le32 phy_cfg;
        struct iwl_calib_ctrl calib_control;
    }

.. _`iwl_phy_cfg_cmd.members`:

Members
-------

phy_cfg
    PHY configuration value, uses \ :c:type:`enum iwl_fw_phy_cfg <iwl_fw_phy_cfg>`\ 

calib_control
    calibration control data

.. _`iwl_dc2dc_config_cmd`:

struct iwl_dc2dc_config_cmd
===========================

.. c:type:: struct iwl_dc2dc_config_cmd

    configure dc2dc values

.. _`iwl_dc2dc_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dc2dc_config_cmd {
        __le32 flags;
        __le32 enable_low_power_mode;
        __le32 dc2dc_freq_tune0;
        __le32 dc2dc_freq_tune1;
    }

.. _`iwl_dc2dc_config_cmd.members`:

Members
-------

flags
    set/get dc2dc

enable_low_power_mode
    not used.

dc2dc_freq_tune0
    frequency divider - digital domain

dc2dc_freq_tune1
    frequency divider - analog domain

.. _`iwl_dc2dc_config_cmd.description`:

Description
-----------

(DC2DC_CONFIG_CMD = 0x83)

Set/Get & configure dc2dc values.
The command always returns the current dc2dc values.

.. _`iwl_dc2dc_config_resp`:

struct iwl_dc2dc_config_resp
============================

.. c:type:: struct iwl_dc2dc_config_resp

    response for iwl_dc2dc_config_cmd

.. _`iwl_dc2dc_config_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dc2dc_config_resp {
        __le32 dc2dc_freq_tune0;
        __le32 dc2dc_freq_tune1;
    }

.. _`iwl_dc2dc_config_resp.members`:

Members
-------

dc2dc_freq_tune0
    frequency divider - digital domain

dc2dc_freq_tune1
    frequency divider - analog domain

.. _`iwl_dc2dc_config_resp.description`:

Description
-----------

Current dc2dc values returned by the FW.

.. This file was automatic generated / don't edit.

