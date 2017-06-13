.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/gadget.h

.. _`usb_request`:

struct usb_request
==================

.. c:type:: struct usb_request

    describes one i/o request

.. _`usb_request.definition`:

Definition
----------

.. code-block:: c

    struct usb_request {
        void *buf;
        unsigned length;
        dma_addr_t dma;
        struct scatterlist *sg;
        unsigned num_sgs;
        unsigned num_mapped_sgs;
        unsigned stream_id:16;
        unsigned no_interrupt:1;
        unsigned zero:1;
        unsigned short_not_ok:1;
        void (*complete)(struct usb_ep *ep, struct usb_request *req);
        void *context;
        struct list_head list;
        int status;
        unsigned actual;
    }

.. _`usb_request.members`:

Members
-------

buf
    Buffer used for data.  Always provide this; some controllers
    only use PIO, or don't use DMA for some endpoints.

length
    Length of that data

dma
    DMA address corresponding to 'buf'.  If you don't set this
    field, and the usb controller needs one, it is responsible
    for mapping and unmapping the buffer.

sg
    a scatterlist for SG-capable controllers.

num_sgs
    number of SG entries

num_mapped_sgs
    number of SG entries mapped to DMA (internal)

stream_id
    The stream id, when USB3.0 bulk streams are being used

no_interrupt
    If true, hints that no completion irq is needed.
    Helpful sometimes with deep request queues that are handled
    directly by DMA controllers.

zero
    If true, when writing data, makes the last packet be "short"
    by adding a zero length packet as needed;

short_not_ok
    When reading data, makes short packets be
    treated as errors (queue stops advancing till cleanup).

complete
    Function called when request completes, so this request and
    its buffer may be re-used.  The function will always be called with
    interrupts disabled, and it must not sleep.
    Reads terminate with a short packet, or when the buffer fills,
    whichever comes first.  When writes terminate, some data bytes
    will usually still be in flight (often in a hardware fifo).
    Errors (for reads or writes) stop the queue from advancing
    until the completion function returns, so that any transfers
    invalidated by the error may first be dequeued.

context
    For use by the completion callback

list
    For use by the gadget driver.

status
    Reports completion code, zero or a negative errno.
    Normally, faults block the transfer queue from advancing until
    the completion callback returns.
    Code "-ESHUTDOWN" indicates completion caused by device disconnect,
    or when the driver disabled the endpoint.

actual
    Reports bytes transferred to/from the buffer.  For reads (OUT
    transfers) this may be less than the requested length.  If the
    short_not_ok flag is set, short reads are treated as errors
    even when status otherwise indicates successful completion.
    Note that for writes (IN transfers) some data bytes may still
    reside in a device-side FIFO when the request is reported as
    complete.

.. _`usb_request.description`:

Description
-----------

These are allocated/freed through the endpoint they're used with.  The
hardware's driver can add extra per-request data to the memory it returns,
which often avoids separate memory allocations (potential failures),
later when the request is queued.

Request flags affect request handling, such as whether a zero length
packet is written (the "zero" flag), whether a short read should be
treated as an error (blocking request queue advance, the "short_not_ok"
flag), or hinting that an interrupt is not required (the "no_interrupt"
flag, for use with deep request queues).

Bulk endpoints can use any size buffers, and can also be used for interrupt
transfers. interrupt-only endpoints can be much less functional.

.. _`usb_request.note`:

NOTE
----

this is analogous to 'struct urb' on the host side, except that
it's thinner and promotes more pre-allocation.

.. _`usb_ep_caps`:

struct usb_ep_caps
==================

.. c:type:: struct usb_ep_caps

    endpoint capabilities description

.. _`usb_ep_caps.definition`:

Definition
----------

.. code-block:: c

    struct usb_ep_caps {
        unsigned type_control:1;
        unsigned type_iso:1;
        unsigned type_bulk:1;
        unsigned type_int:1;
        unsigned dir_in:1;
        unsigned dir_out:1;
    }

.. _`usb_ep_caps.members`:

Members
-------

type_control
    Endpoint supports control type (reserved for ep0).

type_iso
    Endpoint supports isochronous transfers.

type_bulk
    Endpoint supports bulk transfers.

type_int
    Endpoint supports interrupt transfers.

dir_in
    Endpoint supports IN direction.

dir_out
    Endpoint supports OUT direction.

.. _`usb_ep`:

struct usb_ep
=============

.. c:type:: struct usb_ep

    device side representation of USB endpoint

.. _`usb_ep.definition`:

Definition
----------

