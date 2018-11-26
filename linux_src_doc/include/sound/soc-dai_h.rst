.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/soc-dai.h

.. _`snd_soc_dai_set_sdw_stream`:

snd_soc_dai_set_sdw_stream
==========================

.. c:function:: int snd_soc_dai_set_sdw_stream(struct snd_soc_dai *dai, void *stream, int direction)

    Configures a DAI for SDW stream operation

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param stream:
        STREAM
    :type stream: void \*

    :param direction:
        Stream direction(Playback/Capture)
        SoundWire subsystem doesn't have a notion of direction and we reuse
        the ASoC stream direction to configure sink/source ports.
        Playback maps to source ports and Capture for sink ports.
    :type direction: int

.. _`snd_soc_dai_set_sdw_stream.description`:

Description
-----------

This should be invoked with NULL to clear the stream set previously.
Returns 0 on success, a negative error code otherwise.

.. This file was automatic generated / don't edit.

