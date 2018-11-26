.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/core.c

.. _`usb_ep_set_maxpacket_limit`:

usb_ep_set_maxpacket_limit
==========================

.. c:function:: void usb_ep_set_maxpacket_limit(struct usb_ep *ep, unsigned maxpacket_limit)

    set maximum packet size limit for endpoint

    :param ep:
        the endpoint being configured
    :type ep: struct usb_ep \*

    :param maxpacket_limit:
        value of maximum packet size limit
    :type maxpacket_limit: unsigned

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

    :param ep:
        the endpoint being configured.  may not be the endpoint named "ep0".
        drivers discover endpoints through the ep_list of a usb_gadget.
    :type ep: struct usb_ep \*

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

This routine must be called in process context.

returns zero, or a negative error code.

.. _`usb_ep_disable`:

usb_ep_disable
==============

.. c:function:: int usb_ep_disable(struct usb_ep *ep)

    endpoint is no longer usable

    :param ep:
        the endpoint being unconfigured.  may not be the endpoint named "ep0".
    :type ep: struct usb_ep \*

.. _`usb_ep_disable.description`:

Description
-----------

no other task may be using this endpoint when this is called.
any pending and uncompleted requests will complete with status
indicating disconnect (-ESHUTDOWN) before this call returns.
gadget drivers must call \ :c:func:`usb_ep_enable`\  again before queueing
requests to the endpoint.

This routine must be called in process context.

returns zero, or a negative error code.

.. _`usb_ep_alloc_request`:

usb_ep_alloc_request
====================

.. c:function:: struct usb_request *usb_ep_alloc_request(struct usb_ep *ep, gfp_t gfp_flags)

    allocate a request object to use with this endpoint

    :param ep:
        the endpoint to be used with with the request
    :type ep: struct usb_ep \*

    :param gfp_flags:
        GFP\_\* flags to use
    :type gfp_flags: gfp_t

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

    :param ep:
        the endpoint associated with the request
    :type ep: struct usb_ep \*

    :param req:
        the request being freed
    :type req: struct usb_request \*

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

    :param ep:
        the endpoint associated with the request
    :type ep: struct usb_ep \*

    :param req:
        the request being submitted
    :type req: struct usb_request \*

    :param gfp_flags:
        GFP\_\* flags to use in case the lower level driver couldn't
        pre-allocate all necessary memory with the request.
    :type gfp_flags: gfp_t

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

Note that \ ``req``\ 's ->complete() callback must never be called from
within \ :c:func:`usb_ep_queue`\  as that can create deadlock situations.

This routine may be called in interrupt context.

Returns zero, or a negative error code.  Endpoints that are not enabled
report errors; errors will also be
reported when the usb peripheral is disconnected.

If and only if \ ``req``\  is successfully queued (the return value is zero),
\ ``req->complete``\ () will be called exactly once, when the Gadget core and
UDC are finished with the request.  When the completion function is called,
control of the request is returned to the device driver which submitted it.
The completion handler may then immediately free or reuse \ ``req``\ .

.. _`usb_ep_dequeue`:

usb_ep_dequeue
==============

.. c:function:: int usb_ep_dequeue(struct usb_ep *ep, struct usb_request *req)

    dequeues (cancels, unlinks) an I/O request from an endpoint

    :param ep:
        the endpoint associated with the request
    :type ep: struct usb_ep \*

    :param req:
        the request being canceled
    :type req: struct usb_request \*

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

This routine may be called in interrupt context.

.. _`usb_ep_set_halt`:

usb_ep_set_halt
===============

.. c:function:: int usb_ep_set_halt(struct usb_ep *ep)

    sets the endpoint halt feature.

    :param ep:
        the non-isochronous endpoint being stalled
    :type ep: struct usb_ep \*

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

This routine may be called in interrupt context.

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

    :param ep:
        the bulk or interrupt endpoint being reset
    :type ep: struct usb_ep \*

