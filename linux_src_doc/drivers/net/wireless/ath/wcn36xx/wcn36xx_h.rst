.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wcn36xx/wcn36xx.h

.. _`wcn36xx_vif`:

struct wcn36xx_vif
==================

.. c:type:: struct wcn36xx_vif

    holds VIF related fields

.. _`wcn36xx_vif.definition`:

Definition
----------

.. code-block:: c

    struct wcn36xx_vif {
        struct list_head list;
        u8 dtim_period;
        enum ani_ed_type encrypt_type;
        bool is_joining;
        bool sta_assoc;
        struct wcn36xx_hal_mac_ssid ssid;
        enum wcn36xx_hal_bss_type bss_type;
        enum wcn36xx_power_state pw_state;
        u8 bss_index;
        u8 self_sta_index;
        u8 self_dpu_desc_index;
        u8 self_ucast_dpu_sign;
        struct list_head sta_list;
    }

.. _`wcn36xx_vif.members`:

Members
-------

list
    *undescribed*

dtim_period
    *undescribed*

encrypt_type
    *undescribed*

is_joining
    *undescribed*

sta_assoc
    *undescribed*

ssid
    *undescribed*

bss_type
    *undescribed*

pw_state
    *undescribed*

bss_index
    bss_index is initially set to 0xFF. bss_index is received from
    HW after first config_bss call and must be used in delete_bss and
    enter/exit_bmps.

self_sta_index
    *undescribed*

self_dpu_desc_index
    *undescribed*

self_ucast_dpu_sign
    *undescribed*

sta_list
    *undescribed*

.. _`wcn36xx_sta`:

struct wcn36xx_sta
==================

.. c:type:: struct wcn36xx_sta

    holds STA related fields

.. _`wcn36xx_sta.definition`:

Definition
----------

.. code-block:: c

    struct wcn36xx_sta {
        struct list_head list;
        struct wcn36xx_vif *vif;
        u16 aid;
        u16 tid;
        u8 sta_index;
        u8 dpu_desc_index;
        u8 ucast_dpu_sign;
        u8 bss_sta_index;
        u8 bss_dpu_desc_index;
        bool is_data_encrypted;
        struct wcn36xx_hal_supported_rates supported_rates;
        spinlock_t ampdu_lock;
        enum wcn36xx_ampdu_state ampdu_state[16];
        int non_agg_frame_ct;
    }

.. _`wcn36xx_sta.members`:

Members
-------

list
    *undescribed*

vif
    *undescribed*

aid
    *undescribed*

tid
    traffic ID that is used during AMPDU and in TX BD.

sta_index
    STA index is returned from HW after config_sta call and is
    used in both SMD channel and TX BD.

dpu_desc_index
    DPU descriptor index is returned from HW after config_sta
    call and is used in TX BD.

ucast_dpu_sign
    *undescribed*

bss_sta_index
    STA index is returned from HW after config_bss call and is
    used in both SMD channel and TX BD. See table bellow when it is used.

bss_dpu_desc_index
    DPU descriptor index is returned from HW after
    config_bss call and is used in TX BD.
    \______________________________________________
    \|              \|     STA     \|       AP      \|
    \|______________\|_____________\|_______________\|
    \|    TX BD     \|bss_sta_index\|   sta_index   \|
    \|______________\|_____________\|_______________\|
    \|all SMD calls \|bss_sta_index\|   sta_index   \|
    \|______________\|_____________\|_______________\|
    \|smd_delete_sta\|  sta_index  \|   sta_index   \|
    \|______________\|_____________\|_______________\|

is_data_encrypted
    *undescribed*

supported_rates
    *undescribed*

ampdu_lock
    *undescribed*

ampdu_state
    *undescribed*

non_agg_frame_ct
    *undescribed*

.. This file was automatic generated / don't edit.

