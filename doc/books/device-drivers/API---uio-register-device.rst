.. -*- coding: utf-8; mode: rst -*-

.. _API---uio-register-device:

=====================
__uio_register_device
=====================

*man __uio_register_device(9)*

*4.6.0-rc5*

register a new userspace IO device


Synopsis
========

.. c:function:: int __uio_register_device( struct module * owner, struct device * parent, struct uio_info * info )

Arguments
=========

``owner``
    module that creates the new device

``parent``
    parent device

``info``
    UIO device capabilities


Description
===========

returns zero on success or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
