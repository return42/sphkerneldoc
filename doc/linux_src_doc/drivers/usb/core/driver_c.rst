.. -*- coding: utf-8; mode: rst -*-

========
driver.c
========


.. _`usb_driver_claim_interface`:

usb_driver_claim_interface
==========================

.. c:function:: int usb_driver_claim_interface (struct usb_driver *driver, struct usb_interface *iface, void *priv)

    bind a driver to an interface

    :param struct usb_driver \*driver:
        the driver to be bound

    :param struct usb_interface \*iface:
        the interface to which it will be bound; must be in the
        usb device's active configuration

    :param void \*priv:
        driver data associated with that interface



.. _`usb_driver_claim_interface.description`:

Description
-----------

This is used by usb device drivers that need to claim more than one
interface on a device when probing (audio and acm are current examples).
No device driver should directly modify internal usb_interface or
usb_device structure members.

Few drivers should need to use this routine, since the most natural
way to bind to an interface is to return the private data from
the driver's :c:func:`probe` method.

Callers must own the device lock, so driver :c:func:`probe` entries don't need
extra locking, but other call contexts may need to explicitly claim that
lock.



.. _`usb_driver_claim_interface.return`:

Return
------

0 on success.



.. _`usb_driver_release_interface`:

usb_driver_release_interface
============================

.. c:function:: void usb_driver_release_interface (struct usb_driver *driver, struct usb_interface *iface)

    unbind a driver from an interface

    :param struct usb_driver \*driver:
        the driver to be unbound

    :param struct usb_interface \*iface:
        the interface from which it will be unbound



.. _`usb_driver_release_interface.description`:

Description
-----------

This can be used by drivers to release an interface without waiting
for their :c:func:`disconnect` methods to be called.  In typical cases this
also causes the driver :c:func:`disconnect` method to be called.

This call is synchronous, and may not be used in an interrupt context.
Callers must own the device lock, so driver :c:func:`disconnect` entries don't
need extra locking, but other call contexts may need to explicitly claim
that lock.



.. _`usb_match_id`:

usb_match_id
============

.. c:function:: const struct usb_device_id *usb_match_id (struct usb_interface *interface, const struct usb_device_id *id)

    find first usb_device_id matching device or interface

    :param struct usb_interface \*interface:
        the interface of interest

    :param const struct usb_device_id \*id:
        array of usb_device_id structures, terminated by zero entry



.. _`usb_match_id.description`:

Description
-----------

usb_match_id searches an array of usb_device_id's and returns
the first one matching the device or interface, or null.
This is used when binding (or rebinding) a driver to an interface.
Most USB device drivers will use this indirectly, through the usb core,
but some layered driver frameworks use it directly.
These device tables are exported with MODULE_DEVICE_TABLE, through
modutils, to support the driver loading functionality of USB hotplugging.



.. _`usb_match_id.return`:

Return
------

The first matching usb_device_id, or ``NULL``\ .



.. _`usb_match_id.what-matches`:

What Matches
------------


The "match_flags" element in a usb_device_id controls which
members are used.  If the corresponding bit is set, the
value in the device_id must match its corresponding member
in the device or interface descriptor, or else the device_id
does not match.

"driver_info" is normally used only by device drivers,
but you can create a wildcard "matches anything" usb_device_id
as a driver's "modules.usbmap" entry if you provide an id with
only a nonzero "driver_info" field.  If you do this, the USB device
driver's :c:func:`probe` routine should use additional intelligence to
decide whether to bind to the specified interface.



.. _`usb_match_id.what-makes-good-usb_device_id-tables`:

What Makes Good usb_device_id Tables
------------------------------------


The match algorithm is very simple, so that intelligence in
driver selection must come from smart driver id records.
Unless you have good reasons to use another selection policy,
provide match elements only in related groups, and order match
specifiers from specific to general.  Use the macros provided
for that purpose if you can.

The most specific match specifiers use device descriptor
data.  These are commonly used with product-specific matches;
the USB_DEVICE macro lets you provide vendor and product IDs,
and you can also match against ranges of product revisions.
These are widely used for devices with application or vendor
specific bDeviceClass values.

Matches based on device class/subclass/protocol specifications
are slightly more general; use the USB_DEVICE_INFO macro, or
its siblings.  These are used with single-function devices
where bDeviceClass doesn't specify that each interface has
its own class.

