
.. _API-usb-sg-cancel:

=============
usb_sg_cancel
=============

*man usb_sg_cancel(9)*

*4.6.0-rc1*

stop scatter/gather i/o issued by ``usb_sg_wait``


Synopsis
========

.. c:function:: void usb_sg_cancel( struct usb_sg_request * io )

Arguments
=========

``io``
    request block, initialized with ``usb_sg_init``


Description
===========

This stops a request after it has been started by ``usb_sg_wait``. It can also prevents one initialized by ``usb_sg_init`` from starting, so that call just frees resources
allocated to the request.
