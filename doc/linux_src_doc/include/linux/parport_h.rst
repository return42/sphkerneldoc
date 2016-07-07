.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/parport.h

.. _`parport_yield`:

parport_yield
=============

.. c:function:: int parport_yield(struct pardevice *dev)

    relinquish a parallel port temporarily

    :param struct pardevice \*dev:
        a device on the parallel port

.. _`parport_yield.description`:

Description
-----------

This function relinquishes the port if it would be helpful to other
drivers to do so.  Afterwards it tries to reclaim the port using
\ :c:func:`parport_claim`\ , and the return value is the same as for
\ :c:func:`parport_claim`\ .  If it fails, the port is left unclaimed and it is
the driver's responsibility to reclaim the port.

The \ :c:func:`parport_yield`\  and \ :c:func:`parport_yield_blocking`\  functions are for
marking points in the driver at which other drivers may claim the
port and use their devices.  Yielding the port is similar to
releasing it and reclaiming it, but is more efficient because no
action is taken if there are no other devices needing the port.  In
fact, nothing is done even if there are other devices waiting but
the current device is still within its "timeslice".  The default
timeslice is half a second, but it can be adjusted via the /proc
interface.

.. _`parport_yield_blocking`:

parport_yield_blocking
======================

.. c:function:: int parport_yield_blocking(struct pardevice *dev)

    relinquish a parallel port temporarily

    :param struct pardevice \*dev:
        a device on the parallel port

.. _`parport_yield_blocking.description`:

Description
-----------

This function relinquishes the port if it would be helpful to other
drivers to do so.  Afterwards it tries to reclaim the port using
\ :c:func:`parport_claim_or_block`\ , and the return value is the same as for
\ :c:func:`parport_claim_or_block`\ .

.. This file was automatic generated / don't edit.

