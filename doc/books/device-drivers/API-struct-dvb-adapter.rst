.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-dvb-adapter:

==================
struct dvb_adapter
==================

*man struct dvb_adapter(9)*

*4.6.0-rc5*

represents a Digital TV adapter using Linux DVB API


Synopsis
========

.. code-block:: c

    struct dvb_adapter {
      int num;
      struct list_head list_head;
      struct list_head device_list;
      const char * name;
      u8 proposed_mac[6];
      void * priv;
      struct device * device;
      struct module * module;
      int mfe_shared;
      struct dvb_device * mfe_dvbdev;
      struct mutex mfe_lock;
    #if defined(CONFIG_MEDIA_CONTROLLER_DVB)
      struct media_device * mdev;
      struct media_entity * conn;
      struct media_pad * conn_pads;
    #endif
    };


Members
=======

num
    Number of the adapter

list_head
    List with the DVB adapters

device_list
    List with the DVB devices

name
    Name of the adapter

proposed_mac[6]
    proposed MAC address for the adapter

priv
    private data

device
    pointer to struct device

module
    pointer to struct module

mfe_shared
    mfe shared: indicates mutually exclusive frontends Thie usage of
    this flag is currently deprecated

mfe_dvbdev
    Frontend device in use, in the case of MFE

mfe_lock
    Lock to prevent using the other frontends when MFE is used.

mdev
    pointer to struct media_device, used when the media controller is
    used.

conn
    RF connector. Used only if the device has no separate tuner.

conn_pads
    pointer to struct media_pad associated with ``conn``;


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
