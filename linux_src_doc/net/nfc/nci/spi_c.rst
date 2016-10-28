.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/nfc/nci/spi.c

.. _`nci_spi_allocate_spi`:

nci_spi_allocate_spi
====================

.. c:function:: struct nci_spi *nci_spi_allocate_spi(struct spi_device *spi, u8 acknowledge_mode, unsigned int delay, struct nci_dev *ndev)

    allocate a new nci spi

    :param struct spi_device \*spi:
        SPI device

    :param u8 acknowledge_mode:
        Acknowledge mode used by the NFC device

    :param unsigned int delay:
        delay between transactions in us

    :param struct nci_dev \*ndev:
        nci dev to send incoming nci frames to

.. _`nci_spi_read`:

nci_spi_read
============

.. c:function:: struct sk_buff *nci_spi_read(struct nci_spi *nspi)

    read frame from NCI SPI drivers

    :param struct nci_spi \*nspi:
        The nci spi

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

