.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/hvc/hvc_iucv.c

.. _`hvc_iucv_get_private`:

hvc_iucv_get_private
====================

.. c:function:: struct hvc_iucv_private *hvc_iucv_get_private(uint32_t num)

    Return a struct hvc_iucv_private instance.

    :param uint32_t num:
        The HVC virtual terminal number (vtermno)

.. _`hvc_iucv_get_private.description`:

Description
-----------

This function returns the struct hvc_iucv_private instance that corresponds
to the HVC virtual terminal number specified as parameter \ ``num``\ .

.. _`alloc_tty_buffer`:

alloc_tty_buffer
================

.. c:function:: struct iucv_tty_buffer *alloc_tty_buffer(size_t size, gfp_t flags)

    Return a new struct iucv_tty_buffer element.

    :param size_t size:
        Size of the internal buffer used to store data.

    :param gfp_t flags:
        Memory allocation flags passed to mempool.

.. _`alloc_tty_buffer.description`:

Description
-----------

This function allocates a new struct iucv_tty_buffer element and, optionally,
allocates an internal data buffer with the specified size \ ``size``\ .
The internal data buffer is always allocated with GFP_DMA which is
required for receiving and sending data with IUCV.

.. _`alloc_tty_buffer.note`:

Note
----

The total message size arises from the internal buffer size and the
members of the iucv_tty_msg structure.
The function returns NULL if memory allocation has failed.

.. _`destroy_tty_buffer`:

destroy_tty_buffer
==================

.. c:function:: void destroy_tty_buffer(struct iucv_tty_buffer *bufp)

    destroy struct iucv_tty_buffer element.

    :param struct iucv_tty_buffer \*bufp:
        Pointer to a struct iucv_tty_buffer element, SHALL NOT be NULL.

.. _`destroy_tty_buffer_list`:

destroy_tty_buffer_list
=======================

.. c:function:: void destroy_tty_buffer_list(struct list_head *list)

    call \ :c:func:`destroy_tty_buffer`\  for each list element.

    :param struct list_head \*list:
        List containing struct iucv_tty_buffer elements.

.. _`hvc_iucv_write`:

hvc_iucv_write
==============

.. c:function:: int hvc_iucv_write(struct hvc_iucv_private *priv, char *buf, int count, int *has_more_data)

    Receive IUCV message & write data to HVC buffer.

    :param struct hvc_iucv_private \*priv:
        Pointer to struct hvc_iucv_private

    :param char \*buf:
        HVC buffer for writing received terminal data.

    :param int count:
        HVC buffer size.

    :param int \*has_more_data:
        Pointer to an int variable.

.. _`hvc_iucv_write.description`:

Description
-----------

The function picks up pending messages from the input queue and receives
the message data that is then written to the specified buffer \ ``buf``\ .
If the buffer size \ ``count``\  is less than the data message size, the
message is kept on the input queue and \ ``has_more_data``\  is set to 1.
If all message data has been written, the message is removed from
the input queue.

The function returns the number of bytes written to the terminal, zero if
there are no pending data messages available or if there is no established
IUCV path.
If the IUCV path has been severed, then -EPIPE is returned to cause a
hang up (that is issued by the HVC layer).

.. _`hvc_iucv_get_chars`:

hvc_iucv_get_chars
==================

.. c:function:: int hvc_iucv_get_chars(uint32_t vtermno, char *buf, int count)

    HVC get_chars operation.

    :param uint32_t vtermno:
        HVC virtual terminal number.

    :param char \*buf:
        Pointer to a buffer to store data

    :param int count:
        Size of buffer available for writing

.. _`hvc_iucv_get_chars.description`:

Description
-----------

The HVC thread calls this method to read characters from the back-end.
If an IUCV communication path has been established, pending IUCV messages
are received and data is copied into buffer \ ``buf``\  up to \ ``count``\  bytes.

.. _`hvc_iucv_get_chars.locking`:

Locking
-------

The routine gets called under an \ :c:func:`irqsave`\  spinlock; and
the routine locks the struct hvc_iucv_private->lock to call
helper functions.

.. _`hvc_iucv_queue`:

hvc_iucv_queue
==============

.. c:function:: int hvc_iucv_queue(struct hvc_iucv_private *priv, const char *buf, int count)

    Buffer terminal data for sending.

    :param struct hvc_iucv_private \*priv:
        Pointer to struct hvc_iucv_private instance.

    :param const char \*buf:
        Buffer containing data to send.

    :param int count:
        Size of buffer and amount of data to send.

