.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-modparams.h

.. _`iwl_mod_params`:

struct iwl_mod_params
=====================

.. c:type:: struct iwl_mod_params


.. _`iwl_mod_params.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mod_params {
        int swcrypto;
        unsigned int disable_11n;
        int amsdu_size;
        bool fw_restart;
        bool bt_coex_active;
        int led_mode;
        bool power_save;
        int power_level;
    #ifdef CONFIG_IWLWIFI_DEBUG
        u32 debug_level;
    #endif
        int antenna_coupling;
        char *nvm_file;
        u32 uapsd_disable;
        bool d0i3_disable;
        unsigned int d0i3_timeout;
        bool lar_disable;
        bool fw_monitor;
        bool disable_11ac;
    }

.. _`iwl_mod_params.members`:

Members
-------

swcrypto
    using hardware encryption, default = 0

disable_11n
    disable 11n capabilities, default = 0,
    use IWL_[DIS,EN]ABLE_HT\_\* constants

amsdu_size
    See \ :c:type:`enum iwl_amsdu_size <iwl_amsdu_size>`\ .

fw_restart
    restart firmware, default = 1

bt_coex_active
    enable bt coex, default = true

led_mode
    system default, default = 0

power_save
    enable power save, default = false

power_level
    power level, default = 1

debug_level
    levels are IWL_DL\_\*

antenna_coupling
    antenna coupling in dB, default = 0

nvm_file
    specifies a external NVM file

uapsd_disable
    disable U-APSD, see \ :c:type:`enum iwl_uapsd_disable <iwl_uapsd_disable>`\ , default =
    IWL_DISABLE_UAPSD_BSS \| IWL_DISABLE_UAPSD_P2P_CLIENT

d0i3_disable
    disable d0i3, default = 1,

d0i3_timeout
    time to wait after no refs are taken before
    entering D0i3 (in msecs)

lar_disable
    disable LAR (regulatory), default = 0

fw_monitor
    allow to use firmware monitor

disable_11ac
    disable VHT capabilities, default = false.

.. _`iwl_mod_params.description`:

Description
-----------

Holds the module parameters

.. This file was automatic generated / don't edit.