.. _`usb_ep_clear_halt.description`:

Description
-----------

Use this when responding to the standard usb "set interface" request,
for endpoints that aren't reconfigured, after clearing any other state
in the endpoint's i/o queue.

This routine may be called in interrupt context.

Returns zero, or a negative error code.  On success, this call clears
the underlying hardware state reflecting endpoint halt and data toggle.
Note that some hardware can't support this request (like pxa2xx_udc),
and accordingly can't correctly implement interface altsettings.

.. _`usb_ep_set_wedge`:

usb_ep_set_wedge
================

.. c:function:: int usb_ep_set_wedge(struct usb_ep *ep)

    sets the halt feature and ignores clear requests

    :param ep:
        the endpoint being wedged
    :type ep: struct usb_ep \*

.. _`usb_ep_set_wedge.description`:

Description
-----------

Use this to stall an endpoint and ignore CLEAR_FEATURE(HALT_ENDPOINT)
requests. If the gadget driver clears the halt status, it will
automatically unwedge the endpoint.

This routine may be called in interrupt context.

Returns zero on success, else negative errno.

.. _`usb_ep_fifo_status`:

usb_ep_fifo_status
==================

.. c:function:: int usb_ep_fifo_status(struct usb_ep *ep)

    returns number of bytes in fifo, or error

    :param ep:
        the endpoint whose fifo status is being checked.
    :type ep: struct usb_ep \*

.. _`usb_ep_fifo_status.description`:

Description
-----------

FIFO endpoints may have "unclaimed data" in them in certain cases,
such as after aborted transfers.  Hosts may not have collected all
the IN data written by the gadget driver (and reported by a request
completion).  The gadget driver may not have collected all the data
written OUT to it by the host.  Drivers that need precise handling for
fault reporting or recovery may need to use this call.

This routine may be called in interrupt context.

This returns the number of such bytes in the fifo, or a negative
errno if the endpoint doesn't use a FIFO or doesn't support such
precise handling.

.. _`usb_ep_fifo_flush`:

usb_ep_fifo_flush
=================

.. c:function:: void usb_ep_fifo_flush(struct usb_ep *ep)

    flushes contents of a fifo

    :param ep:
        the endpoint whose fifo is being flushed.
    :type ep: struct usb_ep \*

.. _`usb_ep_fifo_flush.description`:

Description
-----------

This call may be used to flush the "unclaimed data" that may exist in
an endpoint fifo after abnormal transaction terminations.  The call
must never be used except when endpoint is not being used for any
protocol translation.

This routine may be called in interrupt context.

.. _`usb_gadget_frame_number`:

usb_gadget_frame_number
=======================

.. c:function:: int usb_gadget_frame_number(struct usb_gadget *gadget)

    returns the current frame number

    :param gadget:
        controller that reports the frame number
    :type gadget: struct usb_gadget \*

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

    :param gadget:
        controller used to wake up the host
    :type gadget: struct usb_gadget \*

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

    :param gadget:
        the device being declared as self-powered
    :type gadget: struct usb_gadget \*

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

    :param gadget:
        the device being declared as bus-powered
    :type gadget: struct usb_gadget \*

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

    :param gadget:
        The device which now has VBUS power.
    :type gadget: struct usb_gadget \*

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

    :param gadget:
        The device whose VBUS usage is being described
    :type gadget: struct usb_gadget \*

    :param mA:
        How much current to draw, in milliAmperes.  This should be twice
        the value listed in the configuration descriptor bMaxPower field.
    :type mA: unsigned

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

    :param gadget:
        the device whose VBUS supply is being described
    :type gadget: struct usb_gadget \*

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

    :param gadget:
        the peripheral being connected
    :type gadget: struct usb_gadget \*

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

    :param gadget:
        the peripheral being disconnected
    :type gadget: struct usb_gadget \*

.. _`usb_gadget_disconnect.description`:

Description
-----------

