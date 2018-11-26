.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/chipidea/udc.c

.. _`hw_ep_bit`:

hw_ep_bit
=========

.. c:function:: int hw_ep_bit(int num, int dir)

    calculates the bit number

    :param num:
        endpoint number
    :type num: int

    :param dir:
        endpoint direction
    :type dir: int

.. _`hw_ep_bit.description`:

Description
-----------

This function returns bit number

.. _`hw_device_state`:

hw_device_state
===============

.. c:function:: int hw_device_state(struct ci_hdrc *ci, u32 dma)

    enables/disables interrupts (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param dma:
        0 => disable, !0 => enable and set dma engine
    :type dma: u32

.. _`hw_device_state.description`:

Description
-----------

This function returns an error code

.. _`hw_ep_flush`:

hw_ep_flush
===========

.. c:function:: int hw_ep_flush(struct ci_hdrc *ci, int num, int dir)

    flush endpoint fifo (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param num:
        endpoint number
    :type num: int

    :param dir:
        endpoint direction
    :type dir: int

.. _`hw_ep_flush.description`:

Description
-----------

This function returns an error code

.. _`hw_ep_disable`:

hw_ep_disable
=============

.. c:function:: int hw_ep_disable(struct ci_hdrc *ci, int num, int dir)

    disables endpoint (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param num:
        endpoint number
    :type num: int

    :param dir:
        endpoint direction
    :type dir: int

.. _`hw_ep_disable.description`:

Description
-----------

This function returns an error code

.. _`hw_ep_enable`:

hw_ep_enable
============

.. c:function:: int hw_ep_enable(struct ci_hdrc *ci, int num, int dir, int type)

    enables endpoint (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param num:
        endpoint number
    :type num: int

    :param dir:
        endpoint direction
    :type dir: int

    :param type:
        endpoint type
    :type type: int

.. _`hw_ep_enable.description`:

Description
-----------

This function returns an error code

.. _`hw_ep_get_halt`:

hw_ep_get_halt
==============

.. c:function:: int hw_ep_get_halt(struct ci_hdrc *ci, int num, int dir)

    return endpoint halt status

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param num:
        endpoint number
    :type num: int

    :param dir:
        endpoint direction
    :type dir: int

.. _`hw_ep_get_halt.description`:

Description
-----------

This function returns 1 if endpoint halted

.. _`hw_ep_prime`:

hw_ep_prime
===========

.. c:function:: int hw_ep_prime(struct ci_hdrc *ci, int num, int dir, int is_ctrl)

    primes endpoint (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param num:
        endpoint number
    :type num: int

    :param dir:
        endpoint direction
    :type dir: int

    :param is_ctrl:
        true if control endpoint
    :type is_ctrl: int

.. _`hw_ep_prime.description`:

Description
-----------

This function returns an error code

.. _`hw_ep_set_halt`:

hw_ep_set_halt
==============

.. c:function:: int hw_ep_set_halt(struct ci_hdrc *ci, int num, int dir, int value)

    configures ep halt & resets data toggle after clear (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param num:
        endpoint number
    :type num: int

    :param dir:
        endpoint direction
    :type dir: int

    :param value:
        true => stall, false => unstall
    :type value: int

.. _`hw_ep_set_halt.description`:

Description
-----------

This function returns an error code

.. _`hw_port_is_high_speed`:

hw_port_is_high_speed
=====================

.. c:function:: int hw_port_is_high_speed(struct ci_hdrc *ci)

    test if port is high speed

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. _`hw_port_is_high_speed.description`:

Description
-----------

This function returns true if high speed port

.. _`hw_test_and_clear_complete`:

hw_test_and_clear_complete
==========================

.. c:function:: int hw_test_and_clear_complete(struct ci_hdrc *ci, int n)

    test & clear complete status (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param n:
        endpoint number
    :type n: int

.. _`hw_test_and_clear_complete.description`:

Description
-----------

This function returns complete status

.. _`hw_test_and_clear_intr_active`:

hw_test_and_clear_intr_active
=============================

.. c:function:: u32 hw_test_and_clear_intr_active(struct ci_hdrc *ci)

    test & clear active interrupts (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. _`hw_test_and_clear_intr_active.description`:

Description
-----------

This function returns active interrutps

.. _`hw_test_and_clear_setup_guard`:

hw_test_and_clear_setup_guard
=============================

.. c:function:: int hw_test_and_clear_setup_guard(struct ci_hdrc *ci)

    test & clear setup guard (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. _`hw_test_and_clear_setup_guard.description`:

Description
-----------

This function returns guard value

.. _`hw_test_and_set_setup_guard`:

hw_test_and_set_setup_guard
===========================

.. c:function:: int hw_test_and_set_setup_guard(struct ci_hdrc *ci)

    test & set setup guard (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. _`hw_test_and_set_setup_guard.description`:

Description
-----------

This function returns guard value

.. _`hw_usb_set_address`:

hw_usb_set_address
==================

.. c:function:: void hw_usb_set_address(struct ci_hdrc *ci, u8 value)

    configures USB address (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param value:
        new USB address
    :type value: u8

.. _`hw_usb_set_address.description`:

Description
-----------

This function explicitly sets the address, without the "USBADRA" (advance)
feature, which is not supported by older versions of the controller.

.. _`hw_usb_reset`:

hw_usb_reset
============

.. c:function:: int hw_usb_reset(struct ci_hdrc *ci)

    restart device after a bus reset (execute without interruption)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. _`hw_usb_reset.description`:

Description
-----------

This function returns an error code

.. _`_usb_addr`:

\_usb_addr
==========

.. c:function:: u8 _usb_addr(struct ci_hw_ep *ep)

    calculates endpoint address from direction & number

    :param ep:
        endpoint
    :type ep: struct ci_hw_ep \*

.. _`_hardware_enqueue`:

\_hardware_enqueue
==================

.. c:function:: int _hardware_enqueue(struct ci_hw_ep *hwep, struct ci_hw_req *hwreq)

    configures a request at hardware level

    :param hwep:
        endpoint
    :type hwep: struct ci_hw_ep \*

    :param hwreq:
        request
    :type hwreq: struct ci_hw_req \*

.. _`_hardware_enqueue.description`:

Description
-----------

This function returns an error code

.. _`_hardware_dequeue`:

\_hardware_dequeue
==================

.. c:function:: int _hardware_dequeue(struct ci_hw_ep *hwep, struct ci_hw_req *hwreq)

    handles a request at hardware level

    :param hwep:
        endpoint
    :type hwep: struct ci_hw_ep \*

    :param hwreq:
        *undescribed*
    :type hwreq: struct ci_hw_req \*

.. _`_hardware_dequeue.description`:

Description
-----------

This function returns an error code

.. _`_ep_nuke`:

\_ep_nuke
=========

.. c:function:: int _ep_nuke(struct ci_hw_ep *hwep)

    dequeues all endpoint requests

    :param hwep:
        endpoint
    :type hwep: struct ci_hw_ep \*

.. _`_ep_nuke.description`:

Description
-----------

This function returns an error code
Caller must hold lock

.. _`_gadget_stop_activity`:

\_gadget_stop_activity
======================

.. c:function:: int _gadget_stop_activity(struct usb_gadget *gadget)

    stops all USB activity, flushes & disables all endpts

    :param gadget:
        gadget
    :type gadget: struct usb_gadget \*

.. _`_gadget_stop_activity.description`:

Description
-----------

This function returns an error code

.. _`isr_reset_handler`:

isr_reset_handler
=================

.. c:function:: void isr_reset_handler(struct ci_hdrc *ci)

    USB reset interrupt handler

    :param ci:
        UDC device
    :type ci: struct ci_hdrc \*

.. _`isr_reset_handler.description`:

Description
-----------

This function resets USB engine after a bus reset occurred

.. _`isr_get_status_complete`:

isr_get_status_complete
=======================

.. c:function:: void isr_get_status_complete(struct usb_ep *ep, struct usb_request *req)

    get_status request complete function

    :param ep:
        endpoint
    :type ep: struct usb_ep \*

    :param req:
        request handled
    :type req: struct usb_request \*

.. _`isr_get_status_complete.description`:

Description
-----------

Caller must release lock

.. _`_ep_queue`:

\_ep_queue
==========

.. c:function:: int _ep_queue(struct usb_ep *ep, struct usb_request *req, gfp_t __maybe_unused gfp_flags)

    queues (submits) an I/O request to an endpoint

    :param ep:
        endpoint
    :type ep: struct usb_ep \*

    :param req:
        request
    :type req: struct usb_request \*

    :param gfp_flags:
        GFP flags (not used)
    :type gfp_flags: gfp_t __maybe_unused

.. _`_ep_queue.description`:

Description
-----------

Caller must hold lock
This function returns an error code

.. _`isr_get_status_response`:

isr_get_status_response
=======================

.. c:function:: int isr_get_status_response(struct ci_hdrc *ci, struct usb_ctrlrequest *setup)

    get_status request response

    :param ci:
        ci struct
    :type ci: struct ci_hdrc \*

    :param setup:
        setup request packet
    :type setup: struct usb_ctrlrequest \*

.. _`isr_get_status_response.description`:

Description
-----------

This function returns an error code

.. _`isr_setup_status_complete`:

isr_setup_status_complete
=========================

.. c:function:: void isr_setup_status_complete(struct usb_ep *ep, struct usb_request *req)

    setup_status request complete function

    :param ep:
        endpoint
    :type ep: struct usb_ep \*

    :param req:
        request handled
    :type req: struct usb_request \*

.. _`isr_setup_status_complete.description`:

Description
-----------

Caller must release lock. Put the port in test mode if test mode
feature is selected.

.. _`isr_setup_status_phase`:

isr_setup_status_phase
======================

.. c:function:: int isr_setup_status_phase(struct ci_hdrc *ci)

    queues the status phase of a setup transation

    :param ci:
        ci struct
    :type ci: struct ci_hdrc \*

.. _`isr_setup_status_phase.description`:

Description
-----------

This function returns an error code

.. _`isr_tr_complete_low`:

isr_tr_complete_low
===================

.. c:function:: int isr_tr_complete_low(struct ci_hw_ep *hwep)

    transaction complete low level handler

    :param hwep:
        endpoint
    :type hwep: struct ci_hw_ep \*

.. _`isr_tr_complete_low.description`:

Description
-----------

This function returns an error code
Caller must hold lock

.. _`isr_setup_packet_handler`:

isr_setup_packet_handler
========================

.. c:function:: void isr_setup_packet_handler(struct ci_hdrc *ci)

    setup packet handler

    :param ci:
        UDC descriptor
    :type ci: struct ci_hdrc \*

.. _`isr_setup_packet_handler.description`:

Description
-----------

This function handles setup packet

.. _`isr_tr_complete_handler`:

isr_tr_complete_handler
=======================

.. c:function:: void isr_tr_complete_handler(struct ci_hdrc *ci)

    transaction complete interrupt handler

    :param ci:
        UDC descriptor
    :type ci: struct ci_hdrc \*

.. _`isr_tr_complete_handler.description`:

Description
-----------

This function handles traffic events

.. _`ep_enable`:

ep_enable
=========

.. c:function:: int ep_enable(struct usb_ep *ep, const struct usb_endpoint_descriptor *desc)

    configure endpoint, making it usable

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

    :param desc:
        *undescribed*
    :type desc: const struct usb_endpoint_descriptor \*

.. _`ep_enable.description`:

Description
-----------

Check \ :c:func:`usb_ep_enable`\  at "usb_gadget.h" for details

.. _`ep_disable`:

ep_disable
==========

.. c:function:: int ep_disable(struct usb_ep *ep)

    endpoint is no longer usable

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

.. _`ep_disable.description`:

Description
-----------

Check \ :c:func:`usb_ep_disable`\  at "usb_gadget.h" for details

.. _`ep_alloc_request`:

ep_alloc_request
================

.. c:function:: struct usb_request *ep_alloc_request(struct usb_ep *ep, gfp_t gfp_flags)

    allocate a request object to use with this endpoint

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

    :param gfp_flags:
        *undescribed*
    :type gfp_flags: gfp_t

.. _`ep_alloc_request.description`:

Description
-----------

Check \ :c:func:`usb_ep_alloc_request`\  at "usb_gadget.h" for details

.. _`ep_free_request`:

ep_free_request
===============

.. c:function:: void ep_free_request(struct usb_ep *ep, struct usb_request *req)

    frees a request object

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

    :param req:
        *undescribed*
    :type req: struct usb_request \*

.. _`ep_free_request.description`:

Description
-----------

Check \ :c:func:`usb_ep_free_request`\  at "usb_gadget.h" for details

.. _`ep_queue`:

ep_queue
========

.. c:function:: int ep_queue(struct usb_ep *ep, struct usb_request *req, gfp_t __maybe_unused gfp_flags)

    queues (submits) an I/O request to an endpoint

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

    :param req:
        *undescribed*
    :type req: struct usb_request \*

    :param gfp_flags:
        *undescribed*
    :type gfp_flags: gfp_t __maybe_unused

.. _`ep_queue.description`:

Description
-----------

Check \ :c:func:`usb_ep_queue`\ \* at usb_gadget.h" for details

.. _`ep_dequeue`:

ep_dequeue
==========

.. c:function:: int ep_dequeue(struct usb_ep *ep, struct usb_request *req)

    dequeues (cancels, unlinks) an I/O request from an endpoint

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

    :param req:
        *undescribed*
    :type req: struct usb_request \*

.. _`ep_dequeue.description`:

Description
-----------

Check \ :c:func:`usb_ep_dequeue`\  at "usb_gadget.h" for details

.. _`ep_set_halt`:

ep_set_halt
===========

.. c:function:: int ep_set_halt(struct usb_ep *ep, int value)

    sets the endpoint halt feature

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

    :param value:
        *undescribed*
    :type value: int

.. _`ep_set_halt.description`:

Description
-----------

Check \ :c:func:`usb_ep_set_halt`\  at "usb_gadget.h" for details

.. _`ep_set_wedge`:

ep_set_wedge
============

.. c:function:: int ep_set_wedge(struct usb_ep *ep)

    sets the halt feature and ignores clear requests

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

.. _`ep_set_wedge.description`:

Description
-----------

Check \ :c:func:`usb_ep_set_wedge`\  at "usb_gadget.h" for details

.. _`ep_fifo_flush`:

ep_fifo_flush
=============

.. c:function:: void ep_fifo_flush(struct usb_ep *ep)

    flushes contents of a fifo

    :param ep:
        *undescribed*
    :type ep: struct usb_ep \*

.. _`ep_fifo_flush.description`:

Description
-----------

Check \ :c:func:`usb_ep_fifo_flush`\  at "usb_gadget.h" for details

.. _`ci_udc_start`:

ci_udc_start
============

.. c:function:: int ci_udc_start(struct usb_gadget *gadget, struct usb_gadget_driver *driver)

    register a gadget driver

    :param gadget:
        our gadget
    :type gadget: struct usb_gadget \*

    :param driver:
        the driver being registered
    :type driver: struct usb_gadget_driver \*

.. _`ci_udc_start.description`:

Description
-----------

Interrupts are enabled here.

.. _`ci_udc_stop`:

ci_udc_stop
===========

.. c:function:: int ci_udc_stop(struct usb_gadget *gadget)

    unregister a gadget driver

    :param gadget:
        *undescribed*
    :type gadget: struct usb_gadget \*

.. _`udc_irq`:

udc_irq
=======

.. c:function:: irqreturn_t udc_irq(struct ci_hdrc *ci)

    ci interrupt handler

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. _`udc_irq.description`:

Description
-----------

This function returns IRQ_HANDLED if the IRQ has been handled
It locks access to registers

.. _`udc_start`:

udc_start
=========

.. c:function:: int udc_start(struct ci_hdrc *ci)

    initialize gadget role

    :param ci:
        chipidea controller
    :type ci: struct ci_hdrc \*

.. _`ci_hdrc_gadget_destroy`:

ci_hdrc_gadget_destroy
======================

.. c:function:: void ci_hdrc_gadget_destroy(struct ci_hdrc *ci)

    parent remove must call this to remove UDC

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. _`ci_hdrc_gadget_destroy.description`:

Description
-----------

No interrupts active, the IRQ has been released

.. _`ci_hdrc_gadget_init`:

ci_hdrc_gadget_init
===================

.. c:function:: int ci_hdrc_gadget_init(struct ci_hdrc *ci)

    initialize device related bits ci: the controller

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. _`ci_hdrc_gadget_init.description`:

Description
-----------

This function initializes the gadget, if the device is "device capable".

.. This file was automatic generated / don't edit.

