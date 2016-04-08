
.. _API-struct-rio-net:

==============
struct rio_net
==============

*man struct rio_net(9)*

*4.6.0-rc1*

RIO network info


Synopsis
========

.. code-block:: c

    struct rio_net {
      struct list_head node;
      struct list_head devices;
      struct list_head switches;
      struct list_head mports;
      struct rio_mport * hport;
      unsigned char id;
      struct device dev;
      void * enum_data;
      void (* release) (struct rio_net *net);
    };


Members
=======

node
    Node in global list of RIO networks

devices
    List of devices in this network

switches
    List of switches in this network

mports
    List of master ports accessing this network

hport
    Default port for accessing this network

id
    RIO network ID

dev
    Device object

enum_data
    private data specific to a network enumerator

release
    enumerator-specific release callback
