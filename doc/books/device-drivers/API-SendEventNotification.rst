.. -*- coding: utf-8; mode: rst -*-

.. _API-SendEventNotification:

=====================
SendEventNotification
=====================

*man SendEventNotification(9)*

*4.6.0-rc5*

Send EventNotification (on or off) request to adapter


Synopsis
========

.. c:function:: int SendEventNotification( MPT_ADAPTER * ioc, u8 EvSwitch, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``EvSwitch``
    Event switch flags

``sleepFlag``
    Specifies whether the process can sleep


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
