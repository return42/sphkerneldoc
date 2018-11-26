.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/vga/vga_switcheroo.c

.. _`overview`:

Overview
========

vga_switcheroo is the Linux subsystem for laptop hybrid graphics.
These come in two flavors:

* muxed: Dual GPUs with a multiplexer chip to switch outputs between GPUs.
* muxless: Dual GPUs but only one of them is connected to outputs.
  The other one is merely used to offload rendering, its results
  are copied over PCIe into the framebuffer. On Linux this is
  supported with DRI PRIME.

Hybrid graphics started to appear in the late Naughties and were initially
all muxed. Newer laptops moved to a muxless architecture for cost reasons.
A notable exception is the MacBook Pro which continues to use a mux.
Muxes come with varying capabilities: Some switch only the panel, others
can also switch external displays. Some switch all display pins at once
while others can switch just the DDC lines. (To allow EDID probing
for the inactive GPU.) Also, muxes are often used to cut power to the
discrete GPU while it is not used.

DRM drivers register GPUs with vga_switcheroo, these are henceforth called
clients. The mux is called the handler. Muxless machines also register a
handler to control the power state of the discrete GPU, its ->switchto
callback is a no-op for obvious reasons. The discrete GPU is often equipped
with an HDA controller for the HDMI/DP audio signal, this will also
register as a client so that vga_switcheroo can take care of the correct
suspend/resume order when changing the discrete GPU's power state. In total
there can thus be up to three clients: Two vga clients (GPUs) and one audio
client (on the discrete GPU). The code is mostly prepared to support
machines with more than two GPUs should they become available.

The GPU to which the outputs are currently switched is called the
active client in vga_switcheroo parlance. The GPU not in use is the
inactive client. When the inactive client's DRM driver is loaded,
it will be unable to probe the panel's EDID and hence depends on
VBIOS to provide its display modes. If the VBIOS modes are bogus or
if there is no VBIOS at all (which is common on the MacBook Pro),
a client may alternatively request that the DDC lines are temporarily
switched to it, provided that the handler supports this. Switching
only the DDC lines and not the entire output avoids unnecessary
flickering.

.. _`vga_switcheroo_client`:

struct vga_switcheroo_client
============================

.. c:type:: struct vga_switcheroo_client

    registered client

.. _`vga_switcheroo_client.definition`:

Definition
----------

.. code-block:: c

    struct vga_switcheroo_client {
        struct pci_dev *pdev;
        struct fb_info *fb_info;
        enum vga_switcheroo_state pwr_state;
        const struct vga_switcheroo_client_ops *ops;
        enum vga_switcheroo_client_id id;
        bool active;
        bool driver_power_control;
        struct list_head list;
        struct pci_dev *vga_dev;
    }

.. _`vga_switcheroo_client.members`:

Members
-------

pdev
    client pci device

fb_info
    framebuffer to which console is remapped on switching

pwr_state
    current power state if manual power control is used.
    For driver power control, call \ :c:func:`vga_switcheroo_pwr_state`\ .

ops
    client callbacks

id
    client identifier. Determining the id requires the handler,
    so gpus are initially assigned VGA_SWITCHEROO_UNKNOWN_ID
    and later given their true id in \ :c:func:`vga_switcheroo_enable`\ 

active
    whether the outputs are currently switched to this client

driver_power_control
    whether power state is controlled by the driver's
    runtime pm. If true, writing ON and OFF to the vga_switcheroo debugfs
    interface is a no-op so as not to interfere with runtime pm

list
    client list

vga_dev
    pci device, indicate which GPU is bound to current audio client

.. _`vga_switcheroo_client.description`:

Description
-----------

Registered client. A client can be either a GPU or an audio device on a GPU.
For audio clients, the \ ``fb_info``\  and \ ``active``\  members are bogus. For GPU
clients, the \ ``vga_dev``\  is bogus.

.. _`vgasr_priv`:

struct vgasr_priv
=================

.. c:type:: struct vgasr_priv

    vga_switcheroo private data

.. _`vgasr_priv.definition`:

Definition
----------

.. code-block:: c

    struct vgasr_priv {
        bool active;
        bool delayed_switch_active;
        enum vga_switcheroo_client_id delayed_client_id;
        struct dentry *debugfs_root;
        struct dentry *switch_file;
        int registered_clients;
        struct list_head clients;
        const struct vga_switcheroo_handler *handler;
        enum vga_switcheroo_handler_flags_t handler_flags;
        struct mutex mux_hw_lock;
        int old_ddc_owner;
    }

.. _`vgasr_priv.members`:

Members
-------

