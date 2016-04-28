.. -*- coding: utf-8; mode: rst -*-

.. _API-ProcessEventNotification:

========================
ProcessEventNotification
========================

*man ProcessEventNotification(9)*

*4.6.0-rc5*

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

Routes a received EventNotificationReply to all currently registered
event handlers. Returns sum of event handlers return values.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
