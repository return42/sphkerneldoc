.. -*- coding: utf-8; mode: rst -*-

=======
hwdep.c
=======

.. _`snd_hwdep_new`:

snd_hwdep_new
=============

.. c:function:: int snd_hwdep_new (struct snd_card *card, char *id, int device, struct snd_hwdep **rhwdep)

    create a new hwdep instance

    :param struct snd_card \*card:
        the card instance

    :param char \*id:
        the id string

    :param int device:
        the device index (zero-based)

    :param struct snd_hwdep \*\*rhwdep:
        the pointer to store the new hwdep instance


.. _`snd_hwdep_new.description`:

Description
-----------

Creates a new hwdep instance with the given index on the card.
The callbacks (hwdep->ops) must be set on the returned instance
after this call manually by the caller.

Return: Zero if successful, or a negative error code on failure.