Matches based on interface class/subclass/protocol are the
most general; they let drivers bind to any interface on a
multiple-function device.  Use the USB_INTERFACE_INFO
macro, or its siblings, to match class-per-interface style
devices (as recorded in bInterfaceClass).

Note that an entry created by USB_INTERFACE_INFO won't match
any interface if the device class is set to Vendor-Specific.
This is deliberate; according to the USB spec the meanings of
the interface class/subclass/protocol for these devices are also
vendor-specific, and hence matching against a standard product
class wouldn't work anyway.  If you really want to use an
interface-based match for such a device, create a match record
that also specifies the vendor ID.  (Unforunately there isn't a
standard macro for creating records like this.)

Within those groups, remember that not all combinations are
meaningful.  For example, don't give a product version range
without vendor and product IDs; or specify a protocol without
its associated class and subclass.



.. _`usb_register_device_driver`:

usb_register_device_driver
==========================

.. c:function:: int usb_register_device_driver (struct usb_device_driver *new_udriver, struct module *owner)

    register a USB device (not interface) driver

    :param struct usb_device_driver \*new_udriver:
        USB operations for the device driver

    :param struct module \*owner:
        module owner of this driver.



.. _`usb_register_device_driver.description`:

Description
-----------

Registers a USB device driver with the USB core.  The list of
unattached devices will be rescanned whenever a new driver is
added, allowing the new driver to attach to any recognized devices.



.. _`usb_register_device_driver.return`:

Return
------

A negative error code on failure and 0 on success.



.. _`usb_deregister_device_driver`:

usb_deregister_device_driver
============================

.. c:function:: void usb_deregister_device_driver (struct usb_device_driver *udriver)

    unregister a USB device (not interface) driver

    :param struct usb_device_driver \*udriver:
        USB operations of the device driver to unregister



.. _`usb_deregister_device_driver.context`:

Context
-------

must be able to sleep



.. _`usb_deregister_device_driver.description`:

Description
-----------

Unlinks the specified driver from the internal USB driver list.



.. _`usb_register_driver`:

usb_register_driver
===================

.. c:function:: int usb_register_driver (struct usb_driver *new_driver, struct module *owner, const char *mod_name)

    register a USB interface driver

    :param struct usb_driver \*new_driver:
        USB operations for the interface driver

    :param struct module \*owner:
        module owner of this driver.

    :param const char \*mod_name:
        module name string



.. _`usb_register_driver.description`:

Description
-----------

Registers a USB interface driver with the USB core.  The list of
unattached interfaces will be rescanned whenever a new driver is
added, allowing the new driver to attach to any recognized interfaces.



.. _`usb_register_driver.return`:

Return
------

A negative error code on failure and 0 on success.



.. _`usb_register_driver.note`:

NOTE
----

if you want your driver to use the USB major number, you must call
:c:func:`usb_register_dev` to enable that functionality.  This function no longer
takes care of that.



.. _`usb_deregister`:

usb_deregister
==============

.. c:function:: void usb_deregister (struct usb_driver *driver)

    unregister a USB interface driver

    :param struct usb_driver \*driver:
        USB operations of the interface driver to unregister



.. _`usb_deregister.context`:

Context
-------

must be able to sleep



.. _`usb_deregister.description`:

Description
-----------

Unlinks the specified driver from the internal USB driver list.



.. _`usb_deregister.note`:

NOTE
----

If you called :c:func:`usb_register_dev`, you still need to call
:c:func:`usb_deregister_dev` to clean up your driver's allocated minor numbers,
this * call will no longer do it for you.



.. _`usb_suspend_both`:

usb_suspend_both
================

.. c:function:: int usb_suspend_both (struct usb_device *udev, pm_message_t msg)

    suspend a USB device and its interfaces

    :param struct usb_device \*udev:
        the usb_device to suspend

    :param pm_message_t msg:
        Power Management message describing this state transition



.. _`usb_suspend_both.description`:

Description
-----------

This is the central routine for suspending USB devices.  It calls the
suspend methods for all the interface drivers in ``udev`` and then calls
the suspend method for ``udev`` itself.  When the routine is called in
autosuspend, if an error occurs at any stage, all the interfaces
which were suspended are resumed so that they remain in the same
state as the device, but when called from system sleep, all error
from suspend methods of interfaces and the non-root-hub device itself
are simply ignored, so all suspended interfaces are only resumed
to the device's state when ``udev`` is root-hub and its suspend method
returns failure.

