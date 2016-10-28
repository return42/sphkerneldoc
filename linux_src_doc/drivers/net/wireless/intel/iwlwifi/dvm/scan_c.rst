.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/scan.c

.. _`iwl_scan_cancel`:

iwl_scan_cancel
===============

.. c:function:: int iwl_scan_cancel(struct iwl_priv *priv)

    Cancel any currently executing HW scan

    :param struct iwl_priv \*priv:
        *undescribed*

.. _`iwl_scan_cancel_timeout`:

iwl_scan_cancel_timeout
=======================

.. c:function:: void iwl_scan_cancel_timeout(struct iwl_priv *priv, unsigned long ms)

    Cancel any currently executing HW scan

    :param struct iwl_priv \*priv:
        *undescribed*

    :param unsigned long ms:
        amount of time to wait (in milliseconds) for scan to abort

.. _`iwl_fill_probe_req`:

iwl_fill_probe_req
==================

.. c:function:: u16 iwl_fill_probe_req(struct ieee80211_mgmt *frame, const u8 *ta, const u8 *ies, int ie_len, const u8 *ssid, u8 ssid_len, int left)

    fill in all required fields and IE for probe request

    :param struct ieee80211_mgmt \*frame:
        *undescribed*

    :param const u8 \*ta:
        *undescribed*

    :param const u8 \*ies:
        *undescribed*

    :param int ie_len:
        *undescribed*

    :param const u8 \*ssid:
        *undescribed*

    :param u8 ssid_len:
        *undescribed*

    :param int left:
        *undescribed*

.. This file was automatic generated / don't edit.

