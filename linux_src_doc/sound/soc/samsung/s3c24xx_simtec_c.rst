.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/samsung/s3c24xx_simtec.c

.. _`speaker_gain_get`:

speaker_gain_get
================

.. c:function:: int speaker_gain_get(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    read the speaker gain setting.

    :param kcontrol:
        The control for the speaker gain.
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        The value that needs to be updated.
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`speaker_gain_get.description`:

Description
-----------

Read the value for the AMP gain control.

.. _`speaker_gain_set`:

speaker_gain_set
================

.. c:function:: void speaker_gain_set(int value)

    set the value of the speaker amp gain

    :param value:
        The value to write.
    :type value: int

.. _`speaker_gain_put`:

speaker_gain_put
================

.. c:function:: int speaker_gain_put(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    set the speaker gain setting.

    :param kcontrol:
        The control for the speaker gain.
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        The value that needs to be set.
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`speaker_gain_put.description`:

Description
-----------

Set the value of the speaker gain from the specified
\ ``ucontrol``\  setting.

Note, if the speaker amp is muted, then we do not set a gain value
as at-least one of the ICs that is fitted will try and power up even
if the main control is set to off.

.. _`spk_unmute_state`:

spk_unmute_state
================

.. c:function:: void spk_unmute_state(int to)

    set the unmute state of the speaker

    :param to:
        zero to unmute, non-zero to ununmute.
    :type to: int

.. _`speaker_unmute_get`:

speaker_unmute_get
==================

.. c:function:: int speaker_unmute_get(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    read the speaker unmute setting.

    :param kcontrol:
        The control for the speaker gain.
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        The value that needs to be updated.
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`speaker_unmute_get.description`:

Description
-----------

Read the value for the AMP gain control.

.. _`speaker_unmute_put`:

speaker_unmute_put
==================

.. c:function:: int speaker_unmute_put(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    set the speaker unmute setting.

    :param kcontrol:
        The control for the speaker gain.
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        The value that needs to be set.
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`speaker_unmute_put.description`:

Description
-----------

Set the value of the speaker gain from the specified
\ ``ucontrol``\  setting.

.. _`simtec_hw_params`:

simtec_hw_params
================

.. c:function:: int simtec_hw_params(struct snd_pcm_substream *substream, struct snd_pcm_hw_params *params)

    update hardware parameters

    :param substream:
        The audio substream instance.
    :type substream: struct snd_pcm_substream \*

    :param params:
        The parameters requested.
    :type params: struct snd_pcm_hw_params \*

.. _`simtec_hw_params.description`:

Description
-----------

Update the codec data routing and configuration  settings
from the supplied data.

.. _`attach_gpio_amp`:

attach_gpio_amp
===============

.. c:function:: int attach_gpio_amp(struct device *dev, struct s3c24xx_audio_simtec_pdata *pd)

    get and configure the necessary gpios

    :param dev:
        The device we're probing.
    :type dev: struct device \*

    :param pd:
        The platform data supplied by the board.
    :type pd: struct s3c24xx_audio_simtec_pdata \*

.. _`attach_gpio_amp.description`:

Description
-----------

If there is a GPIO based amplifier attached to the board, claim
the necessary GPIO lines for it, and set default values.

.. This file was automatic generated / don't edit.

