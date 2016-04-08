
.. _API-struct-w1-netlink-msg:

=====================
struct w1_netlink_msg
=====================

*man struct w1_netlink_msg(9)*

*4.6.0-rc1*

holds w1 message type, id, and result


Synopsis
========

.. code-block:: c

    struct w1_netlink_msg {
      __u8 type;
      __u8 status;
      __u16 len;
      union id;
      __u8 data[0];
    };


Members
=======

type
    one of enum w1_netlink_message_types

status
    kernel feedback for success 0 or errno failure value

len
    length of data following w1_netlink_msg

id
    union holding master bus id (msg.id) and slave device id (id[8]).

data[0]
    start address of any following data


Description
===========

The base message structure for w1 messages over netlink. The netlink connector data sequence is, struct nlmsghdr, struct cn_msg, then one or more struct w1_netlink_msg (each
with optional data).
