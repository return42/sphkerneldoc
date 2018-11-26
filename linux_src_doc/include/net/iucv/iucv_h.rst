.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/iucv/iucv.h

.. _`iucv_register`:

iucv_register
=============

.. c:function:: int iucv_register(struct iucv_handler *handler, int smp)

    :param handler:
        address of iucv handler structure
    :type handler: struct iucv_handler \*

    :param smp:
        != 0 indicates that the handler can deal with out of order messages
    :type smp: int

.. _`iucv_register.description`:

Description
-----------

Registers a driver with IUCV.

Returns 0 on success, -ENOMEM if the memory allocation for the pathid
table failed, or -EIO if IUCV_DECLARE_BUFFER failed on all cpus.

.. _`iucv_unregister`:

iucv_unregister
===============

.. c:function:: void iucv_unregister(struct iucv_handler *handle, int smp)

    :param handle:
        *undescribed*
    :type handle: struct iucv_handler \*

    :param smp:
        != 0 indicates that the handler can deal with out of order messages
    :type smp: int

.. _`iucv_unregister.description`:

Description
-----------

Unregister driver from IUCV.

.. _`iucv_path_alloc`:

iucv_path_alloc
===============

.. c:function:: struct iucv_path *iucv_path_alloc(u16 msglim, u8 flags, gfp_t gfp)

    :param msglim:
        initial message limit
    :type msglim: u16

    :param flags:
        initial flags
    :type flags: u8

    :param gfp:
        kmalloc allocation flag
    :type gfp: gfp_t

.. _`iucv_path_alloc.description`:

Description
-----------

Allocate a new path structure for use with iucv_connect.

Returns NULL if the memory allocation failed or a pointer to the
path structure.

.. _`iucv_path_free`:

iucv_path_free
==============

.. c:function:: void iucv_path_free(struct iucv_path *path)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

.. _`iucv_path_free.description`:

Description
-----------

Frees a path structure.

.. _`iucv_path_accept`:

iucv_path_accept
================

.. c:function:: int iucv_path_accept(struct iucv_path *path, struct iucv_handler *handler, u8 *userdata, void *private)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param handler:
        address of iucv handler structure
    :type handler: struct iucv_handler \*

    :param userdata:
        16 bytes of data reflected to the communication partner
    :type userdata: u8 \*

    :param private:
        private data passed to interrupt handlers for this path
    :type private: void \*

.. _`iucv_path_accept.description`:

Description
-----------

This function is issued after the user received a connection pending
external interrupt and now wishes to complete the IUCV communication path.

Returns the result of the CP IUCV call.

.. _`iucv_path_connect`:

iucv_path_connect
=================

.. c:function:: int iucv_path_connect(struct iucv_path *path, struct iucv_handler *handler, u8 *userid, u8 *system, u8 *userdata, void *private)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param handler:
        address of iucv handler structure
    :type handler: struct iucv_handler \*

    :param userid:
        8-byte user identification
    :type userid: u8 \*

    :param system:
        8-byte target system identification
    :type system: u8 \*

    :param userdata:
        16 bytes of data reflected to the communication partner
    :type userdata: u8 \*

    :param private:
        private data passed to interrupt handlers for this path
    :type private: void \*

.. _`iucv_path_connect.description`:

Description
-----------

This function establishes an IUCV path. Although the connect may complete
successfully, you are not able to use the path until you receive an IUCV
Connection Complete external interrupt.

Returns the result of the CP IUCV call.

.. _`iucv_path_quiesce`:

iucv_path_quiesce
=================

.. c:function:: int iucv_path_quiesce(struct iucv_path *path, u8 *userdata)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param userdata:
        16 bytes of data reflected to the communication partner
    :type userdata: u8 \*

.. _`iucv_path_quiesce.description`:

Description
-----------

This function temporarily suspends incoming messages on an IUCV path.
You can later reactivate the path by invoking the iucv_resume function.

Returns the result from the CP IUCV call.

