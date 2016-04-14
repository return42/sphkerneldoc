.. -*- coding: utf-8; mode: rst -*-

=====
hcd.c
=====

.. _`ascii2desc`:

ascii2desc
==========

.. c:function:: unsigned ascii2desc (char const *s, u8 *buf, unsigned len)

    Helper routine for producing UTF-16LE string descriptors

    :param char const \*s:
        Null-terminated ASCII (actually ISO-8859-1) string

    :param u8 \*buf:
        Buffer for USB string descriptor (header + UTF-16LE)

    :param unsigned len:
        Length (in bytes; may be odd) of descriptor buffer.


.. _`ascii2desc.description`:

Description
-----------

Return: The number of bytes filled in: 2 + 2\\*strlen(s) or ``len``\ ,
whichever is less.

Note:
USB String descriptors can contain at most 126 characters; input
strings longer than that are truncated.


.. _`rh_string`:

rh_string
=========

.. c:function:: unsigned rh_string (int id, struct usb_hcd const *hcd, u8 *data, unsigned len)

    provides string descriptors for root hub

    :param int id:
        the string ID number (0: langids, 1: serial #, 2: product, 3: vendor)

    :param struct usb_hcd const \*hcd:
        the host controller for this root hub

    :param u8 \*data:
        buffer for output packet

    :param unsigned len:
        length of the provided buffer


.. _`rh_string.description`:

Description
-----------

Produces either a manufacturer, product or serial number string for the
virtual root hub device.

Return: The number of bytes filled in: the length of the descriptor or
of the provided buffer, whichever is less.


.. _`usb_bus_init`:

usb_bus_init
============

.. c:function:: void usb_bus_init (struct usb_bus *bus)

    shared initialization code

    :param struct usb_bus \*bus:
        the bus structure being initialized


.. _`usb_bus_init.description`:

Description
-----------

This code is used to initialize a usb_bus structure, memory for which is
separately managed.


.. _`usb_register_bus`:

usb_register_bus
================

.. c:function:: int usb_register_bus (struct usb_bus *bus)

    registers the USB host controller with the usb core

    :param struct usb_bus \*bus:
        pointer to the bus to register
        Context: !:c:func:`in_interrupt`


.. _`usb_register_bus.description`:

Description
-----------

Assigns a bus number, and links the controller into usbcore data
structures so that it can be seen by scanning the bus list.

Return: 0 if successful. A negative error code otherwise.


.. _`usb_deregister_bus`:

usb_deregister_bus
==================

.. c:function:: void usb_deregister_bus (struct usb_bus *bus)

    deregisters the USB host controller

    :param struct usb_bus \*bus:
        pointer to the bus to deregister
        Context: !:c:func:`in_interrupt`


.. _`usb_deregister_bus.description`:

Description
-----------

Recycles the bus number, and unlinks the controller from usbcore data
structures so that it won't be seen by scanning the bus list.


.. _`register_root_hub`:

register_root_hub
=================

.. c:function:: int register_root_hub (struct usb_hcd *hcd)

    called by usb_add_hcd() to register a root hub

    :param struct usb_hcd \*hcd:
        host controller for this root hub


.. _`register_root_hub.description`:

Description
-----------

This function registers the root hub with the USB subsystem.  It sets up
the device properly in the device tree and then calls :c:func:`usb_new_device`
to register the usb device.  It also assigns the root hub's USB address
(always 1).

Return: 0 if successful. A negative error code otherwise.


.. _`usb_calc_bus_time`:

usb_calc_bus_time
=================

.. c:function:: long usb_calc_bus_time (int speed, int is_input, int isoc, int bytecount)

    approximate periodic transaction time in nanoseconds

    :param int speed:
        from dev->speed; USB_SPEED_{LOW,FULL,HIGH}

    :param int is_input:
        true iff the transaction sends data to the host

    :param int isoc:
        true for isochronous transactions, false for interrupt ones

    :param int bytecount:
        how many bytes in the transaction.


.. _`usb_calc_bus_time.description`:

Description
-----------

Return: Approximate bus time in nanoseconds for a periodic transaction.

Note:
See USB 2.0 spec section 5.11.3; only periodic transfers need to be
scheduled in software, this function is only used for such scheduling.


.. _`usb_hcd_link_urb_to_ep`:

usb_hcd_link_urb_to_ep
======================

.. c:function:: int usb_hcd_link_urb_to_ep (struct usb_hcd *hcd, struct urb *urb)

    add an URB to its endpoint queue

    :param struct usb_hcd \*hcd:
        host controller to which ``urb`` was submitted

    :param struct urb \*urb:
        URB being submitted


.. _`usb_hcd_link_urb_to_ep.description`:

Description
-----------

Host controller drivers should call this routine in their :c:func:`enqueue`
method.  The HCD's private spinlock must be held and interrupts must
be disabled.  The actions carried out here are required for URB
submission, as well as for endpoint shutdown and for usb_kill_urb.

Return: 0 for no error, otherwise a negative error code (in which case
the :c:func:`enqueue` method must fail).  If no error occurs but :c:func:`enqueue` fails
anyway, it must call :c:func:`usb_hcd_unlink_urb_from_ep` before releasing
the private spinlock and returning.


.. _`usb_hcd_check_unlink_urb`:

usb_hcd_check_unlink_urb
========================

.. c:function:: int usb_hcd_check_unlink_urb (struct usb_hcd *hcd, struct urb *urb, int status)

    check whether an URB may be unlinked

    :param struct usb_hcd \*hcd:
        host controller to which ``urb`` was submitted

    :param struct urb \*urb:
        URB being checked for unlinkability

    :param int status:
        error code to store in ``urb`` if the unlink succeeds


.. _`usb_hcd_check_unlink_urb.description`:

Description
-----------

Host controller drivers should call this routine in their :c:func:`dequeue`
method.  The HCD's private spinlock must be held and interrupts must
be disabled.  The actions carried out here are required for making
sure than an unlink is valid.

Return: 0 for no error, otherwise a negative error code (in which case
the :c:func:`dequeue` method must fail).  The possible error codes are::

        -EIDRM: ``urb`` was not submitted or has already completed.
                The completion function may not have been called yet.

        -EBUSY: ``urb`` has already been unlinked.


.. _`usb_hcd_unlink_urb_from_ep`:

usb_hcd_unlink_urb_from_ep
==========================

.. c:function:: void usb_hcd_unlink_urb_from_ep (struct usb_hcd *hcd, struct urb *urb)

    remove an URB from its endpoint queue

    :param struct usb_hcd \*hcd:
        host controller to which ``urb`` was submitted

    :param struct urb \*urb:
        URB being unlinked


.. _`usb_hcd_unlink_urb_from_ep.description`:

Description
-----------

Host controller drivers should call this routine before calling
:c:func:`usb_hcd_giveback_urb`.  The HCD's private spinlock must be held and
interrupts must be disabled.  The actions carried out here are required
for URB completion.


.. _`usb_hcd_giveback_urb`:

usb_hcd_giveback_urb
====================

.. c:function:: void usb_hcd_giveback_urb (struct usb_hcd *hcd, struct urb *urb, int status)

    return URB from HCD to device driver

    :param struct usb_hcd \*hcd:
        host controller returning the URB

    :param struct urb \*urb:
        urb being returned to the USB device driver.

    :param int status:
        completion status code for the URB.
        Context: :c:func:`in_interrupt`


.. _`usb_hcd_giveback_urb.description`:

Description
-----------

This hands the URB from HCD to its USB device driver, using its
completion function.  The HCD has freed all per-urb resources
(and is done using urb->hcpriv).  It also released all HCD locks;
the device driver won't cause problems if it frees, modifies,
or resubmits this URB.

If ``urb`` was unlinked, the value of ``status`` will be overridden by
``urb``\ ->unlinked.  Erroneous short transfers are detected in case
the HCD hasn't checked for them.


.. _`usb_hcd_alloc_bandwidth`:

usb_hcd_alloc_bandwidth
=======================

.. c:function:: int usb_hcd_alloc_bandwidth (struct usb_device *udev, struct usb_host_config *new_config, struct usb_host_interface *cur_alt, struct usb_host_interface *new_alt)

    check whether a new bandwidth setting exceeds the bus bandwidth

    :param struct usb_device \*udev:
        target :c:type:`struct usb_device <usb_device>`

    :param struct usb_host_config \*new_config:
        new configuration to install

    :param struct usb_host_interface \*cur_alt:
        the current alternate interface setting

    :param struct usb_host_interface \*new_alt:
        alternate interface setting that is being installed


.. _`usb_hcd_alloc_bandwidth.description`:

Description
-----------

To change configurations, pass in the new configuration in new_config,
and pass NULL for cur_alt and new_alt.

To reset a device's configuration (put the device in the ADDRESSED state),
pass in NULL for new_config, cur_alt, and new_alt.

To change alternate interface settings, pass in NULL for new_config,
pass in the current alternate interface setting in cur_alt,
and pass in the new alternate interface setting in new_alt.

Return: An error if the requested bandwidth change exceeds the
bus bandwidth or host controller internal resources.


.. _`usb_hcd_reset_endpoint`:

usb_hcd_reset_endpoint
======================

.. c:function:: void usb_hcd_reset_endpoint (struct usb_device *udev, struct usb_host_endpoint *ep)

    reset host endpoint state

    :param struct usb_device \*udev:
        USB device.

    :param struct usb_host_endpoint \*ep:
        the endpoint to reset.


.. _`usb_hcd_reset_endpoint.description`:

Description
-----------

Resets any host endpoint state such as the toggle bit, sequence
number and current window.


.. _`usb_alloc_streams`:

usb_alloc_streams
=================

.. c:function:: int usb_alloc_streams (struct usb_interface *interface, struct usb_host_endpoint **eps, unsigned int num_eps, unsigned int num_streams, gfp_t mem_flags)

    allocate bulk endpoint stream IDs.

    :param struct usb_interface \*interface:
        alternate setting that includes all endpoints.

    :param struct usb_host_endpoint \*\*eps:
        array of endpoints that need streams.

    :param unsigned int num_eps:
        number of endpoints in the array.

    :param unsigned int num_streams:
        number of streams to allocate.

    :param gfp_t mem_flags:
        flags hcd should use to allocate memory.


.. _`usb_alloc_streams.description`:

Description
-----------

Sets up a group of bulk endpoints to have ``num_streams`` stream IDs available.
Drivers may queue multiple transfers to different stream IDs, which may
complete in a different order than they were queued.

Return: On success, the number of allocated streams. On failure, a negative
error code.


.. _`usb_free_streams`:

usb_free_streams
================

.. c:function:: int usb_free_streams (struct usb_interface *interface, struct usb_host_endpoint **eps, unsigned int num_eps, gfp_t mem_flags)

    free bulk endpoint stream IDs.

    :param struct usb_interface \*interface:
        alternate setting that includes all endpoints.

    :param struct usb_host_endpoint \*\*eps:
        array of endpoints to remove streams from.

    :param unsigned int num_eps:
        number of endpoints in the array.

    :param gfp_t mem_flags:
        flags hcd should use to allocate memory.


.. _`usb_free_streams.description`:

Description
-----------

Reverts a group of bulk endpoints back to not using stream IDs.
Can fail if we are given bad arguments, or HCD is broken.

Return: 0 on success. On failure, a negative error code.


.. _`usb_hcd_resume_root_hub`:

usb_hcd_resume_root_hub
=======================

.. c:function:: void usb_hcd_resume_root_hub (struct usb_hcd *hcd)

    called by HCD to resume its root hub

    :param struct usb_hcd \*hcd:
        host controller for this root hub


.. _`usb_hcd_resume_root_hub.description`:

Description
-----------

The USB host controller calls this function when its root hub is
suspended (with the remote wakeup feature enabled) and a remote
wakeup request is received.  The routine submits a workqueue request
to resume the root hub (that is, manage its downstream ports again).


.. _`usb_bus_start_enum`:

usb_bus_start_enum
==================

.. c:function:: int usb_bus_start_enum (struct usb_bus *bus, unsigned port_num)

    start immediate enumeration (for OTG)

    :param struct usb_bus \*bus:
        the bus (must use hcd framework)

    :param unsigned port_num:
        1-based number of port; usually bus->otg_port
        Context: :c:func:`in_interrupt`


.. _`usb_bus_start_enum.description`:

Description
-----------

Starts enumeration, with an immediate reset followed later by
hub_wq identifying and possibly configuring the device.
This is needed by OTG controller drivers, where it helps meet
HNP protocol timing requirements for starting a port reset.

Return: 0 if successful.


.. _`usb_hcd_irq`:

usb_hcd_irq
===========

.. c:function:: irqreturn_t usb_hcd_irq (int irq, void *__hcd)

    hook IRQs to HCD framework (bus glue)

    :param int irq:
        the IRQ being raised

    :param void \*__hcd:
        pointer to the HCD whose IRQ is being signaled


.. _`usb_hcd_irq.description`:

Description
-----------

If the controller isn't HALTed, calls the driver's irq handler.
Checks whether the controller is now dead.

Return: ``IRQ_HANDLED`` if the IRQ was handled. ``IRQ_NONE`` otherwise.


.. _`usb_hc_died`:

usb_hc_died
===========

.. c:function:: void usb_hc_died (struct usb_hcd *hcd)

    report abnormal shutdown of a host controller (bus glue)

    :param struct usb_hcd \*hcd:
        pointer to the HCD representing the controller


.. _`usb_hc_died.description`:

Description
-----------

This is called by bus glue to report a USB host controller that died
while operations may still have been pending.  It's called automatically
by the PCI glue, so only glue for non-PCI busses should need to call it.

Only call this function with the primary HCD.


.. _`usb_create_shared_hcd`:

usb_create_shared_hcd
=====================

.. c:function:: struct usb_hcd *usb_create_shared_hcd (const struct hc_driver *driver, struct device *dev, const char *bus_name, struct usb_hcd *primary_hcd)

    create and initialize an HCD structure

    :param const struct hc_driver \*driver:
        HC driver that will use this hcd

    :param struct device \*dev:
        device for this HC, stored in hcd->self.controller

    :param const char \*bus_name:
        value to store in hcd->self.bus_name

    :param struct usb_hcd \*primary_hcd:
        a pointer to the usb_hcd structure that is sharing the
        PCI device.  Only allocate certain resources for the primary HCD

        Context: !:c:func:`in_interrupt`


.. _`usb_create_shared_hcd.description`:

Description
-----------

Allocate a struct usb_hcd, with extra space at the end for the
HC driver's private data.  Initialize the generic members of the
hcd structure.

Return: On success, a pointer to the created and initialized HCD structure.
On failure (e.g. if memory is unavailable), ``NULL``\ .


.. _`usb_create_hcd`:

usb_create_hcd
==============

.. c:function:: struct usb_hcd *usb_create_hcd (const struct hc_driver *driver, struct device *dev, const char *bus_name)

    create and initialize an HCD structure

    :param const struct hc_driver \*driver:
        HC driver that will use this hcd

    :param struct device \*dev:
        device for this HC, stored in hcd->self.controller

    :param const char \*bus_name:
        value to store in hcd->self.bus_name
        Context: !:c:func:`in_interrupt`


.. _`usb_create_hcd.description`:

Description
-----------

Allocate a struct usb_hcd, with extra space at the end for the
HC driver's private data.  Initialize the generic members of the
hcd structure.

Return: On success, a pointer to the created and initialized HCD
structure. On failure (e.g. if memory is unavailable), ``NULL``\ .


.. _`usb_add_hcd`:

usb_add_hcd
===========

.. c:function:: int usb_add_hcd (struct usb_hcd *hcd, unsigned int irqnum, unsigned long irqflags)

    finish generic HCD structure initialization and register

    :param struct usb_hcd \*hcd:
        the usb_hcd structure to initialize

    :param unsigned int irqnum:
        Interrupt line to allocate

    :param unsigned long irqflags:
        Interrupt type flags


.. _`usb_add_hcd.description`:

Description
-----------

Finish the remaining parts of generic HCD initialization: allocate the
buffers of consistent memory, register the bus, request the IRQ line,
and call the driver's :c:func:`reset` and :c:func:`start` routines.


.. _`usb_remove_hcd`:

usb_remove_hcd
==============

.. c:function:: void usb_remove_hcd (struct usb_hcd *hcd)

    shutdown processing for generic HCDs

    :param struct usb_hcd \*hcd:
        the usb_hcd structure to remove
        Context: !:c:func:`in_interrupt`


.. _`usb_remove_hcd.description`:

Description
-----------

Disconnects the root hub, then reverses the effects of :c:func:`usb_add_hcd`,
invoking the HCD's :c:func:`stop` method.

