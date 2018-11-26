.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/sound.c

.. _`snd_request_card`:

snd_request_card
================

.. c:function:: void snd_request_card(int card)

    try to load the card module

    :param card:
        the card number
    :type card: int

.. _`snd_request_card.description`:

Description
-----------

Tries to load the module "snd-card-X" for the given card number
via request_module.  Returns immediately if already loaded.

.. _`snd_lookup_minor_data`:

snd_lookup_minor_data
=====================

.. c:function:: void *snd_lookup_minor_data(unsigned int minor, int type)

    get user data of a registered device

    :param minor:
        the minor number
    :type minor: unsigned int

    :param type:
        device type (SNDRV_DEVICE_TYPE_XXX)
    :type type: int

.. _`snd_lookup_minor_data.description`:

Description
-----------

Checks that a minor device with the specified type is registered, and returns
its user data pointer.

This function increments the reference counter of the card instance
if an associated instance with the given minor number and type is found.
The caller must call \ :c:func:`snd_card_unref`\  appropriately later.

.. _`snd_lookup_minor_data.return`:

Return
------

The user data pointer if the specified device is found. \ ``NULL``\ 
otherwise.

.. _`snd_register_device`:

snd_register_device
===================

.. c:function:: int snd_register_device(int type, struct snd_card *card, int dev, const struct file_operations *f_ops, void *private_data, struct device *device)

    Register the ALSA device file for the card

    :param type:
        the device type, SNDRV_DEVICE_TYPE_XXX
    :type type: int

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param dev:
        the device index
    :type dev: int

    :param f_ops:
        the file operations
    :type f_ops: const struct file_operations \*

    :param private_data:
        user pointer for f_ops->open()
    :type private_data: void \*

    :param device:
        the device to register
    :type device: struct device \*

.. _`snd_register_device.description`:

Description
-----------

Registers an ALSA device file for the given card.
The operators have to be set in reg parameter.

.. _`snd_register_device.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_unregister_device`:

snd_unregister_device
=====================

.. c:function:: int snd_unregister_device(struct device *dev)

    unregister the device on the given card

    :param dev:
        the device instance
    :type dev: struct device \*

.. _`snd_unregister_device.description`:

Description
-----------

Unregisters the device file already registered via
\ :c:func:`snd_register_device`\ .

.. _`snd_unregister_device.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. This file was automatic generated / don't edit.

