.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/main.c

.. _`wil6210_disconnect`:

wil6210_disconnect
==================

.. c:function:: void wil6210_disconnect(struct wil6210_vif *vif, const u8 *bssid, u16 reason_code, bool from_event)

    disconnect one connection

    :param vif:
        virtual interface context
    :type vif: struct wil6210_vif \*

    :param bssid:
        peer to disconnect, NULL to disconnect all
    :type bssid: const u8 \*

    :param reason_code:
        Reason code for the Disassociation frame
    :type reason_code: u16

    :param from_event:
        whether is invoked from FW event handler
    :type from_event: bool

.. _`wil6210_disconnect.description`:

Description
-----------

Disconnect and release associated resources. If invoked not from the
FW event handler, issue WMI command(s) to trigger MAC disconnect.

.. This file was automatic generated / don't edit.