Autosuspend requests originating from a child device or an interface
driver may be made without the protection of ``udev``\ 's device lock, but
all other suspend calls will hold the lock.  Usbcore will insure that
method calls do not arrive during bind, unbind, or reset operations.
However drivers must be prepared to handle suspend calls arriving at
unpredictable times.

This routine can run only in process context.



.. _`usb_suspend_both.return`:

Return
------

0 if the suspend succeeded.



.. _`usb_resume_both`:

usb_resume_both
===============

.. c:function:: int usb_resume_both (struct usb_device *udev, pm_message_t msg)

    resume a USB device and its interfaces

    :param struct usb_device \*udev:
        the usb_device to resume

    :param pm_message_t msg:
        Power Management message describing this state transition



.. _`usb_resume_both.description`:

Description
-----------

This is the central routine for resuming USB devices.  It calls the
the resume method for ``udev`` and then calls the resume methods for all
the interface drivers in ``udev``\ .

Autoresume requests originating from a child device or an interface
driver may be made without the protection of ``udev``\ 's device lock, but
all other resume calls will hold the lock.  Usbcore will insure that
method calls do not arrive during bind, unbind, or reset operations.
However drivers must be prepared to handle resume calls arriving at
unpredictable times.

This routine can run only in process context.



.. _`usb_resume_both.return`:

Return
------

0 on success.



.. _`usb_enable_autosuspend`:

usb_enable_autosuspend
======================

.. c:function:: void usb_enable_autosuspend (struct usb_device *udev)

    allow a USB device to be autosuspended

    :param struct usb_device \*udev:
        the USB device which may be autosuspended



.. _`usb_enable_autosuspend.description`:

Description
-----------

This routine allows ``udev`` to be autosuspended.  An autosuspend won't
take place until the autosuspend_delay has elapsed and all the other
necessary conditions are satisfied.

The caller must hold ``udev``\ 's device lock.



.. _`usb_disable_autosuspend`:

usb_disable_autosuspend
=======================

.. c:function:: void usb_disable_autosuspend (struct usb_device *udev)

    prevent a USB device from being autosuspended

    :param struct usb_device \*udev:
        the USB device which may not be autosuspended



.. _`usb_disable_autosuspend.description`:

Description
-----------

This routine prevents ``udev`` from being autosuspended and wakes it up
if it is already autosuspended.

The caller must hold ``udev``\ 's device lock.



.. _`usb_autosuspend_device`:

usb_autosuspend_device
======================

.. c:function:: void usb_autosuspend_device (struct usb_device *udev)

    delayed autosuspend of a USB device and its interfaces

    :param struct usb_device \*udev:
        the usb_device to autosuspend



.. _`usb_autosuspend_device.description`:

Description
-----------

This routine should be called when a core subsystem is finished using
``udev`` and wants to allow it to autosuspend.  Examples would be when
``udev``\ 's device file in usbfs is closed or after a configuration change.

``udev``\ 's usage counter is decremented; if it drops to 0 and all the
interfaces are inactive then a delayed autosuspend will be attempted.
The attempt may fail (see :c:func:`autosuspend_check`).

The caller must hold ``udev``\ 's device lock.

This routine can run only in process context.



.. _`usb_autoresume_device`:

usb_autoresume_device
=====================

.. c:function:: int usb_autoresume_device (struct usb_device *udev)

    immediately autoresume a USB device and its interfaces

    :param struct usb_device \*udev:
        the usb_device to autoresume



.. _`usb_autoresume_device.description`:

Description
-----------

This routine should be called when a core subsystem wants to use ``udev``
and needs to guarantee that it is not suspended.  No autosuspend will
occur until :c:func:`usb_autosuspend_device` is called.  (Note that this will
not prevent suspend events originating in the PM core.)  Examples would
be when ``udev``\ 's device file in usbfs is opened or when a remote-wakeup
request is received.

``udev``\ 's usage counter is incremented to prevent subsequent autosuspends.
However if the autoresume fails then the usage counter is re-decremented.

The caller must hold ``udev``\ 's device lock.

This routine can run only in process context.



.. _`usb_autoresume_device.return`:

Return
------

0 on success. A negative error code otherwise.



.. _`usb_autopm_put_interface`:

usb_autopm_put_interface
========================

