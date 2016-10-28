.. -*- coding: utf-8; mode: rst -*-

.. _Porting_The_Z8530_Driver:

************************
Porting The Z8530 Driver
************************

The Z8530 driver is written to be portable. In DMA mode it makes
assumptions about the use of ISA DMA. These are probably warranted in
most cases as the Z85230 in particular was designed to glue to PC type
machines. The PIO mode makes no real assumptions.

Should you need to retarget the Z8530 driver to another architecture the
only code that should need changing are the port I/O functions. At the
moment these assume PC I/O port accesses. This may not be appropriate
for all platforms. Replacing :c:func:`z8530_read_port()` and
:c:func:`z8530_write_port()` is intended to be all that is required
to port this driver layer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
