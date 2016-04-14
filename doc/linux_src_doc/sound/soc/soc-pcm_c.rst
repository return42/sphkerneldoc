.. -*- coding: utf-8; mode: rst -*-

=========
soc-pcm.c
=========

.. _`snd_soc_runtime_activate`:

snd_soc_runtime_activate
========================

.. c:function:: void snd_soc_runtime_activate (struct snd_soc_pcm_runtime *rtd, int stream)

    Increment active count for PCM runtime components

    :param struct snd_soc_pcm_runtime \*rtd:
        ASoC PCM runtime that is activated

    :param int stream:
        Direction of the PCM stream


.. _`snd_soc_runtime_activate.description`:

Description
-----------

Increments the active count for all the DAIs and components attached to a PCM
runtime. Should typically be called when a stream is opened.

Must be called with the rtd->pcm_mutex being held


.. _`snd_soc_runtime_deactivate`:

snd_soc_runtime_deactivate
==========================

.. c:function:: void snd_soc_runtime_deactivate (struct snd_soc_pcm_runtime *rtd, int stream)

    Decrement active count for PCM runtime components

    :param struct snd_soc_pcm_runtime \*rtd:
        ASoC PCM runtime that is deactivated

    :param int stream:
        Direction of the PCM stream


.. _`snd_soc_runtime_deactivate.description`:

Description
-----------

Decrements the active count for all the DAIs and components attached to a PCM
runtime. Should typically be called when a stream is closed.

Must be called with the rtd->pcm_mutex being held


.. _`snd_soc_runtime_ignore_pmdown_time`:

snd_soc_runtime_ignore_pmdown_time
==================================

.. c:function:: bool snd_soc_runtime_ignore_pmdown_time (struct snd_soc_pcm_runtime *rtd)

    Check whether to ignore the power down delay

    :param struct snd_soc_pcm_runtime \*rtd:
        The ASoC PCM runtime that should be checked.


.. _`snd_soc_runtime_ignore_pmdown_time.description`:

Description
-----------

This function checks whether the power down delay should be ignored for a
specific PCM runtime. Returns true if the delay is 0, if it the DAI link has
been configured to ignore the delay, or if none of the components benefits
from having the delay.


.. _`snd_soc_set_runtime_hwparams`:

snd_soc_set_runtime_hwparams
============================

.. c:function:: int snd_soc_set_runtime_hwparams (struct snd_pcm_substream *substream, const struct snd_pcm_hardware *hw)

    set the runtime hardware parameters

    :param struct snd_pcm_substream \*substream:
        the pcm substream

    :param const struct snd_pcm_hardware \*hw:
        the hardware parameters


.. _`snd_soc_set_runtime_hwparams.description`:

Description
-----------

Sets the substream runtime hardware parameters.

