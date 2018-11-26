.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/pcm_iec958.c

.. _`snd_pcm_create_iec958_consumer`:

snd_pcm_create_iec958_consumer
==============================

.. c:function:: int snd_pcm_create_iec958_consumer(struct snd_pcm_runtime *runtime, u8 *cs, size_t len)

    create consumer format IEC958 channel status

    :param runtime:
        pcm runtime structure with ->rate filled in
    :type runtime: struct snd_pcm_runtime \*

    :param cs:
        channel status buffer, at least four bytes
    :type cs: u8 \*

    :param len:
        length of channel status buffer
    :type len: size_t

.. _`snd_pcm_create_iec958_consumer.description`:

Description
-----------

Create the consumer format channel status data in \ ``cs``\  of maximum size
\ ``len``\  corresponding to the parameters of the PCM runtime \ ``runtime``\ .

Drivers may wish to tweak the contents of the buffer after creation.

.. _`snd_pcm_create_iec958_consumer.return`:

Return
------

length of buffer, or negative error code if something failed.

.. _`snd_pcm_create_iec958_consumer_hw_params`:

snd_pcm_create_iec958_consumer_hw_params
========================================

.. c:function:: int snd_pcm_create_iec958_consumer_hw_params(struct snd_pcm_hw_params *params, u8 *cs, size_t len)

    create IEC958 channel status

    :param params:
        *undescribed*
    :type params: struct snd_pcm_hw_params \*

    :param cs:
        channel status buffer, at least four bytes
    :type cs: u8 \*

    :param len:
        length of channel status buffer
    :type len: size_t

.. _`snd_pcm_create_iec958_consumer_hw_params.description`:

Description
-----------

Create the consumer format channel status data in \ ``cs``\  of maximum size
\ ``len``\  corresponding to the parameters of the PCM runtime \ ``runtime``\ .

Drivers may wish to tweak the contents of the buffer after creation.

.. _`snd_pcm_create_iec958_consumer_hw_params.return`:

Return
------

length of buffer, or negative error code if something failed.

.. This file was automatic generated / don't edit.

