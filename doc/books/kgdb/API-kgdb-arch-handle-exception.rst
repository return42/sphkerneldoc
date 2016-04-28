.. -*- coding: utf-8; mode: rst -*-

.. _API-kgdb-arch-handle-exception:

==========================
kgdb_arch_handle_exception
==========================

*man kgdb_arch_handle_exception(9)*

*4.6.0-rc5*

Handle architecture specific GDB packets.


Synopsis
========

.. c:function:: int kgdb_arch_handle_exception( int vector, int signo, int err_code, char * remcom_in_buffer, char * remcom_out_buffer, struct pt_regs * regs )

Arguments
=========

``vector``
    The error vector of the exception that happened.

``signo``
    The signal number of the exception that happened.

``err_code``
    The error code of the exception that happened.

``remcom_in_buffer``
    The buffer of the packet we have read.

``remcom_out_buffer``
    The buffer of ``BUFMAX`` bytes to write a packet into.

``regs``
    The ``struct pt_regs`` of the current process.


Description
===========

This function MUST handle the 'c' and 's' command packets, as well
packets to set / remove a hardware breakpoint, if used. If there are
additional packets which the hardware needs to handle, they are handled
here. The code should return -1 if it wants to process more packets, and
a ``0`` or ``1`` if it wants to exit from the kgdb callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
