
.. _API-struct-vga-switcheroo-handler:

=============================
struct vga_switcheroo_handler
=============================

*man struct vga_switcheroo_handler(9)*

*4.6.0-rc1*

handler callbacks


Synopsis
========

.. code-block:: c

    struct vga_switcheroo_handler {
      int (* init) (void);
      int (* switchto) (enum vga_switcheroo_client_id id);
      int (* switch_ddc) (enum vga_switcheroo_client_id id);
      int (* power_state) (enum vga_switcheroo_client_id id,enum vga_switcheroo_state state);
      enum vga_switcheroo_client_id (* get_client_id) (struct pci_dev *pdev);
    };


Members
=======

init
    initialize handler. Optional. This gets called when vga_switcheroo is enabled, i.e. when two vga clients have registered. It allows the handler to perform some delayed
    initialization that depends on the existence of the vga clients. Currently only the radeon and amdgpu drivers use this. The return value is ignored

switchto
    switch outputs to given client. Mandatory. For muxless machines this should be a no-op. Returning 0 denotes success, anything else failure (in which case the switch is aborted)

switch_ddc
    switch DDC lines to given client. Optional. Should return the previous DDC owner on success or a negative int on failure

power_state
    cut or reinstate power of given client. Optional. The return value is ignored

get_client_id
    determine if given pci device is integrated or discrete GPU. Mandatory


Description
===========

Handler callbacks. The multiplexer itself. The ``switchto`` and ``get_client_id`` methods are mandatory, all others may be set to NULL.
