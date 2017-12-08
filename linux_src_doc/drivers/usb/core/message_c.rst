.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/message.c

.. _`usb_control_msg`:

usb_control_msg
===============

.. c:function:: int usb_control_msg(struct usb_device *dev, unsigned int pipe, __u8 request, __u8 requesttype, __u16 value, __u16 index, void *data, __u16 size, int timeout)

    Builds a control urb, sends it off and waits for completion

    :param struct usb_device \*dev:
        pointer to the usb device to send the message to

    :param unsigned int pipe:
        endpoint "pipe" to send the message to

    :param __u8 request:
        USB message request value

    :param __u8 requesttype:
        USB message request type value

    :param __u16 value:
        USB message value

    :param __u16 index:
        USB message index value

    :param void \*data:
        pointer to the data to send

    :param __u16 size:
        length in bytes of the data to send

    :param int timeout:
        time in msecs to wait for the message to complete before timing
        out (if 0 the wait is forever)

.. _`usb_control_msg.context`:

Context
-------

!in_interrupt ()

.. _`usb_control_msg.description`:

Description
-----------

This function sends a simple control message to a specified endpoint and
waits for the message to complete, or timeout.

Don't use this function from within an interrupt context. If you need
an asynchronous message, or need to send a message from within interrupt
context, use \ :c:func:`usb_submit_urb`\ . If a thread in your driver uses this call,
make sure your \ :c:func:`disconnect`\  method can wait for it to complete. Since you
don't have a handle on the URB used, you can't cancel the request.

.. _`usb_control_msg.return`:

Return
------

If successful, the number of bytes transferred. Otherwise, a negative
error number.

.. _`usb_interrupt_msg`:

usb_interrupt_msg
=================

.. c:function:: int usb_interrupt_msg(struct usb_device *usb_dev, unsigned int pipe, void *data, int len, int *actual_length, int timeout)

    Builds an interrupt urb, sends it off and waits for completion

    :param struct usb_device \*usb_dev:
        pointer to the usb device to send the message to

    :param unsigned int pipe:
        endpoint "pipe" to send the message to

    :param void \*data:
        pointer to the data to send

    :param int len:
        length in bytes of the data to send

    :param int \*actual_length:
        pointer to a location to put the actual length transferred
        in bytes

    :param int timeout:
        time in msecs to wait for the message to complete before
        timing out (if 0 the wait is forever)

.. _`usb_interrupt_msg.context`:

Context
-------

!in_interrupt ()

.. _`usb_interrupt_msg.description`:

Description
-----------

This function sends a simple interrupt message to a specified endpoint and
waits for the message to complete, or timeout.

Don't use this function from within an interrupt context. If you need
an asynchronous message, or need to send a message from within interrupt
context, use \ :c:func:`usb_submit_urb`\  If a thread in your driver uses this call,
make sure your \ :c:func:`disconnect`\  method can wait for it to complete. Since you
don't have a handle on the URB used, you can't cancel the request.

.. _`usb_interrupt_msg.return`:

Return
------

If successful, 0. Otherwise a negative error number. The number of actual
bytes transferred will be stored in the \ ``actual_length``\  parameter.

.. _`usb_bulk_msg`:

usb_bulk_msg
============

.. c:function:: int usb_bulk_msg(struct usb_device *usb_dev, unsigned int pipe, void *data, int len, int *actual_length, int timeout)

    Builds a bulk urb, sends it off and waits for completion

    :param struct usb_device \*usb_dev:
        pointer to the usb device to send the message to

    :param unsigned int pipe:
        endpoint "pipe" to send the message to

    :param void \*data:
        pointer to the data to send

    :param int len:
        length in bytes of the data to send

    :param int \*actual_length:
        pointer to a location to put the actual length transferred
        in bytes

    :param int timeout:
        time in msecs to wait for the message to complete before
        timing out (if 0 the wait is forever)

.. _`usb_bulk_msg.context`:

Context
-------

!in_interrupt ()

.. _`usb_bulk_msg.description`:

Description
-----------

