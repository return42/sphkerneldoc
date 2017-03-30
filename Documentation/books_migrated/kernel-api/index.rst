.. -*- coding: utf-8; mode: rst -*-

####################
The Linux Kernel API
####################

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


.. _adt:

**********
Data Types
**********


Doubly Linked Lists
===================


.. kernel-doc:: include/linux/list.h
    :man-sect: 9
    :internal:


.. _libc:

*************************
Basic C Library Functions
*************************

When writing drivers, you cannot in general use routines which are from
the C Library. Some of the functions have been found generally useful
and they are listed below. The behaviour of these functions may vary
slightly from those defined by ANSI, and these deviations are noted in
the text.


String Conversions
==================


.. kernel-doc:: lib/vsprintf.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/kernel.h
    :man-sect: 9
    :functions: kstrtol


.. kernel-doc:: include/linux/kernel.h
    :man-sect: 9
    :functions: kstrtoul


.. kernel-doc:: lib/kstrtox.c
    :man-sect: 9
    :export:


String Manipulation
===================


.. kernel-doc:: lib/string.c
    :man-sect: 9
    :export:


Bit Operations
==============


.. kernel-doc:: arch/x86/include/asm/bitops.h
    :man-sect: 9
    :internal:


.. _kernel-lib:

******************************
Basic Kernel Library Functions
******************************

The Linux kernel provides more basic utility functions.


Bitmap Operations
=================


.. kernel-doc:: lib/bitmap.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/bitmap.c
    :man-sect: 9
    :internal:


Command-line Parsing
====================


.. kernel-doc:: lib/cmdline.c
    :man-sect: 9
    :export:


.. _crc:

CRC Functions
=============


.. kernel-doc:: lib/crc7.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/crc16.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/crc-itu-t.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/crc32.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/crc-ccitt.c
    :man-sect: 9
    :export:


.. _idr:

idr/ida Functions
=================


.. kernel-doc:: include/linux/idr.h
    :man-sect: 9
    :doc: idr sync


.. kernel-doc:: lib/idr.c
    :man-sect: 9
    :doc: IDA description


.. kernel-doc:: lib/idr.c
    :man-sect: 9
    :export:


.. _mm:

**************************
Memory Management in Linux
**************************


The Slab Cache
==============


.. kernel-doc:: include/linux/slab.h
    :man-sect: 9
    :internal:


.. kernel-doc:: mm/slab.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/util.c
    :man-sect: 9
    :export:


User Space Memory Access
========================


.. kernel-doc:: arch/x86/include/asm/uaccess_32.h
    :man-sect: 9
    :internal:


.. kernel-doc:: arch/x86/lib/usercopy_32.c
    :man-sect: 9
    :export:


More Memory Management Functions
================================


.. kernel-doc:: mm/readahead.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/filemap.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/memory.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/vmalloc.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/page_alloc.c
    :man-sect: 9
    :internal:


.. kernel-doc:: mm/mempool.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/dmapool.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/page-writeback.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/truncate.c
    :man-sect: 9
    :export:


.. _ipc:

*********************
Kernel IPC facilities
*********************


IPC utilities
=============


.. kernel-doc:: ipc/util.c
    :man-sect: 9
    :internal:


.. _kfifo:

***********
FIFO Buffer
***********


kfifo interface
===============


.. kernel-doc:: include/linux/kfifo.h
    :man-sect: 9
    :internal:


.. _relayfs:

***********************
relay interface support
***********************

Relay interface support is designed to provide an efficient mechanism
for tools and facilities to relay large amounts of data from kernel
space to user space.


relay interface
===============


.. kernel-doc:: kernel/relay.c
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/relay.c
    :man-sect: 9
    :internal:


.. _modload:

**************
Module Support
**************


Module Loading
==============


.. kernel-doc:: kernel/kmod.c
    :man-sect: 9
    :export:


Inter Module support
====================

Refer to the file kernel/module.c for more information.


.. _hardware:

*******************
Hardware Interfaces
*******************


Interrupt Handling
==================


.. kernel-doc:: kernel/irq/manage.c
    :man-sect: 9
    :export:


DMA Channels
============


.. kernel-doc:: kernel/dma.c
    :man-sect: 9
    :export:


Resources Management
====================


.. kernel-doc:: kernel/resource.c
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/resource.c
    :man-sect: 9
    :export:


MTRR Handling
=============


.. kernel-doc:: arch/x86/kernel/cpu/mtrr/main.c
    :man-sect: 9
    :export:


PCI Support Library
===================


.. kernel-doc:: drivers/pci/pci.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/pci-driver.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/remove.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/search.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/msi.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/bus.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/access.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/irq.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/htirq.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/probe.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/slot.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/rom.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/iov.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/pci-sysfs.c
    :man-sect: 9
    :internal:


PCI Hotplug Support Library
===========================


.. kernel-doc:: drivers/pci/hotplug/pci_hotplug_core.c
    :man-sect: 9
    :export:


.. _firmware:

*******************
Firmware Interfaces
*******************


DMI Interfaces
==============


.. kernel-doc:: drivers/firmware/dmi_scan.c
    :man-sect: 9
    :export:


EDD Interfaces
==============


.. kernel-doc:: drivers/firmware/edd.c
    :man-sect: 9
    :internal:


.. _security:

******************
Security Framework
******************


.. kernel-doc:: security/security.c
    :man-sect: 9
    :internal:


.. kernel-doc:: security/inode.c
    :man-sect: 9
    :export:


.. _audit:

****************
Audit Interfaces
****************


.. kernel-doc:: kernel/audit.c
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/auditsc.c
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/auditfilter.c
    :man-sect: 9
    :internal:


.. _accounting:

********************
Accounting Framework
********************


.. kernel-doc:: kernel/acct.c
    :man-sect: 9
    :internal:


.. _blkdev:

*************
Block Devices
*************


.. kernel-doc:: block/blk-core.c
    :man-sect: 9
    :export:


.. kernel-doc:: block/blk-core.c
    :man-sect: 9
    :internal:


.. kernel-doc:: block/blk-map.c
    :man-sect: 9
    :export:


.. kernel-doc:: block/blk-sysfs.c
    :man-sect: 9
    :internal:


.. kernel-doc:: block/blk-settings.c
    :man-sect: 9
    :export:


.. kernel-doc:: block/blk-exec.c
    :man-sect: 9
    :export:


.. kernel-doc:: block/blk-flush.c
    :man-sect: 9
    :export:


.. kernel-doc:: block/blk-lib.c
    :man-sect: 9
    :export:


.. kernel-doc:: block/blk-tag.c
    :man-sect: 9
    :export:


.. kernel-doc:: block/blk-tag.c
    :man-sect: 9
    :internal:


.. kernel-doc:: block/blk-integrity.c
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/trace/blktrace.c
    :man-sect: 9
    :internal:


.. kernel-doc:: block/genhd.c
    :man-sect: 9
    :internal:


.. kernel-doc:: block/genhd.c
    :man-sect: 9
    :export:


.. _chrdev:

************
Char devices
************


.. kernel-doc:: fs/char_dev.c
    :man-sect: 9
    :export:


.. _miscdev:

*********************
Miscellaneous Devices
*********************


.. kernel-doc:: drivers/char/misc.c
    :man-sect: 9
    :export:


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
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------


.. only:: html

  Retrieval
  =========

  * :ref:`genindex`

.. todolist::