.. code-block:: c

    struct usb_ep {
        void *driver_data;
        const char *name;
        const struct usb_ep_ops *ops;
        struct list_head ep_list;
        struct usb_ep_caps caps;
        bool claimed;
        bool enabled;
        unsigned maxpacket:16;
        unsigned maxpacket_limit:16;
        unsigned max_streams:16;
        unsigned mult:2;
        unsigned maxburst:5;
        u8 address;
        const struct usb_endpoint_descriptor *desc;
        const struct usb_ss_ep_comp_descriptor *comp_desc;
    }

.. _`usb_ep.members`:

Members
-------

driver_data
    for use by the gadget driver.

name
    identifier for the endpoint, such as "ep-a" or "ep9in-bulk"

ops
    Function pointers used to access hardware-specific operations.

ep_list
    the gadget's ep_list holds all of its endpoints

caps
    The structure describing types and directions supported by endoint.

claimed
    *undescribed*

enabled
    *undescribed*

maxpacket
    The maximum packet size used on this endpoint.  The initial
    value can sometimes be reduced (hardware allowing), according to
    the endpoint descriptor used to configure the endpoint.

maxpacket_limit
    The maximum packet size value which can be handled by this
    endpoint. It's set once by UDC driver when endpoint is initialized, and
    should not be changed. Should not be confused with maxpacket.

max_streams
    The maximum number of streams supported
    by this EP (0 - 16, actual number is 2^n)

mult
    multiplier, 'mult' value for SS Isoc EPs

maxburst
    the maximum number of bursts supported by this EP (for usb3)

address
    used to identify the endpoint when finding descriptor that
    matches connection speed

desc
    endpoint descriptor.  This pointer is set before the endpoint is
    enabled and remains valid until the endpoint is disabled.

comp_desc
    In case of SuperSpeed support, this is the endpoint companion
    descriptor that is used to configure the endpoint

.. _`usb_ep.description`:

Description
-----------

the bus controller driver lists all the general purpose endpoints in
gadget->ep_list.  the control endpoint (gadget->ep0) is not in that list,
and is accessed only in response to a driver \ :c:func:`setup`\  callback.

.. _`usb_gadget`:

struct usb_gadget
=================

.. c:type:: struct usb_gadget

    represents a usb slave device

.. _`usb_gadget.definition`:

Definition
----------

.. code-block:: c

    struct usb_gadget {
        struct work_struct work;
        struct usb_udc *udc;
        const struct usb_gadget_ops *ops;
        struct usb_ep *ep0;
        struct list_head ep_list;
        enum usb_device_speed speed;
        enum usb_device_speed max_speed;
        enum usb_device_state state;
        const char *name;
        struct device dev;
        unsigned out_epnum;
        unsigned in_epnum;
        unsigned mA;
        struct usb_otg_caps *otg_caps;
        unsigned sg_supported:1;
        unsigned is_otg:1;
        unsigned is_a_peripheral:1;
        unsigned b_hnp_enable:1;
        unsigned a_hnp_support:1;
        unsigned a_alt_hnp_support:1;
        unsigned hnp_polling_support:1;
        unsigned host_request_flag:1;
        unsigned quirk_ep_out_aligned_size:1;
        unsigned quirk_altset_not_supp:1;
        unsigned quirk_stall_not_supp:1;
        unsigned quirk_zlp_not_supp:1;
        unsigned quirk_avoids_skb_reserve:1;
        unsigned is_selfpowered:1;
        unsigned deactivated:1;
        unsigned connected:1;
    }

.. _`usb_gadget.members`:

Members
-------

work
    (internal use) Workqueue to be used for \ :c:func:`sysfs_notify`\ 

udc
    struct usb_udc pointer for this gadget

ops
    Function pointers used to access hardware-specific operations.

ep0
    Endpoint zero, used when reading or writing responses to
    driver \ :c:func:`setup`\  requests

ep_list
    List of other endpoints supported by the device.

speed
    Speed of current connection to USB host.

max_speed
    Maximal speed the UDC can handle.  UDC must support this
    and all slower speeds.

state
    the state we are now (attached, suspended, configured, etc)

name
    Identifies the controller hardware type.  Used in diagnostics
    and sometimes configuration.

dev
    Driver model state for this abstract device.

out_epnum
    last used out ep number

in_epnum
    last used in ep number

mA
    last set mA value

otg_caps
    OTG capabilities of this gadget.

sg_supported
    true if we can handle scatter-gather

is_otg
    True if the USB device port uses a Mini-AB jack, so that the
    gadget driver must provide a USB OTG descriptor.

