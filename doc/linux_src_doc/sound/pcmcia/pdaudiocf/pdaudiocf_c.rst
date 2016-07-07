.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pcmcia/pdaudiocf/pdaudiocf.c

.. _`snd_pdacf_assign_resources`:

snd_pdacf_assign_resources
==========================

.. c:function:: int snd_pdacf_assign_resources(struct snd_pdacf *pdacf, int port, int irq)

    initialize the hardware and card instance.

    :param struct snd_pdacf \*pdacf:
        *undescribed*

    :param int port:
        i/o port for the card

    :param int irq:
        irq number for the card

.. _`snd_pdacf_assign_resources.description`:

Description
-----------

this function assigns the specified port and irq, boot the card,
create pcm and control instances, and initialize the rest hardware.

returns 0 if successful, or a negative error code.

.. This file was automatic generated / don't edit.

