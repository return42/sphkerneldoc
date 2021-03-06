.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/wimax/op-msg.c

.. _`wimax_msg_alloc`:

wimax_msg_alloc
===============

.. c:function:: struct sk_buff *wimax_msg_alloc(struct wimax_dev *wimax_dev, const char *pipe_name, const void *msg, size_t size, gfp_t gfp_flags)

    Create a new skb for sending a message to userspace

    :param wimax_dev:
        WiMAX device descriptor
    :type wimax_dev: struct wimax_dev \*

    :param pipe_name:
        "named pipe" the message will be sent to
    :type pipe_name: const char \*

    :param msg:
        pointer to the message data to send
    :type msg: const void \*

    :param size:
        size of the message to send (in bytes), including the header.
    :type size: size_t

    :param gfp_flags:
        flags for memory allocation.
    :type gfp_flags: gfp_t

.. _`wimax_msg_alloc.return`:

Return
------

\ ``0``\  if ok, negative errno code on error

.. _`wimax_msg_alloc.description`:

Description
-----------


Allocates an skb that will contain the message to send to user
space over the messaging pipe and initializes it, copying the
payload.

Once this call is done, you can deliver it with
\ :c:func:`wimax_msg_send`\ .

.. _`wimax_msg_alloc.important`:

IMPORTANT
---------


Don't use \ :c:func:`skb_push`\ /skb_pull()/skb_reserve() on the skb, as
\ :c:func:`wimax_msg_send`\  depends on skb->data being placed at the
beginning of the user message.

Unlike other WiMAX stack calls, this call can be used way early,
even before \ :c:func:`wimax_dev_add`\  is called, as long as the
wimax_dev->net_dev pointer is set to point to a proper
net_dev. This is so that drivers can use it early in case they need
to send stuff around or communicate with user space.

.. _`wimax_msg_data_len`:

wimax_msg_data_len
==================

.. c:function:: const void *wimax_msg_data_len(struct sk_buff *msg, size_t *size)

    Return a pointer and size of a message's payload

    :param msg:
        Pointer to a message created with \ :c:func:`wimax_msg_alloc`\ 
    :type msg: struct sk_buff \*

    :param size:
        Pointer to where to store the message's size
    :type size: size_t \*

.. _`wimax_msg_data_len.description`:

Description
-----------

Returns the pointer to the message data.

.. _`wimax_msg_data`:

wimax_msg_data
==============

.. c:function:: const void *wimax_msg_data(struct sk_buff *msg)

    Return a pointer to a message's payload

    :param msg:
        Pointer to a message created with \ :c:func:`wimax_msg_alloc`\ 
    :type msg: struct sk_buff \*

.. _`wimax_msg_len`:

wimax_msg_len
=============

.. c:function:: ssize_t wimax_msg_len(struct sk_buff *msg)

    Return a message's payload length

    :param msg:
        Pointer to a message created with \ :c:func:`wimax_msg_alloc`\ 
    :type msg: struct sk_buff \*

.. _`wimax_msg_send`:

wimax_msg_send
==============

.. c:function:: int wimax_msg_send(struct wimax_dev *wimax_dev, struct sk_buff *skb)

    Send a pre-allocated message to user space

    :param wimax_dev:
        WiMAX device descriptor
    :type wimax_dev: struct wimax_dev \*

    :param skb:
        \ :c:type:`struct sk_buff <sk_buff>`\  returned by \ :c:func:`wimax_msg_alloc`\ . Note the
        ownership of \ ``skb``\  is transferred to this function.
    :type skb: struct sk_buff \*

.. _`wimax_msg_send.return`:

Return
------

0 if ok, < 0 errno code on error

.. _`wimax_msg_send.description`:

Description
-----------


Sends a free-form message that was preallocated with
\ :c:func:`wimax_msg_alloc`\  and filled up.

Assumes that once you pass an skb to this function for sending, it
owns it and will release it when done (on success).

.. _`wimax_msg_send.important`:

IMPORTANT
---------


Don't use \ :c:func:`skb_push`\ /skb_pull()/skb_reserve() on the skb, as
\ :c:func:`wimax_msg_send`\  depends on skb->data being placed at the
beginning of the user message.

Unlike other WiMAX stack calls, this call can be used way early,
even before \ :c:func:`wimax_dev_add`\  is called, as long as the
wimax_dev->net_dev pointer is set to point to a proper
net_dev. This is so that drivers can use it early in case they need
to send stuff around or communicate with user space.

.. _`wimax_msg`:

wimax_msg
=========

.. c:function:: int wimax_msg(struct wimax_dev *wimax_dev, const char *pipe_name, const void *buf, size_t size, gfp_t gfp_flags)

    Send a message to user space

    :param wimax_dev:
        WiMAX device descriptor (properly referenced)
    :type wimax_dev: struct wimax_dev \*

    :param pipe_name:
        "named pipe" the message will be sent to
    :type pipe_name: const char \*

    :param buf:
        pointer to the message to send.
    :type buf: const void \*

    :param size:
        size of the buffer pointed to by \ ``buf``\  (in bytes).
    :type size: size_t

    :param gfp_flags:
        flags for memory allocation.
    :type gfp_flags: gfp_t

.. _`wimax_msg.return`:

Return
------

\ ``0``\  if ok, negative errno code on error.

.. _`wimax_msg.description`:

Description
-----------


Sends a free-form message to user space on the device \ ``wimax_dev``\ .

.. _`wimax_msg.notes`:

NOTES
-----


Once the \ ``skb``\  is given to this function, who will own it and will
release it when done (unless it returns error).

.. This file was automatic generated / don't edit.

