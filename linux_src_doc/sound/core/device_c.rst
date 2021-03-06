.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/device.c

.. _`snd_device_new`:

snd_device_new
==============

.. c:function:: int snd_device_new(struct snd_card *card, enum snd_device_type type, void *device_data, struct snd_device_ops *ops)

    create an ALSA device component

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param type:
        the device type, SNDRV_DEV_XXX
    :type type: enum snd_device_type

    :param device_data:
        the data pointer of this device
    :type device_data: void \*

    :param ops:
        the operator table
    :type ops: struct snd_device_ops \*

.. _`snd_device_new.description`:

Description
-----------

Creates a new device component for the given data pointer.
The device will be assigned to the card and managed together
by the card.

The data pointer plays a role as the identifier, too, so the
pointer address must be unique and unchanged.

.. _`snd_device_new.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_device_disconnect`:

snd_device_disconnect
=====================

.. c:function:: void snd_device_disconnect(struct snd_card *card, void *device_data)

    disconnect the device

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param device_data:
        the data pointer to disconnect
    :type device_data: void \*

.. _`snd_device_disconnect.description`:

Description
-----------

Turns the device into the disconnection state, invoking
dev_disconnect callback, if the device was already registered.

Usually called from \ :c:func:`snd_card_disconnect`\ .

.. _`snd_device_disconnect.return`:

Return
------

Zero if successful, or a negative error code on failure or if the
device not found.

.. _`snd_device_free`:

snd_device_free
===============

.. c:function:: void snd_device_free(struct snd_card *card, void *device_data)

    release the device from the card

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param device_data:
        the data pointer to release
    :type device_data: void \*

.. _`snd_device_free.description`:

Description
-----------

Removes the device from the list on the card and invokes the
callbacks, dev_disconnect and dev_free, corresponding to the state.
Then release the device.

.. _`snd_device_register`:

snd_device_register
===================

.. c:function:: int snd_device_register(struct snd_card *card, void *device_data)

    register the device

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param device_data:
        the data pointer to register
    :type device_data: void \*

.. _`snd_device_register.description`:

Description
-----------

Registers the device which was already created via
\ :c:func:`snd_device_new`\ .  Usually this is called from \ :c:func:`snd_card_register`\ ,
but it can be called later if any new devices are created after
invocation of \ :c:func:`snd_card_register`\ .

.. _`snd_device_register.return`:

Return
------

Zero if successful, or a negative error code on failure or if the
device not found.

.. This file was automatic generated / don't edit.

