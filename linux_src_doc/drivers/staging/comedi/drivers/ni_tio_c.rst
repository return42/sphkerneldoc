.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/ni_tio.c

.. _`ni_tio_write`:

ni_tio_write
============

.. c:function:: void ni_tio_write(struct ni_gpct *counter, unsigned int value, enum ni_gpct_register reg)

    Write a TIO register using the driver provided callback.

    :param counter:
        struct ni_gpct counter.
    :type counter: struct ni_gpct \*

    :param value:
        the value to write
    :type value: unsigned int

    :param reg:
        the register to write.
    :type reg: enum ni_gpct_register

.. _`ni_tio_read`:

ni_tio_read
===========

.. c:function:: unsigned int ni_tio_read(struct ni_gpct *counter, enum ni_gpct_register reg)

    Read a TIO register using the driver provided callback.

    :param counter:
        struct ni_gpct counter.
    :type counter: struct ni_gpct \*

    :param reg:
        the register to read.
    :type reg: enum ni_gpct_register

.. _`ni_tio_set_bits`:

ni_tio_set_bits
===============

.. c:function:: void ni_tio_set_bits(struct ni_gpct *counter, enum ni_gpct_register reg, unsigned int mask, unsigned int value)

    Safely write a counter register.

    :param counter:
        struct ni_gpct counter.
    :type counter: struct ni_gpct \*

    :param reg:
        the register to write.
    :type reg: enum ni_gpct_register

    :param mask:
        the bits to change.
    :type mask: unsigned int

    :param value:
        the new bits value.
    :type value: unsigned int

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

    :param counter:
        struct ni_gpct counter.
    :type counter: const struct ni_gpct \*

    :param reg:
        the register to read.
    :type reg: enum ni_gpct_register

.. _`ni_tio_get_soft_copy.description`:

Description
-----------

Used to get the software copy of a register whose bits might be modified
in interrupt context, or whose software copy might need to be read in
interrupt context.

.. _`ni_tio_get_routing`:

ni_tio_get_routing
==================

.. c:function:: int ni_tio_get_routing(struct ni_gpct_device *counter_dev, unsigned int dest)

    the given destination.

    :param counter_dev:
        *undescribed*
    :type counter_dev: struct ni_gpct_device \*

    :param dest:
        *undescribed*
    :type dest: unsigned int

.. _`ni_tio_get_routing.description`:

Description
-----------

If the terminal for the destination is not already configured as an output,
this function returns -EINVAL as error.

.. _`ni_tio_get_routing.return`:

Return
------

the register value of the destination output selector;
-EINVAL if terminal is not configured for output.

.. _`ni_tio_set_routing`:

ni_tio_set_routing
==================

.. c:function:: int ni_tio_set_routing(struct ni_gpct_device *counter_dev, unsigned int dest, unsigned int reg)

    :param counter_dev:
        Pointer to general counter device.
    :type counter_dev: struct ni_gpct_device \*

    :param dest:
        *undescribed*
    :type dest: unsigned int

    :param reg:
        *undescribed*
    :type reg: unsigned int

.. _`ni_tio_unset_routing`:

ni_tio_unset_routing
====================

.. c:function:: int ni_tio_unset_routing(struct ni_gpct_device *counter_dev, unsigned int dest)

    :param counter_dev:
        *undescribed*
    :type counter_dev: struct ni_gpct_device \*

    :param dest:
        *undescribed*
    :type dest: unsigned int

.. _`ni_tio_unset_routing.return`:

Return
------

0 if successful; -EINVAL if terminal is unknown.

.. This file was automatic generated / don't edit.

