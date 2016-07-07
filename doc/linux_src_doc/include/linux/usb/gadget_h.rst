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
        void (* complete) (struct usb_ep *ep,struct usb_request *req);
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

.. _`usb_ep_set_maxpacket_limit`:

usb_ep_set_maxpacket_limit
==========================

.. c:function:: void usb_ep_set_maxpacket_limit(struct usb_ep *ep, unsigned maxpacket_limit)

    set maximum packet size limit for endpoint

    :param struct usb_ep \*ep:
        the endpoint being configured

    :param unsigned maxpacket_limit:
        value of maximum packet size limit

.. _`usb_ep_set_maxpacket_limit.description`:

Description
-----------

This function should be used only in UDC drivers to initialize endpoint
(usually in probe function).

.. _`usb_ep_enable`:

usb_ep_enable
=============

.. c:function:: int usb_ep_enable(struct usb_ep *ep)

    configure endpoint, making it usable

    :param struct usb_ep \*ep:
        the endpoint being configured.  may not be the endpoint named "ep0".
        drivers discover endpoints through the ep_list of a usb_gadget.

.. _`usb_ep_enable.description`:

Description
-----------

When configurations are set, or when interface settings change, the driver
will enable or disable the relevant endpoints.  while it is enabled, an
endpoint may be used for i/o until the driver receives a \ :c:func:`disconnect`\  from
the host or until the endpoint is disabled.

the ep0 implementation (which calls this routine) must ensure that the
hardware capabilities of each endpoint match the descriptor provided
for it.  for example, an endpoint named "ep2in-bulk" would be usable
for interrupt transfers as well as bulk, but it likely couldn't be used
for iso transfers or for endpoint 14.  some endpoints are fully
configurable, with more generic names like "ep-a".  (remember that for
USB, "in" means "towards the USB master".)

returns zero, or a negative error code.

.. _`usb_ep_disable`:

usb_ep_disable
==============

.. c:function:: int usb_ep_disable(struct usb_ep *ep)

    endpoint is no longer usable

    :param struct usb_ep \*ep:
        the endpoint being unconfigured.  may not be the endpoint named "ep0".

.. _`usb_ep_disable.description`:

Description
-----------

no other task may be using this endpoint when this is called.
any pending and uncompleted requests will complete with status
indicating disconnect (-ESHUTDOWN) before this call returns.
gadget drivers must call \ :c:func:`usb_ep_enable`\  again before queueing
requests to the endpoint.

returns zero, or a negative error code.

.. _`usb_ep_alloc_request`:

usb_ep_alloc_request
====================

.. c:function:: struct usb_request *usb_ep_alloc_request(struct usb_ep *ep, gfp_t gfp_flags)

    allocate a request object to use with this endpoint

    :param struct usb_ep \*ep:
        the endpoint to be used with with the request

    :param gfp_t gfp_flags:
        GFP\_\* flags to use

.. _`usb_ep_alloc_request.description`:

Description
-----------

Request objects must be allocated with this call, since they normally
need controller-specific setup and may even need endpoint-specific
resources such as allocation of DMA descriptors.
Requests may be submitted with \ :c:func:`usb_ep_queue`\ , and receive a single
completion callback.  Free requests with \ :c:func:`usb_ep_free_request`\ , when
they are no longer needed.

Returns the request, or null if one could not be allocated.

.. _`usb_ep_free_request`:

usb_ep_free_request
===================

.. c:function:: void usb_ep_free_request(struct usb_ep *ep, struct usb_request *req)

    frees a request object

    :param struct usb_ep \*ep:
        the endpoint associated with the request

    :param struct usb_request \*req:
        the request being freed

.. _`usb_ep_free_request.description`:

Description
-----------

Reverses the effect of \ :c:func:`usb_ep_alloc_request`\ .
Caller guarantees the request is not queued, and that it will
no longer be requeued (or otherwise used).

