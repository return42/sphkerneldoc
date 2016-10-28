.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/kernel/irq.c

.. _`tbisig_map`:

tbisig_map
==========

.. c:function:: int tbisig_map(unsigned int hw)

    Map a TBI signal number to a virtual IRQ number.

    :param unsigned int hw:
        Number of the TBI signal. Must be in range.

.. _`tbisig_map.return`:

Return
------

The virtual IRQ number of the TBI signal number IRQ specified by
\ ``hw``\ .

.. _`metag_tbisig_map`:

metag_tbisig_map
================

.. c:function:: int metag_tbisig_map(struct irq_domain *d, unsigned int irq, irq_hw_number_t hw)

    map a tbi signal to a Linux virtual IRQ number

    :param struct irq_domain \*d:
        root irq domain

    :param unsigned int irq:
        virtual irq number

    :param irq_hw_number_t hw:
        hardware irq number (TBI signal number)

.. _`metag_tbisig_map.description`:

Description
-----------

This sets up a virtual irq for a specified TBI signal number.

.. This file was automatic generated / don't edit.

