
.. _API-z8530-rtsdtr:

============
z8530_rtsdtr
============

*man z8530_rtsdtr(9)*

*4.6.0-rc1*

Control the outgoing DTS/RTS line


Synopsis
========

.. c:function:: void z8530_rtsdtr( struct z8530_channel * c, int set )

Arguments
=========

``c``
    The Z8530 channel to control;

``set``
    1 to set, 0 to clear


Description
===========

Sets or clears DTR/RTS on the requested line. All locking is handled by the caller. For now we assume all boards use the actual RTS/DTR on the chip. Apparently one or two don't.
We'll scream about them later.
