.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-ops:

==============
struct rio_ops
==============

*man struct rio_ops(9)*

*4.6.0-rc5*

Low-level RIO configuration space operations


Synopsis
========

.. code-block:: c

    struct rio_ops {
      int (* lcread) (struct rio_mport *mport, int index, u32 offset, int len,u32 *data);
      int (* lcwrite) (struct rio_mport *mport, int index, u32 offset, int len,u32 data);
      int (* cread) (struct rio_mport *mport, int index, u16 destid,u8 hopcount, u32 offset, int len, u32 *data);
      int (* cwrite) (struct rio_mport *mport, int index, u16 destid,u8 hopcount, u32 offset, int len, u32 data);
      int (* dsend) (struct rio_mport *mport, int index, u16 destid, u16 data);
      int (* pwenable) (struct rio_mport *mport, int enable);
      int (* open_outb_mbox) (struct rio_mport *mport, void *dev_id,int mbox, int entries);
      void (* close_outb_mbox) (struct rio_mport *mport, int mbox);
      int (* open_inb_mbox) (struct rio_mport *mport, void *dev_id,int mbox, int entries);
      void (* close_inb_mbox) (struct rio_mport *mport, int mbox);
      int (* add_outb_message) (struct rio_mport *mport, struct rio_dev *rdev,int mbox, void *buffer, size_t len);
      int (* add_inb_buffer) (struct rio_mport *mport, int mbox, void *buf);
      void *(* get_inb_message) (struct rio_mport *mport, int mbox);
      int (* map_inb) (struct rio_mport *mport, dma_addr_t lstart,u64 rstart, u32 size, u32 flags);
      void (* unmap_inb) (struct rio_mport *mport, dma_addr_t lstart);
      int (* query_mport) (struct rio_mport *mport,struct rio_mport_attr *attr);
      int (* map_outb) (struct rio_mport *mport, u16 destid, u64 rstart,u32 size, u32 flags, dma_addr_t *laddr);
      void (* unmap_outb) (struct rio_mport *mport, u16 destid, u64 rstart);
    };


Members
=======

lcread
    Callback to perform local (master port) read of config space.

lcwrite
    Callback to perform local (master port) write of config space.

cread
    Callback to perform network read of config space.

cwrite
    Callback to perform network write of config space.

dsend
    Callback to send a doorbell message.

pwenable
    Callback to enable/disable port-write message handling.

open_outb_mbox
    Callback to initialize outbound mailbox.

close_outb_mbox
    Callback to shut down outbound mailbox.

open_inb_mbox
    Callback to initialize inbound mailbox.

close_inb_mbox
    Callback to shut down inbound mailbox.

add_outb_message
    Callback to add a message to an outbound mailbox queue.

add_inb_buffer
    Callback to add a buffer to an inbound mailbox queue.

get_inb_message
    Callback to get a message from an inbound mailbox queue.

map_inb
    Callback to map RapidIO address region into local memory space.

unmap_inb
    Callback to unmap RapidIO address region mapped with ``map_inb``.

query_mport
    Callback to query mport device attributes.

map_outb
    Callback to map outbound address region into local memory space.

unmap_outb
    Callback to unmap outbound RapidIO address region.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
