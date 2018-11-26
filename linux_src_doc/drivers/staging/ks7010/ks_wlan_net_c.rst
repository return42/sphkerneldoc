.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ks7010/ks_wlan_net.c

.. _`is_connect_status`:

is_connect_status
=================

.. c:function:: bool is_connect_status(u32 status)

    return true if status is 'connected'

    :param status:
        high bit is used as FORCE_DISCONNECT, low bits used for
        connect status.
    :type status: u32

.. _`is_disconnect_status`:

is_disconnect_status
====================

.. c:function:: bool is_disconnect_status(u32 status)

    return true if status is 'disconnected'

    :param status:
        high bit is used as FORCE_DISCONNECT, low bits used for
        disconnect status.
    :type status: u32

.. This file was automatic generated / don't edit.

