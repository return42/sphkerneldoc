.. -*- coding: utf-8; mode: rst -*-

.. _API-GetLanConfigPages:

=================
GetLanConfigPages
=================

*man GetLanConfigPages(9)*

*4.6.0-rc5*

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
