.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pcmcia/pdaudiocf/pdaudiocf.c

.. _`snd_pdacf_assign_resources`:

snd_pdacf_assign_resources
==========================

.. c:function:: int snd_pdacf_assign_resources(struct snd_pdacf *pdacf, int port, int irq)

    initialize the hardware and card instance.

    :param pdacf:
        *undescribed*
    :type pdacf: struct snd_pdacf \*

    :param port:
        i/o port for the card
    :type port: int

    :param irq:
        irq number for the card
    :type irq: int

.. _`snd_pdacf_assign_resources.description`:

Description
-----------

this function assigns the specified port and irq, boot the card,
create pcm and control instances, and initialize the rest hardware.

returns 0 if successful, or a negative error code.

.. This file was automatic generated / don't edit.

