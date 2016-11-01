.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/hub.c

.. _`usb_hub_set_port_power`:

usb_hub_set_port_power
======================

.. c:function:: int usb_hub_set_port_power(struct usb_device *hdev, struct usb_hub *hub, int port1, bool set)

    control hub port's power state

    :param struct usb_device \*hdev:
        USB device belonging to the usb hub

    :param struct usb_hub \*hub:
        target hub

    :param int port1:
        port index

    :param bool set:
        expected status

.. _`usb_hub_set_port_power.description`:

Description
-----------

call this function to control port's power via setting or
clearing the port's PORT_POWER feature.

.. _`usb_hub_set_port_power.return`:

Return
------

0 if successful. A negative error code otherwise.

.. _`usb_hub_clear_tt_buffer`:

usb_hub_clear_tt_buffer
=======================

.. c:function:: int usb_hub_clear_tt_buffer(struct urb *urb)

    clear control/bulk TT state in high speed hub

    :param struct urb \*urb:
        an URB associated with the failed or incomplete split transaction

.. _`usb_hub_clear_tt_buffer.description`:

Description
-----------

High speed HCDs use this to tell the hub driver that some split control or
bulk transaction failed in a way that requires clearing internal state of
a transaction translator.  This is normally detected (and reported) from
interrupt context.

It may not be possible for that hub to handle additional full (or low)
speed transactions until that state is fully cleared out.

.. _`usb_hub_clear_tt_buffer.return`:

Return
------

0 if successful. A negative error code otherwise.

.. _`usb_remove_device`:

usb_remove_device
=================

.. c:function:: int usb_remove_device(struct usb_device *udev)

    disable a device's port on its parent hub

    :param struct usb_device \*udev:
        device to be disabled and removed

.. _`usb_remove_device.context`:

Context
-------

@udev locked, must be able to sleep.

.. _`usb_remove_device.description`:

Description
-----------

After \ ``udev``\ 's port has been disabled, hub_wq is notified and it will
see that the device has been disconnected.  When the device is
physically unplugged and something is plugged in, the events will
be received and processed normally.

.. _`usb_remove_device.return`:

Return
------

0 if successful. A negative error code otherwise.

.. _`usb_set_device_state`:

usb_set_device_state
====================

.. c:function:: void usb_set_device_state(struct usb_device *udev, enum usb_device_state new_state)

    change a device's current state (usbcore, hcds)

    :param struct usb_device \*udev:
        pointer to device whose state should be changed

    :param enum usb_device_state new_state:
        new state value to be stored

.. _`usb_set_device_state.description`:

Description
-----------

udev->state is \_not\_ fully protected by the device lock.  Although
most transitions are made only while holding the lock, the state can
can change to USB_STATE_NOTATTACHED at almost any time.  This
is so that devices can be marked as disconnected as soon as possible,
without having to wait for any semaphores to be released.  As a result,
all changes to any device's state must be protected by the
device_state_lock spinlock.

Once a device has been added to the device tree, all changes to its state
should be made using this routine.  The state should \_not\_ be set directly.

If udev->state is already USB_STATE_NOTATTACHED then no change is made.
Otherwise udev->state is set to new_state, and if new_state is
USB_STATE_NOTATTACHED then all of udev's descendants' states are also set
to USB_STATE_NOTATTACHED.

.. _`usb_disconnect`:

usb_disconnect
==============

.. c:function:: void usb_disconnect(struct usb_device **pdev)

    disconnect a device (usbcore-internal)

    :param struct usb_device \*\*pdev:
        pointer to device being disconnected

.. _`usb_disconnect.context`:

Context
-------

!in_interrupt ()

.. _`usb_disconnect.description`:

Description
-----------

Something got disconnected. Get rid of it and all of its children.

If \*pdev is a normal device then the parent hub must already be locked.
If \*pdev is a root hub then the caller must hold the usb_bus_idr_lock,
which protects the set of root hubs as well as the list of buses.

Only hub drivers (including virtual root hub drivers for host
controllers) should ever call this.

This call is synchronous, and may not be used in an interrupt context.

.. _`usb_enumerate_device_otg`:

usb_enumerate_device_otg
========================

.. c:function:: int usb_enumerate_device_otg(struct usb_device *udev)

    FIXME (usbcore-internal)

    :param struct usb_device \*udev:
        newly addressed device (in ADDRESS state)

.. _`usb_enumerate_device_otg.description`:

