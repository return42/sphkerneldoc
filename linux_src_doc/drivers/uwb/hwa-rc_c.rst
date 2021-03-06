.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/hwa-rc.c

.. _`hwarc_filter_evt_beacon_wusb_0100`:

hwarc_filter_evt_beacon_WUSB_0100
=================================

.. c:function:: int hwarc_filter_evt_beacon_WUSB_0100(struct uwb_rc *rc, struct uwb_rceb **header, const size_t buf_size, size_t *new_size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param header:
        the incoming event
    :type header: struct uwb_rceb \*\*

    :param buf_size:
        size of buffer containing incoming event
    :type buf_size: const size_t

    :param new_size:
        size of event after filtering completed
    :type new_size: size_t \*

.. _`hwarc_filter_evt_beacon_wusb_0100.description`:

Description
-----------

The WHCI 0.95 spec has a "Beacon Type" field. This value is unknown at
the time we receive the beacon from WUSB so we just set it to
UWB_RC_BEACON_TYPE_NEIGHBOR as a default.
The solution below allocates memory upon receipt of every beacon from a
WUSB device. This will deteriorate performance. What is the right way to
do this?

.. _`hwarc_filter_evt_drp_avail_wusb_0100`:

hwarc_filter_evt_drp_avail_WUSB_0100
====================================

.. c:function:: int hwarc_filter_evt_drp_avail_WUSB_0100(struct uwb_rc *rc, struct uwb_rceb **header, const size_t buf_size, size_t *new_size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param header:
        the incoming event
    :type header: struct uwb_rceb \*\*

    :param buf_size:
        size of buffer containing incoming event
    :type buf_size: const size_t

    :param new_size:
        size of event after filtering completed
    :type new_size: size_t \*

.. _`hwarc_filter_evt_drp_wusb_0100`:

hwarc_filter_evt_drp_WUSB_0100
==============================

.. c:function:: int hwarc_filter_evt_drp_WUSB_0100(struct uwb_rc *rc, struct uwb_rceb **header, const size_t buf_size, size_t *new_size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param header:
        the incoming event
    :type header: struct uwb_rceb \*\*

    :param buf_size:
        size of buffer containing incoming event
    :type buf_size: const size_t

    :param new_size:
        size of event after filtering completed
    :type new_size: size_t \*

.. _`hwarc_filter_evt_drp_wusb_0100.description`:

Description
-----------

It is hard to manage DRP reservations without having a Reason code.
Unfortunately there is none in the WUSB spec. We just set the default to
DRP IE RECEIVED.
We do not currently use the bBeaconSlotNumber value, so we set this to
zero for now.

.. _`hwarc_filter_cmd_scan_wusb_0100`:

hwarc_filter_cmd_scan_WUSB_0100
===============================

.. c:function:: int hwarc_filter_cmd_scan_WUSB_0100(struct uwb_rc *rc, struct uwb_rccb **header, size_t *size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param header:
        command sent to device (compliant to WHCI 0.95)
    :type header: struct uwb_rccb \*\*

    :param size:
        size of command sent to device
    :type size: size_t \*

.. _`hwarc_filter_cmd_scan_wusb_0100.description`:

Description
-----------

We only reduce the size by two bytes because the WUSB 1.0 scan command
does not have the last field (wStarttime). Also, make sure we don't send
the device an unexpected scan type.

.. _`hwarc_filter_cmd_set_drp_ie_wusb_0100`:

hwarc_filter_cmd_set_drp_ie_WUSB_0100
=====================================

.. c:function:: int hwarc_filter_cmd_set_drp_ie_WUSB_0100(struct uwb_rc *rc, struct uwb_rccb **header, size_t *size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param header:
        command sent to device (compliant to WHCI 0.95)
    :type header: struct uwb_rccb \*\*

    :param size:
        size of command sent to device
    :type size: size_t \*

.. _`hwarc_filter_cmd_set_drp_ie_wusb_0100.description`:

Description
-----------

WUSB has an extra bExplicit field - we assume always explicit
negotiation so this field is set. The command expected by the device is
thus larger than the one prepared by the driver so we need to
reallocate memory to accommodate this.
We trust the driver to send us the correct data so no checking is done
on incoming data - evn though it is variable length.

.. _`hwarc_filter_cmd_wusb_0100`:

hwarc_filter_cmd_WUSB_0100
==========================

.. c:function:: int hwarc_filter_cmd_WUSB_0100(struct uwb_rc *rc, struct uwb_rccb **header, size_t *size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param header:
        WHCI 0.95 compliant command from driver
    :type header: struct uwb_rccb \*\*

    :param size:
        length of command
    :type size: size_t \*

.. _`hwarc_filter_cmd_wusb_0100.description`:

Description
-----------

The routine managing commands to the device (uwb_rc_cmd()) will call the
filtering function pointer (if it exists) before it passes any data to
the device. At this time the command has been formatted according to
WHCI 0.95 and is ready to be sent to the device.

The filter function will be provided with the current command and its
length. The function will manipulate the command if necessary and
potentially reallocate memory for a command that needed more memory that
the given command. If new memory was created the function will return 1
to indicate to the calling function that the memory need to be freed
when not needed any more. The size will contain the new length of the
command.
If memory has not been allocated we rely on the original mechanisms to
free the memory of the command - even when we reduce the value of size.

.. _`hwarc_filter_cmd`:

hwarc_filter_cmd
================

.. c:function:: int hwarc_filter_cmd(struct uwb_rc *rc, struct uwb_rccb **header, size_t *size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param header:
        WHCI 0.95 compliant command from driver
    :type header: struct uwb_rccb \*\*

    :param size:
        length of command
    :type size: size_t \*

.. _`hwarc_filter_cmd.description`:

Description
-----------

Filter commands based on which protocol the device supports. The WUSB
errata should be the same as WHCI 0.95 so we do not filter that here -
only WUSB 1.0.

.. _`hwarc_get_event_size`:

hwarc_get_event_size
====================

.. c:function:: ssize_t hwarc_get_event_size(struct uwb_rc *rc, const struct uwb_rceb *rceb, size_t core_size, size_t offset, const size_t buf_size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param rceb:
        event for which we compute the size, it contains a variable
        length field.
    :type rceb: const struct uwb_rceb \*

    :param core_size:
        size of the "non variable" part of the event
    :type core_size: size_t

    :param offset:
        place in event where the length of the variable part is stored
    :type offset: size_t

    :param buf_size:
        total length of buffer in which event arrived - we need to make
        sure we read the offset in memory that is still part of the event
    :type buf_size: const size_t

.. _`hwarc_filter_event_wusb_0100`:

hwarc_filter_event_WUSB_0100
============================

.. c:function:: int hwarc_filter_event_WUSB_0100(struct uwb_rc *rc, struct uwb_rceb **header, const size_t buf_size, size_t *_real_size, size_t *_new_size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param header:
        incoming event
    :type header: struct uwb_rceb \*\*

    :param buf_size:
        size of buffer in which event arrived
    :type buf_size: const size_t

    :param _real_size:
        *undescribed*
    :type _real_size: size_t \*

    :param _new_size:
        *undescribed*
    :type _new_size: size_t \*

.. _`hwarc_filter_event_wusb_0100.description`:

Description
-----------

We don't know how the buffer is constructed - there may be more than one
event in it so buffer length does not determine event length. We first
determine the expected size of the incoming event. This value is passed
back only if the actual filtering succeeded (so we know the computed
expected size is correct). This value will be zero if
the event did not need any filtering.

WHCI interprets the BP Slot Change event's data differently than
WUSB. The event sizes are exactly the same. The data field
indicates the new beacon slot in which a RC is transmitting its
beacon. The maximum value of this is 96 (wMacBPLength ECMA-368
17.16 (Table 117)). We thus know that the WUSB value will not set
the bit bNoSlot, so we don't really do anything (placeholder).

.. _`hwarc_filter_event`:

hwarc_filter_event
==================

.. c:function:: int hwarc_filter_event(struct uwb_rc *rc, struct uwb_rceb **header, const size_t buf_size, size_t *_real_size, size_t *_new_size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param header:
        incoming event
    :type header: struct uwb_rceb \*\*

    :param buf_size:
        size of buffer in which event arrived
    :type buf_size: const size_t

    :param _real_size:
        *undescribed*
    :type _real_size: size_t \*

    :param _new_size:
        size of event after filtered
    :type _new_size: size_t \*

.. _`hwarc_filter_event.description`:

Description
-----------

Filter events based on which protocol the device supports. The WUSB
errata should be the same as WHCI 0.95 so we do not filter that here -
only WUSB 1.0.

If we don't handle it, we return -ENOANO (why the weird error code?
well, so if I get it, I can pinpoint in the code that raised
it...after all, not too many places use the higher error codes).

.. _`hwarc_cmd`:

hwarc_cmd
=========

.. c:function:: int hwarc_cmd(struct uwb_rc *uwb_rc, const struct uwb_rccb *cmd, size_t cmd_size)

    :param uwb_rc:
        *undescribed*
    :type uwb_rc: struct uwb_rc \*

    :param cmd:
        Buffer containing the RCCB and payload to execute
    :type cmd: const struct uwb_rccb \*

    :param cmd_size:
        Size of the command buffer.
    :type cmd_size: size_t

.. _`hwarc_cmd.note`:

NOTE
----

rc's mutex has to be locked

.. _`hwarc_neep_cb`:

hwarc_neep_cb
=============

.. c:function:: void hwarc_neep_cb(struct urb *urb)

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`hwarc_neep_cb.description`:

Description
-----------

Check's that everything is fine and then passes the read data to
the notification/event handling mechanism (neh).

.. _`hwarc_neep_init`:

hwarc_neep_init
===============

.. c:function:: int hwarc_neep_init(struct uwb_rc *rc)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

.. _`hwarc_neep_init.description`:

Description
-----------

Note this is effectively a parallel thread; it knows that
hwarc->uwb_rc always exists because the existence of a 'hwarc'
means that there is a reverence on the hwarc->uwb_rc (see
\_probe()), and thus \_neep_cb() can execute safely.

.. _`hwarc_get_version`:

hwarc_get_version
=================

.. c:function:: int hwarc_get_version(struct uwb_rc *rc)

    specific descriptor

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

.. _`hwarc_get_version.note`:

NOTE
----

this descriptor comes with the big bundled configuration
descriptor that includes the interfaces' and endpoints', so
we just look for it in the cached copy kept by the USB stack.

.. _`hwarc_get_version.note2`:

NOTE2
-----

We convert LE fields to CPU order.

.. This file was automatic generated / don't edit.

