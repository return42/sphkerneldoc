.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/msg.c

.. _`tipc_buf_acquire`:

tipc_buf_acquire
================

.. c:function:: struct sk_buff *tipc_buf_acquire(u32 size, gfp_t gfp)

    creates a TIPC message buffer

    :param size:
        message size (including TIPC header)
    :type size: u32

    :param gfp:
        *undescribed*
    :type gfp: gfp_t

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

    :param mhdr:
        Message header, to be prepended to data
    :type mhdr: struct tipc_msg \*

    :param m:
        User message
    :type m: struct msghdr \*

    :param offset:
        *undescribed*
    :type offset: int

    :param dsz:
        Total length of user data
    :type dsz: int

    :param pktmax:
        Max packet size that can be used
    :type pktmax: int

    :param list:
        Buffer or chain of buffers to be returned to caller
    :type list: struct sk_buff_head \*

.. _`tipc_msg_build.description`:

Description
-----------

Note that the recursive call we are making here is safe, since it can
logically go only one further level down.

.. _`tipc_msg_build.returns-message-data-size-or-errno`:

Returns message data size or errno
----------------------------------

-ENOMEM, -EFAULT

.. _`tipc_msg_bundle`:

tipc_msg_bundle
===============

.. c:function:: bool tipc_msg_bundle(struct sk_buff *skb, struct tipc_msg *msg, u32 mtu)

    Append contents of a buffer to tail of an existing one

    :param skb:
        the buffer to append to ("bundle")
    :type skb: struct sk_buff \*

    :param msg:
        message to be appended
    :type msg: struct tipc_msg \*

    :param mtu:
        max allowable size for the bundle buffer
        Consumes buffer if successful
        Returns true if bundling could be performed, otherwise false
    :type mtu: u32

.. _`tipc_msg_extract`:

tipc_msg_extract
================

.. c:function:: bool tipc_msg_extract(struct sk_buff *skb, struct sk_buff **iskb, int *pos)

    extract bundled inner packet from buffer

    :param skb:
        buffer to be extracted from.
    :type skb: struct sk_buff \*

    :param iskb:
        extracted inner buffer, to be returned
    :type iskb: struct sk_buff \*\*

    :param pos:
        position in outer message of msg to be extracted.
        Returns position of next msg
        Consumes outer buffer when last packet extracted
        Returns true when when there is an extracted buffer, otherwise false
    :type pos: int \*

.. _`tipc_msg_make_bundle`:

tipc_msg_make_bundle
====================

.. c:function:: bool tipc_msg_make_bundle(struct sk_buff **skb, struct tipc_msg *msg, u32 mtu, u32 dnode)

    Create bundle buf and append message to its tail

    :param skb:
        buffer to be created, appended to and returned in case of success
    :type skb: struct sk_buff \*\*

    :param msg:
        message to be appended
    :type msg: struct tipc_msg \*

    :param mtu:
        max allowable size for the bundle buffer, inclusive header
    :type mtu: u32

    :param dnode:
        destination node for message. (Not always present in header)
        Returns true if success, otherwise false
    :type dnode: u32

.. _`tipc_msg_reverse`:

tipc_msg_reverse
================

.. c:function:: bool tipc_msg_reverse(u32 own_node, struct sk_buff **skb, int err)

    swap source and destination addresses and add error code

    :param own_node:
        originating node id for reversed message
    :type own_node: u32

    :param skb:
        buffer containing message to be reversed; will be consumed
    :type skb: struct sk_buff \*\*

    :param err:
        error code to be set in message, if any
        Replaces consumed buffer with new one when successful
        Returns true if success, otherwise false
    :type err: int

.. _`tipc_msg_lookup_dest`:

tipc_msg_lookup_dest
====================

.. c:function:: bool tipc_msg_lookup_dest(struct net *net, struct sk_buff *skb, int *err)

    try to find new destination for named message

    :param net:
        *undescribed*
    :type net: struct net \*

    :param skb:
        the buffer containing the message.
    :type skb: struct sk_buff \*

    :param err:
        error code to be used by caller if lookup fails
        Does not consume buffer
        Returns true if a destination is found, false otherwise
    :type err: int \*

.. This file was automatic generated / don't edit.