active
    whether vga_switcheroo is enabled.
    Prerequisite is the registration of two GPUs and a handler

delayed_switch_active
    whether a delayed switch is pending

delayed_client_id
    client to which a delayed switch is pending

debugfs_root
    directory for vga_switcheroo debugfs interface

switch_file
    file for vga_switcheroo debugfs interface

registered_clients
    number of registered GPUs
    (counting only vga clients, not audio clients)

clients
    list of registered clients

handler
    registered handler

handler_flags
    flags of registered handler

mux_hw_lock
    protects mux state
    (in particular while DDC lines are temporarily switched)

old_ddc_owner
    client to which DDC lines will be switched back on unlock

.. _`vgasr_priv.description`:

Description
-----------

vga_switcheroo private data. Currently only one vga_switcheroo instance
per system is supported.

.. _`vga_switcheroo_register_handler`:

vga_switcheroo_register_handler
===============================

.. c:function:: int vga_switcheroo_register_handler(const struct vga_switcheroo_handler *handler, enum vga_switcheroo_handler_flags_t handler_flags)

    register handler

    :param handler:
        handler callbacks
    :type handler: const struct vga_switcheroo_handler \*

    :param handler_flags:
        handler flags
    :type handler_flags: enum vga_switcheroo_handler_flags_t

.. _`vga_switcheroo_register_handler.description`:

Description
-----------

Register handler. Enable vga_switcheroo if two vga clients have already
registered.

.. _`vga_switcheroo_register_handler.return`:

Return
------

0 on success, -EINVAL if a handler was already registered.

.. _`vga_switcheroo_unregister_handler`:

vga_switcheroo_unregister_handler
=================================

.. c:function:: void vga_switcheroo_unregister_handler( void)

    unregister handler

    :param void:
        no arguments
    :type void: 

.. _`vga_switcheroo_unregister_handler.description`:

Description
-----------

Unregister handler. Disable vga_switcheroo.

.. _`vga_switcheroo_handler_flags`:

vga_switcheroo_handler_flags
============================

.. c:function:: enum vga_switcheroo_handler_flags_t vga_switcheroo_handler_flags( void)

    obtain handler flags

    :param void:
        no arguments
    :type void: 

.. _`vga_switcheroo_handler_flags.description`:

Description
-----------

Helper for clients to obtain the handler flags bitmask.

.. _`vga_switcheroo_handler_flags.return`:

Return
------

Handler flags. A value of 0 means that no handler is registered
or that the handler has no special capabilities.

.. _`vga_switcheroo_register_client`:

vga_switcheroo_register_client
==============================

.. c:function:: int vga_switcheroo_register_client(struct pci_dev *pdev, const struct vga_switcheroo_client_ops *ops, bool driver_power_control)

    register vga client

    :param pdev:
        client pci device
    :type pdev: struct pci_dev \*

    :param ops:
        client callbacks
    :type ops: const struct vga_switcheroo_client_ops \*

    :param driver_power_control:
        whether power state is controlled by the driver's
        runtime pm
    :type driver_power_control: bool

.. _`vga_switcheroo_register_client.description`:

Description
-----------

Register vga client (GPU). Enable vga_switcheroo if another GPU and a
handler have already registered. The power state of the client is assumed
to be ON. Beforehand, \ :c:func:`vga_switcheroo_client_probe_defer`\  shall be called
to ensure that all prerequisites are met.

.. _`vga_switcheroo_register_client.return`:

Return
------

0 on success, -ENOMEM on memory allocation error.

.. _`vga_switcheroo_register_audio_client`:

vga_switcheroo_register_audio_client
====================================

.. c:function:: int vga_switcheroo_register_audio_client(struct pci_dev *pdev, const struct vga_switcheroo_client_ops *ops, struct pci_dev *vga_dev)

    register audio client

    :param pdev:
        client pci device
    :type pdev: struct pci_dev \*

    :param ops:
        client callbacks
    :type ops: const struct vga_switcheroo_client_ops \*

    :param vga_dev:
        pci device which is bound to current audio client
    :type vga_dev: struct pci_dev \*

.. _`vga_switcheroo_register_audio_client.description`:

Description
-----------

Register audio client (audio device on a GPU). The client is assumed
to use runtime PM. Beforehand, \ :c:func:`vga_switcheroo_client_probe_defer`\ 
shall be called to ensure that all prerequisites are met.

.. _`vga_switcheroo_register_audio_client.return`:

Return
------

0 on success, -ENOMEM on memory allocation error, -EINVAL on getting
client id error.

.. _`vga_switcheroo_client_probe_defer`:

vga_switcheroo_client_probe_defer
=================================