.. _`hvc_iucv_queue.description`:

Description
-----------

The function queues data for sending. To actually send the buffered data,
a work queue function is scheduled (with QUEUE_SNDBUF_DELAY).
The function returns the number of data bytes that has been buffered.

If the device is not connected, data is ignored and the function returns
\ ``count``\ .
If the buffer is full, the function returns 0.
If an existing IUCV communicaton path has been severed, -EPIPE is returned
(that can be passed to HVC layer to cause a tty hangup).

.. _`hvc_iucv_send`:

hvc_iucv_send
=============

.. c:function:: int hvc_iucv_send(struct hvc_iucv_private *priv)

    Send an IUCV message containing terminal data.

    :param struct hvc_iucv_private \*priv:
        Pointer to struct hvc_iucv_private instance.

.. _`hvc_iucv_send.description`:

Description
-----------

If an IUCV communication path has been established, the buffered output data
is sent via an IUCV message and the number of bytes sent is returned.
Returns 0 if there is no established IUCV communication path or
-EPIPE if an existing IUCV communicaton path has been severed.

.. _`hvc_iucv_sndbuf_work`:

hvc_iucv_sndbuf_work
====================

.. c:function:: void hvc_iucv_sndbuf_work(struct work_struct *work)

    Send buffered data over IUCV

    :param struct work_struct \*work:
        Work structure.

.. _`hvc_iucv_sndbuf_work.description`:

Description
-----------

This work queue function sends buffered output data over IUCV and,
if not all buffered data could be sent, reschedules itself.

.. _`hvc_iucv_put_chars`:

hvc_iucv_put_chars
==================

.. c:function:: int hvc_iucv_put_chars(uint32_t vtermno, const char *buf, int count)

    HVC put_chars operation.

    :param uint32_t vtermno:
        HVC virtual terminal number.

    :param const char \*buf:
        Pointer to an buffer to read data from

    :param int count:
        Size of buffer available for reading

.. _`hvc_iucv_put_chars.description`:

Description
-----------

The HVC thread calls this method to write characters to the back-end.
The function calls \ :c:func:`hvc_iucv_queue`\  to queue terminal data for sending.

.. _`hvc_iucv_put_chars.locking`:

Locking
-------

The method gets called under an \ :c:func:`irqsave`\  spinlock; and
locks struct hvc_iucv_private->lock.

.. _`hvc_iucv_notifier_add`:

hvc_iucv_notifier_add
=====================

.. c:function:: int hvc_iucv_notifier_add(struct hvc_struct *hp, int id)

    HVC notifier for opening a TTY for the first time.

    :param struct hvc_struct \*hp:
        Pointer to the HVC device (struct hvc_struct)

    :param int id:
        Additional data (originally passed to hvc_alloc): the index of an struct
        hvc_iucv_private instance.

.. _`hvc_iucv_notifier_add.description`:

Description
-----------

The function sets the tty state to TTY_OPENED for the struct hvc_iucv_private
instance that is derived from \ ``id``\ . Always returns 0.

.. _`hvc_iucv_notifier_add.locking`:

Locking
-------

struct hvc_iucv_private->lock, spin_lock_bh

.. _`hvc_iucv_cleanup`:

hvc_iucv_cleanup
================

.. c:function:: void hvc_iucv_cleanup(struct hvc_iucv_private *priv)

    Clean up and reset a z/VM IUCV HVC instance.

    :param struct hvc_iucv_private \*priv:
        Pointer to the struct hvc_iucv_private instance.

.. _`tty_outqueue_empty`:

tty_outqueue_empty
==================

.. c:function:: int tty_outqueue_empty(struct hvc_iucv_private *priv)

    Test if the tty outq is empty

    :param struct hvc_iucv_private \*priv:
        Pointer to struct hvc_iucv_private instance.

.. _`flush_sndbuf_sync`:

flush_sndbuf_sync
=================

.. c:function:: void flush_sndbuf_sync(struct hvc_iucv_private *priv)

    Flush send buffer and wait for completion

    :param struct hvc_iucv_private \*priv:
        Pointer to struct hvc_iucv_private instance.

.. _`flush_sndbuf_sync.description`:

Description
-----------

The routine cancels a pending sndbuf work, calls \ :c:func:`hvc_iucv_send`\ 
to flush any buffered terminal output data and waits for completion.

.. _`hvc_iucv_hangup`:

hvc_iucv_hangup
===============

