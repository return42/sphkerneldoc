
.. _API-GetIoUnitPage2:

==============
GetIoUnitPage2
==============

*man GetIoUnitPage2(9)*

*4.6.0-rc1*

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

0 for success -ENOMEM if no memory available -EPERM if not allowed due to ISR context -EAGAIN if no msg frames currently available -EFAULT for non-successful reply or no reply
(timeout)
