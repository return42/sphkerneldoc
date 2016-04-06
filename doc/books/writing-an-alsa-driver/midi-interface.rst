
.. _midi-interface:

============================
MIDI (MPU401-UART) Interface
============================


.. _midi-interface-general:

General
=======

Many soundcards have built-in MIDI (MPU401-UART) interfaces. When the soundcard supports the standard MPU401-UART interface, most likely you can use the ALSA MPU401-UART API. The
MPU401-UART API is defined in ``<sound/mpu401.h>``.

Some soundchips have a similar but slightly different implementation of mpu401 stuff. For example, emu10k1 has its own mpu401 routines.


.. _midi-interface-constructor:

Constructor
===========

To create a rawmidi object, call ``snd_mpu401_uart_new()``.


.. code-block:: c

      struct snd_rawmidi &#x22C6;rmidi;
      snd_mpu401_uart_new(card, 0, MPU401_HW_MPU401, port, info_flags,
                          irq, &rmidi);

The first argument is the card pointer, and the second is the index of this component. You can create up to 8 rawmidi devices.

The third argument is the type of the hardware, ``MPU401_HW_XXX``. If it's not a special one, you can use ``MPU401_HW_MPU401``.

The 4th argument is the I/O port address. Many backward-compatible MPU401 have an I/O port such as 0x330. Or, it might be a part of its own PCI I/O region. It depends on the chip
design.

The 5th argument is a bitflag for additional information. When the I/O port address above is part of the PCI I/O region, the MPU401 I/O port might have been already allocated
(reserved) by the driver itself. In such a case, pass a bit flag ``MPU401_INFO_INTEGRATED``, and the mpu401-uart layer will allocate the I/O ports by itself.

When the controller supports only the input or output MIDI stream, pass the ``MPU401_INFO_INPUT`` or ``MPU401_INFO_OUTPUT`` bitflag, respectively. Then the rawmidi instance is
created as a single stream.

``MPU401_INFO_MMIO`` bitflag is used to change the access method to MMIO (via readb and writeb) instead of iob and outb. In this case, you have to pass the iomapped address to
``snd_mpu401_uart_new()``.

When ``MPU401_INFO_TX_IRQ`` is set, the output stream isn't checked in the default interrupt handler. The driver needs to call ``snd_mpu401_uart_interrupt_tx()`` by itself to start
processing the output stream in the irq handler.

If the MPU-401 interface shares its interrupt with the other logical devices on the card, set ``MPU401_INFO_IRQ_HOOK`` (see :ref:`below <midi-interface-interrupt-handler>`).

Usually, the port address corresponds to the command port and port + 1 corresponds to the data port. If not, you may change the ``cport`` field of struct ``snd_mpu401`` manually
afterward. However, ``snd_mpu401`` pointer is not returned explicitly by ``snd_mpu401_uart_new()``. You need to cast rmidi->private_data to ``snd_mpu401`` explicitly,


.. code-block:: c

      struct snd_mpu401 &#x22C6;mpu;
      mpu = rmidi->private_data;

and reset the cport as you like:


.. code-block:: c

      mpu->cport = my_own_control_port;

The 6th argument specifies the ISA irq number that will be allocated. If no interrupt is to be allocated (because your code is already allocating a shared interrupt, or because the
device does not use interrupts), pass -1 instead. For a MPU-401 device without an interrupt, a polling timer will be used instead.


.. _midi-interface-interrupt-handler:

Interrupt Handler
=================

When the interrupt is allocated in ``snd_mpu401_uart_new()``, an exclusive ISA interrupt handler is automatically used, hence you don't have anything else to do than creating the
mpu401 stuff. Otherwise, you have to set ``MPU401_INFO_IRQ_HOOK``, and call ``snd_mpu401_uart_interrupt()`` explicitly from your own interrupt handler when it has determined that a
UART interrupt has occurred.

In this case, you need to pass the private_data of the returned rawmidi object from ``snd_mpu401_uart_new()`` as the second argument of ``snd_mpu401_uart_interrupt()``.


.. code-block:: c

      snd_mpu401_uart_interrupt(irq, rmidi->private_data, regs);


