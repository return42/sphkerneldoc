
.. _API-SendEventNotification:

=====================
SendEventNotification
=====================

*man SendEventNotification(9)*

*4.6.0-rc1*

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
