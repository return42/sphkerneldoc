.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/codecs/sigmadsp.c

.. _`devm_sigmadsp_init`:

devm_sigmadsp_init
==================

.. c:function:: struct sigmadsp *devm_sigmadsp_init(struct device *dev, const struct sigmadsp_ops *ops, const char *firmware_name)

    Initialize SigmaDSP instance

    :param dev:
        The parent device
    :type dev: struct device \*

    :param ops:
        The sigmadsp_ops to use for this instance
    :type ops: const struct sigmadsp_ops \*

    :param firmware_name:
        Name of the firmware file to load
    :type firmware_name: const char \*

.. _`devm_sigmadsp_init.description`:

Description
-----------

Allocates a SigmaDSP instance and loads the specified firmware file.

Returns a pointer to a struct sigmadsp on success, or a \ :c:func:`PTR_ERR`\  on error.

.. _`sigmadsp_attach`:

sigmadsp_attach
===============

.. c:function:: int sigmadsp_attach(struct sigmadsp *sigmadsp, struct snd_soc_component *component)

    Attach a sigmadsp instance to a ASoC component

    :param sigmadsp:
        The sigmadsp instance to attach
    :type sigmadsp: struct sigmadsp \*

    :param component:
        The component to attach to
    :type component: struct snd_soc_component \*

.. _`sigmadsp_attach.description`:

Description
-----------

Typically called in the components probe callback.

Note, once this function has been called the firmware must not be released
until after the ALSA snd_card that the component belongs to has been
disconnected, even if \ :c:func:`sigmadsp_attach`\  returns an error.

.. _`sigmadsp_setup`:

sigmadsp_setup
==============

.. c:function:: int sigmadsp_setup(struct sigmadsp *sigmadsp, unsigned int samplerate)

    Setup the DSP for the specified samplerate

    :param sigmadsp:
        The sigmadsp instance to configure
    :type sigmadsp: struct sigmadsp \*

    :param samplerate:
        The samplerate the DSP should be configured for
    :type samplerate: unsigned int

.. _`sigmadsp_setup.description`:

Description
-----------

Loads the appropriate firmware program and parameter memory (if not already
loaded) and enables the controls for the specified samplerate. Any control
parameter changes that have been made previously will be restored.

Returns 0 on success, a negative error code otherwise.

.. _`sigmadsp_reset`:

sigmadsp_reset
==============

.. c:function:: void sigmadsp_reset(struct sigmadsp *sigmadsp)

    Notify the sigmadsp instance that the DSP has been reset

    :param sigmadsp:
        The sigmadsp instance to reset
    :type sigmadsp: struct sigmadsp \*

.. _`sigmadsp_reset.description`:

Description
-----------

Should be called whenever the DSP has been reset and parameter and program
memory need to be re-loaded.

.. _`sigmadsp_restrict_params`:

sigmadsp_restrict_params
========================

.. c:function:: int sigmadsp_restrict_params(struct sigmadsp *sigmadsp, struct snd_pcm_substream *substream)

    Applies DSP firmware specific constraints

    :param sigmadsp:
        The sigmadsp instance
    :type sigmadsp: struct sigmadsp \*

    :param substream:
        The substream to restrict
    :type substream: struct snd_pcm_substream \*

.. _`sigmadsp_restrict_params.description`:

Description
-----------

Applies samplerate constraints that may be required by the firmware Should
typically be called from the CODEC/component drivers startup callback.

Returns 0 on success, a negative error code otherwise.

.. This file was automatic generated / don't edit.

