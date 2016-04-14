.. -*- coding: utf-8; mode: rst -*-

========
spidev.h
========

.. _`spi_ioc_transfer`:

struct spi_ioc_transfer
=======================

.. c:type:: struct spi_ioc_transfer

    describes a single SPI transfer



Definition
----------

.. code-block:: c

  struct spi_ioc_transfer {
    __u64 tx_buf;
    __u64 rx_buf;
    __u32 len;
    __u32 speed_hz;
    __u16 delay_usecs;
    __u8 bits_per_word;
    __u8 cs_change;
  };



Members
-------

:``tx_buf``:
    Holds pointer to userspace buffer with transmit data, or null.::

            If no data is provided, zeroes are shifted out.

:``rx_buf``:
    Holds pointer to userspace buffer for receive data, or null.

:``len``:
    Length of tx and rx buffers, in bytes.

:``speed_hz``:
    Temporary override of the device's bitrate.

:``delay_usecs``:
    If nonzero, how long to delay after the last bit transfer
    before optionally deselecting the device before the next transfer.

:``bits_per_word``:
    Temporary override of the device's wordsize.

:``cs_change``:
    True to deselect device before starting the next transfer.



Description
-----------

This structure is mapped directly to the kernel spi_transfer structure;
the fields have the same meanings, except of course that the pointers
are in a different address space (and may be of different sizes in some
cases, such as 32-bit i386 userspace over a 64-bit x86_64 kernel).
Zero-initialize the structure, including currently unused fields, to
accommodate potential future updates.

SPI_IOC_MESSAGE gives userspace the equivalent of kernel :c:func:`spi_sync`.
Pass it an array of related transfers, they'll execute together.
Each transfer may be half duplex (either direction) or full duplex.::

        struct spi_ioc_transfer mesg[4];
        ...
        status = ioctl(fd, SPI_IOC_MESSAGE(4), mesg);

So for example one transfer might send a nine bit command (right aligned
in a 16-bit word), the next could read a block of 8-bit data before
terminating that command by temporarily deselecting the chip; the next
could send a different nine bit command (re-selecting the chip), and the
last transfer might write some register values.

