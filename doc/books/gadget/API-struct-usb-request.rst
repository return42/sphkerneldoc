.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-request:

==================
struct usb_request
==================

*man struct usb_request(9)*

*4.6.0-rc5*

describes one i/o request


Synopsis
========

.. code-block:: c

    struct usb_request {
      void * buf;
      unsigned length;
      dma_addr_t dma;
      struct scatterlist * sg;
      unsigned num_sgs;
      unsigned num_mapped_sgs;
      unsigned stream_id:16;
      unsigned no_interrupt:1;
      unsigned zero:1;
      unsigned short_not_ok:1;
      void (* complete) (struct usb_ep *ep,struct usb_request *req);
      void * context;
      struct list_head list;
      int status;
      unsigned actual;
    };


Members
=======

buf
    Buffer used for data. Always provide this; some controllers only use
    PIO, or don't use DMA for some endpoints.

length
    Length of that data

dma
    DMA address corresponding to 'buf'. If you don't set this field, and
    the usb controller needs one, it is responsible for mapping and
    unmapping the buffer.

sg
    a scatterlist for SG-capable controllers.

num_sgs
    number of SG entries

num_mapped_sgs
    number of SG entries mapped to DMA (internal)

stream_id
    The stream id, when USB3.0 bulk streams are being used

no_interrupt
    If true, hints that no completion irq is needed. Helpful sometimes
    with deep request queues that are handled directly by DMA
    controllers.

zero
    If true, when writing data, makes the last packet be “short” by
    adding a zero length packet as needed;

short_not_ok
    When reading data, makes short packets be treated as errors (queue
    stops advancing till cleanup).

complete
    Function called when request completes, so this request and its
    buffer may be re-used. The function will always be called with
    interrupts disabled, and it must not sleep. Reads terminate with a
    short packet, or when the buffer fills, whichever comes first. When
    writes terminate, some data bytes will usually still be in flight
    (often in a hardware fifo). Errors (for reads or writes) stop the
    queue from advancing until the completion function returns, so that
    any transfers invalidated by the error may first be dequeued.

context
    For use by the completion callback

list
    For use by the gadget driver.

status
    Reports completion code, zero or a negative errno. Normally, faults
    block the transfer queue from advancing until the completion
    callback returns. Code “-ESHUTDOWN” indicates completion caused by
    device disconnect, or when the driver disabled the endpoint.

actual
    Reports bytes transferred to/from the buffer. For reads (OUT
    transfers) this may be less than the requested length. If the
    short_not_ok flag is set, short reads are treated as errors even
    when status otherwise indicates successful completion. Note that for
    writes (IN transfers) some data bytes may still reside in a
    device-side FIFO when the request is reported as complete.


Description
===========

These are allocated/freed through the endpoint they're used with. The
hardware's driver can add extra per-request data to the memory it
returns, which often avoids separate memory allocations (potential
failures), later when the request is queued.

Request flags affect request handling, such as whether a zero length
packet is written (the “zero” flag), whether a short read should be
treated as an error (blocking request queue advance, the
“short_not_ok” flag), or hinting that an interrupt is not required
(the “no_interrupt” flag, for use with deep request queues).

Bulk endpoints can use any size buffers, and can also be used for
interrupt transfers. interrupt-only endpoints can be much less
functional.


NOTE
====

this is analogous to 'struct urb' on the host side, except that it's
thinner and promotes more pre-allocation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