This function sends a simple bulk message to a specified endpoint
and waits for the message to complete, or timeout.

Don't use this function from within an interrupt context. If you need
an asynchronous message, or need to send a message from within interrupt
context, use \ :c:func:`usb_submit_urb`\  If a thread in your driver uses this call,
make sure your \ :c:func:`disconnect`\  method can wait for it to complete. Since you
don't have a handle on the URB used, you can't cancel the request.

Because there is no \ :c:func:`usb_interrupt_msg`\  and no USBDEVFS_INTERRUPT ioctl,
users are forced to abuse this routine by using it to submit URBs for
interrupt endpoints.  We will take the liberty of creating an interrupt URB
(with the default interval) if the target is an interrupt endpoint.

.. _`usb_bulk_msg.return`:

Return
------

If successful, 0. Otherwise a negative error number. The number of actual
bytes transferred will be stored in the \ ``actual_length``\  parameter.

.. _`usb_sg_init`:

usb_sg_init
===========

.. c:function:: int usb_sg_init(struct usb_sg_request *io, struct usb_device *dev, unsigned pipe, unsigned period, struct scatterlist *sg, int nents, size_t length, gfp_t mem_flags)

    initializes scatterlist-based bulk/interrupt I/O request

    :param struct usb_sg_request \*io:
        request block being initialized.  until \ :c:func:`usb_sg_wait`\  returns,
        treat this as a pointer to an opaque block of memory,

    :param struct usb_device \*dev:
        the usb device that will send or receive the data

    :param unsigned pipe:
        endpoint "pipe" used to transfer the data

    :param unsigned period:
        polling rate for interrupt endpoints, in frames or
        (for high speed endpoints) microframes; ignored for bulk

    :param struct scatterlist \*sg:
        scatterlist entries

    :param int nents:
        how many entries in the scatterlist

    :param size_t length:
        how many bytes to send from the scatterlist, or zero to
        send every byte identified in the list.

    :param gfp_t mem_flags:
        SLAB_* flags affecting memory allocations in this call

.. _`usb_sg_init.description`:

Description
-----------

This initializes a scatter/gather request, allocating resources such as
I/O mappings and urb memory (except maybe memory used by USB controller
drivers).

The request must be issued using \ :c:func:`usb_sg_wait`\ , which waits for the I/O to
complete (or to be canceled) and then cleans up all resources allocated by
\ :c:func:`usb_sg_init`\ .

The request may be canceled with \ :c:func:`usb_sg_cancel`\ , either before or after
\ :c:func:`usb_sg_wait`\  is called.

.. _`usb_sg_init.return`:

Return
------

Zero for success, else a negative errno value.

.. _`usb_sg_wait`:

usb_sg_wait
===========

.. c:function:: void usb_sg_wait(struct usb_sg_request *io)

    synchronously execute scatter/gather request

    :param struct usb_sg_request \*io:
        request block handle, as initialized with \ :c:func:`usb_sg_init`\ .
        some fields become accessible when this call returns.

.. _`usb_sg_wait.context`:

Context
-------

!in_interrupt ()

.. _`usb_sg_wait.description`:

Description
-----------

This function blocks until the specified I/O operation completes.  It
leverages the grouping of the related I/O requests to get good transfer
rates, by queueing the requests.  At higher speeds, such queuing can
significantly improve USB throughput.

There are three kinds of completion for this function.

(1) success, where io->status is zero.  The number of io->bytes
    transferred is as requested.
(2) error, where io->status is a negative errno value.  The number
    of io->bytes transferred before the error is usually less
    than requested, and can be nonzero.
(3) cancellation, a type of error with status -ECONNRESET that
    is initiated by \ :c:func:`usb_sg_cancel`\ .

When this function returns, all memory allocated through \ :c:func:`usb_sg_init`\  or
this call will have been freed.  The request block parameter may still be
passed to \ :c:func:`usb_sg_cancel`\ , or it may be freed.  It could also be
reinitialized and then reused.

.. _`usb_sg_wait.data-transfer-rates`:

Data Transfer Rates
-------------------


