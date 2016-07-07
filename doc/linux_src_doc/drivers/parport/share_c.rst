.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parport/share.c

.. _`__parport_register_driver`:

__parport_register_driver
=========================

.. c:function:: int __parport_register_driver(struct parport_driver *drv, struct module *owner, const char *mod_name)

    register a parallel port device driver

    :param struct parport_driver \*drv:
        structure describing the driver

    :param struct module \*owner:
        owner module of drv

    :param const char \*mod_name:
        module name string

.. _`__parport_register_driver.description`:

Description
-----------

This can be called by a parallel port device driver in order
to receive notifications about ports being found in the
system, as well as ports no longer available.

If devmodel is true then the new device model is used
for registration.

The \ ``drv``\  structure is allocated by the caller and must not be
deallocated until after calling \ :c:func:`parport_unregister_driver`\ .

.. _`__parport_register_driver.if-using-the-non-device-model`:

If using the non device model
-----------------------------

The driver's \ :c:func:`attach`\  function may block.  The port that
\ :c:func:`attach`\  is given will be valid for the duration of the
callback, but if the driver wants to take a copy of the
pointer it must call \ :c:func:`parport_get_port`\  to do so.  Calling
\ :c:func:`parport_register_device`\  on that port will do this for you.

The driver's \ :c:func:`detach`\  function may block.  The port that
\ :c:func:`detach`\  is given will be valid for the duration of the
callback, but if the driver wants to take a copy of the
pointer it must call \ :c:func:`parport_get_port`\  to do so.


Returns 0 on success. The non device model will always succeeds.
but the new device model can fail and will return the error code.

.. _`parport_unregister_driver`:

parport_unregister_driver
=========================

.. c:function:: void parport_unregister_driver(struct parport_driver *drv)

    deregister a parallel port device driver

    :param struct parport_driver \*drv:
        structure describing the driver that was given to
        \ :c:func:`parport_register_driver`\ 

.. _`parport_unregister_driver.description`:

Description
-----------

This should be called by a parallel port device driver that
has registered itself using \ :c:func:`parport_register_driver`\  when it
is about to be unloaded.

When it returns, the driver's \ :c:func:`attach`\  routine will no longer
be called, and for each port that \ :c:func:`attach`\  was called for, the
\ :c:func:`detach`\  routine will have been called.

All the driver's \ :c:func:`attach`\  and \ :c:func:`detach`\  calls are guaranteed to have
finished by the time this function returns.

.. _`parport_get_port`:

parport_get_port
================

.. c:function:: struct parport *parport_get_port(struct parport *port)

    increment a port's reference count

    :param struct parport \*port:
        the port

.. _`parport_get_port.description`:

Description
-----------

This ensures that a struct parport pointer remains valid
until the matching \ :c:func:`parport_put_port`\  call.

.. _`parport_put_port`:

parport_put_port
================

.. c:function:: void parport_put_port(struct parport *port)

    decrement a port's reference count

    :param struct parport \*port:
        the port

.. _`parport_put_port.description`:

Description
-----------

This should be called once for each call to \ :c:func:`parport_get_port`\ ,
once the port is no longer needed. When the reference count reaches
zero (port is no longer used), free_port is called.

.. _`parport_register_port`:

parport_register_port
=====================

.. c:function:: struct parport *parport_register_port(unsigned long base, int irq, int dma, struct parport_operations *ops)

    register a parallel port

    :param unsigned long base:
        base I/O address

    :param int irq:
        IRQ line

    :param int dma:
        DMA channel

    :param struct parport_operations \*ops:
        pointer to the port driver's port operations structure

.. _`parport_register_port.description`:

Description
-----------

When a parallel port (lowlevel) driver finds a port that
should be made available to parallel port device drivers, it
should call \ :c:func:`parport_register_port`\ .  The \ ``base``\ , \ ``irq``\ , and
\ ``dma``\  parameters are for the convenience of port drivers, and
for ports where they aren't meaningful needn't be set to
anything special.  They can be altered afterwards by adjusting
the relevant members of the parport structure that is returned
and represents the port.  They should not be tampered with
after calling parport_announce_port, however.