Description
-----------

Finish enumeration for On-The-Go devices

.. _`usb_enumerate_device_otg.return`:

Return
------

0 if successful. A negative error code otherwise.

.. _`usb_enumerate_device`:

usb_enumerate_device
====================

.. c:function:: int usb_enumerate_device(struct usb_device *udev)

    Read device configs/intfs/otg (usbcore-internal)

    :param struct usb_device \*udev:
        newly addressed device (in ADDRESS state)

.. _`usb_enumerate_device.description`:

Description
-----------

This is only called by \ :c:func:`usb_new_device`\  and \ :c:func:`usb_authorize_device`\ 
and FIXME -- all comments that apply to them apply here wrt to
environment.

If the device is WUSB and not authorized, we don't attempt to read
the string descriptors, as they will be errored out by the device
until it has been authorized.

.. _`usb_enumerate_device.return`:

Return
------

0 if successful. A negative error code otherwise.

.. _`usb_new_device`:

usb_new_device
==============

.. c:function:: int usb_new_device(struct usb_device *udev)

    perform initial device setup (usbcore-internal)

    :param struct usb_device \*udev:
        newly addressed device (in ADDRESS state)

.. _`usb_new_device.description`:

Description
-----------

This is called with devices which have been detected but not fully
enumerated.  The device descriptor is available, but not descriptors
for any device configuration.  The caller must have locked either
the parent hub (if udev is a normal device) or else the
usb_bus_idr_lock (if udev is a root hub).  The parent's pointer to
udev has already been installed, but udev is not yet visible through
sysfs or other filesystem code.

This call is synchronous, and may not be used in an interrupt context.

Only the hub driver or root-hub registrar should ever call this.

.. _`usb_new_device.return`:

Return
------

Whether the device is configured properly or not. Zero if the
interface was registered with the driver core; else a negative errno
value.

.. _`usb_deauthorize_device`:

usb_deauthorize_device
======================

.. c:function:: int usb_deauthorize_device(struct usb_device *usb_dev)

    deauthorize a device (usbcore-internal)

    :param struct usb_device \*usb_dev:
        USB device

.. _`usb_deauthorize_device.description`:

Description
-----------

Move the USB device to a very basic state where interfaces are disabled
and the device is in fact unconfigured and unusable.

We share a lock (that we have) with \ :c:func:`device_del`\ , so we need to
defer its call.

.. _`usb_deauthorize_device.return`:

Return
------

0.

.. _`usb_root_hub_lost_power`:

usb_root_hub_lost_power
=======================

.. c:function:: void usb_root_hub_lost_power(struct usb_device *rhdev)

    called by HCD if the root hub lost Vbus power

    :param struct usb_device \*rhdev:
        struct usb_device for the root hub

.. _`usb_root_hub_lost_power.description`:

Description
-----------

The USB host controller driver calls this function when its root hub
is resumed and Vbus power has been interrupted or the controller
has been reset.  The routine marks \ ``rhdev``\  as having lost power.
When the hub driver is resumed it will take notice and carry out
power-session recovery for all the "USB-PERSIST"-enabled child devices;
the others will be disconnected.

.. _`usb_reset_and_verify_device`:

usb_reset_and_verify_device
===========================

.. c:function:: int usb_reset_and_verify_device(struct usb_device *udev)

    perform a USB port reset to reinitialize a device

    :param struct usb_device \*udev:
        device to reset (not in SUSPENDED or NOTATTACHED state)

.. _`usb_reset_and_verify_device.description`:

Description
-----------

WARNING - don't use this routine to reset a composite device
(one with multiple interfaces owned by separate drivers)!
Use \ :c:func:`usb_reset_device`\  instead.

Do a port reset, reassign the device's address, and establish its
former operating configuration.  If the reset fails, or the device's
descriptors change from their values before the reset, or the original
configuration and altsettings cannot be restored, a flag will be set
telling hub_wq to pretend the device has been disconnected and then
re-connected.  All drivers will be unbound, and the device will be
re-enumerated and probed all over again.

.. _`usb_reset_and_verify_device.return`:

Return
------

0 if the reset succeeded, -ENODEV if the device has been
flagged for logical disconnection, or some other negative error code
if the reset wasn't even attempted.

.. _`usb_reset_and_verify_device.note`:

Note
----

