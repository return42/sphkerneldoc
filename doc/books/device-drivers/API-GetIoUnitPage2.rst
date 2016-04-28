.. -*- coding: utf-8; mode: rst -*-

.. _API-GetIoUnitPage2:

==============
GetIoUnitPage2
==============

*man GetIoUnitPage2(9)*

*4.6.0-rc5*

Retrieve BIOS version and boot order information.


Synopsis
========

.. c:function:: int GetIoUnitPage2( MPT_ADAPTER * ioc )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure


Returns
=======

0 for success -ENOMEM if no memory available -EPERM if not allowed due
to ISR context -EAGAIN if no msg frames currently available -EFAULT for
non-successful reply or no reply (timeout)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
