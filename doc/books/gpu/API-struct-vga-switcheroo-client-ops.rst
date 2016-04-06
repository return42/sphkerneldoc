
.. _API-struct-vga-switcheroo-client-ops:

================================
struct vga_switcheroo_client_ops
================================

*man struct vga_switcheroo_client_ops(9)*

*4.6.0-rc1*

client callbacks


Synopsis
========

.. code-block:: c

    struct vga_switcheroo_client_ops {
      void (* set_gpu_state) (struct pci_dev *dev, enum vga_switcheroo_state);
      void (* reprobe) (struct pci_dev *dev);
      bool (* can_switch) (struct pci_dev *dev);
    };


Members
=======

set_gpu_state
    do the equivalent of suspend/resume for the card. Mandatory. This should not cut power to the discrete GPU, which is the job of the handler

reprobe
    poll outputs. Optional. This gets called after waking the GPU and switching the outputs to it

can_switch
    check if the device is in a position to switch now. Mandatory. The client should return false if a user space process has one of its device files open


Description
===========

Client callbacks. A client can be either a GPU or an audio device on a GPU. The ``set_gpu_state`` and ``can_switch`` methods are mandatory, ``reprobe`` may be set to NULL. For
audio clients, the ``reprobe`` member is bogus.
