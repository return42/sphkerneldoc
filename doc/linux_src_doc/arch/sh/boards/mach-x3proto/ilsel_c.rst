.. -*- coding: utf-8; mode: rst -*-

=======
ilsel.c
=======



.. _xref_ilsel_enable:

ilsel_enable
============

.. c:function:: int ilsel_enable (ilsel_source_t set)

    Enable an ILSEL set.

    :param ilsel_source_t set:
        ILSEL source (see ilsel_source_t enum in include/asm-sh/ilsel.h).



Description
-----------

Enables a given non-aliased ILSEL source (<= ILSEL_KEY) at the highest
available interrupt level. Callers should take care to order callsites
noting descending interrupt levels. Aliasing FPGA and external board
IRQs need to use :c:func:`ilsel_enable_fixed`.


The return value is an IRQ number that can later be taken down with
:c:func:`ilsel_disable`.




.. _xref_ilsel_enable_fixed:

ilsel_enable_fixed
==================

.. c:function:: int ilsel_enable_fixed (ilsel_source_t set, unsigned int level)

    Enable an ILSEL set at a fixed interrupt level

    :param ilsel_source_t set:
        ILSEL source (see ilsel_source_t enum in include/asm-sh/ilsel.h).

    :param unsigned int level:
        Interrupt level (1 - 15)



Description
-----------

Enables a given ILSEL source at a fixed interrupt level. Necessary
both for level reservation as well as for aliased sources that only
exist on special ILSEL#s.


Returns an IRQ number (as :c:func:`ilsel_enable`).




.. _xref_ilsel_disable:

ilsel_disable
=============

.. c:function:: void ilsel_disable (unsigned int irq)

    Disable an ILSEL set

    :param unsigned int irq:
        Bit position for ILSEL set value (retval from enable routines)



Description
-----------

Disable a previously enabled ILSEL set.


