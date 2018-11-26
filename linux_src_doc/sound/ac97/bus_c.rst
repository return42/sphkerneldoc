.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/ac97/bus.c

.. _`snd_ac97_codec_driver_register`:

snd_ac97_codec_driver_register
==============================

.. c:function:: int snd_ac97_codec_driver_register(struct ac97_codec_driver *drv)

    register an AC97 codec driver

    :param drv:
        *undescribed*
    :type drv: struct ac97_codec_driver \*

.. _`snd_ac97_codec_driver_register.description`:

Description
-----------

Register an AC97 codec driver to the ac97 bus driver, aka. the AC97 digital
controller.

Returns 0 on success or error code

.. _`snd_ac97_codec_driver_unregister`:

snd_ac97_codec_driver_unregister
================================

.. c:function:: void snd_ac97_codec_driver_unregister(struct ac97_codec_driver *drv)

    unregister an AC97 codec driver

    :param drv:
        *undescribed*
    :type drv: struct ac97_codec_driver \*

.. _`snd_ac97_codec_driver_unregister.description`:

Description
-----------

Unregister a previously registered ac97 codec driver.

.. _`snd_ac97_codec_get_platdata`:

snd_ac97_codec_get_platdata
===========================

.. c:function:: void *snd_ac97_codec_get_platdata(const struct ac97_codec_device *adev)

    get platform_data

    :param adev:
        the ac97 codec device
    :type adev: const struct ac97_codec_device \*

.. _`snd_ac97_codec_get_platdata.description`:

Description
-----------

For legacy platforms, in order to have platform_data in codec drivers
available, while ac97 device are auto-created upon probe, this retrieves the
platdata which was setup on ac97 controller registration.

Returns the platform data pointer

.. _`snd_ac97_controller_register`:

snd_ac97_controller_register
============================

.. c:function:: struct ac97_controller *snd_ac97_controller_register(const struct ac97_controller_ops *ops, struct device *dev, unsigned short slots_available, void **codecs_pdata)

    register an ac97 controller

    :param ops:
        the ac97 bus operations
    :type ops: const struct ac97_controller_ops \*

    :param dev:
        the device providing the ac97 DC function
    :type dev: struct device \*

    :param slots_available:
        mask of the ac97 codecs that can be scanned and probed
        bit0 => codec 0, bit1 => codec 1 ... bit 3 => codec 3
    :type slots_available: unsigned short

    :param codecs_pdata:
        *undescribed*
    :type codecs_pdata: void \*\*

.. _`snd_ac97_controller_register.description`:

Description
-----------

Register a digital controller which can control up to 4 ac97 codecs. This is
the controller side of the AC97 AC-link, while the slave side are the codecs.

Returns a valid controller upon success, negative pointer value upon error

.. _`snd_ac97_controller_unregister`:

snd_ac97_controller_unregister
==============================

.. c:function:: void snd_ac97_controller_unregister(struct ac97_controller *ac97_ctrl)

    unregister an ac97 controller

    :param ac97_ctrl:
        the device previously provided to \ :c:func:`ac97_controller_register`\ 
    :type ac97_ctrl: struct ac97_controller \*

.. This file was automatic generated / don't edit.

