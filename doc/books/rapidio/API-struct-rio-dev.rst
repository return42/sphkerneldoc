.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-dev:

==============
struct rio_dev
==============

*man struct rio_dev(9)*

*4.6.0-rc5*

RIO device info


Synopsis
========

.. code-block:: c

    struct rio_dev {
      struct list_head global_list;
      struct list_head net_list;
      struct rio_net * net;
      bool do_enum;
      u16 did;
      u16 vid;
      u32 device_rev;
      u16 asm_did;
      u16 asm_vid;
      u16 asm_rev;
      u16 efptr;
      u32 pef;
      u32 swpinfo;
      u32 src_ops;
      u32 dst_ops;
      u32 comp_tag;
      u32 phys_efptr;
      u32 em_efptr;
      u64 dma_mask;
      struct rio_driver * driver;
      struct device dev;
      struct resource riores[RIO_MAX_DEV_RESOURCES];
      int (* pwcback) (struct rio_dev *rdev, union rio_pw_msg *msg, int step);
      u16 destid;
      u8 hopcount;
      struct rio_dev * prev;
      atomic_t state;
      struct rio_switch rswitch[0];
    };


Members
=======

global_list
    Node in list of all RIO devices

net_list
    Node in list of RIO devices in a network

net
    Network this device is a part of

do_enum
    Enumeration flag

did
    Device ID

vid
    Vendor ID

device_rev
    Device revision

asm_did
    Assembly device ID

asm_vid
    Assembly vendor ID

asm_rev
    Assembly revision

efptr
    Extended feature pointer

pef
    Processing element features

swpinfo
    Switch port info

src_ops
    Source operation capabilities

dst_ops
    Destination operation capabilities

comp_tag
    RIO component tag

phys_efptr
    RIO device extended features pointer

em_efptr
    RIO Error Management features pointer

dma_mask
    Mask of bits of RIO address this device implements

driver
    Driver claiming this device

dev
    Device model device

riores[RIO_MAX_DEV_RESOURCES]
    RIO resources this device owns

pwcback
    port-write callback function for this device

destid
    Network destination ID (or associated destid for switch)

hopcount
    Hopcount to this device

prev
    Previous RIO device connected to the current one

state
    device state

rswitch[0]
    struct rio_switch (if valid for this device)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
