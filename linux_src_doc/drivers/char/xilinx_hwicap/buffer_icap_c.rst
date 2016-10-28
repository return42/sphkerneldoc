.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/xilinx_hwicap/buffer_icap.c

.. _`buffer_icap_get_status`:

buffer_icap_get_status
======================

.. c:function:: u32 buffer_icap_get_status(struct hwicap_drvdata *drvdata)

    Get the contents of the status register.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

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

    :param void __iomem \*base_address:
        contains the base address of the component.

    :param u32 offset:
        The word offset from which the data should be read.

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

    :param void __iomem \*base_address:
        is the base address of the device

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

    :param void __iomem \*base_address:
        is the base address of the device

    :param u32 data:
        The size in bytes.

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

    :param void __iomem \*base_address:
        contains the base address of the device.

    :param u32 data:
        is the value to be written to the data register.

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

    :param void __iomem \*base_address:
        contains the base address of the device.

    :param u32 data:
        is the value to be written to the data register.

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

    :param void __iomem \*base_address:
        contains the base address of the component.

    :param u32 offset:
        The word offset at which the data should be written.

    :param u32 data:
        The value to be written to the bram offset.

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

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

    :param u32 offset:
        The storage buffer start address.

    :param u32 count:
        The number of words (32 bit) to read from the
        device (ICAP).

.. _`buffer_icap_device_write`:

buffer_icap_device_write
========================

.. c:function:: int buffer_icap_device_write(struct hwicap_drvdata *drvdata, u32 offset, u32 count)

    Transfer bytes from ICAP to the storage buffer.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

    :param u32 offset:
        The storage buffer start address.

    :param u32 count:
        The number of words (32 bit) to read from the
        device (ICAP).

.. _`buffer_icap_reset`:

buffer_icap_reset
=================

.. c:function:: void buffer_icap_reset(struct hwicap_drvdata *drvdata)

    Reset the logic of the icap device.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

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

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

    :param u32 \*data:
        Kernel address of the partial bitstream.

    :param u32 size:
        the size of the partial bitstream in 32 bit words.

.. _`buffer_icap_get_configuration`:

buffer_icap_get_configuration
=============================

.. c:function:: int buffer_icap_get_configuration(struct hwicap_drvdata *drvdata, u32 *data, u32 size)

    Read configuration data from the device.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

    :param u32 \*data:
        Address of the data representing the partial bitstream

    :param u32 size:
        the size of the partial bitstream in 32 bit words.

.. This file was automatic generated / don't edit.

