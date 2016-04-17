.. -*- coding: utf-8; mode: rst -*-

=======
sound.c
=======


.. _`snd_request_card`:

snd_request_card
================

.. c:function:: void snd_request_card (int card)

    try to load the card module

    :param int card:
        the card number



.. _`snd_request_card.description`:

Description
-----------

Tries to load the module "snd-card-X" for the given card number
via request_module.  Returns immediately if already loaded.



.. _`snd_lookup_minor_data`:

snd_lookup_minor_data
=====================

.. c:function:: void *snd_lookup_minor_data (unsigned int minor, int type)

    get user data of a registered device

    :param unsigned int minor:
        the minor number

    :param int type:
        device type (SNDRV_DEVICE_TYPE_XXX)



.. _`snd_lookup_minor_data.description`:

Description
-----------

Checks that a minor device with the specified type is registered, and returns
its user data pointer.

This function increments the reference counter of the card instance
if an associated instance with the given minor number and type is found.
The caller must call :c:func:`snd_card_unref` appropriately later.



.. _`snd_lookup_minor_data.return`:

Return
------

The user data pointer if the specified device is found. ``NULL``
otherwise.



.. _`snd_register_device`:

snd_register_device
===================

.. c:function:: int snd_register_device (int type, struct snd_card *card, int dev, const struct file_operations *f_ops, void *private_data, struct device *device)

    Register the ALSA device file for the card

    :param int type:
        the device type, SNDRV_DEVICE_TYPE_XXX

    :param struct snd_card \*card:
        the card instance

    :param int dev:
        the device index

    :param const struct file_operations \*f_ops:
        the file operations

    :param void \*private_data:
        user pointer for f_ops->:c:func:`open`

    :param struct device \*device:
        the device to register



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

.. c:function:: int snd_unregister_device (struct device *dev)

    unregister the device on the given card

    :param struct device \*dev:
        the device instance



.. _`snd_unregister_device.description`:

Description
-----------

Unregisters the device file already registered via
:c:func:`snd_register_device`.



.. _`snd_unregister_device.return`:

Return
------

Zero if successful, or a negative error code on failure.

