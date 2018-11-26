.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/nfc/nci/spi.c

.. _`nci_spi_allocate_spi`:

nci_spi_allocate_spi
====================

.. c:function:: struct nci_spi *nci_spi_allocate_spi(struct spi_device *spi, u8 acknowledge_mode, unsigned int delay, struct nci_dev *ndev)

    allocate a new nci spi

    :param spi:
        SPI device
    :type spi: struct spi_device \*

    :param acknowledge_mode:
        Acknowledge mode used by the NFC device
    :type acknowledge_mode: u8

    :param delay:
        delay between transactions in us
    :type delay: unsigned int

    :param ndev:
        nci dev to send incoming nci frames to
    :type ndev: struct nci_dev \*

.. _`nci_spi_read`:

nci_spi_read
============

.. c:function:: struct sk_buff *nci_spi_read(struct nci_spi *nspi)

    read frame from NCI SPI drivers

    :param nspi:
        The nci spi
    :type nspi: struct nci_spi \*

.. _`nci_spi_read.context`:

Context
-------

can sleep

.. _`nci_spi_read.description`:

Description
-----------

This call may only be used from a context that may sleep.  The sleep
is non-interruptible, and has no timeout.

It returns an allocated skb containing the frame on success, or NULL.

.. This file was automatic generated / don't edit.

