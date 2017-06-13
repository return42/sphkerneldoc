.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/sn/kernel/iomv.c

.. _`sn_io_addr`:

sn_io_addr
==========

.. c:function:: void *sn_io_addr(unsigned long port)

    convert an in/out port to an i/o address

    :param unsigned long port:
        port to convert

.. _`sn_io_addr.description`:

Description
-----------

Legacy in/out instructions are converted to ld/st instructions
on IA64.  This routine will convert a port number into a valid
SN i/o address.  Used by sn_in\*() and sn_out\*().

.. _`__sn_mmiowb`:

__sn_mmiowb
===========

.. c:function:: void __sn_mmiowb( void)

    I/O space memory barrier

    :param  void:
        no arguments

.. _`__sn_mmiowb.description`:

Description
-----------

See arch/ia64/include/asm/io.h and Documentation/driver-api/device-io.rst
for details.

On SN2, we wait for the PIO_WRITE_STATUS SHub register to clear.
See PV 871084 for details about the WAR about zero value.

.. This file was automatic generated / don't edit.

