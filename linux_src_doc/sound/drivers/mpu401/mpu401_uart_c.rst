.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/drivers/mpu401/mpu401_uart.c

.. _`snd_mpu401_uart_interrupt`:

snd_mpu401_uart_interrupt
=========================

.. c:function:: irqreturn_t snd_mpu401_uart_interrupt(int irq, void *dev_id)

    generic MPU401-UART interrupt handler

    :param int irq:
        the irq number

    :param void \*dev_id:
        mpu401 instance

.. _`snd_mpu401_uart_interrupt.description`:

Description
-----------

Processes the interrupt for MPU401-UART i/o.

.. _`snd_mpu401_uart_interrupt.return`:

Return
------

\ ``IRQ_HANDLED``\  if the interrupt was handled. \ ``IRQ_NONE``\  otherwise.

.. _`snd_mpu401_uart_interrupt_tx`:

snd_mpu401_uart_interrupt_tx
============================

.. c:function:: irqreturn_t snd_mpu401_uart_interrupt_tx(int irq, void *dev_id)

    generic MPU401-UART transmit irq handler

    :param int irq:
        the irq number

    :param void \*dev_id:
        mpu401 instance

.. _`snd_mpu401_uart_interrupt_tx.description`:

Description
-----------

Processes the interrupt for MPU401-UART output.

.. _`snd_mpu401_uart_interrupt_tx.return`:

Return
------

\ ``IRQ_HANDLED``\  if the interrupt was handled. \ ``IRQ_NONE``\  otherwise.

.. _`snd_mpu401_uart_new`:

snd_mpu401_uart_new
===================

.. c:function:: int snd_mpu401_uart_new(struct snd_card *card, int device, unsigned short hardware, unsigned long port, unsigned int info_flags, int irq, struct snd_rawmidi **rrawmidi)

    create an MPU401-UART instance

    :param struct snd_card \*card:
        the card instance

    :param int device:
        the device index, zero-based

    :param unsigned short hardware:
        the hardware type, MPU401_HW_XXXX

    :param unsigned long port:
        the base address of MPU401 port

    :param unsigned int info_flags:
        bitflags MPU401_INFO_XXX

    :param int irq:
        the ISA irq number, -1 if not to be allocated

    :param struct snd_rawmidi \*\*rrawmidi:
        the pointer to store the new rawmidi instance

.. _`snd_mpu401_uart_new.description`:

Description
-----------

Creates a new MPU-401 instance.

Note that the rawmidi instance is returned on the rrawmidi argument,
not the mpu401 instance itself.  To access to the mpu401 instance,
cast from rawmidi->private_data (with struct snd_mpu401 magic-cast).

.. _`snd_mpu401_uart_new.return`:

Return
------

Zero if successful, or a negative error code.

.. This file was automatic generated / don't edit.

