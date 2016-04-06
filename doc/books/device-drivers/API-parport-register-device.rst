
.. _API-parport-register-device:

=======================
parport_register_device
=======================

*man parport_register_device(9)*

*4.6.0-rc1*

register a device on a parallel port


Synopsis
========

.. c:function:: struct pardevice ⋆ parport_register_device( struct parport * port, const char * name, int (*pf) void *, void (*kf) void *, void (*irq_func) void *, int flags, void * handle )

Arguments
=========

``port``
    port to which the device is attached

``name``
    a name to refer to the device

``pf``
    preemption callback

``kf``
    kick callback (wake-up)

``irq_func``
    interrupt handler

``flags``
    registration flags

``handle``
    data for callback functions


Description
===========

This function, called by parallel port device drivers, declares that a device is connected to a port, and tells the system all it needs to know.

The ``name`` is allocated by the caller and must not be deallocated until the caller calls ``parport_unregister_device`` for that device.

The preemption callback function, ``pf``, is called when this device driver has claimed access to the port but another device driver wants to use it. It is given ``handle`` as its
parameter, and should return zero if it is willing for the system to release the port to another driver on its behalf. If it wants to keep control of the port it should return
non-zero, and no action will be taken. It is good manners for the driver to try to release the port at the earliest opportunity after its preemption callback rejects a preemption
attempt. Note that if a preemption callback is happy for preemption to go ahead, there is no need to release the port; it is done automatically. This function may not block, as it
may be called from interrupt context. If the device driver does not support preemption, ``pf`` can be ``NULL``.

The wake-up (“kick”) callback function, ``kf``, is called when the port is available to be claimed for exclusive access; that is, ``parport_claim`` is guaranteed to succeed when
called from inside the wake-up callback function. If the driver wants to claim the port it should do so; otherwise, it need not take any action. This function may not block, as it
may be called from interrupt context. If the device driver does not want to be explicitly invited to claim the port in this way, ``kf`` can be ``NULL``.

The interrupt handler, ``irq_func``, is called when an interrupt arrives from the parallel port. Note that if a device driver wants to use interrupts it should use
``parport_enable_irq``, and can also check the irq member of the parport structure representing the port.

The parallel port (lowlevel) driver is the one that has called ``request_irq`` and whose interrupt handler is called first. This handler does whatever needs to be done to the
hardware to acknowledge the interrupt (for PC-style ports there is nothing special to be done). It then tells the IEEE 1284 code about the interrupt, which may involve reacting to
an IEEE 1284 event depending on the current IEEE 1284 phase. After this, it calls ``irq_func``. Needless to say, ``irq_func`` will be called from interrupt context, and may not
block.

The ``PARPORT_DEV_EXCL`` flag is for preventing port sharing, and so should only be used when sharing the port with other device drivers is impossible and would lead to incorrect
behaviour. Use it sparingly! Normally, ``flags`` will be zero.

This function returns a pointer to a structure that represents the device on the port, or ``NULL`` if there is not enough memory to allocate space for that structure.
