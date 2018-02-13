.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/neh.c

.. _`uwb_rc_neh_put`:

uwb_rc_neh_put
==============

.. c:function:: void uwb_rc_neh_put(struct uwb_rc_neh *neh)

    release reference to a neh

    :param struct uwb_rc_neh \*neh:
        the neh

.. _`__uwb_rc_ctx_get`:

\__uwb_rc_ctx_get
=================

.. c:function:: int __uwb_rc_ctx_get(struct uwb_rc *rc, struct uwb_rc_neh *neh)

    :param struct uwb_rc \*rc:
        UWB Radio Controller descriptor; \ ``rc``\ ->neh_lock taken

    :param struct uwb_rc_neh \*neh:
        Notification/Event Handle
        \ ``returns``\  0 if context id was assigned ok; < 0 errno on error (if
        all the context IDs are taken).

.. _`__uwb_rc_ctx_get.description`:

Description
-----------

(assumes \ ``wa``\  is locked).

.. _`__uwb_rc_ctx_get.note`:

NOTE
----

WUSB spec reserves context ids 0x00 for notifications and
0xff is invalid, so they must not be used. Initialization
fills up those two in the bitmap so they are not allocated.

We spread the allocation around to reduce the possibility of two
consecutive opened \ ``neh``\ 's getting the same context ID assigned (to
avoid surprises with late events that timed out long time ago). So
first we search from where \ ``rc``\ ->ctx_roll is, if not found, we
search from zero.

.. _`uwb_rc_neh_add`:

uwb_rc_neh_add
==============

.. c:function:: struct uwb_rc_neh *uwb_rc_neh_add(struct uwb_rc *rc, struct uwb_rccb *cmd, u8 expected_type, u16 expected_event, uwb_rc_cmd_cb_f cb, void *arg)

    add a neh for a radio controller command

    :param struct uwb_rc \*rc:
        the radio controller

    :param struct uwb_rccb \*cmd:
        the radio controller command

    :param u8 expected_type:
        the type of the expected response event

    :param u16 expected_event:
        the expected event ID

    :param uwb_rc_cmd_cb_f cb:
        callback for when the event is received

    :param void \*arg:
        argument for the callback

.. _`uwb_rc_neh_add.description`:

Description
-----------

Creates a neh and adds it to the list of those waiting for an
event.  A context ID will be assigned to the command.

.. _`uwb_rc_neh_rm`:

uwb_rc_neh_rm
=============

.. c:function:: void uwb_rc_neh_rm(struct uwb_rc *rc, struct uwb_rc_neh *neh)

    remove a neh.

    :param struct uwb_rc \*rc:
        the radio controller

    :param struct uwb_rc_neh \*neh:
        the neh to remove

.. _`uwb_rc_neh_rm.description`:

Description
-----------

Remove an active neh immediately instead of waiting for the event
(or a time out).

.. _`uwb_rc_neh_arm`:

uwb_rc_neh_arm
==============

.. c:function:: void uwb_rc_neh_arm(struct uwb_rc *rc, struct uwb_rc_neh *neh)

    arm an event handler timeout timer

    :param struct uwb_rc \*rc:
        UWB Radio Controller

    :param struct uwb_rc_neh \*neh:
        Notification/event handler for \ ``rc``\ 

.. _`uwb_rc_neh_arm.description`:

Description
-----------

The timer is only armed if the neh is active.

.. _`uwb_rc_neh_lookup`:

uwb_rc_neh_lookup
=================

.. c:function:: struct uwb_rc_neh *uwb_rc_neh_lookup(struct uwb_rc *rc, const struct uwb_rceb *rceb)

    :param struct uwb_rc \*rc:
        UWB Radio Controller

    :param const struct uwb_rceb \*rceb:
        Pointer to the RCEB buffer

.. _`uwb_rc_neh_lookup.description`:

Description
-----------

If the listener has no buffer (NULL buffer), one is allocated for
the right size (the amount of data received). \ ``neh``\ ->ptr will point
to the event payload, which always starts with a 'struct
uwb_rceb'. \ :c:func:`kfree`\  it when done.

.. _`uwb_rc_neh_grok`:

uwb_rc_neh_grok
===============

.. c:function:: void uwb_rc_neh_grok(struct uwb_rc *rc, void *buf, size_t buf_size)

    them up and dispatch them.

    :param struct uwb_rc \*rc:
        UWB Radio Controller

    :param void \*buf:
        Buffer with the stream of notifications/events

    :param size_t buf_size:
        Amount of data in the buffer

.. _`uwb_rc_neh_grok.description`:

Description
-----------

Note each notification/event starts always with a 'struct
uwb_rceb', so the minimum size if 4 bytes.

The device may pass us events formatted differently than expected.
These are first filtered, potentially creating a new event in a new
memory location. If a new event is created by the filter it is also
freed here.

For each notif/event, tries to guess the size looking at the EST
tables, then looks for a neh that is waiting for that event and if
found, copies the payload to the neh's buffer and calls it back. If
not, the data is ignored.

Note that if we can't find a size description in the EST tables, we
still might find a size in the 'neh' handle in \ :c:func:`uwb_rc_neh_lookup`\ .

.. _`uwb_rc_neh_grok.assumptions`:

Assumptions
-----------


\ ``rc``\ ->neh_lock is NOT taken

.. _`uwb_rc_neh_grok.size`:

size
----

contains the size of the buffer that is processed for the
incoming event. this buffer may contain events that are not
formatted as WHCI.

.. _`uwb_rc_neh_grok.real_size`:

real_size
---------

the actual space taken by this event in the buffer.
We need to keep track of the real size of an event to be able to
advance the buffer correctly.

.. _`uwb_rc_neh_grok.event_size`:

event_size
----------

the size of the event as expected by the core layer
[OR] the size of the event after filtering. if the filtering
created a new event in a new memory location then this is
effectively the size of a new event buffer

.. _`uwb_rc_neh_error`:

uwb_rc_neh_error
================

.. c:function:: void uwb_rc_neh_error(struct uwb_rc *rc, int error)

    detected an error.

    :param struct uwb_rc \*rc:
        UWB Radio Controller

    :param int error:
        Errno error code

.. This file was automatic generated / don't edit.