.. _`iucv_path_resume`:

iucv_path_resume
================

.. c:function:: int iucv_path_resume(struct iucv_path *path, u8 *userdata)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param userdata:
        16 bytes of data reflected to the communication partner
    :type userdata: u8 \*

.. _`iucv_path_resume.description`:

Description
-----------

This function resumes incoming messages on an IUCV path that has
been stopped with iucv_path_quiesce.

Returns the result from the CP IUCV call.

.. _`iucv_path_sever`:

iucv_path_sever
===============

.. c:function:: int iucv_path_sever(struct iucv_path *path, u8 *userdata)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param userdata:
        16 bytes of data reflected to the communication partner
    :type userdata: u8 \*

.. _`iucv_path_sever.description`:

Description
-----------

This function terminates an IUCV path.

Returns the result from the CP IUCV call.

.. _`iucv_message_purge`:

iucv_message_purge
==================

.. c:function:: int iucv_message_purge(struct iucv_path *path, struct iucv_message *msg, u32 srccls)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param msg:
        address of iucv msg structure
    :type msg: struct iucv_message \*

    :param srccls:
        source class of message
    :type srccls: u32

.. _`iucv_message_purge.description`:

Description
-----------

Cancels a message you have sent.

Returns the result from the CP IUCV call.

.. _`iucv_message_receive`:

iucv_message_receive
====================

.. c:function:: int iucv_message_receive(struct iucv_path *path, struct iucv_message *msg, u8 flags, void *buffer, size_t size, size_t *residual)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param msg:
        address of iucv msg structure
    :type msg: struct iucv_message \*

    :param flags:
        flags that affect how the message is received (IUCV_IPBUFLST)
    :type flags: u8

    :param buffer:
        address of data buffer or address of struct iucv_array
    :type buffer: void \*

    :param size:
        length of data buffer
    :type size: size_t

    :param residual:
        *undescribed*
    :type residual: size_t \*

.. _`iucv_message_receive.description`:

Description
-----------

This function receives messages that are being sent to you over
established paths. This function will deal with RMDATA messages
embedded in struct iucv_message as well.

.. _`iucv_message_receive.locking`:

Locking
-------

local_bh_enable/local_bh_disable

Returns the result from the CP IUCV call.

.. _`__iucv_message_receive`:

\__iucv_message_receive
=======================

.. c:function:: int __iucv_message_receive(struct iucv_path *path, struct iucv_message *msg, u8 flags, void *buffer, size_t size, size_t *residual)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param msg:
        address of iucv msg structure
    :type msg: struct iucv_message \*

    :param flags:
        flags that affect how the message is received (IUCV_IPBUFLST)
    :type flags: u8

    :param buffer:
        address of data buffer or address of struct iucv_array
    :type buffer: void \*

    :param size:
        length of data buffer
    :type size: size_t

    :param residual:
        *undescribed*
    :type residual: size_t \*

.. _`__iucv_message_receive.description`:

Description
-----------

This function receives messages that are being sent to you over
established paths. This function will deal with RMDATA messages
embedded in struct iucv_message as well.

.. _`__iucv_message_receive.locking`:

Locking
-------

no locking.

Returns the result from the CP IUCV call.

.. _`iucv_message_reject`:

iucv_message_reject
===================

.. c:function:: int iucv_message_reject(struct iucv_path *path, struct iucv_message *msg)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param msg:
        address of iucv msg structure
    :type msg: struct iucv_message \*

.. _`iucv_message_reject.description`:

Description
-----------

The reject function refuses a specified message. Between the time you
are notified of a message and the time that you complete the message,
the message may be rejected.

Returns the result from the CP IUCV call.

.. _`iucv_message_reply`:

iucv_message_reply
==================

