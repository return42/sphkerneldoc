.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/ac97/ac97_codec.c

.. _`snd_ac97_write`:

snd_ac97_write
==============

.. c:function:: void snd_ac97_write(struct snd_ac97 *ac97, unsigned short reg, unsigned short value)

    write a value on the given register

    :param ac97:
        the ac97 instance
    :type ac97: struct snd_ac97 \*

    :param reg:
        the register to change
    :type reg: unsigned short

    :param value:
        the value to set
    :type value: unsigned short

.. _`snd_ac97_write.description`:

Description
-----------

Writes a value on the given register.  This will invoke the write
callback directly after the register check.
This function doesn't change the register cache unlike
#snd_ca97_write_cache(), so use this only when you don't want to
reflect the change to the suspend/resume state.

.. _`snd_ac97_read`:

snd_ac97_read
=============

.. c:function:: unsigned short snd_ac97_read(struct snd_ac97 *ac97, unsigned short reg)

    read a value from the given register

    :param ac97:
        the ac97 instance
    :type ac97: struct snd_ac97 \*

    :param reg:
        the register to read
    :type reg: unsigned short

.. _`snd_ac97_read.description`:

Description
-----------

Reads a value from the given register.  This will invoke the read
callback directly after the register check.

.. _`snd_ac97_read.return`:

Return
------

The read value.

.. _`snd_ac97_write_cache`:

snd_ac97_write_cache
====================

.. c:function:: void snd_ac97_write_cache(struct snd_ac97 *ac97, unsigned short reg, unsigned short value)

    write a value on the given register and update the cache

    :param ac97:
        the ac97 instance
    :type ac97: struct snd_ac97 \*

    :param reg:
        the register to change
    :type reg: unsigned short

    :param value:
        the value to set
    :type value: unsigned short

.. _`snd_ac97_write_cache.description`:

Description
-----------

Writes a value on the given register and updates the register
cache.  The cached values are used for the cached-read and the
suspend/resume.

.. _`snd_ac97_update`:

snd_ac97_update
===============

.. c:function:: int snd_ac97_update(struct snd_ac97 *ac97, unsigned short reg, unsigned short value)

    update the value on the given register

    :param ac97:
        the ac97 instance
    :type ac97: struct snd_ac97 \*

    :param reg:
        the register to change
    :type reg: unsigned short

    :param value:
        the value to set
    :type value: unsigned short

.. _`snd_ac97_update.description`:

Description
-----------

Compares the value with the register cache and updates the value
only when the value is changed.

.. _`snd_ac97_update.return`:

Return
------

1 if the value is changed, 0 if no change, or a negative
code on failure.

.. _`snd_ac97_update_bits`:

snd_ac97_update_bits
====================

.. c:function:: int snd_ac97_update_bits(struct snd_ac97 *ac97, unsigned short reg, unsigned short mask, unsigned short value)

    update the bits on the given register

    :param ac97:
        the ac97 instance
    :type ac97: struct snd_ac97 \*

    :param reg:
        the register to change
    :type reg: unsigned short

    :param mask:
        the bit-mask to change
    :type mask: unsigned short

    :param value:
        the value to set
    :type value: unsigned short

.. _`snd_ac97_update_bits.description`:

Description
-----------

Updates the masked-bits on the given register only when the value
is changed.

.. _`snd_ac97_update_bits.return`:

Return
------

1 if the bits are changed, 0 if no change, or a negative
code on failure.

.. _`snd_ac97_get_short_name`:

snd_ac97_get_short_name
=======================

.. c:function:: const char *snd_ac97_get_short_name(struct snd_ac97 *ac97)

    retrieve codec name

    :param ac97:
        the codec instance
    :type ac97: struct snd_ac97 \*

.. _`snd_ac97_get_short_name.return`:

Return
------

The short identifying name of the codec.

.. _`snd_ac97_bus`:

snd_ac97_bus
============

