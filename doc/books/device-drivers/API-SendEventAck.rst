
.. _API-SendEventAck:

============
SendEventAck
============

*man SendEventAck(9)*

*4.6.0-rc1*

Send EventAck request to MPT adapter.


Synopsis
========

.. c:function:: int SendEventAck( MPT_ADAPTER * ioc, EventNotificationReply_t * evnp )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``evnp``
    Pointer to original EventNotification request
