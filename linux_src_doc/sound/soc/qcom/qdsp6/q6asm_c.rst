.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/qcom/qdsp6/q6asm.c

.. _`q6asm_unmap_memory_regions`:

q6asm_unmap_memory_regions
==========================

.. c:function:: int q6asm_unmap_memory_regions(unsigned int dir, struct audio_client *ac)

    unmap memory regions in the dsp.

    :param dir:
        direction of audio stream
    :type dir: unsigned int

    :param ac:
        audio client instanace
    :type ac: struct audio_client \*

.. _`q6asm_unmap_memory_regions.return`:

Return
------

Will be an negative value on failure or zero on success

.. _`q6asm_map_memory_regions`:

q6asm_map_memory_regions
========================

.. c:function:: int q6asm_map_memory_regions(unsigned int dir, struct audio_client *ac, phys_addr_t phys, size_t period_sz, unsigned int periods)

    map memory regions in the dsp.

    :param dir:
        direction of audio stream
    :type dir: unsigned int

    :param ac:
        audio client instanace
    :type ac: struct audio_client \*

    :param phys:
        physcial address that needs mapping.
    :type phys: phys_addr_t

    :param period_sz:
        audio period size
    :type period_sz: size_t

    :param periods:
        number of periods
    :type periods: unsigned int

.. _`q6asm_map_memory_regions.return`:

Return
------

Will be an negative value on failure or zero on success

.. _`q6asm_audio_client_free`:

q6asm_audio_client_free
=======================

.. c:function:: void q6asm_audio_client_free(struct audio_client *ac)

    Freee allocated audio client

    :param ac:
        audio client to free
    :type ac: struct audio_client \*

.. _`q6asm_get_session_id`:

q6asm_get_session_id
====================

.. c:function:: int q6asm_get_session_id(struct audio_client *c)

    get session id for audio client

    :param c:
        audio client pointer
    :type c: struct audio_client \*

.. _`q6asm_get_session_id.return`:

Return
------

Will be an session id of the audio client.

.. _`q6asm_audio_client_alloc`:

q6asm_audio_client_alloc
========================

.. c:function:: struct audio_client *q6asm_audio_client_alloc(struct device *dev, q6asm_cb cb, void *priv, int stream_id, int perf_mode)

    Allocate a new audio client

    :param dev:
        Pointer to asm child device.
    :type dev: struct device \*

    :param cb:
        event callback.
    :type cb: q6asm_cb

    :param priv:
        private data associated with this client.
    :type priv: void \*

    :param stream_id:
        stream id
    :type stream_id: int

    :param perf_mode:
        performace mode for this client
    :type perf_mode: int

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

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

    :param format:
        audio sample format
    :type format: uint32_t

    :param bits_per_sample:
        bits per sample
    :type bits_per_sample: uint16_t

.. _`q6asm_open_write.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_run`:

q6asm_run
=========

.. c:function:: int q6asm_run(struct audio_client *ac, uint32_t flags, uint32_t msw_ts, uint32_t lsw_ts)

    start the audio client

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

    :param flags:
        flags associated with write
    :type flags: uint32_t

    :param msw_ts:
        timestamp msw
    :type msw_ts: uint32_t

    :param lsw_ts:
        timestamp lsw
    :type lsw_ts: uint32_t

.. _`q6asm_run.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_run_nowait`:

q6asm_run_nowait
================

.. c:function:: int q6asm_run_nowait(struct audio_client *ac, uint32_t flags, uint32_t msw_ts, uint32_t lsw_ts)

    start the audio client withou blocking

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

    :param flags:
        flags associated with write
    :type flags: uint32_t

    :param msw_ts:
        timestamp msw
    :type msw_ts: uint32_t

    :param lsw_ts:
        timestamp lsw
    :type lsw_ts: uint32_t

.. _`q6asm_run_nowait.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_media_format_block_multi_ch_pcm`:

q6asm_media_format_block_multi_ch_pcm
=====================================

.. c:function:: int q6asm_media_format_block_multi_ch_pcm(struct audio_client *ac, uint32_t rate, uint32_t channels, u8 channel_map, uint16_t bits_per_sample)

    setup pcm configuration

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

    :param rate:
        audio sample rate
    :type rate: uint32_t

    :param channels:
        number of audio channels.
    :type channels: uint32_t

    :param channel_map:
        channel map pointer
    :type channel_map: u8

    :param bits_per_sample:
        bits per sample
    :type bits_per_sample: uint16_t

.. _`q6asm_media_format_block_multi_ch_pcm.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_enc_cfg_blk_pcm_format_support`:

q6asm_enc_cfg_blk_pcm_format_support
====================================

.. c:function:: int q6asm_enc_cfg_blk_pcm_format_support(struct audio_client *ac, uint32_t rate, uint32_t channels, uint16_t bits_per_sample)

    setup pcm configuration for capture

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

    :param rate:
        audio sample rate
    :type rate: uint32_t

    :param channels:
        number of audio channels.
    :type channels: uint32_t

    :param bits_per_sample:
        bits per sample
    :type bits_per_sample: uint16_t

.. _`q6asm_enc_cfg_blk_pcm_format_support.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_read`:

q6asm_read
==========

.. c:function:: int q6asm_read(struct audio_client *ac)

    read data of period size from audio client

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

.. _`q6asm_read.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_open_read`:

q6asm_open_read
===============

.. c:function:: int q6asm_open_read(struct audio_client *ac, uint32_t format, uint16_t bits_per_sample)

    Open audio client for reading

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

    :param format:
        audio sample format
    :type format: uint32_t

    :param bits_per_sample:
        bits per sample
    :type bits_per_sample: uint16_t

.. _`q6asm_open_read.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_write_async`:

q6asm_write_async
=================

.. c:function:: int q6asm_write_async(struct audio_client *ac, uint32_t len, uint32_t msw_ts, uint32_t lsw_ts, uint32_t wflags)

    non blocking write

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

    :param len:
        lenght in bytes
    :type len: uint32_t

    :param msw_ts:
        timestamp msw
    :type msw_ts: uint32_t

    :param lsw_ts:
        timestamp lsw
    :type lsw_ts: uint32_t

    :param wflags:
        flags associated with write
    :type wflags: uint32_t

.. _`q6asm_write_async.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_cmd`:

q6asm_cmd
=========

.. c:function:: int q6asm_cmd(struct audio_client *ac, int cmd)

    run cmd on audio client

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

    :param cmd:
        command to run on audio client.
    :type cmd: int

.. _`q6asm_cmd.return`:

Return
------

Will be an negative value on error or zero on success

.. _`q6asm_cmd_nowait`:

q6asm_cmd_nowait
================

.. c:function:: int q6asm_cmd_nowait(struct audio_client *ac, int cmd)

    non blocking, run cmd on audio client

    :param ac:
        audio client pointer
    :type ac: struct audio_client \*

    :param cmd:
        command to run on audio client.
    :type cmd: int

.. _`q6asm_cmd_nowait.return`:

Return
------

Will be an negative value on error or zero on success

.. This file was automatic generated / don't edit.

