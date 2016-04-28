.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-sg-request:

=====================
struct usb_sg_request
=====================

*man struct usb_sg_request(9)*

*4.6.0-rc5*

support for scatter/gather I/O


Synopsis
========

.. code-block:: c

    struct usb_sg_request {
      int status;
      size_t bytes;
    };


Members
=======

status
    zero indicates success, else negative errno

bytes
    counts bytes transferred.


Description
===========

These requests are initialized using ``usb_sg_init``, and then are used
as request handles passed to ``usb_sg_wait`` or ``usb_sg_cancel``. Most
members of the request object aren't for driver access.

The status and bytecount values are valid only after ``usb_sg_wait``
returns. If the status is zero, then the bytecount matches the total
from the request.

After an error completion, drivers may need to clear a halt condition on
the endpoint.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
