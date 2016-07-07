.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/hda_beep.c

.. _`snd_hda_enable_beep_device`:

snd_hda_enable_beep_device
==========================

.. c:function:: int snd_hda_enable_beep_device(struct hda_codec *codec, int enable)

    Turn on/off beep sound

    :param struct hda_codec \*codec:
        the HDA codec

    :param int enable:
        flag to turn on/off

.. _`snd_hda_attach_beep_device`:

snd_hda_attach_beep_device
==========================

.. c:function:: int snd_hda_attach_beep_device(struct hda_codec *codec, int nid)

    Attach a beep input device

    :param struct hda_codec \*codec:
        the HDA codec

    :param int nid:
        beep NID

.. _`snd_hda_attach_beep_device.description`:

Description
-----------

Attach a beep object to the given widget.  If beep hint is turned off
explicitly or beep_mode of the codec is turned off, this doesn't nothing.

The attached beep device has to be registered via
\ :c:func:`snd_hda_register_beep_device`\  and released via \ :c:func:`snd_hda_detach_beep_device`\ 
appropriately.

Currently, only one beep device is allowed to each codec.

.. _`snd_hda_detach_beep_device`:

snd_hda_detach_beep_device
==========================

.. c:function:: void snd_hda_detach_beep_device(struct hda_codec *codec)

    Detach the beep device

    :param struct hda_codec \*codec:
        the HDA codec

.. _`snd_hda_register_beep_device`:

snd_hda_register_beep_device
============================

.. c:function:: int snd_hda_register_beep_device(struct hda_codec *codec)

    Register the beep device

    :param struct hda_codec \*codec:
        the HDA codec

.. _`snd_hda_mixer_amp_switch_get_beep`:

snd_hda_mixer_amp_switch_get_beep
=================================

.. c:function:: int snd_hda_mixer_amp_switch_get_beep(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Get callback for beep controls

    :param struct snd_kcontrol \*kcontrol:
        ctl element

    :param struct snd_ctl_elem_value \*ucontrol:
        pointer to get/store the data

.. _`snd_hda_mixer_amp_switch_put_beep`:

snd_hda_mixer_amp_switch_put_beep
=================================

.. c:function:: int snd_hda_mixer_amp_switch_put_beep(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Put callback for beep controls

    :param struct snd_kcontrol \*kcontrol:
        ctl element

    :param struct snd_ctl_elem_value \*ucontrol:
        pointer to get/store the data

.. This file was automatic generated / don't edit.

