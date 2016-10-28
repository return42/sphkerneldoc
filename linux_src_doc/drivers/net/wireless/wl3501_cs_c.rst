.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/wl3501_cs.c

.. _`iw_valid_channel`:

iw_valid_channel
================

.. c:function:: int iw_valid_channel(int reg_domain, int channel)

    validate channel in regulatory domain \ ``reg_comain``\  - regulatory domain \ ``channel``\  - channel to validate

    :param int reg_domain:
        *undescribed*

    :param int channel:
        *undescribed*

.. _`iw_valid_channel.description`:

Description
-----------

Returns 0 if invalid in the specified regulatory domain, non-zero if valid.

.. _`iw_default_channel`:

iw_default_channel
==================

.. c:function:: int iw_default_channel(int reg_domain)

    get default channel for a regulatory domain \ ``reg_comain``\  - regulatory domain

    :param int reg_domain:
        *undescribed*

.. _`iw_default_channel.description`:

Description
-----------

Returns the default channel for a regulatory domain

.. _`wl3501_set_to_wla`:

wl3501_set_to_wla
=================

.. c:function:: void wl3501_set_to_wla(struct wl3501_card *this, u16 dest, void *src, int size)

    Move 'size' bytes from PC to card

    :param struct wl3501_card \*this:
        *undescribed*

    :param u16 dest:
        Card addressing space

    :param void \*src:
        PC addressing space

    :param int size:
        Bytes to move

.. _`wl3501_set_to_wla.description`:

Description
-----------

Move 'size' bytes from PC to card. (Shouldn't be interrupted)

.. _`wl3501_get_from_wla`:

wl3501_get_from_wla
===================

.. c:function:: void wl3501_get_from_wla(struct wl3501_card *this, u16 src, void *dest, int size)

    Move 'size' bytes from card to PC

    :param struct wl3501_card \*this:
        *undescribed*

    :param u16 src:
        Card addressing space

    :param void \*dest:
        PC addressing space

    :param int size:
        Bytes to move

.. _`wl3501_get_from_wla.description`:

Description
-----------

Move 'size' bytes from card to PC. (Shouldn't be interrupted)

.. _`wl3501_send_pkt`:

wl3501_send_pkt
===============

.. c:function:: int wl3501_send_pkt(struct wl3501_card *this, u8 *data, u16 len)

    Send a packet. \ ``this``\  - card

    :param struct wl3501_card \*this:
        *undescribed*

    :param u8 \*data:
        *undescribed*

    :param u16 len:
        *undescribed*

.. _`wl3501_send_pkt.description`:

Description
-----------

Send a packet.

data = Ethernet raw frame.  (e.g. data[0] - data[5] is Dest MAC Addr,
data[6] - data[11] is Src MAC Addr)

.. _`wl3501_send_pkt.ref`:

Ref
---

IEEE 802.11

.. _`wl3501_block_interrupt`:

wl3501_block_interrupt
======================

.. c:function:: int wl3501_block_interrupt(struct wl3501_card *this)

    Mask interrupt from SUTRO \ ``this``\  - card

    :param struct wl3501_card \*this:
        *undescribed*

.. _`wl3501_block_interrupt.description`:

Description
-----------

Mask interrupt from SUTRO. (i.e. SUTRO cannot interrupt the HOST)

.. _`wl3501_block_interrupt.return`:

Return
------

1 if interrupt is originally enabled

.. _`wl3501_unblock_interrupt`:

wl3501_unblock_interrupt
========================

.. c:function:: int wl3501_unblock_interrupt(struct wl3501_card *this)

    Enable interrupt from SUTRO \ ``this``\  - card

    :param struct wl3501_card \*this:
        *undescribed*

.. _`wl3501_unblock_interrupt.description`:

Description
-----------

Enable interrupt from SUTRO. (i.e. SUTRO can interrupt the HOST)

.. _`wl3501_unblock_interrupt.return`:

Return
------

1 if interrupt is originally enabled

.. _`wl3501_receive`:

wl3501_receive
==============

.. c:function:: u16 wl3501_receive(struct wl3501_card *this, u8 *bf, u16 size)

    Receive data from Receive Queue.

    :param struct wl3501_card \*this:
        card

    :param u8 \*bf:
        address of host

    :param u16 size:
        size of buffer.

.. _`wl3501_receive.description`:

Description
-----------

Receive data from Receive Queue.

.. _`wl3501_interrupt`:

wl3501_interrupt
================

.. c:function:: irqreturn_t wl3501_interrupt(int irq, void *dev_id)

    Hardware interrupt from card. \ ``irq``\  - Interrupt number \ ``dev_id``\  - net_device

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        *undescribed*

.. _`wl3501_interrupt.description`:

Description
-----------

We must acknowledge the interrupt as soon as possible, and block the
interrupt from the same card immediately to prevent re-entry.

Before accessing the Control_Status_Block, we must lock SUTRO first.
On the other hand, to prevent SUTRO from malfunctioning, we must
unlock the SUTRO as soon as possible.

.. _`wl3501_reset`:

wl3501_reset
============

.. c:function:: int wl3501_reset(struct net_device *dev)

    Reset the SUTRO. \ ``dev``\  - network device

    :param struct net_device \*dev:
        *undescribed*

.. _`wl3501_reset.description`:

Description
-----------

It is almost the same as \ :c:func:`wl3501_open`\ . In fact, we may just \ :c:func:`wl3501_close`\ 
and \ :c:func:`wl3501_open`\  again, but I wouldn't like to \ :c:func:`free_irq`\  when the driver
is running. It seems to be dangerous.

.. _`wl3501_detach`:

wl3501_detach
=============

.. c:function:: void wl3501_detach(struct pcmcia_device *link)

    deletes a driver "instance" \ ``link``\  - FILL_IN

    :param struct pcmcia_device \*link:
        *undescribed*

.. _`wl3501_detach.description`:

Description
-----------

This deletes a driver "instance". The device is de-registered with Card
Services. If it has been released, all local data structures are freed.
Otherwise, the structures will be freed when the device is released.

.. This file was automatic generated / don't edit.

