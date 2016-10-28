.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/ni_tio.c

.. _`ni_tio_write`:

ni_tio_write
============

.. c:function:: void ni_tio_write(struct ni_gpct *counter, unsigned int value, enum ni_gpct_register reg)

    Write a TIO register using the driver provided callback.

    :param struct ni_gpct \*counter:
        struct ni_gpct counter.

    :param unsigned int value:
        the value to write

    :param enum ni_gpct_register reg:
        the register to write.

.. _`ni_tio_read`:

ni_tio_read
===========

.. c:function:: unsigned int ni_tio_read(struct ni_gpct *counter, enum ni_gpct_register reg)

    Read a TIO register using the driver provided callback.

    :param struct ni_gpct \*counter:
        struct ni_gpct counter.

    :param enum ni_gpct_register reg:
        the register to read.

.. _`ni_tio_set_bits`:

ni_tio_set_bits
===============

.. c:function:: void ni_tio_set_bits(struct ni_gpct *counter, enum ni_gpct_register reg, unsigned int mask, unsigned int value)

    Safely write a counter register.

    :param struct ni_gpct \*counter:
        struct ni_gpct counter.

    :param enum ni_gpct_register reg:
        the register to write.

    :param unsigned int mask:
        the bits to change.

    :param unsigned int value:
        the new bits value.

.. _`ni_tio_set_bits.description`:

Description
-----------

Used to write to, and update the software copy, a register whose bits may
be twiddled in interrupt context, or whose software copy may be read in
interrupt context.

.. _`ni_tio_get_soft_copy`:

ni_tio_get_soft_copy
====================

.. c:function:: unsigned int ni_tio_get_soft_copy(const struct ni_gpct *counter, enum ni_gpct_register reg)

    Safely read the software copy of a counter register.

    :param const struct ni_gpct \*counter:
        struct ni_gpct counter.

    :param enum ni_gpct_register reg:
        the register to read.

.. _`ni_tio_get_soft_copy.description`:

Description
-----------

Used to get the software copy of a register whose bits might be modified
in interrupt context, or whose software copy might need to be read in
interrupt context.

.. This file was automatic generated / don't edit.

