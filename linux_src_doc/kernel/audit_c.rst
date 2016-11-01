.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/audit.c

.. _`audit_log_lost`:

audit_log_lost
==============

.. c:function:: void audit_log_lost(const char *message)

    conditionally log lost audit message event

    :param const char \*message:
        the message stating reason for lost audit message

.. _`audit_log_lost.description`:

Description
-----------

Emit at least 1 message per second, even if audit_rate_check is
throttling.
Always increment the lost messages counter.

.. _`audit_send_reply`:

audit_send_reply
================

.. c:function:: void audit_send_reply(struct sk_buff *request_skb, int seq, int type, int done, int multi, const void *payload, int size)

    send an audit reply message via netlink

    :param struct sk_buff \*request_skb:
        skb of request we are replying to (used to target the reply)

    :param int seq:
        sequence number

    :param int type:
        audit message type

    :param int done:
        done (last) flag

    :param int multi:
        multi-part message flag

    :param const void \*payload:
        payload data

    :param int size:
        payload size

.. _`audit_send_reply.description`:

Description
-----------

Allocates an skb, builds the netlink message, and sends it to the port id.
No failure notifications.

.. _`audit_serial`:

audit_serial
============

.. c:function:: unsigned int audit_serial( void)

    compute a serial number for the audit record

    :param  void:
        no arguments

.. _`audit_serial.description`:

Description
-----------

Compute a serial number for the audit record.  Audit records are
written to user-space as soon as they are generated, so a complete
audit record may be written in several pieces.  The timestamp of the
record and this serial number are used by the user-space tools to
determine which pieces belong to the same audit record.  The
(timestamp,serial) tuple is unique for each syscall and is live from
syscall entry to syscall exit.

.. _`audit_serial.note`:

NOTE
----

Another possibility is to store the formatted records off the
audit context (for those records that have a context), and emit them
all at syscall exit.  However, this could delay the reporting of
significant errors until syscall exit (or never, if the system
halts).

.. _`audit_log_start`:

audit_log_start
===============

.. c:function:: struct audit_buffer *audit_log_start(struct audit_context *ctx, gfp_t gfp_mask, int type)

    obtain an audit buffer

    :param struct audit_context \*ctx:
        audit_context (may be NULL)

    :param gfp_t gfp_mask:
        type of allocation

    :param int type:
        audit message type

.. _`audit_log_start.description`:

Description
-----------

Returns audit_buffer pointer on success or NULL on error.

Obtain an audit buffer.  This routine does locking to obtain the
audit buffer, but then no locking is required for calls to
audit_log\_\*format.  If the task (ctx) is a task that is currently in a
syscall, then the syscall is marked as auditable and an audit record
will be written at syscall exit.  If there is no associated task, then
task context (ctx) should be NULL.

.. _`audit_expand`:

audit_expand
============

.. c:function:: int audit_expand(struct audit_buffer *ab, int extra)

    expand skb in the audit buffer

    :param struct audit_buffer \*ab:
        audit_buffer

    :param int extra:
        space to add at tail of the skb

.. _`audit_expand.description`:

Description
-----------

Returns 0 (no space) on failed expansion, or available space if
successful.

.. _`audit_log_format`:

audit_log_format
================

.. c:function:: void audit_log_format(struct audit_buffer *ab, const char *fmt,  ...)

    format a message into the audit buffer.

    :param struct audit_buffer \*ab:
        audit_buffer

    :param const char \*fmt:
        format string

    :param ... :
        optional parameters matching \ ``fmt``\  string

.. _`audit_log_format.description`:

Description
-----------

All the work is done in audit_log_vformat.

.. _`audit_log_n_hex`:

audit_log_n_hex
===============

.. c:function:: void audit_log_n_hex(struct audit_buffer *ab, const unsigned char *buf, size_t len)

    convert a buffer to hex and append it to the audit skb

    :param struct audit_buffer \*ab:
        the audit_buffer

    :param const unsigned char \*buf:
        buffer to convert to hex

    :param size_t len:
        length of \ ``buf``\  to be converted

.. _`audit_log_n_hex.description`:

Description
-----------

No return value; failure to expand is silently ignored.

