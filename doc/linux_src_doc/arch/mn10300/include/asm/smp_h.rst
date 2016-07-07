.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/include/asm/smp.h

.. _`arch_smp_processor_id`:

arch_smp_processor_id
=====================

.. c:function::  arch_smp_processor_id( void)

    Determine the raw CPU ID of the CPU running it

    :param  void:
        no arguments

.. _`arch_smp_processor_id.description`:

Description
-----------

What we really want to do is to use the CPUID hardware CPU register to get
this information, but accesses to that aren't cached, and run at system bus
speed, not CPU speed.  A copy of this value is, however, stored in the
thread_info struct, and that can be cached.

An alternate way of dealing with this could be to use the EPSW.S bits to
cache this information for systems with up to four CPUs.

.. This file was automatic generated / don't edit.