is_a_peripheral
    False unless is_otg, the "A" end of a USB cable
    is in the Mini-AB jack, and HNP has been used to switch roles
    so that the "A" device currently acts as A-Peripheral, not A-Host.

b_hnp_enable
    OTG device feature flag, indicating that the A-Host
    enabled HNP support.

a_hnp_support
    OTG device feature flag, indicating that the A-Host
    supports HNP at this port.

a_alt_hnp_support
    OTG device feature flag, indicating that the A-Host
    only supports HNP on a different root port.

hnp_polling_support
    OTG device feature flag, indicating if the OTG device
    in peripheral mode can support HNP polling.

host_request_flag
    OTG device feature flag, indicating if A-Peripheral
    or B-Peripheral wants to take host role.

quirk_ep_out_aligned_size
    epout requires buffer size to be aligned to
    MaxPacketSize.

quirk_altset_not_supp
    *undescribed*

quirk_stall_not_supp
    *undescribed*

quirk_zlp_not_supp
    *undescribed*

quirk_avoids_skb_reserve
    udc/platform wants to avoid \ :c:func:`skb_reserve`\  in
    u_ether.c to improve performance.

is_selfpowered
    if the gadget is self-powered.

deactivated
    True if gadget is deactivated - in deactivated state it cannot
    be connected.

connected
    True if gadget is connected.

.. _`usb_gadget.description`:

Description
-----------

Gadgets have a mostly-portable "gadget driver" implementing device
functions, handling all usb configurations and interfaces.  Gadget
drivers talk to hardware-specific code indirectly, through ops vectors.
That insulates the gadget driver from hardware details, and packages
the hardware endpoints through generic i/o queues.  The "usb_gadget"
and "usb_ep" interfaces provide that insulation from the hardware.

Except for the driver data, all fields in this structure are
read-only to the gadget driver.  That driver data is part of the
"driver model" infrastructure in 2.6 (and later) kernels, and for
earlier systems is grouped in a similar structure that's not known
to the rest of the kernel.

Values of the three OTG device feature flags are updated before the
\ :c:func:`setup`\  call corresponding to USB_REQ_SET_CONFIGURATION, and before
driver \ :c:func:`suspend`\  calls.  They are valid only when is_otg, and when the
device is acting as a B-Peripheral (so is_a_peripheral is false).

.. _`usb_ep_align`:

usb_ep_align
============

.. c:function:: size_t usb_ep_align(struct usb_ep *ep, size_t len)

    returns \ ``len``\  aligned to ep's maxpacketsize.

    :param struct usb_ep \*ep:
        the endpoint whose maxpacketsize is used to align \ ``len``\ 

    :param size_t len:
        buffer size's length to align to \ ``ep``\ 's maxpacketsize

.. _`usb_ep_align.description`:

Description
-----------

This helper is used to align buffer's size to an ep's maxpacketsize.

.. _`usb_ep_align_maybe`:

usb_ep_align_maybe
==================

.. c:function:: size_t usb_ep_align_maybe(struct usb_gadget *g, struct usb_ep *ep, size_t len)

    returns \ ``len``\  aligned to ep's maxpacketsize if gadget requires quirk_ep_out_aligned_size, otherwise returns len.

    :param struct usb_gadget \*g:
        controller to check for quirk

    :param struct usb_ep \*ep:
        the endpoint whose maxpacketsize is used to align \ ``len``\ 

    :param size_t len:
        buffer size's length to align to \ ``ep``\ 's maxpacketsize

.. _`usb_ep_align_maybe.description`:

Description
-----------

This helper is used in case it's required for any reason to check and maybe
align buffer's size to an ep's maxpacketsize.

.. _`gadget_is_altset_supported`:

gadget_is_altset_supported
==========================

.. c:function:: int gadget_is_altset_supported(struct usb_gadget *g)

    return true iff the hardware supports altsettings

    :param struct usb_gadget \*g:
        controller to check for quirk

.. _`gadget_is_stall_supported`:

gadget_is_stall_supported
=========================

.. c:function:: int gadget_is_stall_supported(struct usb_gadget *g)

    return true iff the hardware supports stalling

    :param struct usb_gadget \*g:
        controller to check for quirk

.. _`gadget_is_zlp_supported`:

gadget_is_zlp_supported
=======================

.. c:function:: int gadget_is_zlp_supported(struct usb_gadget *g)

    return true iff the hardware supports zlp

    :param struct usb_gadget \*g:
        controller to check for quirk

.. _`gadget_avoids_skb_reserve`:

