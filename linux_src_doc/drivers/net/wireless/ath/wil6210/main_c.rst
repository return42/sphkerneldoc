.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/main.c

.. _`wil6210_disconnect`:

wil6210_disconnect
==================

.. c:function:: void wil6210_disconnect(struct wil6210_vif *vif, const u8 *bssid, u16 reason_code, bool from_event)

    disconnect one connection

    :param struct wil6210_vif \*vif:
        virtual interface context

    :param const u8 \*bssid:
        peer to disconnect, NULL to disconnect all

    :param u16 reason_code:
        Reason code for the Disassociation frame

    :param bool from_event:
        whether is invoked from FW event handler

.. _`wil6210_disconnect.description`:

Description
-----------

Disconnect and release associated resources. If invoked not from the
FW event handler, issue WMI command(s) to trigger MAC disconnect.

.. This file was automatic generated / don't edit.

