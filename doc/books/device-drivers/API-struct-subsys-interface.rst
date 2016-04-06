
.. _API-struct-subsys-interface:

=======================
struct subsys_interface
=======================

*man struct subsys_interface(9)*

*4.6.0-rc1*

interfaces to device functions


Synopsis
========

.. code-block:: c

    struct subsys_interface {
      const char * name;
      struct bus_type * subsys;
      struct list_head node;
      int (* add_dev) (struct device *dev, struct subsys_interface *sif);
      void (* remove_dev) (struct device *dev, struct subsys_interface *sif);
    };


Members
=======

name
    name of the device function

subsys
    subsytem of the devices to attach to

node
    the list of functions registered at the subsystem

add_dev
    device hookup to device function handler

remove_dev
    device hookup to device function handler


Description
===========

Simple interfaces attached to a subsystem. Multiple interfaces can attach to a subsystem and its devices. Unlike drivers, they do not exclusively claim or control devices.
Interfaces usually represent a specific functionality of a subsystem/class of devices.