This function will take the passed buf and convert it into a string of
ascii hex digits. The new string is placed onto the skb.

.. _`audit_string_contains_control`:

audit_string_contains_control
=============================

.. c:function:: bool audit_string_contains_control(const char *string, size_t len)

    does a string need to be logged in hex

    :param const char \*string:
        string to be checked

    :param size_t len:
        max length of the string to check

.. _`audit_log_n_untrustedstring`:

audit_log_n_untrustedstring
===========================

.. c:function:: void audit_log_n_untrustedstring(struct audit_buffer *ab, const char *string, size_t len)

    log a string that may contain random characters

    :param struct audit_buffer \*ab:
        audit_buffer

    :param const char \*string:
        string to be logged

    :param size_t len:
        length of string (not including trailing null)

.. _`audit_log_n_untrustedstring.description`:

Description
-----------

This code will escape a string that is passed to it if the string
contains a control character, unprintable character, double quote mark,
or a space. Unescaped strings will start and end with a double quote mark.
Strings that are escaped are printed in hex (2 digits per char).

The caller specifies the number of characters in the string to log, which may
or may not be the entire string.

.. _`audit_log_untrustedstring`:

audit_log_untrustedstring
=========================

.. c:function:: void audit_log_untrustedstring(struct audit_buffer *ab, const char *string)

    log a string that may contain random characters

    :param struct audit_buffer \*ab:
        audit_buffer

    :param const char \*string:
        string to be logged

.. _`audit_log_untrustedstring.description`:

Description
-----------

Same as \ :c:func:`audit_log_n_untrustedstring`\ , except that strlen is used to
determine string length.

.. _`audit_log_name`:

audit_log_name
==============

.. c:function:: void audit_log_name(struct audit_context *context, struct audit_names *n, struct path *path, int record_num, int *call_panic)

    produce AUDIT_PATH record from struct audit_names

    :param struct audit_context \*context:
        audit_context for the task

    :param struct audit_names \*n:
        audit_names structure with reportable details

    :param struct path \*path:
        optional path to report instead of audit_names->name

    :param int record_num:
        record number to report when handling a list of names

    :param int \*call_panic:
        optional pointer to int that will be updated if secid fails

.. _`audit_log_link_denied`:

audit_log_link_denied
=====================

.. c:function:: void audit_log_link_denied(const char *operation, struct path *link)

    report a link restriction denial

    :param const char \*operation:
        specific link operation

    :param struct path \*link:
        the path that triggered the restriction

.. _`audit_log_end`:

audit_log_end
=============

.. c:function:: void audit_log_end(struct audit_buffer *ab)

    end one audit record

    :param struct audit_buffer \*ab:
        the audit_buffer

.. _`audit_log_end.description`:

Description
-----------

netlink_unicast() cannot be called inside an irq context because it blocks
(last arg, flags, is not set to MSG_DONTWAIT), so the audit buffer is placed
on a queue and a tasklet is scheduled to remove them from the queue outside
the irq context.  May be called in any context.

.. _`audit_log`:

audit_log
=========

.. c:function:: void audit_log(struct audit_context *ctx, gfp_t gfp_mask, int type, const char *fmt,  ...)

    Log an audit record

    :param struct audit_context \*ctx:
        audit context

    :param gfp_t gfp_mask:
        type of allocation

    :param int type:
        audit message type

    :param const char \*fmt:
        format string to use

    :param ... :
        variable parameters matching the format string

.. _`audit_log.description`:

Description
-----------

This is a convenience function that calls audit_log_start,
audit_log_vformat, and audit_log_end.  It may be called
in any context.

.. _`audit_log_secctx`:

audit_log_secctx
================

.. c:function:: void audit_log_secctx(struct audit_buffer *ab, u32 secid)

    Converts and logs SELinux context

    :param struct audit_buffer \*ab:
        audit_buffer

    :param u32 secid:
        security number

.. _`audit_log_secctx.description`:

Description
-----------

This is a helper function that calls security_secid_to_secctx to convert
secid to secctx and then adds the (converted) SELinux context to the audit
log by calling audit_log_format, thus also preventing leak of internal secid
to userspace. If secid cannot be converted audit_panic is called.

.. This file was automatic generated / don't edit.

