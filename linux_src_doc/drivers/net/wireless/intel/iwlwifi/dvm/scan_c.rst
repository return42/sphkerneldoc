.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/scan.c

.. _`iwl_scan_cancel`:

iwl_scan_cancel
===============

.. c:function:: int iwl_scan_cancel(struct iwl_priv *priv)

    Cancel any currently executing HW scan

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

.. _`iwl_scan_cancel_timeout`:

iwl_scan_cancel_timeout
=======================

.. c:function:: void iwl_scan_cancel_timeout(struct iwl_priv *priv, unsigned long ms)

    Cancel any currently executing HW scan

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ms:
        amount of time to wait (in milliseconds) for scan to abort
    :type ms: unsigned long

.. _`iwl_fill_probe_req`:

iwl_fill_probe_req
==================

.. c:function:: u16 iwl_fill_probe_req(struct ieee80211_mgmt *frame, const u8 *ta, const u8 *ies, int ie_len, const u8 *ssid, u8 ssid_len, int left)

    fill in all required fields and IE for probe request

    :param frame:
        *undescribed*
    :type frame: struct ieee80211_mgmt \*

    :param ta:
        *undescribed*
    :type ta: const u8 \*

    :param ies:
        *undescribed*
    :type ies: const u8 \*

    :param ie_len:
        *undescribed*
    :type ie_len: int

    :param ssid:
        *undescribed*
    :type ssid: const u8 \*

    :param ssid_len:
        *undescribed*
    :type ssid_len: u8

    :param left:
        *undescribed*
    :type left: int

.. This file was automatic generated / don't edit.

