.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/msr.h

.. _`rdtsc`:

rdtsc
=====

.. c:function:: unsigned long long rdtsc( void)

    returns the current TSC without ordering constraints

    :param  void:
        no arguments

.. _`rdtsc.description`:

Description
-----------

\ :c:func:`rdtsc`\  returns the result of RDTSC as a 64-bit integer.  The
only ordering constraint it supplies is the ordering implied by
"asm volatile": it will put the RDTSC in the place you expect.  The
CPU can and will speculatively execute that RDTSC, though, so the
results can be non-monotonic if compared on different CPUs.

.. _`rdtsc_ordered`:

rdtsc_ordered
=============

.. c:function:: unsigned long long rdtsc_ordered( void)

    read the current TSC in program order

    :param  void:
        no arguments

.. _`rdtsc_ordered.description`:

Description
-----------

\ :c:func:`rdtsc_ordered`\  returns the result of RDTSC as a 64-bit integer.
It is ordered like a load to a global in-memory counter.  It should
be impossible to observe non-monotonic \ :c:func:`rdtsc_unordered`\  behavior
across multiple CPUs as long as the TSC is synced.

.. This file was automatic generated / don't edit.

