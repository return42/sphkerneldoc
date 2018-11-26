.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/zydas/zd1211rw/zd_usb.c

.. _`zd_usb_disable_tx`:

zd_usb_disable_tx
=================

.. c:function:: void zd_usb_disable_tx(struct zd_usb *usb)

    disable transmission

    :param usb:
        the zd1211rw-private USB structure
    :type usb: struct zd_usb \*

.. _`zd_usb_disable_tx.description`:

Description
-----------

Frees all URBs in the free list and marks the transmission as disabled.

.. _`zd_usb_enable_tx`:

zd_usb_enable_tx
================

.. c:function:: void zd_usb_enable_tx(struct zd_usb *usb)

    enables transmission

    :param usb:
        a \ :c:type:`struct zd_usb <zd_usb>`\  pointer
    :type usb: struct zd_usb \*

.. _`zd_usb_enable_tx.description`:

Description
-----------

This function enables transmission and prepares the \ :c:type:`struct zd_usb_tx <zd_usb_tx>`\  data
structure.

.. _`tx_urb_complete`:

tx_urb_complete
===============

.. c:function:: void tx_urb_complete(struct urb *urb)

    completes the execution of an URB

    :param urb:
        a URB
    :type urb: struct urb \*

.. _`tx_urb_complete.description`:

Description
-----------

This function is called if the URB has been transferred to a device or an
error has happened.

.. _`zd_usb_tx`:

zd_usb_tx
=========

.. c:function:: int zd_usb_tx(struct zd_usb *usb, struct sk_buff *skb)

    initiates transfer of a frame of the device

    :param usb:
        the zd1211rw-private USB structure
    :type usb: struct zd_usb \*

    :param skb:
        a \ :c:type:`struct sk_buff <sk_buff>`\  pointer
    :type skb: struct sk_buff \*

.. _`zd_usb_tx.description`:

Description
-----------

This function tranmits a frame to the device. It doesn't wait for
completion. The frame must contain the control set and have all the
control set information available.

The function returns 0 if the transfer has been successfully initiated.

.. This file was automatic generated / don't edit.