If there are parallel port device drivers in the system that
have registered themselves using \ :c:func:`parport_register_driver`\ ,
they are not told about the port at this time; that is done by
\ :c:func:`parport_announce_port`\ .

The \ ``ops``\  structure is allocated by the caller, and must not be
deallocated before calling \ :c:func:`parport_remove_port`\ .

If there is no memory to allocate a new parport structure,
this function will return \ ``NULL``\ .

.. _`parport_announce_port`:

parport_announce_port
=====================

.. c:function:: void parport_announce_port(struct parport *port)

    tell device drivers about a parallel port

    :param struct parport \*port:
        parallel port to announce

.. _`parport_announce_port.description`:

Description
-----------

After a port driver has registered a parallel port with
parport_register_port, and performed any necessary
initialisation or adjustments, it should call
\ :c:func:`parport_announce_port`\  in order to notify all device drivers
that have called \ :c:func:`parport_register_driver`\ .  Their \ :c:func:`attach`\ 
functions will be called, with \ ``port``\  as the parameter.

.. _`parport_remove_port`:

parport_remove_port
===================

.. c:function:: void parport_remove_port(struct parport *port)

    deregister a parallel port

    :param struct parport \*port:
        parallel port to deregister

.. _`parport_remove_port.description`:

Description
-----------

When a parallel port driver is forcibly unloaded, or a
parallel port becomes inaccessible, the port driver must call
this function in order to deal with device drivers that still
want to use it.

The parport structure associated with the port has its
operations structure replaced with one containing 'null'
operations that return errors or just don't do anything.

Any drivers that have registered themselves using
\ :c:func:`parport_register_driver`\  are notified that the port is no
longer accessible by having their \ :c:func:`detach`\  routines called
with \ ``port``\  as the parameter.

.. _`parport_register_device`:

parport_register_device
=======================

