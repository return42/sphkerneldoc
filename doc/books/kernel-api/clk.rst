.. -*- coding: utf-8; mode: rst -*-

.. _clk:

***************
Clock Framework
***************

The clock framework defines programming interfaces to support software
management of the system clock tree. This framework is widely used with
System-On-Chip (SOC) platforms to support power management and various
devices which may need custom clock rates. Note that these "clocks"
don't relate to timekeeping or real time clocks (RTCs), each of which
have separate frameworks. These :c:type:`struct clk` instances may be
used to manage for example a 96 MHz signal that is used to shift bits
into and out of peripherals or busses, or otherwise trigger synchronous
state machine transitions in system hardware.

Power management is supported by explicit software clock gating: unused
clocks are disabled, so the system doesn't waste power changing the
state of transistors that aren't in active use. On some systems this may
be backed by hardware clock gating, where clocks are gated without being
disabled in software. Sections of chips that are powered but not clocked
may be able to retain their last state. This low power state is often
called a *retention mode*. This mode still incurs leakage currents,
especially with finer circuit geometries, but for CMOS circuits power is
mostly used by clocked state changes.

Power-aware drivers only enable their clocks when the device they manage
is in active use. Also, system sleep states often differ according to
which clock domains are active: while a "standby" state may allow wakeup
from several active domains, a "mem" (suspend-to-RAM) state may require
a more wholesale shutdown of clocks derived from higher speed PLLs and
oscillators, limiting the number of possible wakeup event sources. A
driver's suspend method may need to be aware of system-specific clock
constraints on the target sleep state.

Some platforms support programmable clock generators. These can be used
by external chips of various kinds, such as other CPUs, multimedia
codecs, and devices with strict requirements for interface clocking.


.. kernel-doc:: include/linux/clk.h
    :man-sect: 9
    :internal:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
