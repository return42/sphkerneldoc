.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/qcom/qdsp6/q6asm.c

.. _`q6asm_unmap_memory_regions`:

q6asm_unmap_memory_regions
==========================

.. c:function:: int q6asm_unmap_memory_regions(unsigned int dir, struct audio_client *ac)

    unmap memory regions in the dsp.

    :param unsigned int dir:
        direction of audio stream

    :param struct audio_client \*ac:
        audio client instanace

.. _`q6asm_unmap_memory_regions.return`:

Return
------

Will be an negative value on failure or zero on success

.. _`q6asm_map_memory_regions`:

q6asm_map_memory_regions
========================

.. c:function:: int q6asm_map_memory_regions(unsigned int dir, struct audio_client *ac, phys_addr_t phys, size_t period_sz, unsigned int periods)

    map memory regions in the dsp.

    :param unsigned int dir:
        direction of audio stream

    :param struct audio_client \*ac:
        audio client instanace

    :param phys_addr_t phys:
        physcial address that needs mapping.

    :param size_t period_sz:
        audio period size

    :param unsigned int periods:
        number of periods

.. _`q6asm_map_memory_regions.return`:

Return
------

Will be an negative value on failure or zero on success

.. _`q6asm_audio_client_free`:

q6asm_audio_client_free
=======================

.. c:function:: void q6asm_audio_client_free(struct audio_client *ac)

    Freee allocated audio client

    :param struct audio_client \*ac:
        audio client to free

.. _`q6asm_get_session_id`:

q6asm_get_session_id
====================

.. c:function:: int q6asm_get_session_id(struct audio_client *c)

    get session id for audio client

    :param struct audio_client \*c:
        audio client pointer

.. _`q6asm_get_session_id.return`:

Return
------

Will be an session id of the audio client.

.. _`q6asm_audio_client_alloc`:

q6asm_audio_client_alloc
========================

.. c:function:: struct audio_client *q6asm_audio_client_alloc(struct device *dev, q6asm_cb cb, void *priv, int stream_id, int perf_mode)

    Allocate a new audio client

    :param struct device \*dev:
        Pointer to asm child device.

    :param q6asm_cb cb:
        event callback.

    :param void \*priv:
        private data associated with this client.

    :param int stream_id:
        stream id

    :param int perf_mode:
        performace mode for this client

.. _`q6asm_audio_client_alloc.return`:

Return
------

Will be an error pointer on error or a valid audio client
on success.

.. _`q6asm_open_write`:

q6asm_open_write
================

.. c:function:: int q6asm_open_write(struct audio_client *ac, uint32_t format, uint16_t bits_per_sample)

    Open audio client for writing

    :param struct audio_client \*ac:
        audio client pointer

    :param uint32_t format:
        audio sample format

    :param uint16_t bits_per_sample:
        bits per sample

.. _`q6asm_open_write.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_run`:

q6asm_run
=========

.. c:function:: int q6asm_run(struct audio_client *ac, uint32_t flags, uint32_t msw_ts, uint32_t lsw_ts)

    start the audio client

    :param struct audio_client \*ac:
        audio client pointer

    :param uint32_t flags:
        flags associated with write

    :param uint32_t msw_ts:
        timestamp msw

    :param uint32_t lsw_ts:
        timestamp lsw

.. _`q6asm_run.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_run_nowait`:

q6asm_run_nowait
================

.. c:function:: int q6asm_run_nowait(struct audio_client *ac, uint32_t flags, uint32_t msw_ts, uint32_t lsw_ts)

    start the audio client withou blocking

    :param struct audio_client \*ac:
        audio client pointer

    :param uint32_t flags:
        flags associated with write

    :param uint32_t msw_ts:
        timestamp msw

    :param uint32_t lsw_ts:
        timestamp lsw

.. _`q6asm_run_nowait.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_media_format_block_multi_ch_pcm`:

q6asm_media_format_block_multi_ch_pcm
=====================================

.. c:function:: int q6asm_media_format_block_multi_ch_pcm(struct audio_client *ac, uint32_t rate, uint32_t channels, u8 channel_map, uint16_t bits_per_sample)

    setup pcm configuration

    :param struct audio_client \*ac:
        audio client pointer

    :param uint32_t rate:
        audio sample rate

    :param uint32_t channels:
        number of audio channels.

    :param u8 channel_map:
        channel map pointer

    :param uint16_t bits_per_sample:
        bits per sample

.. _`q6asm_media_format_block_multi_ch_pcm.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_enc_cfg_blk_pcm_format_support`:

q6asm_enc_cfg_blk_pcm_format_support
====================================

.. c:function:: int q6asm_enc_cfg_blk_pcm_format_support(struct audio_client *ac, uint32_t rate, uint32_t channels, uint16_t bits_per_sample)

    setup pcm configuration for capture

    :param struct audio_client \*ac:
        audio client pointer

    :param uint32_t rate:
        audio sample rate

    :param uint32_t channels:
        number of audio channels.

    :param uint16_t bits_per_sample:
        bits per sample

.. _`q6asm_enc_cfg_blk_pcm_format_support.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_read`:

q6asm_read
==========

.. c:function:: int q6asm_read(struct audio_client *ac)

    read data of period size from audio client

    :param struct audio_client \*ac:
        audio client pointer

.. _`q6asm_read.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_open_read`:

q6asm_open_read
===============

.. c:function:: int q6asm_open_read(struct audio_client *ac, uint32_t format, uint16_t bits_per_sample)

    Open audio client for reading

    :param struct audio_client \*ac:
        audio client pointer

    :param uint32_t format:
        audio sample format

    :param uint16_t bits_per_sample:
        bits per sample

.. _`q6asm_open_read.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_write_async`:

q6asm_write_async
=================

.. c:function:: int q6asm_write_async(struct audio_client *ac, uint32_t len, uint32_t msw_ts, uint32_t lsw_ts, uint32_t wflags)

    non blocking write

    :param struct audio_client \*ac:
        audio client pointer

    :param uint32_t len:
        lenght in bytes

    :param uint32_t msw_ts:
        timestamp msw

    :param uint32_t lsw_ts:
        timestamp lsw

    :param uint32_t wflags:
        flags associated with write

.. _`q6asm_write_async.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_cmd`:

q6asm_cmd
=========

.. c:function:: int q6asm_cmd(struct audio_client *ac, int cmd)

    run cmd on audio client

    :param struct audio_client \*ac:
        audio client pointer

    :param int cmd:
        command to run on audio client.

.. _`q6asm_cmd.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_cmd_nowait`:

q6asm_cmd_nowait
================

.. c:function:: int q6asm_cmd_nowait(struct audio_client *ac, int cmd)

    non blocking, run cmd on audio client

    :param struct audio_client \*ac:
        audio client pointer

    :param int cmd:
        command to run on audio client.

.. _`q6asm_cmd_nowait.return`:

Return
------

Will be an negative value on error or zero on success

.. This file was automatic generated / don't edit.