.. c:function:: struct pardevice *parport_register_device(struct parport *port, const char *name, int (*) pf (void *, void (*) kf (void *, void (*) irq_func (void *, int flags, void *handle)

    register a device on a parallel port

    :param struct parport \*port:
        port to which the device is attached

    :param const char \*name:
        a name to refer to the device

    :param (int (\*) pf (void \*):
        preemption callback

    :param (void (\*) kf (void \*):
        kick callback (wake-up)

    :param (void (\*) irq_func (void \*):
        interrupt handler

    :param int flags:
        registration flags

    :param void \*handle:
        data for callback functions

.. _`parport_register_device.description`:

Description
-----------

This function, called by parallel port device drivers,
declares that a device is connected to a port, and tells the
system all it needs to know.

The \ ``name``\  is allocated by the caller and must not be
deallocated until the caller calls \ ``parport_unregister_device``\ 
for that device.

The preemption callback function, \ ``pf``\ , is called when this
device driver has claimed access to the port but another
device driver wants to use it.  It is given \ ``handle``\  as its
parameter, and should return zero if it is willing for the
system to release the port to another driver on its behalf.
If it wants to keep control of the port it should return
non-zero, and no action will be taken.  It is good manners for
the driver to try to release the port at the earliest
opportunity after its preemption callback rejects a preemption
attempt.  Note that if a preemption callback is happy for
preemption to go ahead, there is no need to release the port;
it is done automatically.  This function may not block, as it
may be called from interrupt context.  If the device driver
does not support preemption, \ ``pf``\  can be \ ``NULL``\ .

The wake-up ("kick") callback function, \ ``kf``\ , is called when
the port is available to be claimed for exclusive access; that
is, \ :c:func:`parport_claim`\  is guaranteed to succeed when called from
inside the wake-up callback function.  If the driver wants to
claim the port it should do so; otherwise, it need not take
any action.  This function may not block, as it may be called
from interrupt context.  If the device driver does not want to
be explicitly invited to claim the port in this way, \ ``kf``\  can
be \ ``NULL``\ .

The interrupt handler, \ ``irq_func``\ , is called when an interrupt
arrives from the parallel port.  Note that if a device driver
wants to use interrupts it should use \ :c:func:`parport_enable_irq`\ ,
and can also check the irq member of the parport structure
representing the port.

The parallel port (lowlevel) driver is the one that has called
\ :c:func:`request_irq`\  and whose interrupt handler is called first.
This handler does whatever needs to be done to the hardware to
acknowledge the interrupt (for PC-style ports there is nothing
special to be done).  It then tells the IEEE 1284 code about
the interrupt, which may involve reacting to an IEEE 1284
event depending on the current IEEE 1284 phase.  After this,
it calls \ ``irq_func``\ .  Needless to say, \ ``irq_func``\  will be called
from interrupt context, and may not block.

The \ ``PARPORT_DEV_EXCL``\  flag is for preventing port sharing, and
so should only be used when sharing the port with other device
drivers is impossible and would lead to incorrect behaviour.
Use it sparingly!  Normally, \ ``flags``\  will be zero.

This function returns a pointer to a structure that represents
the device on the port, or \ ``NULL``\  if there is not enough memory
to allocate space for that structure.

.. _`parport_unregister_device`:

parport_unregister_device
=========================

.. c:function:: void parport_unregister_device(struct pardevice *dev)

    deregister a device on a parallel port

    :param struct pardevice \*dev:
        pointer to structure representing device

.. _`parport_unregister_device.description`:

Description
-----------

This undoes the effect of \ :c:func:`parport_register_device`\ .

.. _`parport_find_number`:

parport_find_number
===================

.. c:function:: struct parport *parport_find_number(int number)

    find a parallel port by number

    :param int number:
        parallel port number

.. _`parport_find_number.description`:

Description
-----------

This returns the parallel port with the specified number, or
\ ``NULL``\  if there is none.

There is an implicit \ :c:func:`parport_get_port`\  done already; to throw
away the reference to the port that \ :c:func:`parport_find_number`\ 
gives you, use \ :c:func:`parport_put_port`\ .

.. _`parport_find_base`:

parport_find_base
=================

.. c:function:: struct parport *parport_find_base(unsigned long base)

    find a parallel port by base address

    :param unsigned long base:
        base I/O address

.. _`parport_find_base.description`:

Description
-----------

This returns the parallel port with the specified base
address, or \ ``NULL``\  if there is none.

There is an implicit \ :c:func:`parport_get_port`\  done already; to throw
away the reference to the port that \ :c:func:`parport_find_base`\ 
gives you, use \ :c:func:`parport_put_port`\ .

.. _`parport_claim`:

parport_claim
=============

.. c:function:: int parport_claim(struct pardevice *dev)

    claim access to a parallel port device

    :param struct pardevice \*dev:
        pointer to structure representing a device on the port

.. _`parport_claim.description`:

Description
-----------

This function will not block and so can be used from interrupt
context.  If \ :c:func:`parport_claim`\  succeeds in claiming access to
the port it returns zero and the port is available to use.  It
may fail (returning non-zero) if the port is in use by another
driver and that driver is not willing to relinquish control of
the port.

.. _`parport_claim_or_block`:

parport_claim_or_block
======================

.. c:function:: int parport_claim_or_block(struct pardevice *dev)

    claim access to a parallel port device

    :param struct pardevice \*dev:
        pointer to structure representing a device on the port

.. _`parport_claim_or_block.description`:

Description
-----------

This behaves like \ :c:func:`parport_claim`\ , but will block if necessary
to wait for the port to be free.  A return value of 1
indicates that it slept; 0 means that it succeeded without
needing to sleep.  A negative error code indicates failure.

.. _`parport_release`:

parport_release
===============

.. c:function:: void parport_release(struct pardevice *dev)

    give up access to a parallel port device

    :param struct pardevice \*dev:
        pointer to structure representing parallel port device

.. _`parport_release.description`:

Description
-----------

This function cannot fail, but it should not be called without
the port claimed.  Similarly, if the port is already claimed
you should not try claiming it again.

.. This file was automatic generated / don't edit.