.. c:function:: void hvc_iucv_hangup(struct hvc_iucv_private *priv)

    Sever IUCV path and schedule hvc tty hang up

    :param struct hvc_iucv_private \*priv:
        Pointer to hvc_iucv_private structure

.. _`hvc_iucv_hangup.description`:

Description
-----------

This routine severs an existing IUCV communication path and hangs
up the underlying HVC terminal device.
The hang-up occurs only if an IUCV communication path is established;
otherwise there is no need to hang up the terminal device.

The IUCV HVC hang-up is separated into two steps:
1. After the IUCV path has been severed, the iucv_state is set to
IUCV_SEVERED.
2. Later, when the HVC thread calls \ :c:func:`hvc_iucv_get_chars`\ , the
IUCV_SEVERED state causes the tty hang-up in the HVC layer.

If the tty has not yet been opened, clean up the hvc_iucv_private
structure to allow re-connects.
If the tty has been opened, let \ :c:func:`get_chars`\  return -EPIPE to signal
the HVC layer to hang up the tty and, if so, wake up the HVC thread
to call \ :c:func:`get_chars`\ ...

.. _`hvc_iucv_hangup.special-notes-on-hanging-up-a-hvc-terminal-instantiated-as-console`:

Special notes on hanging up a HVC terminal instantiated as console
------------------------------------------------------------------

Hang-up:     1. \ :c:func:`do_tty_hangup`\  replaces file ops (= hung_up_tty_fops)
2. \ :c:func:`do_tty_hangup`\  calls tty->ops->close() for console_filp
=> no hangup notifier is called by HVC (default)
2. \ :c:func:`hvc_close`\  returns because of tty_hung_up_p(filp)
=> no delete notifier is called!
Finally, the back-end is not being notified, thus, the tty session is
kept active (TTY_OPEN) to be ready for re-connects.

.. _`hvc_iucv_hangup.locking`:

Locking
-------

spin_lock(&priv->lock) w/o disabling bh

.. _`hvc_iucv_notifier_hangup`:

hvc_iucv_notifier_hangup
========================

.. c:function:: void hvc_iucv_notifier_hangup(struct hvc_struct *hp, int id)

    HVC notifier for TTY hangups.

    :param struct hvc_struct \*hp:
        Pointer to the HVC device (struct hvc_struct)

    :param int id:
        Additional data (originally passed to hvc_alloc):
        the index of an struct hvc_iucv_private instance.

.. _`hvc_iucv_notifier_hangup.description`:

Description
-----------

This routine notifies the HVC back-end that a tty hangup (carrier loss,
virtual or otherwise) has occurred.
The z/VM IUCV HVC device driver ignores virtual hangups (vhangup())
to keep an existing IUCV communication path established.
(Background: \ :c:func:`vhangup`\  is called from user space (by getty or login) to
disable writing to the tty by other applications).
If the tty has been opened and an established IUCV path has been severed
(we caused the tty hangup), the function calls \ :c:func:`hvc_iucv_cleanup`\ .

.. _`hvc_iucv_notifier_hangup.locking`:

Locking
-------

struct hvc_iucv_private->lock

.. _`hvc_iucv_dtr_rts`:

hvc_iucv_dtr_rts
================

.. c:function:: void hvc_iucv_dtr_rts(struct hvc_struct *hp, int raise)

    HVC notifier for handling DTR/RTS

    :param struct hvc_struct \*hp:
        Pointer the HVC device (struct hvc_struct)

    :param int raise:
        Non-zero to raise or zero to lower DTR/RTS lines

.. _`hvc_iucv_dtr_rts.description`:

Description
-----------

This routine notifies the HVC back-end to raise or lower DTR/RTS
lines.  Raising DTR/RTS is ignored.  Lowering DTR/RTS indicates to
drop the IUCV connection (similar to hang up the modem).

.. _`hvc_iucv_notifier_del`:

hvc_iucv_notifier_del
=====================

.. c:function:: void hvc_iucv_notifier_del(struct hvc_struct *hp, int id)

    HVC notifier for closing a TTY for the last time.

    :param struct hvc_struct \*hp:
        Pointer to the HVC device (struct hvc_struct)

    :param int id:
        Additional data (originally passed to hvc_alloc):
        the index of an struct hvc_iucv_private instance.

.. _`hvc_iucv_notifier_del.description`:

Description
-----------

