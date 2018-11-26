.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/cevt-r4k.c

.. _`calculate_min_delta`:

calculate_min_delta
===================

.. c:function:: unsigned int calculate_min_delta( void)

    Calculate a good minimum delta for \ :c:func:`mips_next_event`\ .

    :param void:
        no arguments
    :type void: 

.. _`calculate_min_delta.description`:

Description
-----------

Running under virtualisation can introduce overhead into \ :c:func:`mips_next_event`\  in
the form of hypervisor emulation of CP0_Count/CP0_Compare registers,
potentially with an unnatural frequency, which makes a fixed min_delta_ns
value inappropriate as it may be too small.

It can also introduce occasional latency from the guest being descheduled.

This function calculates a good minimum delta based roughly on the 75th
percentile of the time taken to do the \ :c:func:`mips_next_event`\  sequence, in order
to handle potentially higher overhead while also eliminating outliers due to
unpredictable hypervisor latency (which can be handled by retries).

.. _`calculate_min_delta.return`:

Return
------

An appropriate minimum delta for the clock event device.

.. This file was automatic generated / don't edit.

