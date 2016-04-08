
.. _API-snd-mpu401-uart-new:

===================
snd_mpu401_uart_new
===================

*man snd_mpu401_uart_new(9)*

*4.6.0-rc1*

create an MPU401-UART instance


Synopsis
========

.. c:function:: int snd_mpu401_uart_new( struct snd_card * card, int device, unsigned short hardware, unsigned long port, unsigned int info_flags, int irq, struct snd_rawmidi ** rrawmidi )

Arguments
=========

``card``
    the card instance

``device``
    the device index, zero-based

``hardware``
    the hardware type, MPU401_HW_XXXX

``port``
    the base address of MPU401 port

``info_flags``
    bitflags MPU401_INFO_XXX

``irq``
    the ISA irq number, -1 if not to be allocated

``rrawmidi``
    the pointer to store the new rawmidi instance


Description
===========

Creates a new MPU-401 instance.

Note that the rawmidi instance is returned on the rrawmidi argument, not the mpu401 instance itself. To access to the mpu401 instance, cast from rawmidi->private_data (with struct
snd_mpu401 magic-cast).


Return
======

Zero if successful, or a negative error code.