.. c:function:: void usb_autopm_put_interface (struct usb_interface *intf)

    decrement a USB interface's PM-usage counter

    :param struct usb_interface \*intf:
        the usb_interface whose counter should be decremented



.. _`usb_autopm_put_interface.description`:

Description
-----------

This routine should be called by an interface driver when it is
finished using ``intf`` and wants to allow it to autosuspend.  A typical
example would be a character-device driver when its device file is
closed.

The routine decrements ``intf``\ 's usage counter.  When the counter reaches
0, a delayed autosuspend request for ``intf``\ 's device is attempted.  The
attempt may fail (see :c:func:`autosuspend_check`).

This routine can run only in process context.



.. _`usb_autopm_put_interface_async`:

usb_autopm_put_interface_async
==============================

.. c:function:: void usb_autopm_put_interface_async (struct usb_interface *intf)

    decrement a USB interface's PM-usage counter

    :param struct usb_interface \*intf:
        the usb_interface whose counter should be decremented



.. _`usb_autopm_put_interface_async.description`:

Description
-----------

This routine does much the same thing as :c:func:`usb_autopm_put_interface`:
It decrements ``intf``\ 's usage counter and schedules a delayed
autosuspend request if the counter is <= 0.  The difference is that it
does not perform any synchronization; callers should hold a private
lock and handle all synchronization issues themselves.

Typically a driver would call this routine during an URB's completion
handler, if no more URBs were pending.

This routine can run in atomic context.



.. _`usb_autopm_put_interface_no_suspend`:

usb_autopm_put_interface_no_suspend
===================================

.. c:function:: void usb_autopm_put_interface_no_suspend (struct usb_interface *intf)

    decrement a USB interface's PM-usage counter

    :param struct usb_interface \*intf:
        the usb_interface whose counter should be decremented



.. _`usb_autopm_put_interface_no_suspend.description`:

Description
-----------

This routine decrements ``intf``\ 's usage counter but does not carry out an
autosuspend.

This routine can run in atomic context.



.. _`usb_autopm_get_interface`:

usb_autopm_get_interface
========================

.. c:function:: int usb_autopm_get_interface (struct usb_interface *intf)

    increment a USB interface's PM-usage counter

    :param struct usb_interface \*intf:
        the usb_interface whose counter should be incremented



.. _`usb_autopm_get_interface.description`:

Description
-----------

This routine should be called by an interface driver when it wants to
use ``intf`` and needs to guarantee that it is not suspended.  In addition,
the routine prevents ``intf`` from being autosuspended subsequently.  (Note
that this will not prevent suspend events originating in the PM core.)
This prevention will persist until :c:func:`usb_autopm_put_interface` is called
or ``intf`` is unbound.  A typical example would be a character-device
driver when its device file is opened.

``intf``\ 's usage counter is incremented to prevent subsequent autosuspends.
However if the autoresume fails then the counter is re-decremented.

This routine can run only in process context.



.. _`usb_autopm_get_interface.return`:

Return
------

0 on success.



.. _`usb_autopm_get_interface_async`:

usb_autopm_get_interface_async
==============================

.. c:function:: int usb_autopm_get_interface_async (struct usb_interface *intf)

    increment a USB interface's PM-usage counter

    :param struct usb_interface \*intf:
        the usb_interface whose counter should be incremented



.. _`usb_autopm_get_interface_async.description`:

Description
-----------

This routine does much the same thing as
:c:func:`usb_autopm_get_interface`: It increments ``intf``\ 's usage counter and
queues an autoresume request if the device is suspended.  The
differences are that it does not perform any synchronization (callers
should hold a private lock and handle all synchronization issues
themselves), and it does not autoresume the device directly (it only
queues a request).  After a successful call, the device may not yet be
resumed.

This routine can run in atomic context.



.. _`usb_autopm_get_interface_async.return`:

Return
------

0 on success. A negative error code otherwise.



.. _`usb_autopm_get_interface_no_resume`:

usb_autopm_get_interface_no_resume
==================================

.. c:function:: void usb_autopm_get_interface_no_resume (struct usb_interface *intf)

    increment a USB interface's PM-usage counter

    :param struct usb_interface \*intf:
        the usb_interface whose counter should be incremented



.. _`usb_autopm_get_interface_no_resume.description`:

Description
-----------

This routine increments ``intf``\ 's usage counter but does not carry out an
autoresume.

This routine can run in atomic context.

