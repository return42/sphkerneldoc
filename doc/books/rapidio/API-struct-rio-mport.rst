.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-mport:

================
struct rio_mport
================

*man struct rio_mport(9)*

*4.6.0-rc5*

RIO master port info


Synopsis
========

.. code-block:: c

    struct rio_mport {
      struct list_head dbells;
      struct list_head pwrites;
      struct list_head node;
      struct list_head nnode;
      struct rio_net * net;
      struct mutex lock;
      struct resource iores;
      struct resource riores[RIO_MAX_MPORT_RESOURCES];
      struct rio_msg inb_msg[RIO_MAX_MBOX];
      struct rio_msg outb_msg[RIO_MAX_MBOX];
      int host_deviceid;
      struct rio_ops * ops;
      unsigned char id;
      unsigned char index;
      unsigned int sys_size;
      enum rio_phy_type phy_type;
      u32 phys_efptr;
      unsigned char name[RIO_MAX_MPORT_NAME];
      struct device dev;
      void * priv;
    #ifdef CONFIG_RAPIDIO_DMA_ENGINE
      struct dma_device dma;
    #endif
      struct rio_scan * nscan;
      atomic_t state;
      unsigned int pwe_refcnt;
    };


Members
=======

dbells
    List of doorbell events

pwrites
    List of portwrite events

node
    Node in global list of master ports

nnode
    Node in network list of master ports

net
    RIO net this mport is attached to

lock
    lock to synchronize lists manipulations

iores
    I/O mem resource that this master port interface owns

riores[RIO_MAX_MPORT_RESOURCES]
    RIO resources that this master port interfaces owns

inb_msg[RIO_MAX_MBOX]
    RIO inbound message event descriptors

outb_msg[RIO_MAX_MBOX]
    RIO outbound message event descriptors

host_deviceid
    Host device ID associated with this master port

ops
    configuration space functions

id
    Port ID, unique among all ports

index
    Port index, unique among all port interfaces of the same type

sys_size
    RapidIO common transport system size

phy_type
    RapidIO phy type

phys_efptr
    RIO port extended features pointer

name[RIO_MAX_MPORT_NAME]
    Port name string

dev
    device structure associated with an mport

priv
    Master port private data

dma
    DMA device associated with mport

nscan
    RapidIO network enumeration/discovery operations

state
    mport device state

pwe_refcnt
    port-write enable ref counter to track enable/disable requests


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
