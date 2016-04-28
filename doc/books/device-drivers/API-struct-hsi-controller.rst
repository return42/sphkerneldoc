.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-hsi-controller:

=====================
struct hsi_controller
=====================

*man struct hsi_controller(9)*

*4.6.0-rc5*

HSI controller device


Synopsis
========

.. code-block:: c

    struct hsi_controller {
      struct device device;
      struct module * owner;
      unsigned int id;
      unsigned int num_ports;
      struct hsi_port ** port;
    };


Members
=======

device
    Driver model representation of the device

owner
    Pointer to the module owning the controller

id
    HSI controller ID

num_ports
    Number of ports in the HSI controller

port
    Array of HSI ports


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