.. c:function:: int iucv_message_reply(struct iucv_path *path, struct iucv_message *msg, u8 flags, void *reply, size_t size)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param msg:
        address of iucv msg structure
    :type msg: struct iucv_message \*

    :param flags:
        how the reply is sent (IUCV_IPRMDATA, IUCV_IPPRTY, IUCV_IPBUFLST)
    :type flags: u8

    :param reply:
        address of data buffer or address of struct iucv_array
    :type reply: void \*

    :param size:
        length of reply data buffer
    :type size: size_t

.. _`iucv_message_reply.description`:

Description
-----------

This function responds to the two-way messages that you receive. You
must identify completely the message to which you wish to reply. ie,
pathid, msgid, and trgcls. Prmmsg signifies the data is moved into
the parameter list.

Returns the result from the CP IUCV call.

.. _`iucv_message_send`:

iucv_message_send
=================

.. c:function:: int iucv_message_send(struct iucv_path *path, struct iucv_message *msg, u8 flags, u32 srccls, void *buffer, size_t size)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param msg:
        address of iucv msg structure
    :type msg: struct iucv_message \*

    :param flags:
        how the message is sent (IUCV_IPRMDATA, IUCV_IPPRTY, IUCV_IPBUFLST)
    :type flags: u8

    :param srccls:
        source class of message
    :type srccls: u32

    :param buffer:
        address of data buffer or address of struct iucv_array
    :type buffer: void \*

    :param size:
        length of send buffer
    :type size: size_t

.. _`iucv_message_send.description`:

Description
-----------

This function transmits data to another application. Data to be
transmitted is in a buffer and this is a one-way message and the
receiver will not reply to the message.

.. _`iucv_message_send.locking`:

Locking
-------

local_bh_enable/local_bh_disable

Returns the result from the CP IUCV call.

.. _`__iucv_message_send`:

\__iucv_message_send
====================

.. c:function:: int __iucv_message_send(struct iucv_path *path, struct iucv_message *msg, u8 flags, u32 srccls, void *buffer, size_t size)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param msg:
        address of iucv msg structure
    :type msg: struct iucv_message \*

    :param flags:
        how the message is sent (IUCV_IPRMDATA, IUCV_IPPRTY, IUCV_IPBUFLST)
    :type flags: u8

    :param srccls:
        source class of message
    :type srccls: u32

    :param buffer:
        address of data buffer or address of struct iucv_array
    :type buffer: void \*

    :param size:
        length of send buffer
    :type size: size_t

.. _`__iucv_message_send.description`:

Description
-----------

This function transmits data to another application. Data to be
transmitted is in a buffer and this is a one-way message and the
receiver will not reply to the message.

.. _`__iucv_message_send.locking`:

Locking
-------

no locking.

Returns the result from the CP IUCV call.

.. _`iucv_message_send2way`:

iucv_message_send2way
=====================

.. c:function:: int iucv_message_send2way(struct iucv_path *path, struct iucv_message *msg, u8 flags, u32 srccls, void *buffer, size_t size, void *answer, size_t asize, size_t *residual)

    :param path:
        address of iucv path structure
    :type path: struct iucv_path \*

    :param msg:
        address of iucv msg structure
    :type msg: struct iucv_message \*

    :param flags:
        how the message is sent and the reply is received
        (IUCV_IPRMDATA, IUCV_IPBUFLST, IUCV_IPPRTY, IUCV_ANSLST)
    :type flags: u8

    :param srccls:
        source class of message
    :type srccls: u32

    :param buffer:
        address of data buffer or address of struct iucv_array
    :type buffer: void \*

    :param size:
        length of send buffer
    :type size: size_t

    :param answer:
        *undescribed*
    :type answer: void \*

    :param asize:
        size of reply buffer
    :type asize: size_t

    :param residual:
        *undescribed*
    :type residual: size_t \*

.. _`iucv_message_send2way.description`:

Description
-----------

This function transmits data to another application. Data to be
transmitted is in a buffer. The receiver of the send is expected to
reply to the message and a buffer is provided into which IUCV moves
the reply to this message.

Returns the result from the CP IUCV call.

.. This file was automatic generated / don't edit.

