.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/drivers/vx/vx_core.c

.. _`snd_vx_load_boot_image`:

snd_vx_load_boot_image
======================

.. c:function:: int snd_vx_load_boot_image(struct vx_core *chip, const struct firmware *boot)

    boot up the xilinx interface

    :param chip:
        VX core instance
    :type chip: struct vx_core \*

    :param boot:
        the boot record to load
    :type boot: const struct firmware \*

.. _`snd_vx_irq_handler`:

snd_vx_irq_handler
==================

.. c:function:: irqreturn_t snd_vx_irq_handler(int irq, void *dev)

    interrupt handler

    :param irq:
        irq number
    :type irq: int

    :param dev:
        VX core instance
    :type dev: void \*

.. _`snd_vx_dsp_boot`:

snd_vx_dsp_boot
===============

.. c:function:: int snd_vx_dsp_boot(struct vx_core *chip, const struct firmware *boot)

    load the DSP boot

    :param chip:
        VX core instance
    :type chip: struct vx_core \*

    :param boot:
        firmware data
    :type boot: const struct firmware \*

.. _`snd_vx_dsp_load`:

snd_vx_dsp_load
===============

.. c:function:: int snd_vx_dsp_load(struct vx_core *chip, const struct firmware *dsp)

    load the DSP image

    :param chip:
        VX core instance
    :type chip: struct vx_core \*

    :param dsp:
        firmware data
    :type dsp: const struct firmware \*

.. _`snd_vx_create`:

snd_vx_create
=============

.. c:function:: struct vx_core *snd_vx_create(struct snd_card *card, struct snd_vx_hardware *hw, struct snd_vx_ops *ops, int extra_size)

    constructor for struct vx_core

    :param card:
        card instance
    :type card: struct snd_card \*

    :param hw:
        hardware specific record
    :type hw: struct snd_vx_hardware \*

    :param ops:
        VX ops pointer
    :type ops: struct snd_vx_ops \*

    :param extra_size:
        extra byte size to allocate appending to chip
    :type extra_size: int

.. _`snd_vx_create.description`:

Description
-----------

this function allocates the instance and prepare for the hardware
initialization.

return the instance pointer if successful, NULL in error.

.. This file was automatic generated / don't edit.

