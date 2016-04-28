.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-dp-mst-branch:

========================
struct drm_dp_mst_branch
========================

*man struct drm_dp_mst_branch(9)*

*4.6.0-rc5*

MST branch device.


Synopsis
========

.. code-block:: c

    struct drm_dp_mst_branch {
      struct kref kref;
      u8 rad[8];
      u8 lct;
      int num_ports;
      int msg_slots;
      struct list_head ports;
      struct drm_dp_mst_port * port_parent;
      struct drm_dp_mst_topology_mgr * mgr;
      struct drm_dp_sideband_msg_tx * tx_slots[2];
      int last_seqno;
      bool link_address_sent;
      u8 guid[16];
    };


Members
=======

kref
    reference count for this port.

rad[8]
    Relative Address to talk to this branch device.

lct
    Link count total to talk to this branch device.

num_ports
    number of ports on the branch.

msg_slots
    one bit per transmitted msg slot.

ports
    linked list of ports on this branch.

port_parent
    pointer to the port parent, NULL if toplevel.

mgr
    topology manager for this branch device.

tx_slots[2]
    transmission slots for this device.

last_seqno
    last sequence number used to talk to this.

link_address_sent
    if a link address message has been sent to this device yet.

guid[16]
    guid for DP 1.2 branch device. port under this branch can be
    identified by port #.


Description
===========

This structure represents an MST branch device, there is one primary
branch device at the root, along with any other branches connected to
downstream port of parent branches.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
