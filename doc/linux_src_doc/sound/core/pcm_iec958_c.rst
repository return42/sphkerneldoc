.. -*- coding: utf-8; mode: rst -*-

============
pcm_iec958.c
============


.. _`snd_pcm_create_iec958_consumer`:

snd_pcm_create_iec958_consumer
==============================

.. c:function:: int snd_pcm_create_iec958_consumer (struct snd_pcm_runtime *runtime, u8 *cs, size_t len)

    create consumer format IEC958 channel status

    :param struct snd_pcm_runtime \*runtime:
        pcm runtime structure with ->rate filled in

    :param u8 \*cs:
        channel status buffer, at least four bytes

    :param size_t len:
        length of channel status buffer



.. _`snd_pcm_create_iec958_consumer.description`:

Description
-----------

Create the consumer format channel status data in ``cs`` of maximum size
``len`` corresponding to the parameters of the PCM runtime ``runtime``\ .

Drivers may wish to tweak the contents of the buffer after creation.



.. _`snd_pcm_create_iec958_consumer.returns`:

Returns
-------

length of buffer, or negative error code if something failed.

