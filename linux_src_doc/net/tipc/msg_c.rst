.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/msg.c

.. _`tipc_buf_acquire`:

tipc_buf_acquire
================

.. c:function:: struct sk_buff *tipc_buf_acquire(u32 size, gfp_t gfp)

    creates a TIPC message buffer

    :param u32 size:
        message size (including TIPC header)

    :param gfp_t gfp:
        *undescribed*

.. _`tipc_buf_acquire.description`:

Description
-----------

Returns a new buffer with data pointers set to the specified size.

.. _`tipc_buf_acquire.note`:

NOTE
----

Headroom is reserved to allow prepending of a data link header.
There may also be unrequested tailroom present at the buffer's end.

.. _`tipc_msg_build`:

tipc_msg_build
==============

.. c:function:: int tipc_msg_build(struct tipc_msg *mhdr, struct msghdr *m, int offset, int dsz, int pktmax, struct sk_buff_head *list)

    create buffer chain containing specified header and data

    :param struct tipc_msg \*mhdr:
        Message header, to be prepended to data

    :param struct msghdr \*m:
        User message

    :param int offset:
        *undescribed*

    :param int dsz:
        Total length of user data

    :param int pktmax:
        Max packet size that can be used

    :param struct sk_buff_head \*list:
        Buffer or chain of buffers to be returned to caller

.. _`tipc_msg_build.returns-message-data-size-or-errno`:

Returns message data size or errno
----------------------------------

-ENOMEM, -EFAULT

.. _`tipc_msg_bundle`:

tipc_msg_bundle
===============

.. c:function:: bool tipc_msg_bundle(struct sk_buff *skb, struct tipc_msg *msg, u32 mtu)

    Append contents of a buffer to tail of an existing one

    :param struct sk_buff \*skb:
        the buffer to append to ("bundle")

    :param struct tipc_msg \*msg:
        message to be appended

    :param u32 mtu:
        max allowable size for the bundle buffer
        Consumes buffer if successful
        Returns true if bundling could be performed, otherwise false

.. _`tipc_msg_extract`:

tipc_msg_extract
================

.. c:function:: bool tipc_msg_extract(struct sk_buff *skb, struct sk_buff **iskb, int *pos)

    extract bundled inner packet from buffer

    :param struct sk_buff \*skb:
        buffer to be extracted from.

    :param struct sk_buff \*\*iskb:
        extracted inner buffer, to be returned

    :param int \*pos:
        position in outer message of msg to be extracted.
        Returns position of next msg
        Consumes outer buffer when last packet extracted
        Returns true when when there is an extracted buffer, otherwise false

.. _`tipc_msg_make_bundle`:

tipc_msg_make_bundle
====================

.. c:function:: bool tipc_msg_make_bundle(struct sk_buff **skb, struct tipc_msg *msg, u32 mtu, u32 dnode)

    Create bundle buf and append message to its tail

    :param struct sk_buff \*\*skb:
        buffer to be created, appended to and returned in case of success

    :param struct tipc_msg \*msg:
        message to be appended

    :param u32 mtu:
        max allowable size for the bundle buffer, inclusive header

    :param u32 dnode:
        destination node for message. (Not always present in header)
        Returns true if success, otherwise false

.. _`tipc_msg_reverse`:

tipc_msg_reverse
================

.. c:function:: bool tipc_msg_reverse(u32 own_node, struct sk_buff **skb, int err)

    swap source and destination addresses and add error code

    :param u32 own_node:
        originating node id for reversed message

    :param struct sk_buff \*\*skb:
        buffer containing message to be reversed; may be replaced.

    :param int err:
        error code to be set in message, if any
        Consumes buffer at failure
        Returns true if success, otherwise false

.. _`tipc_msg_lookup_dest`:

tipc_msg_lookup_dest
====================

.. c:function:: bool tipc_msg_lookup_dest(struct net *net, struct sk_buff *skb, int *err)

    try to find new destination for named message

    :param struct net \*net:
        *undescribed*

    :param struct sk_buff \*skb:
        the buffer containing the message.

    :param int \*err:
        error code to be used by caller if lookup fails
        Does not consume buffer
        Returns true if a destination is found, false otherwise

.. This file was automatic generated / don't edit.