Bulk transfers are valid for full or high speed endpoints.
The best full speed data rate is 19 packets of 64 bytes each
per frame, or 1216 bytes per millisecond.
The best high speed data rate is 13 packets of 512 bytes each
per microframe, or 52 KBytes per millisecond.

The reason to use interrupt transfers through this API would most likely
be to reserve high speed bandwidth, where up to 24 KBytes per millisecond
could be transferred.  That capability is less useful for low or full
speed interrupt endpoints, which allow at most one packet per millisecond,
of at most 8 or 64 bytes (respectively).

It is not necessary to call this function to reserve bandwidth for devices
under an xHCI host controller, as the bandwidth is reserved when the
configuration or interface alt setting is selected.

.. _`usb_sg_cancel`:

usb_sg_cancel
=============

.. c:function:: void usb_sg_cancel(struct usb_sg_request *io)

    stop scatter/gather i/o issued by \ :c:func:`usb_sg_wait`\ 

    :param struct usb_sg_request \*io:
        request block, initialized with \ :c:func:`usb_sg_init`\ 

.. _`usb_sg_cancel.description`:

Description
-----------

This stops a request after it has been started by \ :c:func:`usb_sg_wait`\ .
It can also prevents one initialized by \ :c:func:`usb_sg_init`\  from starting,
so that call just frees resources allocated to the request.

.. _`usb_get_descriptor`:

usb_get_descriptor
==================

.. c:function:: int usb_get_descriptor(struct usb_device *dev, unsigned char type, unsigned char index, void *buf, int size)

    issues a generic GET_DESCRIPTOR request

    :param struct usb_device \*dev:
        the device whose descriptor is being retrieved

    :param unsigned char type:
        the descriptor type (USB_DT_*)

    :param unsigned char index:
        the number of the descriptor

    :param void \*buf:
        where to put the descriptor

    :param int size:
        how big is "buf"?

.. _`usb_get_descriptor.context`:

Context
-------

!in_interrupt ()

.. _`usb_get_descriptor.description`:

Description
-----------

Gets a USB descriptor.  Convenience functions exist to simplify
getting some types of descriptors.  Use
\ :c:func:`usb_get_string`\  or \ :c:func:`usb_string`\  for USB_DT_STRING.
Device (USB_DT_DEVICE) and configuration descriptors (USB_DT_CONFIG)
are part of the device structure.
In addition to a number of USB-standard descriptors, some
devices also use class-specific or vendor-specific descriptors.

This call is synchronous, and may not be used in an interrupt context.

.. _`usb_get_descriptor.return`:

Return
------

The number of bytes received on success, or else the status code
returned by the underlying \ :c:func:`usb_control_msg`\  call.

.. _`usb_get_string`:

usb_get_string
==============

.. c:function:: int usb_get_string(struct usb_device *dev, unsigned short langid, unsigned char index, void *buf, int size)

    gets a string descriptor

    :param struct usb_device \*dev:
        the device whose string descriptor is being retrieved

    :param unsigned short langid:
        code for language chosen (from string descriptor zero)

    :param unsigned char index:
        the number of the descriptor

    :param void \*buf:
        where to put the string

    :param int size:
        how big is "buf"?

.. _`usb_get_string.context`:

Context
-------

!in_interrupt ()

.. _`usb_get_string.description`:

Description
-----------

Retrieves a string, encoded using UTF-16LE (Unicode, 16 bits per character,
in little-endian byte order).
The \ :c:func:`usb_string`\  function will often be a convenient way to turn
these strings into kernel-printable form.

Strings may be referenced in device, configuration, interface, or other
descriptors, and could also be used in vendor-specific ways.

This call is synchronous, and may not be used in an interrupt context.

.. _`usb_get_string.return`:

Return
------

The number of bytes received on success, or else the status code
returned by the underlying \ :c:func:`usb_control_msg`\  call.

.. _`usb_string`:

usb_string
==========

.. c:function:: int usb_string(struct usb_device *dev, int index, char *buf, size_t size)

    returns UTF-8 version of a string descriptor

    :param struct usb_device \*dev:
        the device whose string descriptor is being retrieved

    :param int index:
        the number of the descriptor

    :param char \*buf:
        where to put the string

    :param size_t size:
        how big is "buf"?

