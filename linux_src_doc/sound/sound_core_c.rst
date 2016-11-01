.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/sound_core.c

.. _`register_sound_special_device`:

register_sound_special_device
=============================

.. c:function:: int register_sound_special_device(const struct file_operations *fops, int unit, struct device *dev)

    register a special sound node

    :param const struct file_operations \*fops:
        File operations for the driver

    :param int unit:
        Unit number to allocate

    :param struct device \*dev:
        device pointer

.. _`register_sound_special_device.description`:

Description
-----------

     Allocate a special sound device by minor number from the sound
     subsystem.

.. _`register_sound_special_device.return`:

Return
------

The allocated number is returned on success. On failure,
     a negative error code is returned.

.. _`register_sound_mixer`:

register_sound_mixer
====================

.. c:function:: int register_sound_mixer(const struct file_operations *fops, int dev)

    register a mixer device

    :param const struct file_operations \*fops:
        File operations for the driver

    :param int dev:
        Unit number to allocate

.. _`register_sound_mixer.description`:

Description
-----------

     Allocate a mixer device. Unit is the number of the mixer requested.
     Pass -1 to request the next free mixer unit.

.. _`register_sound_mixer.return`:

Return
------

On success, the allocated number is returned. On failure,
     a negative error code is returned.

.. _`register_sound_midi`:

register_sound_midi
===================

.. c:function:: int register_sound_midi(const struct file_operations *fops, int dev)

    register a midi device

    :param const struct file_operations \*fops:
        File operations for the driver

    :param int dev:
        Unit number to allocate

.. _`register_sound_midi.description`:

Description
-----------

     Allocate a midi device. Unit is the number of the midi device requested.
     Pass -1 to request the next free midi unit.

.. _`register_sound_midi.return`:

Return
------

On success, the allocated number is returned. On failure,
     a negative error code is returned.

.. _`register_sound_dsp`:

register_sound_dsp
==================

.. c:function:: int register_sound_dsp(const struct file_operations *fops, int dev)

    register a DSP device

    :param const struct file_operations \*fops:
        File operations for the driver

    :param int dev:
        Unit number to allocate

.. _`register_sound_dsp.description`:

Description
-----------

     Allocate a DSP device. Unit is the number of the DSP requested.
     Pass -1 to request the next free DSP unit.

     This function allocates both the audio and dsp device entries together
     and will always allocate them as a matching pair - eg dsp3/audio3

.. _`register_sound_dsp.return`:

Return
------

On success, the allocated number is returned. On failure,
     a negative error code is returned.

.. _`unregister_sound_special`:

unregister_sound_special
========================

.. c:function:: void unregister_sound_special(int unit)

    unregister a special sound device

    :param int unit:
        unit number to allocate

.. _`unregister_sound_special.description`:

Description
-----------

     Release a sound device that was allocated with
     \ :c:func:`register_sound_special`\ . The unit passed is the return value from
     the register function.

.. _`unregister_sound_mixer`:

unregister_sound_mixer
======================

.. c:function:: void unregister_sound_mixer(int unit)

    unregister a mixer

    :param int unit:
        unit number to allocate

.. _`unregister_sound_mixer.description`:

Description
-----------

     Release a sound device that was allocated with \ :c:func:`register_sound_mixer`\ .
     The unit passed is the return value from the register function.

.. _`unregister_sound_midi`:

unregister_sound_midi
=====================

.. c:function:: void unregister_sound_midi(int unit)

    unregister a midi device

    :param int unit:
        unit number to allocate

.. _`unregister_sound_midi.description`:

Description
-----------

     Release a sound device that was allocated with \ :c:func:`register_sound_midi`\ .
     The unit passed is the return value from the register function.

.. _`unregister_sound_dsp`:

unregister_sound_dsp
====================

.. c:function:: void unregister_sound_dsp(int unit)

    unregister a DSP device

    :param int unit:
        unit number to allocate

.. _`unregister_sound_dsp.description`:

Description
-----------

     Release a sound device that was allocated with \ :c:func:`register_sound_dsp`\ .
     The unit passed is the return value from the register function.

     Both of the allocated units are released together automatically.

.. This file was automatic generated / don't edit.

