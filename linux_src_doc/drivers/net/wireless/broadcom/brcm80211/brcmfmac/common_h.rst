.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.h

.. _`brcmf_mp_global_t`:

struct brcmf_mp_global_t
========================

.. c:type:: struct brcmf_mp_global_t

    Global module paramaters.

.. _`brcmf_mp_global_t.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_mp_global_t {
        char firmware_path[BRCMF_FW_ALTPATH_LEN];
    }

.. _`brcmf_mp_global_t.members`:

Members
-------

firmware_path
    Alternative firmware path.

.. _`brcmf_mp_device`:

struct brcmf_mp_device
======================

.. c:type:: struct brcmf_mp_device

    Device module paramaters.

.. _`brcmf_mp_device.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_mp_device {
        bool p2p_enable;
        unsigned int feature_disable;
        int fcmode;
        bool roamoff;
        bool ignore_probe_fail;
        struct brcmfmac_pd_cc *country_codes;
        union bus;
    }

.. _`brcmf_mp_device.members`:

Members
-------

p2p_enable
    Legacy P2P0 enable (old wpa_supplicant).

feature_disable
    Feature_disable bitmask.

fcmode
    FWS flow control.

roamoff
    Firmware roaming off?

ignore_probe_fail
    Ignore probe failure.

country_codes
    If available, pointer to struct for translating country codes

bus
    Bus specific platform data. Only SDIO at the mmoment.

.. This file was automatic generated / don't edit.