.. _`usb_string.context`:

Context
-------

!in_interrupt ()

.. _`usb_string.description`:

Description
-----------

This converts the UTF-16LE encoded strings returned by devices, from
\ :c:func:`usb_get_string_descriptor`\ , to null-terminated UTF-8 encoded ones
that are more usable in most kernel contexts.  Note that this function
chooses strings in the first language supported by the device.

This call is synchronous, and may not be used in an interrupt context.

.. _`usb_string.return`:

Return
------

length of the string (>= 0) or usb_control_msg status (< 0).

.. _`usb_cache_string`:

usb_cache_string
================

.. c:function:: char *usb_cache_string(struct usb_device *udev, int index)

    read a string descriptor and cache it for later use

    :param struct usb_device \*udev:
        the device whose string descriptor is being read

    :param int index:
        the descriptor index

.. _`usb_cache_string.return`:

Return
------

A pointer to a kmalloc'ed buffer containing the descriptor string,
or \ ``NULL``\  if the index is 0 or the string could not be read.

.. _`usb_get_status`:

usb_get_status
==============

.. c:function:: int usb_get_status(struct usb_device *dev, int recip, int type, int target, void *data)

    issues a GET_STATUS call

    :param struct usb_device \*dev:
        the device whose status is being checked

    :param int recip:
        USB_RECIP_*; for device, interface, or endpoint

    :param int type:
        USB_STATUS_TYPE_*; for standard or PTM status types

    :param int target:
        zero (for device), else interface or endpoint number

    :param void \*data:
        pointer to two bytes of bitmap data

.. _`usb_get_status.context`:

Context
-------

!in_interrupt ()

.. _`usb_get_status.description`:

Description
-----------

Returns device, interface, or endpoint status.  Normally only of
interest to see if the device is self powered, or has enabled the
remote wakeup facility; or whether a bulk or interrupt endpoint
is halted ("stalled").

Bits in these status bitmaps are set using the SET_FEATURE request,
and cleared using the CLEAR_FEATURE request.  The \ :c:func:`usb_clear_halt`\ 
function should be used to clear halt ("stall") status.

This call is synchronous, and may not be used in an interrupt context.

Returns 0 and the status value in *@data (in host byte order) on success,
or else the status code from the underlying \ :c:func:`usb_control_msg`\  call.

.. _`usb_clear_halt`:

usb_clear_halt
==============

.. c:function:: int usb_clear_halt(struct usb_device *dev, int pipe)

    tells device to clear endpoint halt/stall condition

    :param struct usb_device \*dev:
        device whose endpoint is halted

    :param int pipe:
        endpoint "pipe" being cleared

.. _`usb_clear_halt.context`:

Context
-------

!in_interrupt ()

.. _`usb_clear_halt.description`:

Description
-----------

This is used to clear halt conditions for bulk and interrupt endpoints,
as reported by URB completion status.  Endpoints that are halted are
sometimes referred to as being "stalled".  Such endpoints are unable
to transmit or receive data until the halt status is cleared.  Any URBs
queued for such an endpoint should normally be unlinked by the driver
before clearing the halt condition, as described in sections 5.7.5
and 5.8.5 of the USB 2.0 spec.

Note that control and isochronous endpoints don't halt, although control
endpoints report "protocol stall" (for unsupported requests) using the
same status code used to report a true stall.

This call is synchronous, and may not be used in an interrupt context.

.. _`usb_clear_halt.return`:

Return
------

Zero on success, or else the status code returned by the
underlying \ :c:func:`usb_control_msg`\  call.

.. _`usb_disable_endpoint`:

usb_disable_endpoint
====================

.. c:function:: void usb_disable_endpoint(struct usb_device *dev, unsigned int epaddr, bool reset_hardware)

    - Disable an endpoint by address

    :param struct usb_device \*dev:
        the device whose endpoint is being disabled

    :param unsigned int epaddr:
        the endpoint's address.  Endpoint number for output,
        endpoint number + USB_DIR_IN for input

    :param bool reset_hardware:
        flag to erase any endpoint state stored in the
        controller hardware