The caller must own the device lock and the port lock, the latter is
taken by \ :c:func:`usb_reset_device`\ .  For example, it's safe to use
\ :c:func:`usb_reset_device`\  from a driver \ :c:func:`probe`\  routine after downloading
new firmware.  For calls that might not occur during \ :c:func:`probe`\ , drivers
should lock the device using \ :c:func:`usb_lock_device_for_reset`\ .

.. _`usb_reset_and_verify_device.locking-exception`:

Locking exception
-----------------

This routine may also be called from within an
autoresume handler.  Such usage won't conflict with other tasks
holding the device lock because these tasks should always call
\ :c:func:`usb_autopm_resume_device`\ , thereby preventing any unwanted
autoresume.  The autoresume handler is expected to have already
acquired the port lock before calling this routine.

.. _`usb_reset_device`:

usb_reset_device
================

.. c:function:: int usb_reset_device(struct usb_device *udev)

    warn interface drivers and perform a USB port reset

    :param struct usb_device \*udev:
        device to reset (not in SUSPENDED or NOTATTACHED state)

.. _`usb_reset_device.description`:

Description
-----------

Warns all drivers bound to registered interfaces (using their pre_reset
method), performs the port reset, and then lets the drivers know that
the reset is over (using their post_reset method).

.. _`usb_reset_device.return`:

Return
------

The same as for \ :c:func:`usb_reset_and_verify_device`\ .

.. _`usb_reset_device.note`:

Note
----

The caller must own the device lock.  For example, it's safe to use
this from a driver \ :c:func:`probe`\  routine after downloading new firmware.
For calls that might not occur during \ :c:func:`probe`\ , drivers should lock
the device using \ :c:func:`usb_lock_device_for_reset`\ .

If an interface is currently being probed or disconnected, we assume
its driver knows how to handle resets.  For all other interfaces,
if the driver doesn't have pre_reset and post_reset methods then
we attempt to unbind it and rebind afterward.

.. _`usb_queue_reset_device`:

usb_queue_reset_device
======================

.. c:function:: void usb_queue_reset_device(struct usb_interface *iface)

    Reset a USB device from an atomic context

    :param struct usb_interface \*iface:
        USB interface belonging to the device to reset

.. _`usb_queue_reset_device.description`:

Description
-----------

This function can be used to reset a USB device from an atomic
context, where \ :c:func:`usb_reset_device`\  won't work (as it blocks).

Doing a reset via this method is functionally equivalent to calling
\ :c:func:`usb_reset_device`\ , except for the fact that it is delayed to a
workqueue. This means that any drivers bound to other interfaces
might be unbound, as well as users from usbfs in user space.

.. _`usb_queue_reset_device.corner-cases`:

Corner cases
------------


- Scheduling two resets at the same time from two different drivers
attached to two different interfaces of the same device is
possible; depending on how the driver attached to each interface
handles ->pre_reset(), the second reset might happen or not.

- If the reset is delayed so long that the interface is unbound from
its driver, the reset will be skipped.

- This function can be called during .probe().  It can also be called
during .disconnect(), but doing so is pointless because the reset
will not occur.  If you really want to reset the device during
.disconnect(), call \ :c:func:`usb_reset_device`\  directly -- but watch out
for nested unbinding issues!

.. _`usb_hub_find_child`:

usb_hub_find_child
==================

.. c:function:: struct usb_device *usb_hub_find_child(struct usb_device *hdev, int port1)

    Get the pointer of child device attached to the port which is specified by \ ``port1``\ .

    :param struct usb_device \*hdev:
        USB device belonging to the usb hub

    :param int port1:
        port num to indicate which port the child device
        is attached to.

.. _`usb_hub_find_child.description`:

Description
-----------

USB drivers call this function to get hub's child device
pointer.

.. _`usb_hub_find_child.return`:

Return
------

%NULL if input param is invalid and
child's usb_device pointer if non-NULL.

.. _`usb_get_hub_port_acpi_handle`:

usb_get_hub_port_acpi_handle
============================

.. c:function:: acpi_handle usb_get_hub_port_acpi_handle(struct usb_device *hdev, int port1)

    Get the usb port's acpi handle

    :param struct usb_device \*hdev:
        USB device belonging to the usb hub

    :param int port1:
        port num of the port

.. _`usb_get_hub_port_acpi_handle.return`:

Return
------

Port's acpi handle if successful, \ ``NULL``\  if params are
invalid.

.. This file was automatic generated / don't edit.

