.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/drivers/vx/vx_core.c

.. _`snd_vx_load_boot_image`:

snd_vx_load_boot_image
======================

.. c:function:: int snd_vx_load_boot_image(struct vx_core *chip, const struct firmware *boot)

    boot up the xilinx interface

    :param struct vx_core \*chip:
        VX core instance

    :param const struct firmware \*boot:
        the boot record to load

.. _`snd_vx_irq_handler`:

snd_vx_irq_handler
==================

.. c:function:: irqreturn_t snd_vx_irq_handler(int irq, void *dev)

    interrupt handler

    :param int irq:
        irq number

    :param void \*dev:
        VX core instance

.. _`snd_vx_dsp_boot`:

snd_vx_dsp_boot
===============

.. c:function:: int snd_vx_dsp_boot(struct vx_core *chip, const struct firmware *boot)

    load the DSP boot

    :param struct vx_core \*chip:
        VX core instance

    :param const struct firmware \*boot:
        firmware data

.. _`snd_vx_dsp_load`:

snd_vx_dsp_load
===============

.. c:function:: int snd_vx_dsp_load(struct vx_core *chip, const struct firmware *dsp)

    load the DSP image

    :param struct vx_core \*chip:
        VX core instance

    :param const struct firmware \*dsp:
        firmware data

.. _`snd_vx_create`:

snd_vx_create
=============

.. c:function:: struct vx_core *snd_vx_create(struct snd_card *card, struct snd_vx_hardware *hw, struct snd_vx_ops *ops, int extra_size)

    constructor for struct vx_core

    :param struct snd_card \*card:
        card instance

    :param struct snd_vx_hardware \*hw:
        hardware specific record

    :param struct snd_vx_ops \*ops:
        VX ops pointer

    :param int extra_size:
        extra byte size to allocate appending to chip

.. _`snd_vx_create.description`:

Description
-----------

this function allocates the instance and prepare for the hardware
initialization.

return the instance pointer if successful, NULL in error.

.. This file was automatic generated / don't edit.