.. _`usb_disable_endpoint.description`:

Description
-----------

Disables the endpoint for URB submission and nukes all pending URBs.
If \ ``reset_hardware``\  is set then also deallocates hcd/hardware state
for the endpoint.

.. _`usb_reset_endpoint`:

usb_reset_endpoint
==================

.. c:function:: void usb_reset_endpoint(struct usb_device *dev, unsigned int epaddr)

    Reset an endpoint's state.

    :param struct usb_device \*dev:
        the device whose endpoint is to be reset

    :param unsigned int epaddr:
        the endpoint's address.  Endpoint number for output,
        endpoint number + USB_DIR_IN for input

.. _`usb_reset_endpoint.description`:

Description
-----------

Resets any host-side endpoint state such as the toggle bit,
sequence number or current window.

.. _`usb_disable_interface`:

usb_disable_interface
=====================

.. c:function:: void usb_disable_interface(struct usb_device *dev, struct usb_interface *intf, bool reset_hardware)

    - Disable all endpoints for an interface

    :param struct usb_device \*dev:
        the device whose interface is being disabled

    :param struct usb_interface \*intf:
        pointer to the interface descriptor

    :param bool reset_hardware:
        flag to erase any endpoint state stored in the
        controller hardware

.. _`usb_disable_interface.description`:

Description
-----------

Disables all the endpoints for the interface's current altsetting.

.. _`usb_disable_device`:

usb_disable_device
==================

.. c:function:: void usb_disable_device(struct usb_device *dev, int skip_ep0)

    Disable all the endpoints for a USB device

    :param struct usb_device \*dev:
        the device whose endpoints are being disabled

    :param int skip_ep0:
        0 to disable endpoint 0, 1 to skip it.

.. _`usb_disable_device.description`:

Description
-----------

Disables all the device's endpoints, potentially including endpoint 0.
Deallocates hcd/hardware state for the endpoints (nuking all or most
pending urbs) and usbcore state for the interfaces, so that usbcore
must \ :c:func:`usb_set_configuration`\  before any interfaces could be used.

.. _`usb_enable_endpoint`:

usb_enable_endpoint
===================

.. c:function:: void usb_enable_endpoint(struct usb_device *dev, struct usb_host_endpoint *ep, bool reset_ep)

    Enable an endpoint for USB communications

    :param struct usb_device \*dev:
        the device whose interface is being enabled

    :param struct usb_host_endpoint \*ep:
        the endpoint

    :param bool reset_ep:
        flag to reset the endpoint state

.. _`usb_enable_endpoint.description`:

Description
-----------

Resets the endpoint state if asked, and sets dev->ep_{in,out} pointers.
For control endpoints, both the input and output sides are handled.

.. _`usb_enable_interface`:

usb_enable_interface
====================

.. c:function:: void usb_enable_interface(struct usb_device *dev, struct usb_interface *intf, bool reset_eps)

    Enable all the endpoints for an interface

    :param struct usb_device \*dev:
        the device whose interface is being enabled

    :param struct usb_interface \*intf:
        pointer to the interface descriptor

    :param bool reset_eps:
        flag to reset the endpoints' state

.. _`usb_enable_interface.description`:

Description
-----------

Enables all the endpoints for the interface's current altsetting.

.. _`usb_set_interface`:

usb_set_interface
=================

.. c:function:: int usb_set_interface(struct usb_device *dev, int interface, int alternate)

    Makes a particular alternate setting be current

    :param struct usb_device \*dev:
        the device whose interface is being updated

    :param int interface:
        the interface being updated

    :param int alternate:
        the setting being chosen.

.. _`usb_set_interface.context`:

Context
-------

!in_interrupt ()

.. _`usb_set_interface.description`:

Description
-----------

This is used to enable data transfers on interfaces that may not
be enabled by default.  Not all devices support such configurability.
Only the driver bound to an interface may change its setting.

