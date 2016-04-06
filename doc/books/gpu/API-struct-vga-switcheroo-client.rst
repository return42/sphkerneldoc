
.. _API-struct-vga-switcheroo-client:

============================
struct vga_switcheroo_client
============================

*man struct vga_switcheroo_client(9)*

*4.6.0-rc1*

registered client


Synopsis
========

.. code-block:: c

    struct vga_switcheroo_client {
      struct pci_dev * pdev;
      struct fb_info * fb_info;
      enum vga_switcheroo_state pwr_state;
      const struct vga_switcheroo_client_ops * ops;
      enum vga_switcheroo_client_id id;
      bool active;
      bool driver_power_control;
      struct list_head list;
    };


Members
=======

pdev
    client pci device

fb_info
    framebuffer to which console is remapped on switching

pwr_state
    current power state

ops
    client callbacks

id
    client identifier. Determining the id requires the handler, so gpus are initially assigned VGA_SWITCHEROO_UNKNOWN_ID and later given their true id in
    ``vga_switcheroo_enable``

active
    whether the outputs are currently switched to this client

driver_power_control
    whether power state is controlled by the driver's runtime pm. If true, writing ON and OFF to the vga_switcheroo debugfs interface is a no-op so as not to interfere with
    runtime pm

list
    client list


Description
===========

Registered client. A client can be either a GPU or an audio device on a GPU. For audio clients, the ``fb_info``, ``active`` and ``driver_power_control`` members are bogus.
