.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/sound/sound.c

.. _`channel`:

struct channel
==============

.. c:type:: struct channel

    private structure to keep channel specific data

.. _`channel.definition`:

Definition
----------

.. code-block:: c

    struct channel {
        struct snd_pcm_substream *substream;
        struct snd_pcm_hardware pcm_hardware;
        struct most_interface *iface;
        struct most_channel_config *cfg;
        struct snd_card *card;
        struct list_head list;
        int id;
        unsigned int period_pos;
        unsigned int buffer_pos;
        bool is_stream_running;
        struct task_struct *playback_task;
        wait_queue_head_t playback_waitq;
        void (*copy_fn)(void *alsa, void *most, unsigned int bytes);
    }

.. _`channel.members`:

Members
-------

substream
    stores the substream structure

pcm_hardware
    *undescribed*

iface
    interface for which the channel belongs to

cfg
    channel configuration

card
    registered sound card

list
    list for private use

id
    channel index

period_pos
    current period position (ring buffer)

buffer_pos
    current buffer position (ring buffer)

is_stream_running
    identifies whether a stream is running or not

playback_task
    playback thread

playback_waitq
    waitq used by playback thread

copy_fn
    *undescribed*

.. _`get_channel`:

get_channel
===========

.. c:function:: struct channel *get_channel(struct most_interface *iface, int channel_id)

    get pointer to channel

    :param iface:
        interface structure
    :type iface: struct most_interface \*

    :param channel_id:
        channel ID
    :type channel_id: int

.. _`get_channel.description`:

Description
-----------

This traverses the channel list and returns the channel matching the
ID and interface.

Returns pointer to channel on success or NULL otherwise.

.. _`copy_data`:

copy_data
=========

.. c:function:: bool copy_data(struct channel *channel, struct mbo *mbo)

    implements data copying function

    :param channel:
        channel
    :type channel: struct channel \*

    :param mbo:
        MBO from core
    :type mbo: struct mbo \*

.. _`copy_data.description`:

Description
-----------

Copy data from/to ring buffer to/from MBO and update the buffer position

.. _`playback_thread`:

playback_thread
===============

.. c:function:: int playback_thread(void *data)

    function implements the playback thread

    :param data:
        private data
    :type data: void \*

.. _`playback_thread.description`:

Description
-----------

Thread which does the playback functionality in a loop. It waits for a free
MBO from mostcore for a particular channel and copy the data from ring buffer
to MBO. Submit the MBO back to mostcore, after copying the data.

Returns 0 on success or error code otherwise.

.. _`pcm_open`:

pcm_open
========

.. c:function:: int pcm_open(struct snd_pcm_substream *substream)

    implements open callback function for PCM middle layer

    :param substream:
        pointer to ALSA PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`pcm_open.description`:

Description
-----------

This is called when a PCM substream is opened. At least, the function should
initialize the runtime->hw record.

Returns 0 on success or error code otherwise.

.. _`pcm_close`:

pcm_close
=========

.. c:function:: int pcm_close(struct snd_pcm_substream *substream)

    implements close callback function for PCM middle layer

    :param substream:
        sub-stream pointer
    :type substream: struct snd_pcm_substream \*

.. _`pcm_close.description`:

Description
-----------

Obviously, this is called when a PCM substream is closed. Any private
instance for a PCM substream allocated in the open callback will be
released here.

Returns 0 on success or error code otherwise.

.. _`pcm_hw_params`:

pcm_hw_params
=============

.. c:function:: int pcm_hw_params(struct snd_pcm_substream *substream, struct snd_pcm_hw_params *hw_params)

    implements hw_params callback function for PCM middle layer

    :param substream:
        sub-stream pointer
    :type substream: struct snd_pcm_substream \*

    :param hw_params:
        contains the hardware parameters set by the application
    :type hw_params: struct snd_pcm_hw_params \*

.. _`pcm_hw_params.description`:

Description
-----------

This is called when the hardware parameters is set by the application, that
is, once when the buffer size, the period size, the format, etc. are defined
for the PCM substream. Many hardware setups should be done is this callback,
including the allocation of buffers.

Returns 0 on success or error code otherwise.

.. _`pcm_hw_free`:

pcm_hw_free
===========