This routine notifies the HVC back-end that the last tty device fd has been
closed.  The function cleans up tty resources.  The clean-up of the IUCV
connection is done in \ :c:func:`hvc_iucv_dtr_rts`\  and depends on the HUPCL termios
control setting.

.. _`hvc_iucv_notifier_del.locking`:

Locking
-------

struct hvc_iucv_private->lock

.. _`hvc_iucv_filter_connreq`:

hvc_iucv_filter_connreq
=======================

.. c:function:: int hvc_iucv_filter_connreq(u8 ipvmid)

    Filter connection request based on z/VM user ID

    :param u8 ipvmid:
        Originating z/VM user ID (right padded with blanks)

.. _`hvc_iucv_filter_connreq.description`:

Description
-----------

Returns 0 if the z/VM user ID that is specified with \ ``ipvmid``\  is permitted to
connect, otherwise non-zero.

.. _`hvc_iucv_path_pending`:

hvc_iucv_path_pending
=====================

.. c:function:: int hvc_iucv_path_pending(struct iucv_path *path, u8 *ipvmid, u8 *ipuser)

    IUCV handler to process a connection request.

    :param struct iucv_path \*path:
        Pending path (struct iucv_path)

    :param u8 \*ipvmid:
        z/VM system identifier of originator

    :param u8 \*ipuser:
        User specified data for this path
        (AF_IUCV: port/service name and originator port)

.. _`hvc_iucv_path_pending.description`:

Description
-----------

The function uses the \ ``ipuser``\  data to determine if the pending path belongs
to a terminal managed by this device driver.
If the path belongs to this driver, ensure that the terminal is not accessed
multiple times (only one connection to a terminal is allowed).
If the terminal is not yet connected, the pending path is accepted and is
associated to the appropriate struct hvc_iucv_private instance.

Returns 0 if \ ``path``\  belongs to a terminal managed by the this device driver;
otherwise returns -ENODEV in order to dispatch this path to other handlers.

.. _`hvc_iucv_path_pending.locking`:

Locking
-------

struct hvc_iucv_private->lock

.. _`hvc_iucv_path_severed`:

hvc_iucv_path_severed
=====================

.. c:function:: void hvc_iucv_path_severed(struct iucv_path *path, u8 *ipuser)

    IUCV handler to process a path sever.

    :param struct iucv_path \*path:
        Pending path (struct iucv_path)

    :param u8 \*ipuser:
        User specified data for this path
        (AF_IUCV: port/service name and originator port)

.. _`hvc_iucv_path_severed.description`:

Description
-----------

This function calls the \ :c:func:`hvc_iucv_hangup`\  function for the
respective IUCV HVC terminal.

.. _`hvc_iucv_path_severed.locking`:

Locking
-------

struct hvc_iucv_private->lock

.. _`hvc_iucv_msg_pending`:

hvc_iucv_msg_pending
====================

.. c:function:: void hvc_iucv_msg_pending(struct iucv_path *path, struct iucv_message *msg)

    IUCV handler to process an incoming IUCV message.

    :param struct iucv_path \*path:
        Pending path (struct iucv_path)

    :param struct iucv_message \*msg:
        Pointer to the IUCV message

.. _`hvc_iucv_msg_pending.description`:

Description
-----------

The function puts an incoming message on the input queue for later
processing (by \ :c:func:`hvc_iucv_get_chars`\  / \ :c:func:`hvc_iucv_write`\ ).
If the tty has not yet been opened, the message is rejected.

.. _`hvc_iucv_msg_pending.locking`:

Locking
-------

struct hvc_iucv_private->lock

.. _`hvc_iucv_msg_complete`:

hvc_iucv_msg_complete
=====================

.. c:function:: void hvc_iucv_msg_complete(struct iucv_path *path, struct iucv_message *msg)

    IUCV handler to process message completion

    :param struct iucv_path \*path:
        Pending path (struct iucv_path)

    :param struct iucv_message \*msg:
        Pointer to the IUCV message

.. _`hvc_iucv_msg_complete.description`:

Description
-----------

The function is called upon completion of message delivery to remove the
message from the outqueue. Additional delivery information can be found
msg->audit: rejected messages (0x040000 (IPADRJCT)), and
purged messages   (0x010000 (IPADPGNR)).

.. _`hvc_iucv_msg_complete.locking`:

Locking
-------

struct hvc_iucv_private->lock

.. _`hvc_iucv_pm_freeze`:

hvc_iucv_pm_freeze
==================

.. c:function:: int hvc_iucv_pm_freeze(struct device *dev)

    Freeze PM callback

    :param struct device \*dev:
        IUVC HVC terminal device

