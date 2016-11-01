.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/greybus/greybus_protocols.h

.. _`gb_spi_transfer`:

struct gb_spi_transfer
======================

.. c:type:: struct gb_spi_transfer

    a read/write buffer pair

.. _`gb_spi_transfer.definition`:

Definition
----------

.. code-block:: c

    struct gb_spi_transfer {
        __le32 speed_hz;
        __le32 len;
        __le16 delay_usecs;
        __u8 cs_change;
        __u8 bits_per_word;
        __u8 xfer_flags;
    #define GB_SPI_XFER_READ 0x01
    #define GB_SPI_XFER_WRITE 0x02
    #define GB_SPI_XFER_INPROGRESS 0x04
    }

.. _`gb_spi_transfer.members`:

Members
-------

speed_hz
    Select a speed other than the device default for this transfer. If
    0 the default (from \ ``spi_device``\ ) is used.

len
    size of rx and tx buffers (in bytes)

delay_usecs
    microseconds to delay after this transfer before (optionally)
    changing the chipselect status, then starting the next transfer or
    completing this spi_message.

cs_change
    affects chipselect after this transfer completes

bits_per_word
    select a bits_per_word other than the device default for this
    transfer. If 0 the default (from \ ``spi_device``\ ) is used.

xfer_flags
    *undescribed*

.. This file was automatic generated / don't edit.

