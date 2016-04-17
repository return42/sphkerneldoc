.. -*- coding: utf-8; mode: rst -*-

==========
vxpocket.c
==========


.. _`snd_vxpocket_assign_resources`:

snd_vxpocket_assign_resources
=============================

.. c:function:: int snd_vxpocket_assign_resources (struct vx_core *chip, int port, int irq)

    initialize the hardware and card instance.

    :param struct vx_core \*chip:
        VX core instance

    :param int port:
        i/o port for the card

    :param int irq:
        irq number for the card



.. _`snd_vxpocket_assign_resources.description`:

Description
-----------

this function assigns the specified port and irq, boot the card,
create pcm and control instances, and initialize the rest hardware.

returns 0 if successful, or a negative error code.