.. _`usb_ep_queue`:

usb_ep_queue
============

.. c:function:: int usb_ep_queue(struct usb_ep *ep, struct usb_request *req, gfp_t gfp_flags)

    queues (submits) an I/O request to an endpoint.

    :param struct usb_ep \*ep:
        the endpoint associated with the request

    :param struct usb_request \*req:
        the request being submitted

    :param gfp_t gfp_flags:
        GFP\_\* flags to use in case the lower level driver couldn't
        pre-allocate all necessary memory with the request.

.. _`usb_ep_queue.description`:

Description
-----------

This tells the device controller to perform the specified request through
that endpoint (reading or writing a buffer).  When the request completes,
including being canceled by \ :c:func:`usb_ep_dequeue`\ , the request's completion
routine is called to return the request to the driver.  Any endpoint
(except control endpoints like ep0) may have more than one transfer
request queued; they complete in FIFO order.  Once a gadget driver
submits a request, that request may not be examined or modified until it
is given back to that driver through the completion callback.

Each request is turned into one or more packets.  The controller driver
never merges adjacent requests into the same packet.  OUT transfers
will sometimes use data that's already buffered in the hardware.
Drivers can rely on the fact that the first byte of the request's buffer
always corresponds to the first byte of some USB packet, for both
IN and OUT transfers.

Bulk endpoints can queue any amount of data; the transfer is packetized
automatically.  The last packet will be short if the request doesn't fill it
out completely.  Zero length packets (ZLPs) should be avoided in portable
protocols since not all usb hardware can successfully handle zero length
packets.  (ZLPs may be explicitly written, and may be implicitly written if
the request 'zero' flag is set.)  Bulk endpoints may also be used
for interrupt transfers; but the reverse is not true, and some endpoints
won't support every interrupt transfer.  (Such as 768 byte packets.)

Interrupt-only endpoints are less functional than bulk endpoints, for
example by not supporting queueing or not handling buffers that are
larger than the endpoint's maxpacket size.  They may also treat data
toggle differently.

Control endpoints ... after getting a \ :c:func:`setup`\  callback, the driver queues
one response (even if it would be zero length).  That enables the
status ack, after transferring data as specified in the response.  Setup
functions may return negative error codes to generate protocol stalls.
(Note that some USB device controllers disallow protocol stall responses
in some cases.)  When control responses are deferred (the response is
written after the setup callback returns), then \ :c:func:`usb_ep_set_halt`\  may be
used on ep0 to trigger protocol stalls.  Depending on the controller,
it may not be possible to trigger a status-stage protocol stall when the
data stage is over, that is, from within the response's completion
routine.

For periodic endpoints, like interrupt or isochronous ones, the usb host
arranges to poll once per interval, and the gadget driver usually will
have queued some data to transfer at that time.

Returns zero, or a negative error code.  Endpoints that are not enabled
report errors; errors will also be
reported when the usb peripheral is disconnected.

.. _`usb_ep_dequeue`:

usb_ep_dequeue
==============

.. c:function:: int usb_ep_dequeue(struct usb_ep *ep, struct usb_request *req)

    dequeues (cancels, unlinks) an I/O request from an endpoint

    :param struct usb_ep \*ep:
        the endpoint associated with the request

    :param struct usb_request \*req:
        the request being canceled

.. _`usb_ep_dequeue.description`:

Description
-----------

If the request is still active on the endpoint, it is dequeued and its
completion routine is called (with status -ECONNRESET); else a negative
error code is returned. This is guaranteed to happen before the call to
\ :c:func:`usb_ep_dequeue`\  returns.

Note that some hardware can't clear out write fifos (to unlink the request
at the head of the queue) except as part of disconnecting from usb. Such
restrictions prevent drivers from supporting configuration changes,
even to configuration zero (a "chapter 9" requirement).

.. _`usb_ep_set_halt`:

usb_ep_set_halt
===============