.. c:function:: bool vga_switcheroo_client_probe_defer(struct pci_dev *pdev)

    whether to defer probing a given client

    :param pdev:
        client pci device
    :type pdev: struct pci_dev \*

.. _`vga_switcheroo_client_probe_defer.description`:

Description
-----------

Determine whether any prerequisites are not fulfilled to probe a given
client. Drivers shall invoke this early on in their ->probe callback
and return \ ``-EPROBE_DEFER``\  if it evaluates to \ ``true``\ . Thou shalt not
register the client ere thou hast called this.

.. _`vga_switcheroo_client_probe_defer.return`:

Return
------

\ ``true``\  if probing should be deferred, otherwise \ ``false``\ .

.. _`vga_switcheroo_get_client_state`:

vga_switcheroo_get_client_state
===============================

.. c:function:: enum vga_switcheroo_state vga_switcheroo_get_client_state(struct pci_dev *pdev)

    obtain power state of a given client

    :param pdev:
        client pci device
    :type pdev: struct pci_dev \*

.. _`vga_switcheroo_get_client_state.description`:

Description
-----------

Obtain power state of a given client as seen from vga_switcheroo.
The function is only called from hda_intel.c.

.. _`vga_switcheroo_get_client_state.return`:

Return
------

Power state.

.. _`vga_switcheroo_unregister_client`:

vga_switcheroo_unregister_client
================================

.. c:function:: void vga_switcheroo_unregister_client(struct pci_dev *pdev)

    unregister client

    :param pdev:
        client pci device
    :type pdev: struct pci_dev \*

.. _`vga_switcheroo_unregister_client.description`:

Description
-----------

Unregister client. Disable vga_switcheroo if this is a vga client (GPU).

.. _`vga_switcheroo_client_fb_set`:

vga_switcheroo_client_fb_set
============================

.. c:function:: void vga_switcheroo_client_fb_set(struct pci_dev *pdev, struct fb_info *info)

    set framebuffer of a given client

    :param pdev:
        client pci device
    :type pdev: struct pci_dev \*

    :param info:
        framebuffer
    :type info: struct fb_info \*

.. _`vga_switcheroo_client_fb_set.description`:

Description
-----------

Set framebuffer of a given client. The console will be remapped to this
on switching.

.. _`vga_switcheroo_lock_ddc`:

vga_switcheroo_lock_ddc
=======================

.. c:function:: int vga_switcheroo_lock_ddc(struct pci_dev *pdev)

    temporarily switch DDC lines to a given client

    :param pdev:
        client pci device
    :type pdev: struct pci_dev \*

.. _`vga_switcheroo_lock_ddc.description`:

Description
-----------

Temporarily switch DDC lines to the client identified by \ ``pdev``\ 
(but leave the outputs otherwise switched to where they are).
This allows the inactive client to probe EDID. The DDC lines must
afterwards be switched back by calling \ :c:func:`vga_switcheroo_unlock_ddc`\ ,
even if this function returns an error.

.. _`vga_switcheroo_lock_ddc.return`:

Return
------

Previous DDC owner on success or a negative int on error.
Specifically, \ ``-ENODEV``\  if no handler has registered or if the handler
does not support switching the DDC lines. Also, a negative value
returned by the handler is propagated back to the caller.
The return value has merely an informational purpose for any caller
which might be interested in it. It is acceptable to ignore the return
value and simply rely on the result of the subsequent EDID probe,
which will be \ ``NULL``\  if DDC switching failed.

.. _`vga_switcheroo_unlock_ddc`:

vga_switcheroo_unlock_ddc
=========================

.. c:function:: int vga_switcheroo_unlock_ddc(struct pci_dev *pdev)

    switch DDC lines back to previous owner

    :param pdev:
        client pci device
    :type pdev: struct pci_dev \*

.. _`vga_switcheroo_unlock_ddc.description`:

Description
-----------

Switch DDC lines back to the previous owner after calling
\ :c:func:`vga_switcheroo_lock_ddc`\ . This must be called even if
\ :c:func:`vga_switcheroo_lock_ddc`\  returned an error.

.. _`vga_switcheroo_unlock_ddc.return`:

Return
------

Previous DDC owner on success (i.e. the client identifier of \ ``pdev``\ )
or a negative int on error.
Specifically, \ ``-ENODEV``\  if no handler has registered or if the handler
does not support switching the DDC lines. Also, a negative value
returned by the handler is propagated back to the caller.
Finally, invoking this function without calling \ :c:func:`vga_switcheroo_lock_ddc`\ 
first is not allowed and will result in \ ``-EINVAL``\ .

