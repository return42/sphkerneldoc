.. -*- coding: utf-8; mode: rst -*-

.. _bugs:

**************************
Known Bugs And Assumptions
**************************

Interrupt Locking
    The locking in the driver is done via the global cli/sti lock. This
    makes for relatively poor SMP performance. Switching this to use a
    per device spin lock would probably materially improve performance.

Occasional Failures
    We have reports of occasional failures when run for very long
    periods of time and the driver starts to receive junk frames. At the
    moment the cause of this is not clear.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
