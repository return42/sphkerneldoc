
.. _API-enum-w1-cn-msg-flags:

====================
enum w1_cn_msg_flags
====================

*man enum w1_cn_msg_flags(9)*

*4.6.0-rc1*

bitfield flags for struct cn_msg.flags


Synopsis
========

.. code-block:: c

    enum w1_cn_msg_flags {
      W1_CN_BUNDLE
    };


Constants
=========

W1_CN_BUNDLE
    Request bundling replies into fewer messagse. Be prepared to handle multiple struct cn_msg, struct w1_netlink_msg, and struct w1_netlink_cmd in one packet.
