.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_msg.c

.. _`vmw_open_channel`:

vmw_open_channel
================

.. c:function:: int vmw_open_channel(struct rpc_channel *channel, unsigned int protocol)

    :param struct rpc_channel \*channel:
        RPC channel

    :param unsigned int protocol:
        *undescribed*

.. _`vmw_open_channel.return`:

Return
------

0 on success

.. _`vmw_close_channel`:

vmw_close_channel
=================

.. c:function:: int vmw_close_channel(struct rpc_channel *channel)

    :param struct rpc_channel \*channel:
        RPC channel

.. _`vmw_close_channel.return`:

Return
------

0 on success

.. _`vmw_send_msg`:

vmw_send_msg
============

.. c:function:: int vmw_send_msg(struct rpc_channel *channel, const char *msg)

    Sends a message to the host

    :param struct rpc_channel \*channel:
        RPC channel

    :param const char \*msg:
        *undescribed*

.. _`vmw_send_msg.return`:

Return
------

0 on success

.. _`vmw_recv_msg`:

vmw_recv_msg
============

.. c:function:: int vmw_recv_msg(struct rpc_channel *channel, void **msg, size_t *msg_len)

    Receives a message from the host

    :param struct rpc_channel \*channel:
        channel opened by vmw_open_channel

    :param void \*\*msg:
        [OUT] message received from the host

    :param size_t \*msg_len:
        message length

.. _`vmw_recv_msg.note`:

Note
----

It is the caller's responsibility to call \ :c:func:`kfree`\  on msg.

.. _`vmw_host_get_guestinfo`:

vmw_host_get_guestinfo
======================

.. c:function:: int vmw_host_get_guestinfo(const char *guest_info_param, char *buffer, size_t *length)

    Gets a GuestInfo parameter

    :param const char \*guest_info_param:
        Parameter to get, e.g. GuestInfo.svga.gl3

    :param char \*buffer:
        if NULL, \*reply_len will contain reply size.

    :param size_t \*length:
        size of the reply_buf.  Set to size of reply upon return

.. _`vmw_host_get_guestinfo.description`:

Description
-----------

Gets the value of a  GuestInfo.\* parameter.  The value returned will be in
a string, and it is up to the caller to post-process.

.. _`vmw_host_get_guestinfo.return`:

Return
------

0 on success

.. _`vmw_host_log`:

vmw_host_log
============

.. c:function:: int vmw_host_log(const char *log)

    Sends a log message to the host

    :param const char \*log:
        NULL terminated string

.. _`vmw_host_log.return`:

Return
------

0 on success

.. This file was automatic generated / don't edit.