Disables the D+ (or potentially D-) pullup, which the host may see
as a disconnect (when a VBUS session is active).  Not all systems
support software pullup controls.

Following a successful disconnect, invoke the ->disconnect() callback
for the current gadget driver so that UDC drivers don't need to.

Returns zero on success, else negative errno.

.. _`usb_gadget_deactivate`:

usb_gadget_deactivate
=====================

.. c:function:: int usb_gadget_deactivate(struct usb_gadget *gadget)

    deactivate function which is not ready to work

    :param gadget:
        the peripheral being deactivated
    :type gadget: struct usb_gadget \*

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

    :param gadget:
        the peripheral being activated
    :type gadget: struct usb_gadget \*

.. _`usb_gadget_activate.description`:

Description
-----------

This routine activates gadget which was previously deactivated with
\ :c:func:`usb_gadget_deactivate`\  call. It calls \ :c:func:`usb_gadget_connect`\  if needed.

Returns zero on success, else negative errno.

.. _`usb_gadget_giveback_request`:

usb_gadget_giveback_request
===========================

.. c:function:: void usb_gadget_giveback_request(struct usb_ep *ep, struct usb_request *req)

    give the request back to the gadget layer

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

    :param req:
        *undescribed*
    :type req: struct usb_request \*

.. _`usb_gadget_giveback_request.context`:

Context
-------

\ :c:func:`in_interrupt`\ 

.. _`usb_gadget_giveback_request.description`:

Description
-----------

This is called by device controller drivers in order to return the
completed request back to the gadget layer.

.. _`gadget_find_ep_by_name`:

gadget_find_ep_by_name
======================

.. c:function:: struct usb_ep *gadget_find_ep_by_name(struct usb_gadget *g, const char *name)

    returns ep whose name is the same as sting passed in second parameter or NULL if searched endpoint not found

    :param g:
        controller to check for quirk
    :type g: struct usb_gadget \*

    :param name:
        name of searched endpoint
    :type name: const char \*

.. _`usb_udc_vbus_handler`:

usb_udc_vbus_handler
====================

.. c:function:: void usb_udc_vbus_handler(struct usb_gadget *gadget, bool status)

    updates the udc core vbus status, and try to connect or disconnect gadget

    :param gadget:
        The gadget which vbus change occurs
    :type gadget: struct usb_gadget \*

    :param status:
        The vbus status
    :type status: bool

.. _`usb_udc_vbus_handler.description`:

Description
-----------

The udc driver calls it when it wants to connect or disconnect gadget
according to vbus status.

.. _`usb_gadget_udc_reset`:

usb_gadget_udc_reset
====================

.. c:function:: void usb_gadget_udc_reset(struct usb_gadget *gadget, struct usb_gadget_driver *driver)

    notifies the udc core that bus reset occurs

    :param gadget:
        The gadget which bus reset occurs
    :type gadget: struct usb_gadget \*

    :param driver:
        The gadget driver we want to notify
    :type driver: struct usb_gadget_driver \*

.. _`usb_gadget_udc_reset.description`:

Description
-----------

If the udc driver has bus reset handler, it needs to call this when the bus
reset occurs, it notifies the gadget driver that the bus reset occurs as
well as updates gadget state.

.. _`usb_gadget_udc_start`:

usb_gadget_udc_start
====================

.. c:function:: int usb_gadget_udc_start(struct usb_udc *udc)

    tells usb device controller to start up

    :param udc:
        The UDC to be started
    :type udc: struct usb_udc \*

.. _`usb_gadget_udc_start.description`:

Description
-----------

This call is issued by the UDC Class driver when it's about
to register a gadget driver to the device controller, before
calling gadget driver's \ :c:func:`bind`\  method.

It allows the controller to be powered off until strictly
necessary to have it powered on.

Returns zero on success, else negative errno.

.. _`usb_gadget_udc_stop`:

usb_gadget_udc_stop
===================

