.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/xilinx_hwicap/fifo_icap.c

.. _`xhi_ipixr_rfull_mask`:

XHI_IPIXR_RFULL_MASK
====================

.. c:function::  XHI_IPIXR_RFULL_MASK()

.. _`xhi_ipixr_rfull_mask.description`:

Description
-----------

Interrupt Status Register (IPISR) : This register holds the
interrupt status flags for the device. These bits are toggle on
write.

Interrupt Enable Register (IPIER) : This register is used to enable
interrupt sources for the device.
Writing a '1' to a bit enables the corresponding interrupt.
Writing a '0' to a bit disables the corresponding interrupt.

IPISR/IPIER registers have the same bit definitions and are only defined
once.

.. _`fifo_icap_fifo_write`:

fifo_icap_fifo_write
====================

.. c:function:: void fifo_icap_fifo_write(struct hwicap_drvdata *drvdata, u32 data)

    Write data to the write FIFO.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

    :param u32 data:
        the 32-bit value to be written to the FIFO.

.. _`fifo_icap_fifo_write.description`:

Description
-----------

This function will silently fail if the fifo is full.

.. _`fifo_icap_fifo_read`:

fifo_icap_fifo_read
===================

.. c:function:: u32 fifo_icap_fifo_read(struct hwicap_drvdata *drvdata)

    Read data from the Read FIFO.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

.. _`fifo_icap_fifo_read.description`:

Description
-----------

This function will silently fail if the fifo is empty.

.. _`fifo_icap_set_read_size`:

fifo_icap_set_read_size
=======================

.. c:function:: void fifo_icap_set_read_size(struct hwicap_drvdata *drvdata, u32 data)

    Set the the size register.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

    :param u32 data:
        the size of the following read transaction, in words.

.. _`fifo_icap_start_config`:

fifo_icap_start_config
======================

.. c:function:: void fifo_icap_start_config(struct hwicap_drvdata *drvdata)

    Initiate a configuration (write) to the device.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

.. _`fifo_icap_start_readback`:

fifo_icap_start_readback
========================

.. c:function:: void fifo_icap_start_readback(struct hwicap_drvdata *drvdata)

    Initiate a readback from the device.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

.. _`fifo_icap_get_status`:

fifo_icap_get_status
====================

.. c:function:: u32 fifo_icap_get_status(struct hwicap_drvdata *drvdata)

    Get the contents of the status register.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

.. _`fifo_icap_get_status.description`:

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

.. _`fifo_icap_busy`:

fifo_icap_busy
==============

.. c:function:: u32 fifo_icap_busy(struct hwicap_drvdata *drvdata)

    Return true if the ICAP is still processing a transaction.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

.. _`fifo_icap_write_fifo_vacancy`:

fifo_icap_write_fifo_vacancy
============================

.. c:function:: u32 fifo_icap_write_fifo_vacancy(struct hwicap_drvdata *drvdata)

    Query the write fifo available space.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

.. _`fifo_icap_write_fifo_vacancy.description`:

Description
-----------

Return the number of words that can be safely pushed into the write fifo.

.. _`fifo_icap_read_fifo_occupancy`:

fifo_icap_read_fifo_occupancy
=============================

.. c:function:: u32 fifo_icap_read_fifo_occupancy(struct hwicap_drvdata *drvdata)

    Query the read fifo available data.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

.. _`fifo_icap_read_fifo_occupancy.description`:

Description
-----------

Return the number of words that can be safely read from the read fifo.

.. _`fifo_icap_set_configuration`:

fifo_icap_set_configuration
===========================

.. c:function:: int fifo_icap_set_configuration(struct hwicap_drvdata *drvdata, u32 *frame_buffer, u32 num_words)

    Send configuration data to the ICAP.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

    :param u32 \*frame_buffer:
        a pointer to the data to be written to the
        ICAP device.

    :param u32 num_words:
        the number of words (32 bit) to write to the ICAP
        device.
        This function writes the given user data to the Write FIFO in
        polled mode and starts the transfer of the data to
        the ICAP device.

.. _`fifo_icap_get_configuration`:

fifo_icap_get_configuration
===========================

.. c:function:: int fifo_icap_get_configuration(struct hwicap_drvdata *drvdata, u32 *frame_buffer, u32 num_words)

    Read configuration data from the device.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

    :param u32 \*frame_buffer:
        *undescribed*

    :param u32 num_words:
        *undescribed*

.. _`fifo_icap_get_configuration.description`:

Description
-----------

This function reads the specified number of words from the ICAP device in
the polled mode.

.. _`fifo_icap_reset`:

fifo_icap_reset
===============

.. c:function:: void fifo_icap_reset(struct hwicap_drvdata *drvdata)

    Reset the logic of the icap device.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

.. _`fifo_icap_reset.description`:

Description
-----------

This function forces the software reset of the complete HWICAP device.
All the registers will return to the default value and the FIFO is also
flushed as a part of this software reset.

.. _`fifo_icap_flush_fifo`:

fifo_icap_flush_fifo
====================

.. c:function:: void fifo_icap_flush_fifo(struct hwicap_drvdata *drvdata)

    This function flushes the FIFOs in the device.

    :param struct hwicap_drvdata \*drvdata:
        a pointer to the drvdata.

.. This file was automatic generated / don't edit.

