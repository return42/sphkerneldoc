
.. _API-struct-hsi-controller:

=====================
struct hsi_controller
=====================

*man struct hsi_controller(9)*

*4.6.0-rc1*

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
