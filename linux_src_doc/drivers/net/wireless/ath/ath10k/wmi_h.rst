.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath10k/wmi.h

.. _`wmi_10_4_feature_mask`:

enum wmi_10_4_feature_mask
==========================

.. c:type:: enum wmi_10_4_feature_mask

    WMI 10.4 feature enable/disable flags

.. _`wmi_10_4_feature_mask.definition`:

Definition
----------

.. code-block:: c

    enum wmi_10_4_feature_mask {
        WMI_10_4_LTEU_SUPPORT,
        WMI_10_4_COEX_GPIO_SUPPORT,
        WMI_10_4_AUX_RADIO_SPECTRAL_INTF,
        WMI_10_4_AUX_RADIO_CHAN_LOAD_INTF,
        WMI_10_4_BSS_CHANNEL_INFO_64,
        WMI_10_4_PEER_STATS
    };

.. _`wmi_10_4_feature_mask.constants`:

Constants
---------

WMI_10_4_LTEU_SUPPORT
    LTEU config

WMI_10_4_COEX_GPIO_SUPPORT
    COEX GPIO config

WMI_10_4_AUX_RADIO_SPECTRAL_INTF
    AUX Radio Enhancement for spectral scan

WMI_10_4_AUX_RADIO_CHAN_LOAD_INTF
    AUX Radio Enhancement for chan load scan

WMI_10_4_BSS_CHANNEL_INFO_64
    BSS channel info stats

WMI_10_4_PEER_STATS
    Per station stats

.. This file was automatic generated / don't edit.

