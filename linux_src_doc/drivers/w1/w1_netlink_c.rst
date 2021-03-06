.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/w1/w1_netlink.c

.. _`w1_reply_len`:

w1_reply_len
============

.. c:function:: u16 w1_reply_len(struct w1_cb_block *block)

    calculate current reply length, compare to maxlen

    :param block:
        block to calculate
    :type block: struct w1_cb_block \*

.. _`w1_reply_len.description`:

Description
-----------

Calculates the current message length including possible multiple
cn_msg and data, excludes the first sizeof(struct cn_msg).  Direclty
compariable to maxlen and usable to send the message.

.. _`w1_reply_make_space`:

w1_reply_make_space
===================

.. c:function:: void w1_reply_make_space(struct w1_cb_block *block, u16 space)

    send message if needed to make space

    :param block:
        block to make space on
    :type block: struct w1_cb_block \*

    :param space:
        how many bytes requested
    :type space: u16

.. _`w1_reply_make_space.description`:

Description
-----------

Verify there is enough room left for the caller to add "space" bytes to the
message, if there isn't send the message and reset.

.. _`w1_netlink_setup_msg`:

w1_netlink_setup_msg
====================

.. c:function:: void w1_netlink_setup_msg(struct w1_cb_block *block, u32 ack)

    prepare to write block->msg

    :param block:
        block to operate on
    :type block: struct w1_cb_block \*

    :param ack:
        determines if cn can be reused
    :type ack: u32

.. _`w1_netlink_setup_msg.description`:

Description
-----------

block->cn will be setup with the correct ack, advancing if needed
block->cn->len does not include space for block->msg
block->msg advances but remains uninitialized

.. _`w1_netlink_send_error`:

w1_netlink_send_error
=====================

.. c:function:: void w1_netlink_send_error(struct cn_msg *cn, struct w1_netlink_msg *msg, int portid, int error)

    sends the error message now

    :param cn:
        original cn_msg
    :type cn: struct cn_msg \*

    :param msg:
        original w1_netlink_msg
    :type msg: struct w1_netlink_msg \*

    :param portid:
        where to send it
    :type portid: int

    :param error:
        error status
    :type error: int

.. _`w1_netlink_send_error.description`:

Description
-----------

Use when a block isn't available to queue the message to and cn, msg
might not be contiguous.

.. _`w1_netlink_send`:

w1_netlink_send
===============

.. c:function:: void w1_netlink_send(struct w1_master *dev, struct w1_netlink_msg *msg)

    sends w1 netlink notifications

    :param dev:
        w1_master the even is associated with or for
    :type dev: struct w1_master \*

    :param msg:
        w1_netlink_msg message to be sent
    :type msg: struct w1_netlink_msg \*

.. _`w1_netlink_send.description`:

Description
-----------

This are notifications generated from the kernel.

.. This file was automatic generated / don't edit.

