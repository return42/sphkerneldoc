
.. _API-parport-wait-event:

==================
parport_wait_event
==================

*man parport_wait_event(9)*

*4.6.0-rc1*

wait for an event on a parallel port


Synopsis
========

.. c:function:: int parport_wait_event( struct parport * port, signed long timeout )

Arguments
=========

``port``
    port to wait on

``timeout``
    time to wait (in jiffies)


Description
===========

This function waits for up to ``timeout`` jiffies for an interrupt to occur on a parallel port. If the port timeout is set to zero, it returns immediately.

If an interrupt occurs before the timeout period elapses, this function returns zero immediately. If it times out, it returns one. An error code less than zero indicates an error
(most likely a pending signal), and the calling code should finish what it's doing as soon as it can.
