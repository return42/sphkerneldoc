.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/zydas/zd1211rw/zd_usb.h

.. _`zd_usb_tx`:

struct zd_usb_tx
================

.. c:type:: struct zd_usb_tx

    structure used for transmitting frames

.. _`zd_usb_tx.definition`:

Definition
----------

.. code-block:: c

    struct zd_usb_tx {
        atomic_t enabled;
        spinlock_t lock;
        struct delayed_work watchdog_work;
        struct sk_buff_head submitted_skbs;
        struct usb_anchor submitted;
        int submitted_urbs;
        u8 stopped:1, watchdog_enabled:1;
    }

.. _`zd_usb_tx.members`:

Members
-------

enabled
    atomic enabled flag, indicates whether tx is enabled

lock
    lock for transmission

watchdog_work
    *undescribed*

submitted_skbs
    *undescribed*

submitted
    anchor for URBs sent to device

submitted_urbs
    atomic integer that counts the URBs having sent to the
    device, which haven't been completed

stopped
    indicates whether higher level tx queues are stopped

watchdog_enabled
    *undescribed*

.. This file was automatic generated / don't edit.