gadget_avoids_skb_reserve
=========================

.. c:function:: int gadget_avoids_skb_reserve(struct usb_gadget *g)

    return true iff the hardware would like to avoid skb_reserve to improve performance.

    :param struct usb_gadget \*g:
        controller to check for quirk

.. _`gadget_is_dualspeed`:

gadget_is_dualspeed
===================

.. c:function:: int gadget_is_dualspeed(struct usb_gadget *g)

    return true iff the hardware handles high speed

    :param struct usb_gadget \*g:
        controller that might support both high and full speeds

.. _`gadget_is_superspeed`:

gadget_is_superspeed
====================

.. c:function:: int gadget_is_superspeed(struct usb_gadget *g)

    return true if the hardware handles superspeed

    :param struct usb_gadget \*g:
        controller that might support superspeed

.. _`gadget_is_superspeed_plus`:

gadget_is_superspeed_plus
=========================

.. c:function:: int gadget_is_superspeed_plus(struct usb_gadget *g)

    return true if the hardware handles superspeed plus

    :param struct usb_gadget \*g:
        controller that might support superspeed plus

.. _`gadget_is_otg`:

gadget_is_otg
=============

.. c:function:: int gadget_is_otg(struct usb_gadget *g)

    return true iff the hardware is OTG-ready

    :param struct usb_gadget \*g:
        controller that might have a Mini-AB connector

.. _`gadget_is_otg.description`:

Description
-----------

This is a runtime test, since kernels with a USB-OTG stack sometimes
run on boards which only have a Mini-B (or Mini-A) connector.

.. _`usb_gadget_driver`:

struct usb_gadget_driver
========================

.. c:type:: struct usb_gadget_driver

    driver for usb 'slave' devices

.. _`usb_gadget_driver.definition`:

Definition
----------

.. code-block:: c

    struct usb_gadget_driver {
        char *function;
        enum usb_device_speed max_speed;
        int (*bind)(struct usb_gadget *gadget, struct usb_gadget_driver *driver);
        void (*unbind)(struct usb_gadget *);
        int (*setup)(struct usb_gadget *, const struct usb_ctrlrequest *);
        void (*disconnect)(struct usb_gadget *);
        void (*suspend)(struct usb_gadget *);
        void (*resume)(struct usb_gadget *);
        void (*reset)(struct usb_gadget *);
        struct device_driver driver;
        char *udc_name;
        struct list_head pending;
        unsigned match_existing_only:1;
    }

.. _`usb_gadget_driver.members`:

Members
-------

function
    String describing the gadget's function

max_speed
    Highest speed the driver handles.

bind
    the driver's bind callback

unbind
    Invoked when the driver is unbound from a gadget,
    usually from rmmod (after a disconnect is reported).
    Called in a context that permits sleeping.

setup
    Invoked for ep0 control requests that aren't handled by
    the hardware level driver. Most calls must be handled by
    the gadget driver, including descriptor and configuration
    management.  The 16 bit members of the setup data are in
    USB byte order. Called in_interrupt; this may not sleep.  Driver
    queues a response to ep0, or returns negative to stall.

disconnect
    Invoked after all transfers have been stopped,
    when the host is disconnected.  May be called in_interrupt; this
    may not sleep.  Some devices can't detect disconnect, so this might
    not be called except as part of controller shutdown.

suspend
    Invoked on USB suspend.  May be called in_interrupt.

resume
    Invoked on USB resume.  May be called in_interrupt.

reset
    Invoked on USB bus reset. It is mandatory for all gadget drivers
    and should be called in_interrupt.

driver
    Driver model state for this driver.

udc_name
    A name of UDC this driver should be bound to. If udc_name is NULL,
    this driver will be bound to any available UDC.

pending
    UDC core private data used for deferred probe of this driver.

match_existing_only
    If udc is not found, return an error and don't add this
    gadget driver to list of pending driver

.. _`usb_gadget_driver.description`:

Description
-----------

Devices are disabled till a gadget driver successfully \ :c:func:`bind`\ s, which
means the driver will handle \ :c:func:`setup`\  requests needed to enumerate (and
meet "chapter 9" requirements) then do some useful work.

If gadget->is_otg is true, the gadget driver must provide an OTG
descriptor during enumeration, or else fail the \ :c:func:`bind`\  call.  In such
cases, no USB traffic may flow until both \ :c:func:`bind`\  returns without
having called \ :c:func:`usb_gadget_disconnect`\ , and the USB host stack has
initialized.