.. _`hvc_iucv_pm_freeze.description`:

Description
-----------

Sever an established IUCV communication path and
trigger a hang-up of the underlying HVC terminal.

.. _`hvc_iucv_pm_restore_thaw`:

hvc_iucv_pm_restore_thaw
========================

.. c:function:: int hvc_iucv_pm_restore_thaw(struct device *dev)

    Thaw and restore PM callback

    :param struct device \*dev:
        IUVC HVC terminal device

.. _`hvc_iucv_pm_restore_thaw.description`:

Description
-----------

Wake up the HVC thread to trigger hang-up and respective
HVC back-end notifier invocations.

.. _`hvc_iucv_alloc`:

hvc_iucv_alloc
==============

.. c:function:: int hvc_iucv_alloc(int id, unsigned int is_console)

    Allocates a new struct hvc_iucv_private instance

    :param int id:
        hvc_iucv_table index

    :param unsigned int is_console:
        Flag if the instance is used as Linux console

.. _`hvc_iucv_alloc.description`:

Description
-----------

This function allocates a new hvc_iucv_private structure and stores
the instance in hvc_iucv_table at index \ ``id``\ .
Returns 0 on success; otherwise non-zero.

.. _`hvc_iucv_destroy`:

hvc_iucv_destroy
================

.. c:function:: void hvc_iucv_destroy(struct hvc_iucv_private *priv)

    Destroy and free hvc_iucv_private instances

    :param struct hvc_iucv_private \*priv:
        *undescribed*

.. _`hvc_iucv_parse_filter`:

hvc_iucv_parse_filter
=====================

.. c:function:: const char *hvc_iucv_parse_filter(const char *filter, char *dest)

    Parse filter for a single z/VM user ID

    :param const char \*filter:
        String containing a comma-separated list of z/VM user IDs

    :param char \*dest:
        Location where to store the parsed z/VM user ID

.. _`hvc_iucv_setup_filter`:

hvc_iucv_setup_filter
=====================

.. c:function:: int hvc_iucv_setup_filter(const char *val)

    Set up z/VM user ID filter

    :param const char \*val:
        *undescribed*

.. _`hvc_iucv_setup_filter.description`:

Description
-----------

The function parses the \ ``filter``\  string and creates an array containing
the list of z/VM user ID filter entries.
Return code 0 means success, -EINVAL if the filter is syntactically
incorrect, -ENOMEM if there was not enough memory to allocate the
filter list array, or -ENOSPC if too many z/VM user IDs have been specified.

.. _`param_set_vmidfilter`:

param_set_vmidfilter
====================

.. c:function:: int param_set_vmidfilter(const char *val, const struct kernel_param *kp)

    Set z/VM user ID filter parameter

    :param const char \*val:
        String consisting of a comma-separated list of z/VM user IDs

    :param const struct kernel_param \*kp:
        Kernel parameter pointing to hvc_iucv_filter array

.. _`param_set_vmidfilter.description`:

Description
-----------

The function sets up the z/VM user ID filter specified as comma-separated
list of user IDs in \ ``val``\ .

.. _`param_set_vmidfilter.note`:

Note
----

If it is called early in the boot process, \ ``val``\  is stored and
parsed later in \ :c:func:`hvc_iucv_init`\ .

.. _`param_get_vmidfilter`:

param_get_vmidfilter
====================

.. c:function:: int param_get_vmidfilter(char *buffer, const struct kernel_param *kp)

    Get z/VM user ID filter

    :param char \*buffer:
        Buffer to store z/VM user ID filter,
        (buffer size assumption PAGE_SIZE)

    :param const struct kernel_param \*kp:
        Kernel parameter pointing to the hvc_iucv_filter array

.. _`param_get_vmidfilter.description`:

Description
-----------

The function stores the filter as a comma-separated list of z/VM user IDs
in \ ``buffer``\ . Typically, sysfs routines call this function for attr show.

.. _`hvc_iucv_init`:

hvc_iucv_init
=============

.. c:function:: int hvc_iucv_init( void)

    z/VM IUCV HVC device driver initialization

    :param  void:
        no arguments

.. _`hvc_iucv_config`:

hvc_iucv_config
===============

.. c:function:: int hvc_iucv_config(char *val)

    Parsing of hvc_iucv=  kernel command line parameter

    :param char \*val:
        Parameter value (numeric)

.. This file was automatic generated / don't edit.

