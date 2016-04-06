
.. _API-struct-vgasr-priv:

=================
struct vgasr_priv
=================

*man struct vgasr_priv(9)*

*4.6.0-rc1*

vga_switcheroo private data


Synopsis
========

.. code-block:: c

    struct vgasr_priv {
      bool active;
      bool delayed_switch_active;
      enum vga_switcheroo_client_id delayed_client_id;
      struct dentry * debugfs_root;
      struct dentry * switch_file;
      int registered_clients;
      struct list_head clients;
      const struct vga_switcheroo_handler * handler;
      enum vga_switcheroo_handler_flags_t handler_flags;
      struct mutex mux_hw_lock;
      int old_ddc_owner;
    };


Members
=======

active
    whether vga_switcheroo is enabled. Prerequisite is the registration of two GPUs and a handler

delayed_switch_active
    whether a delayed switch is pending

delayed_client_id
    client to which a delayed switch is pending

debugfs_root
    directory for vga_switcheroo debugfs interface

switch_file
    file for vga_switcheroo debugfs interface

registered_clients
    number of registered GPUs (counting only vga clients, not audio clients)

clients
    list of registered clients

handler
    registered handler

handler_flags
    flags of registered handler

mux_hw_lock
    protects mux state (in particular while DDC lines are temporarily switched)

old_ddc_owner
    client to which DDC lines will be switched back on unlock


Description
===========

vga_switcheroo private data. Currently only one vga_switcheroo instance per system is supported.