Drivers use hardware-specific knowledge to configure the usb hardware.
endpoint addressing is only one of several hardware characteristics that
are in descriptors the ep0 implementation returns from \ :c:func:`setup`\  calls.

Except for ep0 implementation, most driver code shouldn't need change to
run on top of different usb controllers.  It'll use endpoints set up by
that ep0 implementation.

The usb controller driver handles a few standard usb requests.  Those
include set_address, and feature flags for devices, interfaces, and
endpoints (the get_status, set_feature, and clear_feature requests).

Accordingly, the driver's \ :c:func:`setup`\  callback must always implement all
get_descriptor requests, returning at least a device descriptor and
a configuration descriptor.  Drivers must make sure the endpoint
descriptors match any hardware constraints. Some hardware also constrains
other descriptors. (The pxa250 allows only configurations 1, 2, or 3).

The driver's \ :c:func:`setup`\  callback must also implement set_configuration,
and should also implement set_interface, get_configuration, and
get_interface.  Setting a configuration (or interface) is where
endpoints should be activated or (config 0) shut down.

(Note that only the default control endpoint is supported.  Neither
hosts nor devices generally support control traffic except to ep0.)

Most devices will ignore USB suspend/resume operations, and so will
not provide those callbacks.  However, some may need to change modes
when the host is not longer directing those activities.  For example,
local controls (buttons, dials, etc) may need to be re-enabled since
the (remote) host can't do that any longer; or an error state might
be cleared, to make the device behave identically whether or not
power is maintained.

.. _`usb_gadget_probe_driver`:

usb_gadget_probe_driver
=======================

.. c:function:: int usb_gadget_probe_driver(struct usb_gadget_driver *driver)

    probe a gadget driver

    :param struct usb_gadget_driver \*driver:
        the driver being registered

.. _`usb_gadget_probe_driver.context`:

Context
-------

can sleep

.. _`usb_gadget_probe_driver.description`:

Description
-----------

Call this in your gadget driver's module initialization function,
to tell the underlying usb controller driver about your driver.
The \ ``bind``\ () function will be called to bind it to a gadget before this
registration call returns.  It's expected that the \ ``bind``\ () function will
be in init sections.

.. _`usb_gadget_unregister_driver`:

usb_gadget_unregister_driver
============================

.. c:function:: int usb_gadget_unregister_driver(struct usb_gadget_driver *driver)

    unregister a gadget driver

    :param struct usb_gadget_driver \*driver:
        the driver being unregistered

.. _`usb_gadget_unregister_driver.context`:

Context
-------

can sleep

.. _`usb_gadget_unregister_driver.description`:

Description
-----------

Call this in your gadget driver's module cleanup function,
to tell the underlying usb controller that your driver is
going away.  If the controller is connected to a USB host,
it will first \ :c:func:`disconnect`\ .  The driver is also requested
to \ :c:func:`unbind`\  and clean up any device state, before this procedure
finally returns.  It's expected that the \ :c:func:`unbind`\  functions
will in in exit sections, so may not be linked in some kernels.

.. _`usb_string`:

struct usb_string
=================

.. c:type:: struct usb_string

    wraps a C string and its USB id

.. _`usb_string.definition`:

Definition
----------

.. code-block:: c

    struct usb_string {
        u8 id;
        const char *s;
    }

.. _`usb_string.members`:

Members
-------

id
    the (nonzero) ID for this string

s
    the string, in UTF-8 encoding

.. _`usb_string.description`:

Description
-----------

If you're using \ :c:func:`usb_gadget_get_string`\ , use this to wrap a string
together with its ID.

.. _`usb_gadget_strings`:

struct usb_gadget_strings
=========================

.. c:type:: struct usb_gadget_strings

    a set of USB strings in a given language

.. _`usb_gadget_strings.definition`:

Definition
----------

.. code-block:: c

    struct usb_gadget_strings {
        u16 language;
        struct usb_string *strings;
    }

.. _`usb_gadget_strings.members`:

Members
-------

language
    identifies the strings' language (0x0409 for en-us)

strings
    array of strings with their ids

.. _`usb_gadget_strings.description`:

Description
-----------

If you're using \ :c:func:`usb_gadget_get_string`\ , use this to wrap all the
strings for a given language.

.. _`usb_free_descriptors`:

usb_free_descriptors
====================

.. c:function:: void usb_free_descriptors(struct usb_descriptor_header **v)

    free descriptors returned by \ :c:func:`usb_copy_descriptors`\ 

    :param struct usb_descriptor_header \*\*v:
        vector of descriptors

.. This file was automatic generated / don't edit.

