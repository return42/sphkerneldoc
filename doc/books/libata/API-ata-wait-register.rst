
.. _API-ata-wait-register:

=================
ata_wait_register
=================

*man ata_wait_register(9)*

*4.6.0-rc1*

wait until register value changes


Synopsis
========

.. c:function:: u32 ata_wait_register( struct ata_port * ap, void __iomem * reg, u32 mask, u32 val, unsigned long interval, unsigned long timeout )

Arguments
=========

``ap``
    ATA port to wait register for, can be NULL

``reg``
    IO-mapped register

``mask``
    Mask to apply to read register value

``val``
    Wait condition

``interval``
    polling interval in milliseconds

``timeout``
    timeout in milliseconds


Description
===========

Waiting for some bits of register to change is a common operation for ATA controllers. This function reads 32bit LE IO-mapped register ``reg`` and tests for the following
condition.

(⋆``reg`` & mask) != val

If the condition is met, it returns; otherwise, the process is repeated after ``interval_msec`` until timeout.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

The final register value.
