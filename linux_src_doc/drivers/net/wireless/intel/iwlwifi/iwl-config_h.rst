.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-config.h

.. _`iwl_tt_params`:

struct iwl_tt_params
====================

.. c:type:: struct iwl_tt_params

    thermal throttling parameters

.. _`iwl_tt_params.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tt_params {
        u32 ct_kill_entry;
        u32 ct_kill_exit;
        u32 ct_kill_duration;
        u32 dynamic_smps_entry;
        u32 dynamic_smps_exit;
        u32 tx_protection_entry;
        u32 tx_protection_exit;
        struct iwl_tt_tx_backoff tx_backoff[TT_TX_BACKOFF_SIZE];
        u8 support_ct_kill:1;
        u8 support_dynamic_smps:1:1;
        u8 support_tx_protection:1:1:1;
        u8 support_tx_backoff:1:1:1:1;
    }

.. _`iwl_tt_params.members`:

Members
-------

ct_kill_entry
    CT Kill entry threshold

ct_kill_exit
    CT Kill exit threshold

ct_kill_duration
    The time  intervals (in uSec) in which the driver needs
    to checks whether to exit CT Kill.

dynamic_smps_entry
    Dynamic SMPS entry threshold

dynamic_smps_exit
    Dynamic SMPS exit threshold

tx_protection_entry
    TX protection entry threshold

tx_protection_exit
    TX protection exit threshold

tx_backoff
    Array of thresholds for tx-backoff , in ascending order.

support_ct_kill
    Support CT Kill?

support_dynamic_smps
    Support dynamic SMPS?

support_tx_protection
    Support tx protection?

support_tx_backoff
    Support tx-backoff?

.. _`iwl_cfg`:

struct iwl_cfg
==============

.. c:type:: struct iwl_cfg


.. _`iwl_cfg.definition`:

Definition
----------

.. code-block:: c

    struct iwl_cfg {
        const char *name;
        const char *fw_name_pre;
        const char *fw_name_pre_next_step;
        const struct iwl_base_params *base_params;
        const struct iwl_ht_params *ht_params;
        const struct iwl_eeprom_params *eeprom_params;
        const struct iwl_pwr_tx_backoff *pwr_tx_backoffs;
        const char *default_nvm_file_B_step;
        const char *default_nvm_file_C_step;
        const struct iwl_tt_params *thermal_params;
        enum iwl_device_family device_family;
        enum iwl_led_mode led_mode;
        u32 max_data_size;
        u32 max_inst_size;
        netdev_features_t features;
        u32 dccm_offset;
        u32 dccm_len;
        u32 dccm2_offset;
        u32 dccm2_len;
        u32 smem_offset;
        u32 smem_len;
        u16 nvm_ver;
        u16 nvm_calib_ver;
        u16 rx_with_siso_diversity:1;
        u16 bt_shared_single_ant:1:1;
        u16 internal_wimax_coex:1:1:1;
        u16 host_interrupt_operation_mode:1:1:1:1;
        u16 high_temp:1:1:1:1:1;
        u16 mac_addr_from_csr:1:1:1:1:1:1;
        u16 lp_xtal_workaround:1:1:1:1:1:1:1;
        u16 disable_dummy_notification:1:1:1:1:1:1:1:1;
        u16 apmg_not_supported:1:1:1:1:1:1:1:1:1;
        u16 mq_rx_supported:1:1:1:1:1:1:1:1:1:1;
        u16 vht_mu_mimo_supported:1:1:1:1:1:1:1:1:1:1:1;
        u16 rf_id:1:1:1:1:1:1:1:1:1:1:1:1;
        u16 integrated:1:1:1:1:1:1:1:1:1:1:1:1:1;
        u16 use_tfh:1:1:1:1:1:1:1:1:1:1:1:1:1:1;
        u16 gen2:1:1:1:1:1:1:1:1:1:1:1:1:1:1:1;
        u16 cdb:1:1:1:1:1:1:1:1:1:1:1:1:1:1:1:1;
        u8 valid_tx_ant;
        u8 valid_rx_ant;
        u8 non_shared_ant;
        u8 nvm_hw_section_num;
        u8 max_rx_agg_size;
        u8 max_tx_agg_size;
        u8 max_ht_ampdu_exponent;
        u8 max_vht_ampdu_exponent;
        u8 ucode_api_max;
        u8 ucode_api_min;
    }

.. _`iwl_cfg.members`:

Members
-------

name
    Official name of the device

fw_name_pre
    Firmware filename prefix. The api version and extension
    (.ucode) will be added to filename before loading from disk. The
    filename is constructed as fw_name_pre<api>.ucode.

fw_name_pre_next_step
    same as \ ``fw_name_pre``\ , only for next step
    (if supported)

base_params
    pointer to basic parameters

ht_params
    point to ht parameters

eeprom_params
    *undescribed*

pwr_tx_backoffs
    translation table between power limits and backoffs

default_nvm_file_B_step
    *undescribed*

default_nvm_file_C_step
    *undescribed*

thermal_params
    *undescribed*

device_family
    *undescribed*

led_mode
    0=blinking, 1=On(RF On)/Off(RF Off)

max_data_size
    The maximal length of the fw data section

max_inst_size
    The maximal length of the fw inst section

features
    hw features, any combination of feature_whitelist

dccm_offset
    offset from which DCCM begins

dccm_len
    length of DCCM (including runtime stack CCM)

dccm2_offset
    offset from which the second DCCM begins

dccm2_len
    length of the second DCCM

smem_offset
    offset from which the SMEM begins

smem_len
    the length of SMEM

nvm_ver
    NVM version

nvm_calib_ver
    NVM calibration version

rx_with_siso_diversity
    1x1 device with rx antenna diversity

bt_shared_single_ant
    *undescribed*

internal_wimax_coex
    internal wifi/wimax combo device

host_interrupt_operation_mode
    device needs host interrupt operation
    mode set

high_temp
    Is this NIC is designated to be in high temperature.

mac_addr_from_csr
    read HW address from CSR registers

lp_xtal_workaround
    *undescribed*

disable_dummy_notification
    *undescribed*

apmg_not_supported
    *undescribed*

mq_rx_supported
    multi-queue rx support

vht_mu_mimo_supported
    VHT MU-MIMO support

rf_id
    need to read rf_id to determine the firmware image

integrated
    discrete or integrated

use_tfh
    *undescribed*

gen2
    a000 and on transport operation

cdb
    CDB support

valid_tx_ant
    valid transmit antenna

valid_rx_ant
    valid receive antenna

non_shared_ant
    the antenna that is for WiFi only

nvm_hw_section_num
    the ID of the HW NVM section

max_rx_agg_size
    max RX aggregation size of the ADDBA request/response

max_tx_agg_size
    max TX aggregation size of the ADDBA request/response

max_ht_ampdu_exponent
    *undescribed*

max_vht_ampdu_exponent
    the exponent of the max length of A-MPDU that the
    station can receive in VHT

ucode_api_max
    Highest version of uCode API supported by driver.

ucode_api_min
    Lowest version of uCode API supported by driver.

.. _`iwl_cfg.description`:

Description
-----------

We enable the driver to be backward compatible wrt. hardware features.
API differences in uCode shouldn't be handled here but through TLVs
and/or the uCode API version instead.

.. This file was automatic generated / don't edit.

