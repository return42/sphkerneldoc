.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-w1-cn-msg-flags:

====================
enum w1_cn_msg_flags
====================

*man enum w1_cn_msg_flags(9)*

*4.6.0-rc5*

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
    Request bundling replies into fewer messagse. Be prepared to handle
    multiple struct cn_msg, struct w1_netlink_msg, and struct
    w1_netlink_cmd in one packet.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
