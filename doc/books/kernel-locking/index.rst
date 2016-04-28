.. -*- coding: utf-8; mode: rst -*-

+++++++++++++++++++++++++++
Unreliable Guide To Locking
+++++++++++++++++++++++++++

:author:    Russell Rusty
:address:   rusty@rustcorp.com.au

**Copyright** 2003 : Rusty Russell

This documentation is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

For more details see the file COPYING in the source distribution of
Linux.


.. toctree::
    :maxdepth: 1

    intro
    races
    locks
    hardirq-context
    cheatsheet
    trylock-functions
    Examples
    common-problems
    Efficiency
    sleeping-things
    apiref-mutex
    apiref-futex
    references
    thanks

Glossary
========

preemption
Prior to 2.5, or when ``CONFIG_PREEMPT`` is unset, processes in user
context inside the kernel would not preempt each other (ie. you had that
CPU until you gave it up, except for interrupts). With the addition of
``CONFIG_PREEMPT`` in 2.5.4, this changed: when in user context, higher
priority tasks can "cut in": spinlocks were changed to disable
preemption, even on UP.

bh
Bottom Half: for historical reasons, functions with '_bh' in them often
now refer to any software interrupt, e.g. ``spin_lock_bh()`` blocks any
software interrupt on the current CPU. Bottom halves are deprecated, and
will eventually be replaced by tasklets. Only one bottom half will be
running at any time.

Hardware Interrupt / Hardware IRQ
Hardware interrupt request. ``in_irq()`` returns true in a hardware
interrupt handler.

Interrupt Context
Not user context: processing a hardware irq or software irq. Indicated
by the ``in_interrupt()`` macro returning true.

SMP
Symmetric Multi-Processor: kernels compiled for multiple-CPU machines.
(CONFIG_SMP=y).

Software Interrupt / softirq
Software interrupt handler. ``in_irq()`` returns false; ``in_softirq()``
returns true. Tasklets and softirqs both fall into the category of
'software interrupts'.

Strictly speaking a softirq is one of up to 32 enumerated software
interrupts which can run on multiple CPUs at once. Sometimes used to
refer to tasklets as well (ie. all software interrupts).

tasklet
A dynamically-registrable software interrupt, which is guaranteed to
only run on one CPU at a time.

timer
A dynamically-registrable software interrupt, which is run at (or close
to) a given time. When running, it is just like a tasklet (in fact, they
are called from the TIMER_SOFTIRQ).

UP
Uni-Processor: Non-SMP. (CONFIG_SMP=n).

User Context
The kernel executing on behalf of a particular process (ie. a system
call or trap) or kernel thread. You can tell which process with the
``current`` macro.) Not to be confused with userspace. Can be
interrupted by software or hardware interrupts.

Userspace
A process executing its own code outside the kernel.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. only:: html

  Retrieval
  =========

  * :ref:`genindex`
  * :ref:`search`