.. c:function:: int usb_ep_set_halt(struct usb_ep *ep)

    sets the endpoint halt feature.

    :param struct usb_ep \*ep:
        the non-isochronous endpoint being stalled

.. _`usb_ep_set_halt.description`:

Description
-----------

Use this to stall an endpoint, perhaps as an error report.
Except for control endpoints,
the endpoint stays halted (will not stream any data) until the host
clears this feature; drivers may need to empty the endpoint's request
queue first, to make sure no inappropriate transfers happen.

Note that while an endpoint CLEAR_FEATURE will be invisible to the
gadget driver, a SET_INTERFACE will not be.  To reset endpoints for the
current altsetting, see \ :c:func:`usb_ep_clear_halt`\ .  When switching altsettings,
it's simplest to use \ :c:func:`usb_ep_enable`\  or \ :c:func:`usb_ep_disable`\  for the endpoints.

Returns zero, or a negative error code.  On success, this call sets
underlying hardware state that blocks data transfers.
Attempts to halt IN endpoints will fail (returning -EAGAIN) if any
transfer requests are still queued, or if the controller hardware
(usually a FIFO) still holds bytes that the host hasn't collected.

.. _`usb_ep_clear_halt`:

usb_ep_clear_halt
=================

.. c:function:: int usb_ep_clear_halt(struct usb_ep *ep)

    clears endpoint halt, and resets toggle

    :param struct usb_ep \*ep:
        the bulk or interrupt endpoint being reset

.. _`usb_ep_clear_halt.description`:

Description
-----------

Use this when responding to the standard usb "set interface" request,
for endpoints that aren't reconfigured, after clearing any other state
in the endpoint's i/o queue.

Returns zero, or a negative error code.  On success, this call clears
the underlying hardware state reflecting endpoint halt and data toggle.
Note that some hardware can't support this request (like pxa2xx_udc),
and accordingly can't correctly implement interface altsettings.

.. _`usb_ep_set_wedge`:

usb_ep_set_wedge
================

.. c:function:: int usb_ep_set_wedge(struct usb_ep *ep)

    sets the halt feature and ignores clear requests

    :param struct usb_ep \*ep:
        the endpoint being wedged

.. _`usb_ep_set_wedge.description`:

Description
-----------

Use this to stall an endpoint and ignore CLEAR_FEATURE(HALT_ENDPOINT)
requests. If the gadget driver clears the halt status, it will
automatically unwedge the endpoint.

Returns zero on success, else negative errno.

.. _`usb_ep_fifo_status`:

usb_ep_fifo_status
==================

.. c:function:: int usb_ep_fifo_status(struct usb_ep *ep)

    returns number of bytes in fifo, or error

    :param struct usb_ep \*ep:
        the endpoint whose fifo status is being checked.

.. _`usb_ep_fifo_status.description`:

Description
-----------

FIFO endpoints may have "unclaimed data" in them in certain cases,
such as after aborted transfers.  Hosts may not have collected all
the IN data written by the gadget driver (and reported by a request
completion).  The gadget driver may not have collected all the data
written OUT to it by the host.  Drivers that need precise handling for
fault reporting or recovery may need to use this call.

This returns the number of such bytes in the fifo, or a negative
errno if the endpoint doesn't use a FIFO or doesn't support such
precise handling.

.. _`usb_ep_fifo_flush`:

usb_ep_fifo_flush
=================

.. c:function:: void usb_ep_fifo_flush(struct usb_ep *ep)

    flushes contents of a fifo

    :param struct usb_ep \*ep:
        the endpoint whose fifo is being flushed.

.. _`usb_ep_fifo_flush.description`:

Description
-----------

This call may be used to flush the "unclaimed data" that may exist in
an endpoint fifo after abnormal transaction terminations.  The call
must never be used except when endpoint is not being used for any
protocol translation.

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

.. _`usb_ep_align_maybe`:

