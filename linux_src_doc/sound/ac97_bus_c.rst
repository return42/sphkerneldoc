.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/ac97_bus.c

.. _`snd_ac97_reset`:

snd_ac97_reset
==============

.. c:function:: int snd_ac97_reset(struct snd_ac97 *ac97, bool try_warm, unsigned int id, unsigned int id_mask)

    Reset AC'97 device

    :param ac97:
        The AC'97 device to reset
    :type ac97: struct snd_ac97 \*

    :param try_warm:
        Try a warm reset first
    :type try_warm: bool

    :param id:
        Expected device vendor ID
    :type id: unsigned int

    :param id_mask:
        Mask that is applied to the device ID before comparing to \ ``id``\ 
    :type id_mask: unsigned int

.. _`snd_ac97_reset.description`:

Description
-----------

This function resets the AC'97 device. If \ ``try_warm``\  is true the function
first performs a warm reset. If the warm reset is successful the function
returns 1. Otherwise or if \ ``try_warm``\  is false the function issues cold reset
followed by a warm reset. If this is successful the function returns 0,
otherwise a negative error code. If \ ``id``\  is 0 any valid device ID will be
accepted, otherwise only the ID that matches \ ``id``\  and \ ``id_mask``\  is accepted.

.. This file was automatic generated / don't edit.

