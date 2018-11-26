.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/drp-avail.c

.. _`uwb_drp_avail_init`:

uwb_drp_avail_init
==================

.. c:function:: void uwb_drp_avail_init(struct uwb_rc *rc)

    initialize an RC's MAS availability

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

.. _`uwb_drp_avail_init.description`:

Description
-----------

All MAS are available initially.  The RC will inform use which
slots are used for the BP (it may change in size).

.. _`uwb_drp_avail_reserve_pending`:

uwb_drp_avail_reserve_pending
=============================

.. c:function:: int uwb_drp_avail_reserve_pending(struct uwb_rc *rc, struct uwb_mas_bm *mas)

    reserve MAS for a new reservation

    :param rc:
        the radio controller
    :type rc: struct uwb_rc \*

    :param mas:
        the MAS to reserve
    :type mas: struct uwb_mas_bm \*

.. _`uwb_drp_avail_reserve_pending.description`:

Description
-----------

Returns 0 on success, or -EBUSY if the MAS requested aren't available.

.. _`uwb_drp_avail_reserve`:

uwb_drp_avail_reserve
=====================

.. c:function:: void uwb_drp_avail_reserve(struct uwb_rc *rc, struct uwb_mas_bm *mas)

    reserve MAS for an established reservation

    :param rc:
        the radio controller
    :type rc: struct uwb_rc \*

    :param mas:
        the MAS to reserve
    :type mas: struct uwb_mas_bm \*

.. _`uwb_drp_avail_release`:

uwb_drp_avail_release
=====================

.. c:function:: void uwb_drp_avail_release(struct uwb_rc *rc, struct uwb_mas_bm *mas)

    release MAS from a pending or established reservation

    :param rc:
        the radio controller
    :type rc: struct uwb_rc \*

    :param mas:
        the MAS to release
    :type mas: struct uwb_mas_bm \*

.. _`uwb_drp_avail_ie_update`:

uwb_drp_avail_ie_update
=======================

.. c:function:: void uwb_drp_avail_ie_update(struct uwb_rc *rc)

    update the DRP Availability IE

    :param rc:
        the radio controller
    :type rc: struct uwb_rc \*

.. _`uwb_drp_avail_ie_update.description`:

Description
-----------

avail = global & local

.. _`get_val`:

get_val
=======

.. c:function:: unsigned long get_val(u8 *array, size_t itr, size_t len)

    :param array:
        pointer to buffer
    :type array: u8 \*

    :param itr:
        index of buffer from where we start
    :type itr: size_t

    :param len:
        the buffer's remaining size may not be exact multiple of
        sizeof(unsigned long), \ ``len``\  is the length of buffer that needs
        to be converted. This will be sizeof(unsigned long) or smaller
        (BUG if not). If it is smaller then we will pad the remaining
        space of the result with zeroes.
    :type len: size_t

.. _`buffer_to_bmp`:

buffer_to_bmp
=============

.. c:function:: void buffer_to_bmp(unsigned long *bmp_itr, void *_buffer, size_t buffer_size)

    :param bmp_itr:
        pointer to bitmap (can be declared with DECLARE_BITMAP)
    :type bmp_itr: unsigned long \*

    :param _buffer:
        *undescribed*
    :type _buffer: void \*

    :param buffer_size:
        number of bytes with which bitmap should be initialized
    :type buffer_size: size_t

.. _`buffer_to_bmp.description`:

Description
-----------

The bitmap to be converted could come from a IE, for example a
DRP Availability IE.
From ECMA-368 1.0 [16.8.7]: "

.. _`buffer_to_bmp.octets`:

octets
------

1            1               N \* (0 to 32)
Element ID   Length (=N)     DRP Availability Bitmap

The DRP Availability Bitmap field is up to 256 bits long, one
bit for each MAS in the superframe, where the least-significant
bit of the field corresponds to the first MAS in the superframe
and successive bits correspond to successive MASs."

The DRP Availability bitmap is in octets from 0 to 32, so octet
32 contains bits for MAS 1-8, etc. If the bitmap is smaller than 32
octets, the bits in octets not included at the end of the bitmap are
treated as zero. In this case (when the bitmap is smaller than 32
octets) the MAS represented range from MAS 1 to MAS (size of bitmap)
with the last octet still containing bits for MAS 1-8, etc.

.. _`buffer_to_bmp.for-example`:

For example
-----------

F00F0102 03040506 0708090A 0B0C0D0E 0F010203
^^^^
\|\|\|\|
\|\|\|\|
\|\|\|\LSB of byte is MAS 9
\|\|\MSB of byte is MAS 16
\|\LSB of first byte is MAS 1
\ MSB of byte is MAS 8

An example of this encoding can be found in ECMA-368 Annex-D [Table D.11]

.. _`buffer_to_bmp.the-resulting-bitmap-will-have-the-following-mapping`:

The resulting bitmap will have the following mapping
----------------------------------------------------

bit position 0 == MAS 1
bit position 1 == MAS 2
...
bit position (UWB_NUM_MAS - 1) == MAS UWB_NUM_MAS

.. _`uwbd_evt_get_drp_avail`:

uwbd_evt_get_drp_avail
======================

.. c:function:: int uwbd_evt_get_drp_avail(struct uwb_event *evt, unsigned long *bmp)

    :param evt:
        *undescribed*
    :type evt: struct uwb_event \*

    :param bmp:
        *undescribed*
    :type bmp: unsigned long \*

.. _`uwbd_evt_get_drp_avail.description`:

Description
-----------

The notification that comes in contains a bitmap of (UWB_NUM_MAS / 8) bytes
We convert that to our internal representation.

.. _`uwbd_evt_handle_rc_drp_avail`:

uwbd_evt_handle_rc_drp_avail
============================

.. c:function:: int uwbd_evt_handle_rc_drp_avail(struct uwb_event *evt)

    :param evt:
        Event information (packs the actual event data, which
        radio controller it came to, etc).
    :type evt: struct uwb_event \*

.. _`uwbd_evt_handle_rc_drp_avail.description`:

Description
-----------

According to ECMA-368 1.0 [16.8.7], bits set to ONE indicate that
the MAS slot is available, bits set to ZERO indicate that the slot
is busy.

So we clear available slots, we set used slots :)

The notification only marks non-availability based on the BP and
received DRP IEs that are not for this radio controller.  A copy of
this bitmap is needed to generate the real availability (which
includes local and pending reservations).

The DRP Availability IE that this radio controller emits will need
to be updated.

.. This file was automatic generated / don't edit.