usb_ep_align_maybe
==================

.. c:function:: size_t usb_ep_align_maybe(struct usb_gadget *g, struct usb_ep *ep, size_t len)

    returns \ ``len``\  aligned to ep's maxpacketsize if gadget requires quirk_ep_out_aligned_size, otherwise reguens len.

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

.. _`usb_gadget_frame_number`:

usb_gadget_frame_number
=======================

.. c:function:: int usb_gadget_frame_number(struct usb_gadget *gadget)

    returns the current frame number

    :param struct usb_gadget \*gadget:
        controller that reports the frame number

.. _`usb_gadget_frame_number.description`:

Description
-----------

Returns the usb frame number, normally eleven bits from a SOF packet,
or negative errno if this device doesn't support this capability.

.. _`usb_gadget_wakeup`:

usb_gadget_wakeup
=================

.. c:function:: int usb_gadget_wakeup(struct usb_gadget *gadget)

    tries to wake up the host connected to this gadget

    :param struct usb_gadget \*gadget:
        controller used to wake up the host

.. _`usb_gadget_wakeup.description`:

Description
-----------

Returns zero on success, else negative error code if the hardware
doesn't support such attempts, or its support has not been enabled
by the usb host.  Drivers must return device descriptors that report
their ability to support this, or hosts won't enable it.

This may also try to use SRP to wake the host and start enumeration,
even if OTG isn't otherwise in use.  OTG devices may also start
remote wakeup even when hosts don't explicitly enable it.

.. _`usb_gadget_set_selfpowered`:

usb_gadget_set_selfpowered
==========================

.. c:function:: int usb_gadget_set_selfpowered(struct usb_gadget *gadget)

    sets the device selfpowered feature.

    :param struct usb_gadget \*gadget:
        the device being declared as self-powered

.. _`usb_gadget_set_selfpowered.description`:

Description
-----------

this affects the device status reported by the hardware driver
to reflect that it now has a local power supply.

returns zero on success, else negative errno.

.. _`usb_gadget_clear_selfpowered`:

usb_gadget_clear_selfpowered
============================

.. c:function:: int usb_gadget_clear_selfpowered(struct usb_gadget *gadget)

    clear the device selfpowered feature.

    :param struct usb_gadget \*gadget:
        the device being declared as bus-powered

.. _`usb_gadget_clear_selfpowered.description`:

Description
-----------

this affects the device status reported by the hardware driver.
some hardware may not support bus-powered operation, in which
case this feature's value can never change.

returns zero on success, else negative errno.

.. _`usb_gadget_vbus_connect`:

usb_gadget_vbus_connect
=======================

.. c:function:: int usb_gadget_vbus_connect(struct usb_gadget *gadget)

    Notify controller that VBUS is powered

    :param struct usb_gadget \*gadget:
        The device which now has VBUS power.

.. _`usb_gadget_vbus_connect.context`:

Context
-------

can sleep

.. _`usb_gadget_vbus_connect.description`:

Description
-----------

This call is used by a driver for an external transceiver (or GPIO)
that detects a VBUS power session starting.  Common responses include
resuming the controller, activating the D+ (or D-) pullup to let the
host detect that a USB device is attached, and starting to draw power
(8mA or possibly more, especially after SET_CONFIGURATION).

Returns zero on success, else negative errno.

.. _`usb_gadget_vbus_draw`:

usb_gadget_vbus_draw
====================

.. c:function:: int usb_gadget_vbus_draw(struct usb_gadget *gadget, unsigned mA)

    constrain controller's VBUS power usage

    :param struct usb_gadget \*gadget:
        The device whose VBUS usage is being described

    :param unsigned mA:
        How much current to draw, in milliAmperes.  This should be twice
        the value listed in the configuration descriptor bMaxPower field.

.. _`usb_gadget_vbus_draw.description`:

Description
-----------

