.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/audit.c

.. _`audit_net`:

struct audit_net
================

.. c:type:: struct audit_net

    audit private network namespace data

.. _`audit_net.definition`:

Definition
----------

.. code-block:: c

    struct audit_net {
        struct sock *sk;
    }

.. _`audit_net.members`:

Members
-------

sk
    communication socket

.. _`auditd_test_task`:

auditd_test_task
================

.. c:function:: int auditd_test_task(struct task_struct *task)

    Check to see if a given task is an audit daemon

    :param struct task_struct \*task:
        the task to check

.. _`auditd_test_task.description`:

Description
-----------

Return 1 if the task is a registered audit daemon, 0 otherwise.

.. _`audit_ctl_lock`:

audit_ctl_lock
==============

.. c:function:: void audit_ctl_lock( void)

    Take the audit control lock

    :param  void:
        no arguments

.. _`audit_ctl_unlock`:

audit_ctl_unlock
================

.. c:function:: void audit_ctl_unlock( void)

    Drop the audit control lock

    :param  void:
        no arguments

.. _`audit_ctl_owner_current`:

audit_ctl_owner_current
=======================

.. c:function:: bool audit_ctl_owner_current( void)

    Test to see if the current task owns the lock

    :param  void:
        no arguments

.. _`audit_ctl_owner_current.description`:

Description
-----------

Return true if the current task owns the audit control lock, false if it
doesn't own the lock.

.. _`auditd_pid_vnr`:

auditd_pid_vnr
==============

.. c:function:: pid_t auditd_pid_vnr( void)

    Return the auditd PID relative to the namespace

    :param  void:
        no arguments

.. _`auditd_pid_vnr.description`:

Description
-----------

Returns the PID in relation to the namespace, 0 on failure.

.. _`audit_get_sk`:

audit_get_sk
============

.. c:function:: struct sock *audit_get_sk(const struct net *net)

    Return the audit socket for the given network namespace

    :param const struct net \*net:
        the destination network namespace

.. _`audit_get_sk.description`:

Description
-----------

Returns the sock pointer if valid, NULL otherwise.  The caller must ensure
that a reference is held for the network namespace while the sock is in use.

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

.. _`auditd_conn_free`:

auditd_conn_free
================

.. c:function:: void auditd_conn_free(struct rcu_head *rcu)

    RCU helper to release an auditd connection struct

    :param struct rcu_head \*rcu:
        RCU head

.. _`auditd_conn_free.description`:

Description
-----------

Drop any references inside the auditd connection tracking struct and free
the memory.

.. _`auditd_set`:

auditd_set
==========

.. c:function:: int auditd_set(struct pid *pid, u32 portid, struct net *net)

    Set/Reset the auditd connection state

    :param struct pid \*pid:
        auditd PID

    :param u32 portid:
        auditd netlink portid

    :param struct net \*net:
        auditd network namespace pointer

.. _`auditd_set.description`:

Description
-----------

This function will obtain and drop network namespace references as
necessary.  Returns zero on success, negative values on failure.

.. _`kauditd_printk_skb`:

kauditd_printk_skb
==================

.. c:function:: void kauditd_printk_skb(struct sk_buff *skb)

    Print the audit record to the ring buffer

    :param struct sk_buff \*skb:
        audit record

.. _`kauditd_printk_skb.description`:

Description
-----------

Whatever the reason, this packet may not make it to the auditd connection
so write it via printk so the information isn't completely lost.

.. _`kauditd_rehold_skb`:

kauditd_rehold_skb
==================

.. c:function:: void kauditd_rehold_skb(struct sk_buff *skb)

    Handle a audit record send failure in the hold queue

    :param struct sk_buff \*skb:
        audit record

.. _`kauditd_rehold_skb.description`:

Description
-----------

This should only be used by the kauditd_thread when it fails to flush the
hold queue.

.. _`kauditd_hold_skb`:

kauditd_hold_skb
================

.. c:function:: void kauditd_hold_skb(struct sk_buff *skb)

    Queue an audit record, waiting for auditd

    :param struct sk_buff \*skb:
        audit record

.. _`kauditd_hold_skb.description`:

Description
-----------

Queue the audit record, waiting for an instance of auditd.  When this
function is called we haven't given up yet on sending the record, but things
are not looking good.  The first thing we want to do is try to write the
record via printk and then see if we want to try and hold on to the record
and queue it, if we have room.  If we want to hold on to the record, but we
don't have room, record a record lost message.

.. _`kauditd_retry_skb`:

kauditd_retry_skb
=================