.. _`manual-switching-and-manual-power-control`:

Manual switching and manual power control
=========================================

In this mode of use, the file /sys/kernel/debug/vgaswitcheroo/switch
can be read to retrieve the current vga_switcheroo state and commands
can be written to it to change the state. The file appears as soon as
two GPU drivers and one handler have registered with vga_switcheroo.
The following commands are understood:

* OFF: Power off the device not in use.
* ON: Power on the device not in use.
* IGD: Switch to the integrated graphics device.
  Power on the integrated GPU if necessary, power off the discrete GPU.
  Prerequisite is that no user space processes (e.g. Xorg, alsactl)
  have opened device files of the GPUs or the audio client. If the
  switch fails, the user may invoke lsof(8) or fuser(1) on /dev/dri/
  and /dev/snd/controlC1 to identify processes blocking the switch.
* DIS: Switch to the discrete graphics device.
* DIGD: Delayed switch to the integrated graphics device.
  This will perform the switch once the last user space process has
  closed the device files of the GPUs and the audio client.
* DDIS: Delayed switch to the discrete graphics device.
* MIGD: Mux-only switch to the integrated graphics device.
  Does not remap console or change the power state of either gpu.
  If the integrated GPU is currently off, the screen will turn black.
  If it is on, the screen will show whatever happens to be in VRAM.
  Either way, the user has to blindly enter the command to switch back.
* MDIS: Mux-only switch to the discrete graphics device.

For GPUs whose power state is controlled by the driver's runtime pm,
the ON and OFF commands are a no-op (see next section).

For muxless machines, the IGD/DIS, DIGD/DDIS and MIGD/MDIS commands
should not be used.

.. _`vga_switcheroo_process_delayed_switch`:

vga_switcheroo_process_delayed_switch
=====================================

.. c:function:: int vga_switcheroo_process_delayed_switch( void)

    helper for delayed switching

    :param void:
        no arguments
    :type void: 

.. _`vga_switcheroo_process_delayed_switch.description`:

Description
-----------

Process a delayed switch if one is pending. DRM drivers should call this
from their ->lastclose callback.

.. _`vga_switcheroo_process_delayed_switch.return`:

Return
------

0 on success. -EINVAL if no delayed switch is pending, if the client
has unregistered in the meantime or if there are other clients blocking the
switch. If the actual switch fails, an error is reported and 0 is returned.

.. _`driver-power-control`:

Driver power control
====================

In this mode of use, the discrete GPU automatically powers up and down at
the discretion of the driver's runtime pm. On muxed machines, the user may
still influence the muxer state by way of the debugfs interface, however
the ON and OFF commands become a no-op for the discrete GPU.

This mode is the default on Nvidia HybridPower/Optimus and ATI PowerXpress.
Specifying nouveau.runpm=0, radeon.runpm=0 or amdgpu.runpm=0 on the kernel
command line disables it.

After the GPU has been suspended, the handler needs to be called to cut
power to the GPU. Likewise it needs to reinstate power before the GPU
can resume. This is achieved by \ :c:func:`vga_switcheroo_init_domain_pm_ops`\ ,
which augments the GPU's suspend/resume functions by the requisite
calls to the handler.

When the audio device resumes, the GPU needs to be woken. This is achieved
by a PCI quirk which calls \ :c:func:`device_link_add`\  to declare a dependency on the
GPU. That way, the GPU is kept awake whenever and as long as the audio
device is in use.

On muxed machines, if the mux is initially switched to the discrete GPU,
the user ends up with a black screen when the GPU powers down after boot.
As a workaround, the mux is forced to the integrated GPU on runtime suspend,
cf. https://bugs.freedesktop.org/show_bug.cgi?id=75917

.. _`vga_switcheroo_init_domain_pm_ops`:

vga_switcheroo_init_domain_pm_ops
=================================

.. c:function:: int vga_switcheroo_init_domain_pm_ops(struct device *dev, struct dev_pm_domain *domain)

    helper for driver power control

    :param dev:
        vga client device
    :type dev: struct device \*

    :param domain:
        power domain
    :type domain: struct dev_pm_domain \*

.. _`vga_switcheroo_init_domain_pm_ops.description`:

Description
-----------

Helper for GPUs whose power state is controlled by the driver's runtime pm.
After the GPU has been suspended, the handler needs to be called to cut
power to the GPU. Likewise it needs to reinstate power before the GPU
can resume. To this end, this helper augments the suspend/resume functions
by the requisite calls to the handler. It needs only be called on platforms
where the power switch is separate to the device being powered down.

.. This file was automatic generated / don't edit.

