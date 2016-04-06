
.. _API-ProcessEventNotification:

========================
ProcessEventNotification
========================

*man ProcessEventNotification(9)*

*4.6.0-rc1*

Route EventNotificationReply to all event handlers


Synopsis
========

.. c:function:: int ProcessEventNotification( MPT_ADAPTER * ioc, EventNotificationReply_t * pEventReply, int * evHandlers )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``pEventReply``
    Pointer to EventNotification reply frame

``evHandlers``
    Pointer to integer, number of event handlers


Description
===========

Routes a received EventNotificationReply to all currently registered event handlers. Returns sum of event handlers return values.
