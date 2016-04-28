.. -*- coding: utf-8; mode: rst -*-

.. _API-kgdb-roundup-cpus:

=================
kgdb_roundup_cpus
=================

*man kgdb_roundup_cpus(9)*

*4.6.0-rc5*

Get other CPUs into a holding pattern


Synopsis
========

.. c:function:: void kgdb_roundup_cpus( unsigned long flags )

Arguments
=========

``flags``
    Current IRQ state


Description
===========

On SMP systems, we need to get the attention of the other CPUs and get
them into a known state. This should do what is needed to get the other
CPUs to call ``kgdb_wait``. Note that on some arches, the NMI approach
is not used for rounding up all the CPUs. For example, in case of MIPS,
``smp_call_function`` is used to roundup CPUs. In this case, we have to
make sure that interrupts are enabled before calling
``smp_call_function``. The argument to this function is the flags that
will be used when restoring the interrupts. There is ``local_irq_save``
call before ``kgdb_roundup_cpus``.

On non-SMP systems, this is not called.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
