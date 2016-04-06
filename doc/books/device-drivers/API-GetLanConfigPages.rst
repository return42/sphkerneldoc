
.. _API-GetLanConfigPages:

=================
GetLanConfigPages
=================

*man GetLanConfigPages(9)*

*4.6.0-rc1*

Fetch LANConfig pages.


Synopsis
========

.. c:function:: int GetLanConfigPages( MPT_ADAPTER * ioc )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure


Return
======

0 for success -ENOMEM if no memory available -EPERM if not allowed due to ISR context -EAGAIN if no msg frames currently available -EFAULT for non-successful reply or no reply
(timeout)
