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
        WMI_10_4_PEER_STATS,
        WMI_10_4_VDEV_STATS,
        WMI_10_4_TDLS,
        WMI_10_4_TDLS_OFFCHAN,
        WMI_10_4_TDLS_UAPSD_BUFFER_STA,
        WMI_10_4_TDLS_UAPSD_SLEEP_STA,
        WMI_10_4_TDLS_CONN_TRACKER_IN_HOST_MODE,
        WMI_10_4_TDLS_EXPLICIT_MODE_ONLY
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

WMI_10_4_VDEV_STATS
    Per vdev stats

WMI_10_4_TDLS
    Implicit TDLS support in firmware enable/disable

WMI_10_4_TDLS_OFFCHAN
    TDLS offchannel support enable/disable

WMI_10_4_TDLS_UAPSD_BUFFER_STA
    TDLS buffer sta support enable/disable

WMI_10_4_TDLS_UAPSD_SLEEP_STA
    TDLS sleep sta support enable/disable

WMI_10_4_TDLS_CONN_TRACKER_IN_HOST_MODE
    TDLS connection tracker in host
    enable/disable

WMI_10_4_TDLS_EXPLICIT_MODE_ONLY
    Explicit TDLS mode enable/disable

.. This file was automatic generated / don't edit.

