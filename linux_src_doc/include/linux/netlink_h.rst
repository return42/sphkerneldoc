.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/netlink.h

.. _`netlink_ext_ack`:

struct netlink_ext_ack
======================

.. c:type:: struct netlink_ext_ack

    netlink extended ACK report struct

.. _`netlink_ext_ack.definition`:

Definition
----------

.. code-block:: c

    struct netlink_ext_ack {
        const char *_msg;
        const struct nlattr *bad_attr;
        u8 cookie[NETLINK_MAX_COOKIE_LEN];
        u8 cookie_len;
    }

.. _`netlink_ext_ack.members`:

Members
-------

_msg
    message string to report - don't access directly, use
    \ ``NL_SET_ERR_MSG``\ 

bad_attr
    attribute with error

cookie
    cookie data to return to userspace (for success)

cookie_len
    actual cookie data length

.. This file was automatic generated / don't edit.

