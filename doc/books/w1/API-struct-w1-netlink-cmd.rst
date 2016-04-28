.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-w1-netlink-cmd:

=====================
struct w1_netlink_cmd
=====================

*man struct w1_netlink_cmd(9)*

*4.6.0-rc5*

holds the command and data


Synopsis
========

.. code-block:: c

    struct w1_netlink_cmd {
      __u8 cmd;
      __u8 res;
      __u16 len;
      __u8 data[0];
    };


Members
=======

cmd
    one of enum w1_commands

res
    reserved

len
    length of data following w1_netlink_cmd

data[0]
    start address of any following data


Description
===========

One or more struct w1_netlink_cmd is placed starting at
w1_netlink_msg.data each with optional data.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
