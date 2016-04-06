
.. _API---test-and-clear-bit:

====================
__test_and_clear_bit
====================

*man __test_and_clear_bit(9)*

*4.6.0-rc1*

Clear a bit and return its old value


Synopsis
========

.. c:function:: int __test_and_clear_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    Bit to clear

``addr``
    Address to count from


Description
===========

This operation is non-atomic and can be reordered. If two examples of this operation race, one can appear to succeed but actually fail. You must protect multiple accesses with a
lock.


Note
====

the operation is performed atomically with respect to the local CPU, but not other CPUs. Portable code should not rely on this behaviour. KVM relies on this behaviour on x86 for
modifying memory that is also


accessed from a hypervisor on the same CPU if running in a VM
=============================================================

don't change this without also updating arch/x86/kernel/kvm.c
