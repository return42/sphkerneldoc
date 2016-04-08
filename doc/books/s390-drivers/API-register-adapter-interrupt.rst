
.. _API-register-adapter-interrupt:

==========================
register_adapter_interrupt
==========================

*man register_adapter_interrupt(9)*

*4.6.0-rc1*

register adapter interrupt handler


Synopsis
========

.. c:function:: int register_adapter_interrupt( struct airq_struct * airq )

Arguments
=========

``airq``
    pointer to adapter interrupt descriptor


Description
===========

Returns 0 on success, or -EINVAL.
