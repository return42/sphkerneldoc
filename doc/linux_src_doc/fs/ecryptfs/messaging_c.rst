.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/messaging.c

.. _`list_head`:

LIST_HEAD
=========

.. c:function::  LIST_HEAD( ecryptfs_msg_ctx_free_list)

    Linux filesystem encryption layer

    :param  ecryptfs_msg_ctx_free_list:
        *undescribed*

.. _`list_head.description`:

Description
-----------

Copyright (C) 2004-2008 International Business Machines Corp.
Author(s): Michael A. Halcrow <mhalcrow\ ``us``\ .ibm.com>
Tyler Hicks <tyhicks\ ``ou``\ .edu>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License version
2 as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
02111-1307, USA.

.. _`ecryptfs_acquire_free_msg_ctx`:

ecryptfs_acquire_free_msg_ctx
=============================

.. c:function:: int ecryptfs_acquire_free_msg_ctx(struct ecryptfs_msg_ctx **msg_ctx)

    :param struct ecryptfs_msg_ctx \*\*msg_ctx:
        The context that was acquired from the free list

.. _`ecryptfs_acquire_free_msg_ctx.description`:

Description
-----------

Acquires a context element from the free list and locks the mutex
on the context.  Sets the msg_ctx task to current.  Returns zero on
success; non-zero on error or upon failure to acquire a free
context element.  Must be called with ecryptfs_msg_ctx_lists_mux
held.

.. _`ecryptfs_msg_ctx_free_to_alloc`:

ecryptfs_msg_ctx_free_to_alloc
==============================

.. c:function:: void ecryptfs_msg_ctx_free_to_alloc(struct ecryptfs_msg_ctx *msg_ctx)

    :param struct ecryptfs_msg_ctx \*msg_ctx:
        The context to move from the free list to the alloc list

.. _`ecryptfs_msg_ctx_free_to_alloc.description`:

Description
-----------

Must be called with ecryptfs_msg_ctx_lists_mux held.

.. _`ecryptfs_msg_ctx_alloc_to_free`:

ecryptfs_msg_ctx_alloc_to_free
==============================

.. c:function:: void ecryptfs_msg_ctx_alloc_to_free(struct ecryptfs_msg_ctx *msg_ctx)

    :param struct ecryptfs_msg_ctx \*msg_ctx:
        The context to move from the alloc list to the free list

.. _`ecryptfs_msg_ctx_alloc_to_free.description`:

Description
-----------

Must be called with ecryptfs_msg_ctx_lists_mux held.

.. _`ecryptfs_find_daemon_by_euid`:

ecryptfs_find_daemon_by_euid
============================

.. c:function:: int ecryptfs_find_daemon_by_euid(struct ecryptfs_daemon **daemon)

    :param struct ecryptfs_daemon \*\*daemon:
        If return value is zero, points to the desired daemon pointer

.. _`ecryptfs_find_daemon_by_euid.description`:

Description
-----------

Must be called with ecryptfs_daemon_hash_mux held.

Search the hash list for the current effective user id.

Returns zero if the user id exists in the list; non-zero otherwise.

.. _`ecryptfs_spawn_daemon`:

ecryptfs_spawn_daemon
=====================

.. c:function:: int ecryptfs_spawn_daemon(struct ecryptfs_daemon **daemon, struct file *file)

    Create and initialize a new daemon struct

    :param struct ecryptfs_daemon \*\*daemon:
        Pointer to set to newly allocated daemon struct

    :param struct file \*file:
        File used when opening /dev/ecryptfs

.. _`ecryptfs_spawn_daemon.description`:

Description
-----------

Must be called ceremoniously while in possession of
ecryptfs_sacred_daemon_hash_mux

Returns zero on success; non-zero otherwise

.. _`ecryptfs_exorcise_daemon`:

ecryptfs_exorcise_daemon
========================

.. c:function:: int ecryptfs_exorcise_daemon(struct ecryptfs_daemon *daemon)

    Destroy the daemon struct

    :param struct ecryptfs_daemon \*daemon:
        *undescribed*

.. _`ecryptfs_exorcise_daemon.description`:

Description
-----------

Must be called ceremoniously while in possession of
ecryptfs_daemon_hash_mux and the daemon's own mux.

.. _`ecryptfs_process_response`:

ecryptfs_process_response
=========================

.. c:function:: int ecryptfs_process_response(struct ecryptfs_daemon *daemon, struct ecryptfs_message *msg, u32 seq)

    :param struct ecryptfs_daemon \*daemon:
        *undescribed*

    :param struct ecryptfs_message \*msg:
        The ecryptfs message received; the caller should sanity check
        msg->data_len and free the memory

    :param u32 seq:
        The sequence number of the message; must match the sequence
        number for the existing message context waiting for this
        response

.. _`ecryptfs_process_response.description`:

Description
-----------

Processes a response message after sending an operation request to
userspace. Some other process is awaiting this response. Before
sending out its first communications, the other process allocated a
msg_ctx from the ecryptfs_msg_ctx_arr at a particular index. The
response message contains this index so that we can copy over the
response message into the msg_ctx that the process holds a
reference to. The other process is going to wake up, check to see
that msg_ctx->state == ECRYPTFS_MSG_CTX_STATE_DONE, and then
proceed to read off and process the response message. Returns zero
upon delivery to desired context element; non-zero upon delivery
failure or error.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_send_message_locked`:

ecryptfs_send_message_locked
============================

.. c:function:: int ecryptfs_send_message_locked(char *data, int data_len, u8 msg_type, struct ecryptfs_msg_ctx **msg_ctx)

    :param char \*data:
        The data to send

    :param int data_len:
        The length of data

    :param u8 msg_type:
        *undescribed*

    :param struct ecryptfs_msg_ctx \*\*msg_ctx:
        The message context allocated for the send

.. _`ecryptfs_send_message_locked.description`:

Description
-----------

Must be called with ecryptfs_daemon_hash_mux held.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_send_message`:

ecryptfs_send_message
=====================

.. c:function:: int ecryptfs_send_message(char *data, int data_len, struct ecryptfs_msg_ctx **msg_ctx)

    :param char \*data:
        The data to send

    :param int data_len:
        The length of data

    :param struct ecryptfs_msg_ctx \*\*msg_ctx:
        The message context allocated for the send

.. _`ecryptfs_send_message.description`:

Description
-----------

Grabs ecryptfs_daemon_hash_mux.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_wait_for_response`:

ecryptfs_wait_for_response
==========================

.. c:function:: int ecryptfs_wait_for_response(struct ecryptfs_msg_ctx *msg_ctx, struct ecryptfs_message **msg)

    :param struct ecryptfs_msg_ctx \*msg_ctx:
        The context that was assigned when sending a message

    :param struct ecryptfs_message \*\*msg:
        The incoming message from userspace; not set if rc != 0

.. _`ecryptfs_wait_for_response.description`:

Description
-----------

Sleeps until awaken by ecryptfs_receive_message or until the amount
of time exceeds ecryptfs_message_wait_timeout.  If zero is
returned, msg will point to a valid message from userspace; a
non-zero value is returned upon failure to receive a message or an
error occurs. Callee must free \ ``msg``\  on success.

.. This file was automatic generated / don't edit.