.. c:function:: int pcm_hw_free(struct snd_pcm_substream *substream)

    implements hw_free callback function for PCM middle layer

    :param substream:
        substream pointer
    :type substream: struct snd_pcm_substream \*

.. _`pcm_hw_free.description`:

Description
-----------

This is called to release the resources allocated via hw_params.
This function will be always called before the close callback is called.

Returns 0 on success or error code otherwise.

.. _`pcm_prepare`:

pcm_prepare
===========

.. c:function:: int pcm_prepare(struct snd_pcm_substream *substream)

    implements prepare callback function for PCM middle layer

    :param substream:
        substream pointer
    :type substream: struct snd_pcm_substream \*

.. _`pcm_prepare.description`:

Description
-----------

This callback is called when the PCM is "prepared". Format rate, sample rate,
etc., can be set here. This callback can be called many times at each setup.

Returns 0 on success or error code otherwise.

.. _`pcm_trigger`:

pcm_trigger
===========

.. c:function:: int pcm_trigger(struct snd_pcm_substream *substream, int cmd)

    implements trigger callback function for PCM middle layer

    :param substream:
        substream pointer
    :type substream: struct snd_pcm_substream \*

    :param cmd:
        action to perform
    :type cmd: int

.. _`pcm_trigger.description`:

Description
-----------

This is called when the PCM is started, stopped or paused. The action will be
specified in the second argument, SNDRV_PCM_TRIGGER_XXX

Returns 0 on success or error code otherwise.

.. _`pcm_pointer`:

pcm_pointer
===========

.. c:function:: snd_pcm_uframes_t pcm_pointer(struct snd_pcm_substream *substream)

    implements pointer callback function for PCM middle layer

    :param substream:
        substream pointer
    :type substream: struct snd_pcm_substream \*

.. _`pcm_pointer.description`:

Description
-----------

This callback is called when the PCM middle layer inquires the current
hardware position on the buffer. The position must be returned in frames,
ranging from 0 to buffer_size-1.

.. _`audio_probe_channel`:

audio_probe_channel
===================

.. c:function:: int audio_probe_channel(struct most_interface *iface, int channel_id, struct most_channel_config *cfg, char *arg_list)

    probe function of the driver module

    :param iface:
        pointer to interface instance
    :type iface: struct most_interface \*

    :param channel_id:
        channel index/ID
    :type channel_id: int

    :param cfg:
        pointer to actual channel configuration
    :type cfg: struct most_channel_config \*

    :param arg_list:
        string that provides the name of the device to be created in /dev
        plus the desired audio resolution
    :type arg_list: char \*

.. _`audio_probe_channel.description`:

Description
-----------

Creates sound card, pcm device, sets pcm ops and registers sound card.

Returns 0 on success or error code otherwise.

.. _`audio_disconnect_channel`:

audio_disconnect_channel
========================

.. c:function:: int audio_disconnect_channel(struct most_interface *iface, int channel_id)

    function to disconnect a channel

    :param iface:
        pointer to interface instance
    :type iface: struct most_interface \*

    :param channel_id:
        channel index
    :type channel_id: int

.. _`audio_disconnect_channel.description`:

Description
-----------

This frees allocated memory and removes the sound card from ALSA

Returns 0 on success or error code otherwise.

.. _`audio_rx_completion`:

audio_rx_completion
===================

.. c:function:: int audio_rx_completion(struct mbo *mbo)

    completion handler for rx channels

    :param mbo:
        pointer to buffer object that has completed
    :type mbo: struct mbo \*

.. _`audio_rx_completion.description`:

Description
-----------

This searches for the channel this MBO belongs to and copy the data from MBO
to ring buffer

Returns 0 on success or error code otherwise.

.. _`audio_tx_completion`:

audio_tx_completion
===================

.. c:function:: int audio_tx_completion(struct most_interface *iface, int channel_id)

    completion handler for tx channels

    :param iface:
        pointer to interface instance
    :type iface: struct most_interface \*

    :param channel_id:
        channel index/ID
    :type channel_id: int

.. _`audio_tx_completion.description`:

Description
-----------

This searches the channel that belongs to this combination of interface
pointer and channel ID and wakes a process sitting in the wait queue of
this channel.

Returns 0 on success or error code otherwise.

.. This file was automatic generated / don't edit.