.. c:function:: void usb_gadget_udc_stop(struct usb_udc *udc)

    tells usb device controller we don't need it anymore

    :param udc:
        *undescribed*
    :type udc: struct usb_udc \*

.. _`usb_gadget_udc_stop.description`:

Description
-----------

This call is issued by the UDC Class driver after calling
gadget driver's \ :c:func:`unbind`\  method.

The details are implementation specific, but it can go as
far as powering off UDC completely and disable its data
line pullups.

.. _`usb_gadget_udc_set_speed`:

usb_gadget_udc_set_speed
========================

.. c:function:: void usb_gadget_udc_set_speed(struct usb_udc *udc, enum usb_device_speed speed)

    tells usb device controller speed supported by current driver

    :param udc:
        The device we want to set maximum speed
    :type udc: struct usb_udc \*

    :param speed:
        The maximum speed to allowed to run
    :type speed: enum usb_device_speed

.. _`usb_gadget_udc_set_speed.description`:

Description
-----------

This call is issued by the UDC Class driver before calling
\ :c:func:`usb_gadget_udc_start`\  in order to make sure that we don't try to
connect on speeds the gadget driver doesn't support.

.. _`usb_udc_release`:

usb_udc_release
===============

.. c:function:: void usb_udc_release(struct device *dev)

    release the usb_udc struct

    :param dev:
        the dev member within usb_udc
    :type dev: struct device \*

.. _`usb_udc_release.description`:

Description
-----------

This is called by driver's core in order to free memory once the last
reference is released.

.. _`usb_add_gadget_udc_release`:

usb_add_gadget_udc_release
==========================

.. c:function:: int usb_add_gadget_udc_release(struct device *parent, struct usb_gadget *gadget, void (*release)(struct device *dev))

    adds a new gadget to the udc class driver list

    :param parent:
        the parent device to this udc. Usually the controller driver's
        device.
    :type parent: struct device \*

    :param gadget:
        the gadget to be added to the list.
    :type gadget: struct usb_gadget \*

    :param void (\*release)(struct device \*dev):
        a gadget release function.

.. _`usb_add_gadget_udc_release.description`:

Description
-----------

Returns zero on success, negative errno otherwise.
Calls the gadget release function in the latter case.

.. _`usb_get_gadget_udc_name`:

usb_get_gadget_udc_name
=======================

.. c:function:: char *usb_get_gadget_udc_name( void)

    get the name of the first UDC controller This functions returns the name of the first UDC controller in the system. Please note that this interface is usefull only for legacy drivers which assume that there is only one UDC controller in the system and they need to get its name before initialization. There is no guarantee that the UDC of the returned name will be still available, when gadget driver registers itself.

    :param void:
        no arguments
    :type void: 

.. _`usb_get_gadget_udc_name.description`:

Description
-----------

Returns pointer to string with UDC controller name on success, NULL
otherwise. Caller should \ :c:func:`kfree`\  returned string.

.. _`usb_add_gadget_udc`:

usb_add_gadget_udc
==================

.. c:function:: int usb_add_gadget_udc(struct device *parent, struct usb_gadget *gadget)

    adds a new gadget to the udc class driver list

    :param parent:
        the parent device to this udc. Usually the controller
        driver's device.
    :type parent: struct device \*

    :param gadget:
        the gadget to be added to the list
    :type gadget: struct usb_gadget \*

.. _`usb_add_gadget_udc.description`:

Description
-----------

Returns zero on success, negative errno otherwise.

.. _`usb_del_gadget_udc`:

usb_del_gadget_udc
==================

.. c:function:: void usb_del_gadget_udc(struct usb_gadget *gadget)

    deletes \ ``udc``\  from udc_list

    :param gadget:
        the gadget to be removed.
    :type gadget: struct usb_gadget \*

.. _`usb_del_gadget_udc.description`:

Description
-----------

This, will call \ :c:func:`usb_gadget_unregister_driver`\  if
the \ ``udc``\  is still busy.

.. This file was automatic generated / don't edit.