This call is used by gadget drivers during SET_CONFIGURATION calls,
reporting how much power the device may consume.  For example, this
could affect how quickly batteries are recharged.

Returns zero on success, else negative errno.

.. _`usb_gadget_vbus_disconnect`:

usb_gadget_vbus_disconnect
==========================

.. c:function:: int usb_gadget_vbus_disconnect(struct usb_gadget *gadget)

    notify controller about VBUS session end

    :param struct usb_gadget \*gadget:
        the device whose VBUS supply is being described

.. _`usb_gadget_vbus_disconnect.context`:

Context
-------

can sleep

.. _`usb_gadget_vbus_disconnect.description`:

Description
-----------

This call is used by a driver for an external transceiver (or GPIO)
that detects a VBUS power session ending.  Common responses include
reversing everything done in \ :c:func:`usb_gadget_vbus_connect`\ .

Returns zero on success, else negative errno.

.. _`usb_gadget_connect`:

usb_gadget_connect
==================

.. c:function:: int usb_gadget_connect(struct usb_gadget *gadget)

    software-controlled connect to USB host

    :param struct usb_gadget \*gadget:
        the peripheral being connected

.. _`usb_gadget_connect.description`:

Description
-----------

Enables the D+ (or potentially D-) pullup.  The host will start
enumerating this gadget when the pullup is active and a VBUS session
is active (the link is powered).  This pullup is always enabled unless
\ :c:func:`usb_gadget_disconnect`\  has been used to disable it.

Returns zero on success, else negative errno.

.. _`usb_gadget_disconnect`:

usb_gadget_disconnect
=====================

.. c:function:: int usb_gadget_disconnect(struct usb_gadget *gadget)

    software-controlled disconnect from USB host

    :param struct usb_gadget \*gadget:
        the peripheral being disconnected

.. _`usb_gadget_disconnect.description`:

Description
-----------

Disables the D+ (or potentially D-) pullup, which the host may see
as a disconnect (when a VBUS session is active).  Not all systems
support software pullup controls.

Returns zero on success, else negative errno.

.. _`usb_gadget_deactivate`:

usb_gadget_deactivate
=====================

.. c:function:: int usb_gadget_deactivate(struct usb_gadget *gadget)

    deactivate function which is not ready to work

    :param struct usb_gadget \*gadget:
        the peripheral being deactivated

.. _`usb_gadget_deactivate.description`:

Description
-----------

This routine may be used during the gadget driver \ :c:func:`bind`\  call to prevent
the peripheral from ever being visible to the USB host, unless later
\ :c:func:`usb_gadget_activate`\  is called.  For example, user mode components may
need to be activated before the system can talk to hosts.

Returns zero on success, else negative errno.

.. _`usb_gadget_activate`:

usb_gadget_activate
===================

.. c:function:: int usb_gadget_activate(struct usb_gadget *gadget)

    activate function which is not ready to work

    :param struct usb_gadget \*gadget:
        the peripheral being activated

.. _`usb_gadget_activate.description`:

Description
-----------

This routine activates gadget which was previously deactivated with
\ :c:func:`usb_gadget_deactivate`\  call. It calls \ :c:func:`usb_gadget_connect`\  if needed.

Returns zero on success, else negative errno.

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
        int (* bind) (struct usb_gadget *gadget,struct usb_gadget_driver *driver);
        void (* unbind) (struct usb_gadget *);
        int (* setup) (struct usb_gadget *,const struct usb_ctrlrequest *);
        void (* disconnect) (struct usb_gadget *);
        void (* suspend) (struct usb_gadget *);
        void (* resume) (struct usb_gadget *);
        void (* reset) (struct usb_gadget *);
        struct device_driver driver;
        char *udc_name;
        struct list_head pending;
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
The @\ :c:func:`bind`\  function will be called to bind it to a gadget before this
registration call returns.  It's expected that the @\ :c:func:`bind`\  function will
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

