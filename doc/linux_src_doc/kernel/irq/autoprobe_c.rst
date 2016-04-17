.. -*- coding: utf-8; mode: rst -*-

===========
autoprobe.c
===========


.. _`probe_irq_on`:

probe_irq_on
============

.. c:function:: unsigned long probe_irq_on ( void)

    begin an interrupt autodetect

    :param void:
        no arguments



.. _`probe_irq_on.description`:

Description
-----------


Commence probing for an interrupt. The interrupts are scanned
and a mask of potential interrupt lines is returned.



.. _`probe_irq_mask`:

probe_irq_mask
==============

.. c:function:: unsigned int probe_irq_mask (unsigned long val)

    scan a bitmap of interrupt lines

    :param unsigned long val:
        mask of interrupts to consider



.. _`probe_irq_mask.description`:

Description
-----------

Scan the interrupt lines and return a bitmap of active
autodetect interrupts. The interrupt probe logic state
is then returned to its previous value.



.. _`probe_irq_mask.note`:

Note
----

we need to scan all the irq's even though we will
only return autodetect irq numbers - just so that we reset
them all to a known state.



.. _`probe_irq_off`:

probe_irq_off
=============

.. c:function:: int probe_irq_off (unsigned long val)

    end an interrupt autodetect

    :param unsigned long val:
        mask of potential interrupts (unused)



.. _`probe_irq_off.description`:

Description
-----------

Scans the unused interrupt lines and returns the line which
appears to have triggered the interrupt. If no interrupt was
found then zero is returned. If more than one interrupt is
found then minus the first candidate is returned to indicate
their is doubt.

The interrupt probe logic state is returned to its previous
value.



.. _`probe_irq_off.bugs`:

BUGS
----

When used in a module (which arguably shouldn't happen)
nothing prevents two IRQ probe callers from overlapping. The
results of this are non-optimal.

