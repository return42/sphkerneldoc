.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libsas/sas_host_smp.c

.. _`to_sas_gpio_gp_bit`:

to_sas_gpio_gp_bit
==================

.. c:function:: u8 *to_sas_gpio_gp_bit(unsigned int od, u8 *data, u8 index, u8 count, u8 *bit)

    given the gpio frame data find the byte/bit position of 'od'

    :param od:
        od bit to find
    :type od: unsigned int

    :param data:
        incoming bitstream (from frame)
    :type data: u8 \*

    :param index:
        requested data register index (from frame)
    :type index: u8

    :param count:
        total number of registers in the bitstream (from frame)
    :type count: u8

    :param bit:
        bit position of 'od' in the returned byte
    :type bit: u8 \*

.. _`to_sas_gpio_gp_bit.description`:

Description
-----------

returns NULL if 'od' is not in 'data'

From SFF-8485 v0.7:
"In GPIO_TX[1], bit 0 of byte 3 contains the first bit (i.e., OD0.0)
and bit 7 of byte 0 contains the 32nd bit (i.e., OD10.1).

In GPIO_TX[2], bit 0 of byte 3 contains the 33rd bit (i.e., OD10.2)
and bit 7 of byte 0 contains the 64th bit (i.e., OD21.0)."

The general-purpose (raw-bitstream) RX registers have the same layout
although 'od' is renamed 'id' for 'input data'.

SFF-8489 defines the behavior of the LEDs in response to the 'od' values.

.. This file was automatic generated / don't edit.

