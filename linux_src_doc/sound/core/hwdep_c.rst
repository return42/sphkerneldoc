.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/hwdep.c

.. _`snd_hwdep_new`:

snd_hwdep_new
=============

.. c:function:: int snd_hwdep_new(struct snd_card *card, char *id, int device, struct snd_hwdep **rhwdep)

    create a new hwdep instance

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param id:
        the id string
    :type id: char \*

    :param device:
        the device index (zero-based)
    :type device: int

    :param rhwdep:
        the pointer to store the new hwdep instance
    :type rhwdep: struct snd_hwdep \*\*

.. _`snd_hwdep_new.description`:

Description
-----------

Creates a new hwdep instance with the given index on the card.
The callbacks (hwdep->ops) must be set on the returned instance
after this call manually by the caller.

.. _`snd_hwdep_new.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. This file was automatic generated / don't edit.

