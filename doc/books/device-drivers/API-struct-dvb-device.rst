.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-dvb-device:

=================
struct dvb_device
=================

*man struct dvb_device(9)*

*4.6.0-rc5*

represents a DVB device node


Synopsis
========

.. code-block:: c

    struct dvb_device {
      struct list_head list_head;
      const struct file_operations * fops;
      struct dvb_adapter * adapter;
      int type;
      int minor;
      u32 id;
      int readers;
      int writers;
      int users;
      wait_queue_head_t wait_queue;
      int (* kernel_ioctl) (struct file *file, unsigned int cmd, void *arg);
    #if defined(CONFIG_MEDIA_CONTROLLER_DVB)
      const char * name;
      struct media_intf_devnode * intf_devnode;
      unsigned tsout_num_entities;
      struct media_entity * entity;
      struct media_entity * tsout_entity;
      struct media_pad * pads;
      struct media_pad * tsout_pads;
    #endif
      void * priv;
    };


Members
=======

list_head
    List head with all DVB devices

fops
    pointer to struct file_operations

adapter
    pointer to the adapter that holds this device node

type
    type of the device: DVB_DEVICE_SEC, DVB_DEVICE_FRONTEND,
    DVB_DEVICE_DEMUX, DVB_DEVICE_DVR, DVB_DEVICE_CA,
    DVB_DEVICE_NET

minor
    devnode minor number. Major number is always DVB_MAJOR.

id
    device ID number, inside the adapter

readers
    Initialized by the caller. Each call to ``open`` in Read Only mode
    decreases this counter by one.

writers
    Initialized by the caller. Each call to ``open`` in Read/Write mode
    decreases this counter by one.

users
    Initialized by the caller. Each call to ``open`` in any mode
    decreases this counter by one.

wait_queue
    wait queue, used to wait for certain events inside one of the DVB
    API callers

kernel_ioctl
    callback function used to handle ioctl calls from userspace.

name
    Name to be used for the device at the Media Controller

intf_devnode
    Pointer to media_intf_devnode. Used by the dvbdev core to store
    the MC device node interface

tsout_num_entities
    Number of Transport Stream output entities

entity
    pointer to struct media_entity associated with the device node

tsout_entity
    array with MC entities associated to each TS output node

pads
    pointer to struct media_pad associated with ``entity``;

tsout_pads
    array with the source pads for each ``tsout_entity``

priv
    private data


Description
===========

This structure is used by the DVB core (frontend, CA, net, demux) in
order to create the device nodes. Usually, driver should not initialize
this struct diretly.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