.. c:function:: int snd_ac97_bus(struct snd_card *card, int num, struct snd_ac97_bus_ops *ops, void *private_data, struct snd_ac97_bus **rbus)

    create an AC97 bus component

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param num:
        the bus number
    :type num: int

    :param ops:
        the bus callbacks table
    :type ops: struct snd_ac97_bus_ops \*

    :param private_data:
        private data pointer for the new instance
    :type private_data: void \*

    :param rbus:
        the pointer to store the new AC97 bus instance.
    :type rbus: struct snd_ac97_bus \*\*

.. _`snd_ac97_bus.description`:

Description
-----------

Creates an AC97 bus component.  An struct snd_ac97_bus instance is newly
allocated and initialized.

The ops table must include valid callbacks (at least read and
write).  The other callbacks, wait and reset, are not mandatory.

The clock is set to 48000.  If another clock is needed, set
``(*rbus)->clock`` manually.

The AC97 bus instance is registered as a low-level device, so you don't
have to release it manually.

.. _`snd_ac97_bus.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_ac97_mixer`:

snd_ac97_mixer
==============

.. c:function:: int snd_ac97_mixer(struct snd_ac97_bus *bus, struct snd_ac97_template *template, struct snd_ac97 **rac97)

    create an Codec97 component

    :param bus:
        the AC97 bus which codec is attached to
    :type bus: struct snd_ac97_bus \*

    :param template:
        the template of ac97, including index, callbacks and
        the private data.
    :type template: struct snd_ac97_template \*

    :param rac97:
        the pointer to store the new ac97 instance.
    :type rac97: struct snd_ac97 \*\*

.. _`snd_ac97_mixer.description`:

Description
-----------

Creates an Codec97 component.  An struct snd_ac97 instance is newly
allocated and initialized from the template.  The codec
is then initialized by the standard procedure.

The template must include the codec number (num) and address (addr),
and the private data (private_data).

The ac97 instance is registered as a low-level device, so you don't
have to release it manually.

.. _`snd_ac97_mixer.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_ac97_update_power`:

snd_ac97_update_power
=====================

.. c:function:: int snd_ac97_update_power(struct snd_ac97 *ac97, int reg, int powerup)

    update the powerdown register

    :param ac97:
        the codec instance
    :type ac97: struct snd_ac97 \*

    :param reg:
        the rate register, e.g. AC97_PCM_FRONT_DAC_RATE
    :type reg: int

    :param powerup:
        non-zero when power up the part
    :type powerup: int

.. _`snd_ac97_update_power.description`:

Description
-----------

Update the AC97 powerdown register bits of the given part.

.. _`snd_ac97_update_power.return`:

Return
------

Zero.

.. _`snd_ac97_suspend`:

snd_ac97_suspend
================

.. c:function:: void snd_ac97_suspend(struct snd_ac97 *ac97)

    General suspend function for AC97 codec

    :param ac97:
        the ac97 instance
    :type ac97: struct snd_ac97 \*

.. _`snd_ac97_suspend.description`:

Description
-----------

Suspends the codec, power down the chip.

.. _`snd_ac97_resume`:

snd_ac97_resume
===============

.. c:function:: void snd_ac97_resume(struct snd_ac97 *ac97)

    General resume function for AC97 codec

    :param ac97:
        the ac97 instance
    :type ac97: struct snd_ac97 \*

.. _`snd_ac97_resume.description`:

Description
-----------

Do the standard resume procedure, power up and restoring the
old register values.

.. _`snd_ac97_tune_hardware`:

snd_ac97_tune_hardware
======================

.. c:function:: int snd_ac97_tune_hardware(struct snd_ac97 *ac97, const struct ac97_quirk *quirk, const char *override)

    tune up the hardware

    :param ac97:
        the ac97 instance
    :type ac97: struct snd_ac97 \*

    :param quirk:
        quirk list
    :type quirk: const struct ac97_quirk \*

    :param override:
        explicit quirk value (overrides the list if non-NULL)
    :type override: const char \*

.. _`snd_ac97_tune_hardware.description`:

Description
-----------

Do some workaround for each pci device, such as renaming of the
headphone (true line-out) control as "Master".
The quirk-list must be terminated with a zero-filled entry.

.. _`snd_ac97_tune_hardware.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. This file was automatic generated / don't edit.

