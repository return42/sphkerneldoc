.. -*- coding: utf-8; mode: rst -*-

.. _genericinterfaces:

******************
Generic interfaces
******************

Some interfaces are available to other drivers that do not necessarily
have anything to do with the busses described above, but still are
indirectly using basic infrastructure in the common I/O layer. One
example is the support for adapter interrupts.


.. kernel-doc:: drivers/s390/cio/airq.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
