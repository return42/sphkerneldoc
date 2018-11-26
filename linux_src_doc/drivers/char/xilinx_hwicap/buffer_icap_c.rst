.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/xilinx_hwicap/buffer_icap.c

.. _`buffer_icap_get_status`:

buffer_icap_get_status
======================

.. c:function:: u32 buffer_icap_get_status(struct hwicap_drvdata *drvdata)

    Get the contents of the status register.

    :param drvdata:
        a pointer to the drvdata.
    :type drvdata: struct hwicap_drvdata \*

.. _`buffer_icap_get_status.description`:

Description
-----------

The status register contains the ICAP status and the done bit.

D8 - cfgerr
D7 - dalign
D6 - rip
D5 - in_abort_l
D4 - Always 1
D3 - Always 1
D2 - Always 1
D1 - Always 1
D0 - Done bit

.. _`buffer_icap_get_bram`:

buffer_icap_get_bram
====================

.. c:function:: u32 buffer_icap_get_bram(void __iomem *base_address, u32 offset)

    Reads data from the storage buffer bram.

    :param base_address:
        contains the base address of the component.
    :type base_address: void __iomem \*

    :param offset:
        The word offset from which the data should be read.
    :type offset: u32

.. _`buffer_icap_get_bram.description`:

Description
-----------

A bram is used as a configuration memory cache.  One frame of data can
be stored in this "storage buffer".

.. _`buffer_icap_busy`:

buffer_icap_busy
================

.. c:function:: bool buffer_icap_busy(void __iomem *base_address)

    Return true if the icap device is busy

    :param base_address:
        is the base address of the device
    :type base_address: void __iomem \*

.. _`buffer_icap_busy.description`:

Description
-----------

The queries the low order bit of the status register, which
indicates whether the current configuration or readback operation
has completed.

.. _`buffer_icap_set_size`:

buffer_icap_set_size
====================

.. c:function:: void buffer_icap_set_size(void __iomem *base_address, u32 data)

    Set the size register.

    :param base_address:
        is the base address of the device
    :type base_address: void __iomem \*

    :param data:
        The size in bytes.
    :type data: u32

.. _`buffer_icap_set_size.description`:

Description
-----------

The size register holds the number of 8 bit bytes to transfer between
bram and the icap (or icap to bram).

.. _`buffer_icap_set_offset`:

buffer_icap_set_offset
======================

.. c:function:: void buffer_icap_set_offset(void __iomem *base_address, u32 data)

    Set the bram offset register.

    :param base_address:
        contains the base address of the device.
    :type base_address: void __iomem \*

    :param data:
        is the value to be written to the data register.
    :type data: u32

.. _`buffer_icap_set_offset.description`:

Description
-----------

The bram offset register holds the starting bram address to transfer
data from during configuration or write data to during readback.

.. _`buffer_icap_set_rnc`:

buffer_icap_set_rnc
===================

.. c:function:: void buffer_icap_set_rnc(void __iomem *base_address, u32 data)

    Set the RNC (Readback not Configure) register.

    :param base_address:
        contains the base address of the device.
    :type base_address: void __iomem \*

    :param data:
        is the value to be written to the data register.
    :type data: u32

.. _`buffer_icap_set_rnc.description`:

Description
-----------

The RNC register determines the direction of the data transfer.  It
controls whether a configuration or readback take place.  Writing to
this register initiates the transfer.  A value of 1 initiates a
readback while writing a value of 0 initiates a configuration.

.. _`buffer_icap_set_bram`:

buffer_icap_set_bram
====================

.. c:function:: void buffer_icap_set_bram(void __iomem *base_address, u32 offset, u32 data)

    Write data to the storage buffer bram.

    :param base_address:
        contains the base address of the component.
    :type base_address: void __iomem \*

    :param offset:
        The word offset at which the data should be written.
    :type offset: u32

    :param data:
        The value to be written to the bram offset.
    :type data: u32

.. _`buffer_icap_set_bram.description`:

Description
-----------

A bram is used as a configuration memory cache.  One frame of data can
be stored in this "storage buffer".

.. _`buffer_icap_device_read`:

buffer_icap_device_read
=======================

.. c:function:: int buffer_icap_device_read(struct hwicap_drvdata *drvdata, u32 offset, u32 count)

    Transfer bytes from ICAP to the storage buffer.

    :param drvdata:
        a pointer to the drvdata.
    :type drvdata: struct hwicap_drvdata \*

    :param offset:
        The storage buffer start address.
    :type offset: u32

    :param count:
        The number of words (32 bit) to read from the
        device (ICAP).
    :type count: u32

.. _`buffer_icap_device_write`:

buffer_icap_device_write
========================

.. c:function:: int buffer_icap_device_write(struct hwicap_drvdata *drvdata, u32 offset, u32 count)

    Transfer bytes from ICAP to the storage buffer.

    :param drvdata:
        a pointer to the drvdata.
    :type drvdata: struct hwicap_drvdata \*

    :param offset:
        The storage buffer start address.
    :type offset: u32

    :param count:
        The number of words (32 bit) to read from the
        device (ICAP).
    :type count: u32

.. _`buffer_icap_reset`:

buffer_icap_reset
=================

.. c:function:: void buffer_icap_reset(struct hwicap_drvdata *drvdata)

    Reset the logic of the icap device.

    :param drvdata:
        a pointer to the drvdata.
    :type drvdata: struct hwicap_drvdata \*

.. _`buffer_icap_reset.description`:

Description
-----------

Writing to the status register resets the ICAP logic in an internal
version of the core.  For the version of the core published in EDK,
this is a noop.

.. _`buffer_icap_set_configuration`:

buffer_icap_set_configuration
=============================

.. c:function:: int buffer_icap_set_configuration(struct hwicap_drvdata *drvdata, u32 *data, u32 size)

    Load a partial bitstream from system memory.

    :param drvdata:
        a pointer to the drvdata.
    :type drvdata: struct hwicap_drvdata \*

    :param data:
        Kernel address of the partial bitstream.
    :type data: u32 \*

    :param size:
        the size of the partial bitstream in 32 bit words.
    :type size: u32

.. _`buffer_icap_get_configuration`:

buffer_icap_get_configuration
=============================

.. c:function:: int buffer_icap_get_configuration(struct hwicap_drvdata *drvdata, u32 *data, u32 size)

    Read configuration data from the device.

    :param drvdata:
        a pointer to the drvdata.
    :type drvdata: struct hwicap_drvdata \*

    :param data:
        Address of the data representing the partial bitstream
    :type data: u32 \*

    :param size:
        the size of the partial bitstream in 32 bit words.
    :type size: u32

.. This file was automatic generated / don't edit.

