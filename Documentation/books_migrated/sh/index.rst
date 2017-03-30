.. -*- coding: utf-8; mode: rst -*-

#######################
SuperH Interfaces Guide
#######################

:author:    Mundt Paul
:address:   lethal@linux-sh.org

**Copyright** 2008-2010 : Paul Mundt

**Copyright** 2008-2010 : Renesas Technology Corp.

**Copyright** 2010 : Renesas Electronics Corp.

This documentation is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

For more details see the file COPYING in the source distribution of
Linux.


.. _mm:

*****************
Memory Management
*****************


.. _sh4:

SH-4
====


.. _sq:

Store Queue API
---------------


.. kernel-doc:: arch/sh/kernel/cpu/sh4/sq.c
    :man-sect: 9
    :export:


.. _sh5:

SH-5
====


.. _tlb:

TLB Interfaces
--------------


.. kernel-doc:: arch/sh/mm/tlb-sh5.c
    :man-sect: 9
    :internal:


.. kernel-doc:: arch/sh/include/asm/tlb_64.h
    :man-sect: 9
    :internal:


.. _mach:

***************************
Machine Specific Interfaces
***************************


.. _dreamcast:

mach-dreamcast
==============


.. kernel-doc:: arch/sh/boards/mach-dreamcast/rtc.c
    :man-sect: 9
    :internal:


.. _x3proto:

mach-x3proto
============


.. kernel-doc:: arch/sh/boards/mach-x3proto/ilsel.c
    :man-sect: 9
    :export:


.. _busses:

******
Busses
******


.. _superhyway:

SuperHyway
==========


.. kernel-doc:: drivers/sh/superhyway/superhyway.c
    :man-sect: 9
    :export:


.. _maple:

Maple
=====


.. kernel-doc:: drivers/sh/maple/maple.c
    :man-sect: 9
    :export:




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

