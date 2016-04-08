
.. _API-request-percpu-irq:

==================
request_percpu_irq
==================

*man request_percpu_irq(9)*

*4.6.0-rc1*

allocate a percpu interrupt line


Synopsis
========

.. c:function:: int request_percpu_irq( unsigned int irq, irq_handler_t handler, const char * devname, void __percpu * dev_id )

Arguments
=========

``irq``
    Interrupt line to allocate

``handler``
    Function to be called when the IRQ occurs.

``devname``
    An ascii name for the claiming device

``dev_id``
    A percpu cookie passed back to the handler function


Description
===========

This call allocates interrupt resources and enables the interrupt on the local CPU. If the interrupt is supposed to be enabled on other CPUs, it has to be done on each CPU using
``enable_percpu_irq``.

Dev_id must be globally unique. It is a per-cpu variable, and the handler gets called with the interrupted CPU's instance of that variable.
