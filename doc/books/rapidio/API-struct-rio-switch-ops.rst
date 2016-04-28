.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-switch-ops:

=====================
struct rio_switch_ops
=====================

*man struct rio_switch_ops(9)*

*4.6.0-rc5*

Per-switch operations


Synopsis
========

.. code-block:: c

    struct rio_switch_ops {
      struct module * owner;
      int (* add_entry) (struct rio_mport *mport, u16 destid, u8 hopcount,u16 table, u16 route_destid, u8 route_port);
      int (* get_entry) (struct rio_mport *mport, u16 destid, u8 hopcount,u16 table, u16 route_destid, u8 *route_port);
      int (* clr_table) (struct rio_mport *mport, u16 destid, u8 hopcount,u16 table);
      int (* set_domain) (struct rio_mport *mport, u16 destid, u8 hopcount,u8 sw_domain);
      int (* get_domain) (struct rio_mport *mport, u16 destid, u8 hopcount,u8 *sw_domain);
      int (* em_init) (struct rio_dev *dev);
      int (* em_handle) (struct rio_dev *dev, u8 swport);
    };


Members
=======

owner
    The module owner of this structure

add_entry
    Callback for switch-specific route add function

get_entry
    Callback for switch-specific route get function

clr_table
    Callback for switch-specific clear route table function

set_domain
    Callback for switch-specific domain setting function

get_domain
    Callback for switch-specific domain get function

em_init
    Callback for switch-specific error management init function

em_handle
    Callback for switch-specific error management handler function


Description
===========

Defines the operations that are necessary to initialize/control a
particular RIO switch device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
