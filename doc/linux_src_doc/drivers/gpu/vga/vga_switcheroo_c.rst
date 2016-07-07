.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/vga/vga_switcheroo.c

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
    }

.. _`vga_switcheroo_client.members`:

Members
-------

pdev
    client pci device

fb_info
    framebuffer to which console is remapped on switching

pwr_state
    current power state

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

.. _`vga_switcheroo_client.description`:

Description
-----------

Registered client. A client can be either a GPU or an audio device on a GPU.
For audio clients, the \ ``fb_info``\ , \ ``active``\  and \ ``driver_power_control``\  members
are bogus.

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

    :param const struct vga_switcheroo_handler \*handler:
        handler callbacks

    :param enum vga_switcheroo_handler_flags_t handler_flags:
        handler flags

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

    :param  void:
        no arguments

.. _`vga_switcheroo_unregister_handler.description`:

Description
-----------

Unregister handler. Disable vga_switcheroo.

.. _`vga_switcheroo_handler_flags`:

vga_switcheroo_handler_flags
============================

.. c:function:: enum vga_switcheroo_handler_flags_t vga_switcheroo_handler_flags( void)

    obtain handler flags

    :param  void:
        no arguments

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

    :param struct pci_dev \*pdev:
        client pci device

    :param const struct vga_switcheroo_client_ops \*ops:
        client callbacks

    :param bool driver_power_control:
        whether power state is controlled by the driver's
        runtime pm

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

.. c:function:: int vga_switcheroo_register_audio_client(struct pci_dev *pdev, const struct vga_switcheroo_client_ops *ops, enum vga_switcheroo_client_id id)

    register audio client

    :param struct pci_dev \*pdev:
        client pci device

    :param const struct vga_switcheroo_client_ops \*ops:
        client callbacks

    :param enum vga_switcheroo_client_id id:
        client identifier

.. _`vga_switcheroo_register_audio_client.description`:

Description
-----------

Register audio client (audio device on a GPU). The power state of the
client is assumed to be ON. Beforehand, \ :c:func:`vga_switcheroo_client_probe_defer`\ 
shall be called to ensure that all prerequisites are met.

.. _`vga_switcheroo_register_audio_client.return`:

Return
------

0 on success, -ENOMEM on memory allocation error.

.. _`vga_switcheroo_client_probe_defer`:

vga_switcheroo_client_probe_defer
=================================

.. c:function:: bool vga_switcheroo_client_probe_defer(struct pci_dev *pdev)

    whether to defer probing a given client

    :param struct pci_dev \*pdev:
        client pci device

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

    :param struct pci_dev \*pdev:
        client pci device

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

    :param struct pci_dev \*pdev:
        client pci device

.. _`vga_switcheroo_unregister_client.description`:

Description
-----------

Unregister client. Disable vga_switcheroo if this is a vga client (GPU).

.. _`vga_switcheroo_client_fb_set`:

vga_switcheroo_client_fb_set
============================

.. c:function:: void vga_switcheroo_client_fb_set(struct pci_dev *pdev, struct fb_info *info)

    set framebuffer of a given client

    :param struct pci_dev \*pdev:
        client pci device

    :param struct fb_info \*info:
        framebuffer

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

    :param struct pci_dev \*pdev:
        client pci device

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

    :param struct pci_dev \*pdev:
        client pci device

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

.. _`vga_switcheroo_process_delayed_switch`:

vga_switcheroo_process_delayed_switch
=====================================

.. c:function:: int vga_switcheroo_process_delayed_switch( void)

    helper for delayed switching

    :param  void:
        no arguments

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

.. _`vga_switcheroo_set_dynamic_switch`:

vga_switcheroo_set_dynamic_switch
=================================

.. c:function:: void vga_switcheroo_set_dynamic_switch(struct pci_dev *pdev, enum vga_switcheroo_state dynamic)

    helper for driver power control

    :param struct pci_dev \*pdev:
        client pci device

    :param enum vga_switcheroo_state dynamic:
        new power state

.. _`vga_switcheroo_set_dynamic_switch.description`:

Description
-----------

Helper for GPUs whose power state is controlled by the driver's runtime pm.
When the driver decides to power up or down, it notifies vga_switcheroo
thereof using this helper so that it can (a) power the audio device on
the GPU up or down, and (b) update its internal power state representation
for the device.

.. _`vga_switcheroo_init_domain_pm_ops`:

vga_switcheroo_init_domain_pm_ops
=================================

.. c:function:: int vga_switcheroo_init_domain_pm_ops(struct device *dev, struct dev_pm_domain *domain)

    helper for driver power control

    :param struct device \*dev:
        vga client device

    :param struct dev_pm_domain \*domain:
        power domain

.. _`vga_switcheroo_init_domain_pm_ops.description`:

Description
-----------

Helper for GPUs whose power state is controlled by the driver's runtime pm.
After the GPU has been suspended, the handler needs to be called to cut
power to the GPU. Likewise it needs to reinstate power before the GPU
can resume. To this end, this helper augments the suspend/resume functions
by the requisite calls to the handler. It needs only be called on platforms
where the power switch is separate to the device being powered down.

.. _`vga_switcheroo_init_domain_pm_optimus_hdmi_audio`:

vga_switcheroo_init_domain_pm_optimus_hdmi_audio
================================================

.. c:function:: int vga_switcheroo_init_domain_pm_optimus_hdmi_audio(struct device *dev, struct dev_pm_domain *domain)

    helper for driver power control

    :param struct device \*dev:
        audio client device

    :param struct dev_pm_domain \*domain:
        power domain

.. _`vga_switcheroo_init_domain_pm_optimus_hdmi_audio.description`:

Description
-----------

Helper for GPUs whose power state is controlled by the driver's runtime pm.
When the audio device resumes, the GPU needs to be woken. This helper
augments the audio device's resume function to do that.

.. _`vga_switcheroo_init_domain_pm_optimus_hdmi_audio.return`:

Return
------

0 on success, -EINVAL if no power management operations are
defined for this device.

.. This file was automatic generated / don't edit.

