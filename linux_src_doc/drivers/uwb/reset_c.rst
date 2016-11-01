.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/reset.c

.. _`__uwb_rc_cmd`:

__uwb_rc_cmd
============

.. c:function:: ssize_t __uwb_rc_cmd(struct uwb_rc *rc, const char *cmd_name, struct uwb_rccb *cmd, size_t cmd_size, struct uwb_rceb *reply, size_t reply_size, u8 expected_type, u16 expected_event, struct uwb_rceb **preply)

    :param struct uwb_rc \*rc:
        UWB Radio Control descriptor

    :param const char \*cmd_name:
        Name of the command being issued (for error messages)

    :param struct uwb_rccb \*cmd:
        Pointer to rccb structure containing the command;
        normally you embed this structure as the first member of
        the full command structure.

    :param size_t cmd_size:
        Size of the whole command buffer pointed to by \ ``cmd``\ .

    :param struct uwb_rceb \*reply:
        Pointer to where to store the reply

    :param size_t reply_size:
        @reply's size

    :param u8 expected_type:
        Expected type in the return event

    :param u16 expected_event:
        Expected event code in the return event

    :param struct uwb_rceb \*\*preply:
        Here a pointer to where the event data is received will
        be stored. Once done with the data, free with \ :c:func:`kfree`\ .

.. _`__uwb_rc_cmd.description`:

Description
-----------

This function is generic; it works for commands that return a fixed
and known size or for commands that return a variable amount of data.

If a buffer is provided, that is used, although it could be chopped
to the maximum size of the buffer. If the buffer is NULL, then one
be allocated in \*preply with the whole contents of the reply.

\ ``rc``\  needs to be referenced

.. _`uwb_rc_cmd`:

uwb_rc_cmd
==========

.. c:function:: ssize_t uwb_rc_cmd(struct uwb_rc *rc, const char *cmd_name, struct uwb_rccb *cmd, size_t cmd_size, struct uwb_rceb *reply, size_t reply_size)

    :param struct uwb_rc \*rc:
        UWB Radio Control descriptor

    :param const char \*cmd_name:
        Name of the command being issued (for error messages)

    :param struct uwb_rccb \*cmd:
        Pointer to rccb structure containing the command;
        normally you embed this structure as the first member of
        the full command structure.

    :param size_t cmd_size:
        Size of the whole command buffer pointed to by \ ``cmd``\ .

    :param struct uwb_rceb \*reply:
        Pointer to the beginning of the confirmation event
        buffer. Normally bigger than an 'struct hwarc_rceb'.
        You need to fill out reply->bEventType and reply->wEvent (in
        cpu order) as the function will use them to verify the
        confirmation event.

    :param size_t reply_size:
        Size of the reply buffer

.. _`uwb_rc_cmd.description`:

Description
-----------

The function checks that the length returned in the reply is at
least as big as \ ``reply_size``\ ; if not, it will be deemed an error and
-EIO returned.

\ ``rc``\  needs to be referenced

.. _`uwb_rc_vcmd`:

uwb_rc_vcmd
===========

.. c:function:: ssize_t uwb_rc_vcmd(struct uwb_rc *rc, const char *cmd_name, struct uwb_rccb *cmd, size_t cmd_size, u8 expected_type, u16 expected_event, struct uwb_rceb **preply)

    Interface that return an unknown amount of data

    :param struct uwb_rc \*rc:
        UWB Radio Control descriptor

    :param const char \*cmd_name:
        Name of the command being issued (for error messages)

    :param struct uwb_rccb \*cmd:
        Pointer to rccb structure containing the command;
        normally you embed this structure as the first member of
        the full command structure.

    :param size_t cmd_size:
        Size of the whole command buffer pointed to by \ ``cmd``\ .

    :param u8 expected_type:
        Expected type in the return event

    :param u16 expected_event:
        Expected event code in the return event

    :param struct uwb_rceb \*\*preply:
        Here a pointer to where the event data is received will
        be stored. Once done with the data, free with \ :c:func:`kfree`\ .

.. _`uwb_rc_vcmd.description`:

Description
-----------

The function checks that the length returned in the reply is at
least as big as a 'struct uwb_rceb \*'; if not, it will be deemed an
error and -EIO returned.

\ ``rc``\  needs to be referenced

.. _`uwb_rc_reset`:

uwb_rc_reset
============

.. c:function:: int uwb_rc_reset(struct uwb_rc *rc)

    :param struct uwb_rc \*rc:
        Host Controller descriptor

.. _`uwb_rc_reset.description`:

Description
-----------

We put the command on kmalloc'ed memory as some arches cannot do
USB from the stack. The reply event is copied from an stage buffer,
so it can be in the stack. See WUSB1.0[8.6.2.4] for more details.

.. _`uwb_rc_reset_all`:

uwb_rc_reset_all
================

.. c:function:: void uwb_rc_reset_all(struct uwb_rc *rc)

    request a reset of the radio controller and PALs

    :param struct uwb_rc \*rc:
        the radio controller of the hardware device to be reset.

.. _`uwb_rc_reset_all.description`:

Description
-----------

The full hardware reset of the radio controller and all the PALs
will be scheduled.

.. This file was automatic generated / don't edit.

