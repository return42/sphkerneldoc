.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/s3cmci.c

.. _`s3cmci_host_usedma`:

s3cmci_host_usedma
==================

.. c:function:: bool s3cmci_host_usedma(struct s3cmci_host *host)

    return whether the host is using dma or pio

    :param host:
        The host state
    :type host: struct s3cmci_host \*

.. _`s3cmci_host_usedma.description`:

Description
-----------

Return true if the host is using DMA to transfer data, else false
to use PIO mode. Will return static data depending on the driver
configuration.

.. _`s3cmci_check_sdio_irq`:

s3cmci_check_sdio_irq
=====================

.. c:function:: void s3cmci_check_sdio_irq(struct s3cmci_host *host)

    test whether the SDIO IRQ is being signalled

    :param host:
        The host to check.
    :type host: struct s3cmci_host \*

.. _`s3cmci_check_sdio_irq.description`:

Description
-----------

Test to see if the SDIO interrupt is being signalled in case the
controller has failed to re-detect a card interrupt. Read GPE8 and
see if it is low and if so, signal a SDIO interrupt.

This is currently called if a request is finished (we assume that the
bus is now idle) and when the SDIO IRQ is enabled in case the IRQ is
already being indicated.

.. _`s3cmci_enable_irq`:

s3cmci_enable_irq
=================

.. c:function:: void s3cmci_enable_irq(struct s3cmci_host *host, bool more)

    enable IRQ, after having disabled it.

    :param host:
        The device state.
    :type host: struct s3cmci_host \*

    :param more:
        True if more IRQs are expected from transfer.
    :type more: bool

.. _`s3cmci_enable_irq.description`:

Description
-----------

Enable the main IRQ if needed after it has been disabled.

.. _`s3cmci_enable_irq.the-irq-can-be-one-of-the-following-states`:

The IRQ can be one of the following states
------------------------------------------

- disabled during IDLE
- disabled whilst processing data
- enabled during transfer
- enabled whilst awaiting SDIO interrupt detection

.. This file was automatic generated / don't edit.

