.. -*- coding: utf-8; mode: rst -*-

================
vga_switcheroo.h
================

.. _`vga_switcheroo_handler_flags_t`:

enum vga_switcheroo_handler_flags_t
===================================

.. c:type:: enum vga_switcheroo_handler_flags_t

    handler flags bitmask



Constants
---------

:``VGA_SWITCHEROO_CAN_SWITCH_DDC``:
    whether the handler is able to switch the
    DDC lines separately. This signals to clients that they should call
    :c:func:`drm_get_edid_switcheroo` to probe the EDID

:``VGA_SWITCHEROO_NEEDS_EDP_CONFIG``:
    whether the handler is unable to switch
    the AUX channel separately. This signals to clients that the active
    GPU needs to train the link and communicate the link parameters to the
    inactive GPU (mediated by vga_switcheroo). The inactive GPU may then
    skip the AUX handshake and set up its output with these pre-calibrated
    values (DisplayPort specification v1.1a, section 2.5.3.3)


Description
-----------

Handler flags bitmask. Used by handlers to declare their capabilities upon
registering with vga_switcheroo.


.. _`vga_switcheroo_state`:

enum vga_switcheroo_state
=========================

.. c:type:: enum vga_switcheroo_state

    client power state



Constants
---------

:``VGA_SWITCHEROO_OFF``:
    off

:``VGA_SWITCHEROO_ON``:
    on

:``VGA_SWITCHEROO_NOT_FOUND``:
    client has not registered with vga_switcheroo.::

            Only used in :c:func:`vga_switcheroo_get_client_state` which in turn is only
            called from hda_intel.c


Description
-----------

Client power state.


.. _`vga_switcheroo_client_id`:

enum vga_switcheroo_client_id
=============================

.. c:type:: enum vga_switcheroo_client_id

    client identifier



Constants
---------

:``VGA_SWITCHEROO_UNKNOWN_ID``:
    initial identifier assigned to vga clients.::

            Determining the id requires the handler, so GPUs are given their
            true id in a delayed fashion in :c:func:`vga_switcheroo_enable`

:``VGA_SWITCHEROO_IGD``:
    integrated graphics device

:``VGA_SWITCHEROO_DIS``:
    discrete graphics device

:``VGA_SWITCHEROO_MAX_CLIENTS``:
    currently no more than two GPUs are supported


Description
-----------

Client identifier. Audio clients use the same identifier & 0x100.


.. _`vga_switcheroo_handler`:

struct vga_switcheroo_handler
=============================

.. c:type:: struct vga_switcheroo_handler

    handler callbacks



Definition
----------

.. code-block:: c

  struct vga_switcheroo_handler {
    int (* init) (void);
    int (* switchto) (enum vga_switcheroo_client_id id);
    int (* switch_ddc) (enum vga_switcheroo_client_id id);
    int (* power_state) (enum vga_switcheroo_client_id id,enum vga_switcheroo_state state);
    enum vga_switcheroo_client_id (* get_client_id) (struct pci_dev *pdev);
  };



Members
-------

:``init``:
    initialize handler.::

            Optional. This gets called when vga_switcheroo is enabled, i.e. when
            two vga clients have registered. It allows the handler to perform
            some delayed initialization that depends on the existence of the
            vga clients. Currently only the radeon and amdgpu drivers use this.
            The return value is ignored

:``switchto``:
    switch outputs to given client.::

            Mandatory. For muxless machines this should be a no-op. Returning 0
            denotes success, anything else failure (in which case the switch is
            aborted)

:``switch_ddc``:
    switch DDC lines to given client.::

            Optional. Should return the previous DDC owner on success or a
            negative int on failure

:``power_state``:
    cut or reinstate power of given client.::

            Optional. The return value is ignored

:``get_client_id``:
    determine if given pci device is integrated or discrete GPU.::

            Mandatory



Description
-----------

Handler callbacks. The multiplexer itself. The ``switchto`` and ``get_client_id``
methods are mandatory, all others may be set to NULL.


.. _`vga_switcheroo_client_ops`:

struct vga_switcheroo_client_ops
================================

.. c:type:: struct vga_switcheroo_client_ops

    client callbacks



Definition
----------

.. code-block:: c

  struct vga_switcheroo_client_ops {
    void (* set_gpu_state) (struct pci_dev *dev, enum vga_switcheroo_state);
    void (* reprobe) (struct pci_dev *dev);
    bool (* can_switch) (struct pci_dev *dev);
  };



Members
-------

:``set_gpu_state``:
    do the equivalent of suspend/resume for the card.::

            Mandatory. This should not cut power to the discrete GPU,
            which is the job of the handler

:``reprobe``:
    poll outputs.::

            Optional. This gets called after waking the GPU and switching
            the outputs to it

:``can_switch``:
    check if the device is in a position to switch now.::

            Mandatory. The client should return false if a user space process
            has one of its device files open



Description
-----------

Client callbacks. A client can be either a GPU or an audio device on a GPU.
The ``set_gpu_state`` and ``can_switch`` methods are mandatory, ``reprobe`` may be
set to NULL. For audio clients, the ``reprobe`` member is bogus.