Within any given configuration, each interface may have several
alternative settings.  These are often used to control levels of
bandwidth consumption.  For example, the default setting for a high
speed interrupt endpoint may not send more than 64 bytes per microframe,
while interrupt transfers of up to 3KBytes per microframe are legal.
Also, isochronous endpoints may never be part of an
interface's default setting.  To access such bandwidth, alternate
interface settings must be made current.

Note that in the Linux USB subsystem, bandwidth associated with
an endpoint in a given alternate setting is not reserved until an URB
is submitted that needs that bandwidth.  Some other operating systems
allocate bandwidth early, when a configuration is chosen.

This call is synchronous, and may not be used in an interrupt context.
Also, drivers must not change altsettings while urbs are scheduled for
endpoints in that interface; all such urbs must first be completed
(perhaps forced by unlinking).

.. _`usb_set_interface.return`:

Return
------

Zero on success, or else the status code returned by the
underlying \ :c:func:`usb_control_msg`\  call.

.. _`usb_reset_configuration`:

usb_reset_configuration
=======================

.. c:function:: int usb_reset_configuration(struct usb_device *dev)

    lightweight device reset

    :param struct usb_device \*dev:
        the device whose configuration is being reset

.. _`usb_reset_configuration.description`:

Description
-----------

This issues a standard SET_CONFIGURATION request to the device using
the current configuration.  The effect is to reset most USB-related
state in the device, including interface altsettings (reset to zero),
endpoint halts (cleared), and endpoint state (only for bulk and interrupt
endpoints).  Other usbcore state is unchanged, including bindings of
usb device drivers to interfaces.

Because this affects multiple interfaces, avoid using this with composite
(multi-interface) devices.  Instead, the driver for each interface may
use \ :c:func:`usb_set_interface`\  on the interfaces it claims.  Be careful though;
some devices don't support the SET_INTERFACE request, and others won't
reset all the interface state (notably endpoint state).  Resetting the whole
configuration would affect other drivers' interfaces.

The caller must own the device lock.

.. _`usb_reset_configuration.return`:

Return
------

Zero on success, else a negative error code.

.. _`usb_driver_set_configuration`:

usb_driver_set_configuration
============================

.. c:function:: int usb_driver_set_configuration(struct usb_device *udev, int config)

    Provide a way for drivers to change device configurations

    :param struct usb_device \*udev:
        the device whose configuration is being updated

    :param int config:
        the configuration being chosen.

.. _`usb_driver_set_configuration.context`:

Context
-------

In process context, must be able to sleep

.. _`usb_driver_set_configuration.description`:

Description
-----------

Device interface drivers are not allowed to change device configurations.
This is because changing configurations will destroy the interface the
driver is bound to and create new ones; it would be like a floppy-disk
driver telling the computer to replace the floppy-disk drive with a
tape drive!

Still, in certain specialized circumstances the need may arise.  This
routine gets around the normal restrictions by using a work thread to
submit the change-config request.

.. _`usb_driver_set_configuration.return`:

Return
------

0 if the request was successfully queued, error code otherwise.
The caller has no way to know whether the queued request will eventually
succeed.

.. _`cdc_parse_cdc_header`:

cdc_parse_cdc_header
====================

.. c:function:: int cdc_parse_cdc_header(struct usb_cdc_parsed_header *hdr, struct usb_interface *intf, u8 *buffer, int buflen)

    parse the extra headers present in CDC devices

    :param struct usb_cdc_parsed_header \*hdr:
        the place to put the results of the parsing

    :param struct usb_interface \*intf:
        the interface for which parsing is requested

    :param u8 \*buffer:
        pointer to the extra headers to be parsed

    :param int buflen:
        length of the extra headers

.. _`cdc_parse_cdc_header.description`:

Description
-----------

This evaluates the extra headers present in CDC devices which
bind the interfaces for data and control and provide details
about the capabilities of the device.

.. _`cdc_parse_cdc_header.return`:

Return
------

number of descriptors parsed or -EINVAL
if the header is contradictory beyond salvage

.. This file was automatic generated / don't edit.