.. c:function:: void kauditd_retry_skb(struct sk_buff *skb)

    Queue an audit record, attempt to send again to auditd

    :param struct sk_buff \*skb:
        audit record

.. _`kauditd_retry_skb.description`:

Description
-----------

Not as serious as \ :c:func:`kauditd_hold_skb`\  as we still have a connected auditd,
but for some reason we are having problems sending it audit records so
queue the given record and attempt to resend.

.. _`auditd_reset`:

auditd_reset
============

.. c:function:: void auditd_reset(const struct auditd_connection *ac)

    Disconnect the auditd connection

    :param const struct auditd_connection \*ac:
        auditd connection state

.. _`auditd_reset.description`:

Description
-----------

Break the auditd/kauditd connection and move all the queued records into the
hold queue in case auditd reconnects.  It is important to note that the \ ``ac``\ 
pointer should never be dereferenced inside this function as it may be NULL
or invalid, you can only compare the memory address!  If \ ``ac``\  is NULL then
the connection will always be reset.

.. _`auditd_send_unicast_skb`:

auditd_send_unicast_skb
=======================

.. c:function:: int auditd_send_unicast_skb(struct sk_buff *skb)

    Send a record via unicast to auditd

    :param struct sk_buff \*skb:
        audit record

.. _`auditd_send_unicast_skb.description`:

Description
-----------

Send a skb to the audit daemon, returns positive/zero values on success and
negative values on failure; in all cases the skb will be consumed by this
function.  If the send results in -ECONNREFUSED the connection with auditd
will be reset.  This function may sleep so callers should not hold any locks
where this would cause a problem.

.. _`kauditd_send_queue`:

kauditd_send_queue
==================

.. c:function:: int kauditd_send_queue(struct sock *sk, u32 portid, struct sk_buff_head *queue, unsigned int retry_limit, void (*skb_hook)(struct sk_buff *skb), void (*err_hook)(struct sk_buff *skb))

    Helper for kauditd_thread to flush skb queues

    :param struct sock \*sk:
        the sending sock

    :param u32 portid:
        the netlink destination

    :param struct sk_buff_head \*queue:
        the skb queue to process

    :param unsigned int retry_limit:
        limit on number of netlink unicast failures

    :param void (\*skb_hook)(struct sk_buff \*skb):
        per-skb hook for additional processing

    :param void (\*err_hook)(struct sk_buff \*skb):
        hook called if the skb fails the netlink unicast send

.. _`kauditd_send_queue.description`:

Description
-----------

Run through the given queue and attempt to send the audit records to auditd,
returns zero on success, negative values on failure.  It is up to the caller
to ensure that the \ ``sk``\  is valid for the duration of this function.

.. _`kauditd_thread`:

kauditd_thread
==============

.. c:function:: int kauditd_thread(void *dummy)

    Worker thread to send audit records to userspace

    :param void \*dummy:
        unused

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

.. _`audit_receive`:

audit_receive
=============

.. c:function:: void audit_receive(struct sk_buff *skb)

    receive messages from a netlink control socket

    :param struct sk_buff \*skb:
        the message buffer

.. _`audit_receive.description`:

Description
-----------

Parse the provided skb and deal with any messages that may be present,
malformed skbs are discarded.

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
audit_log_*format.  If the task (ctx) is a task that is currently in a
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

    :param ellipsis ellipsis:
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

.. c:function:: void audit_log_name(struct audit_context *context, struct audit_names *n, const struct path *path, int record_num, int *call_panic)

    produce AUDIT_PATH record from struct audit_names

    :param struct audit_context \*context:
        audit_context for the task

    :param struct audit_names \*n:
        audit_names structure with reportable details

    :param const struct path \*path:
        optional path to report instead of audit_names->name

    :param int record_num:
        record number to report when handling a list of names

    :param int \*call_panic:
        optional pointer to int that will be updated if secid fails

.. _`audit_log_link_denied`:

audit_log_link_denied
=====================

.. c:function:: void audit_log_link_denied(const char *operation)

    report a link restriction denial

    :param const char \*operation:
        specific link operation

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

We can not do a netlink send inside an irq context because it blocks (last
arg, flags, is not set to MSG_DONTWAIT), so the audit buffer is placed on a
queue and a tasklet is scheduled to remove them from the queue outside the
irq context.  May be called in any context.

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

    :param ellipsis ellipsis:
        variable parameters matching the format string

.. _`audit_log.description`:

Description
-----------

This is a convenience function that calls audit_log_start,
audit_log_vformat, and audit_log_end.  It may be called
in any context.

.. This file was automatic generated / don't edit.

