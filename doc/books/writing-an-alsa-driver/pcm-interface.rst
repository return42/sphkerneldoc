.. -*- coding: utf-8; mode: rst -*-

.. _pcm-interface:

=============
PCM Interface
=============


.. _pcm-interface-general:

General
=======

The PCM middle layer of ALSA is quite powerful and it is only necessary
for each driver to implement the low-level functions to access its
hardware.

For accessing to the PCM layer, you need to include ``<sound/pcm.h>``
first. In addition, ``<sound/pcm_params.h>`` might be needed if you
access to some functions related with hw_param.

Each card device can have up to four pcm instances. A pcm instance
corresponds to a pcm device file. The limitation of number of instances
comes only from the available bit size of the Linux's device numbers.
Once when 64bit device number is used, we'll have more pcm instances
available.

A pcm instance consists of pcm playback and capture streams, and each
pcm stream consists of one or more pcm substreams. Some soundcards
support multiple playback functions. For example, emu10k1 has a PCM
playback of 32 stereo substreams. In this case, at each open, a free
substream is (usually) automatically chosen and opened. Meanwhile, when
only one substream exists and it was already opened, the successful open
will either block or error with ``EAGAIN`` according to the file open
mode. But you don't have to care about such details in your driver. The
PCM middle layer will take care of such work.


.. _pcm-interface-example:

Full Code Example
=================

The example code below does not include any hardware access routines but
shows only the skeleton, how to build up the PCM interfaces.


.. code-block:: c

      #include <sound/pcm.h>
      ....

      /* hardware definition */
      static struct snd_pcm_hardware snd_mychip_playback_hw = {
              .info = (SNDRV_PCM_INFO_MMAP |
                       SNDRV_PCM_INFO_INTERLEAVED |
                       SNDRV_PCM_INFO_BLOCK_TRANSFER |
                       SNDRV_PCM_INFO_MMAP_VALID),
              .formats =          SNDRV_PCM_FMTBIT_S16_LE,
              .rates =            SNDRV_PCM_RATE_8000_48000,
              .rate_min =         8000,
              .rate_max =         48000,
              .channels_min =     2,
              .channels_max =     2,
              .buffer_bytes_max = 32768,
              .period_bytes_min = 4096,
              .period_bytes_max = 32768,
              .periods_min =      1,
              .periods_max =      1024,
      };

      /* hardware definition */
      static struct snd_pcm_hardware snd_mychip_capture_hw = {
              .info = (SNDRV_PCM_INFO_MMAP |
                       SNDRV_PCM_INFO_INTERLEAVED |
                       SNDRV_PCM_INFO_BLOCK_TRANSFER |
                       SNDRV_PCM_INFO_MMAP_VALID),
              .formats =          SNDRV_PCM_FMTBIT_S16_LE,
              .rates =            SNDRV_PCM_RATE_8000_48000,
              .rate_min =         8000,
              .rate_max =         48000,
              .channels_min =     2,
              .channels_max =     2,
              .buffer_bytes_max = 32768,
              .period_bytes_min = 4096,
              .period_bytes_max = 32768,
              .periods_min =      1,
              .periods_max =      1024,
      };

      /* open callback */
      static int snd_mychip_playback_open(struct snd_pcm_substream *substream)
      {
              struct mychip *chip = snd_pcm_substream_chip(substream);
              struct snd_pcm_runtime *runtime = substream->runtime;

              runtime->hw = snd_mychip_playback_hw;
              /* more hardware-initialization will be done here */
              ....
              return 0;
      }

      /* close callback */
      static int snd_mychip_playback_close(struct snd_pcm_substream *substream)
      {
              struct mychip *chip = snd_pcm_substream_chip(substream);
              /* the hardware-specific codes will be here */
              ....
              return 0;

      }

      /* open callback */
      static int snd_mychip_capture_open(struct snd_pcm_substream *substream)
      {
              struct mychip *chip = snd_pcm_substream_chip(substream);
              struct snd_pcm_runtime *runtime = substream->runtime;

              runtime->hw = snd_mychip_capture_hw;
              /* more hardware-initialization will be done here */
              ....
              return 0;
      }

      /* close callback */
      static int snd_mychip_capture_close(struct snd_pcm_substream *substream)
      {
              struct mychip *chip = snd_pcm_substream_chip(substream);
              /* the hardware-specific codes will be here */
              ....
              return 0;

      }

      /* hw_params callback */
      static int snd_mychip_pcm_hw_params(struct snd_pcm_substream *substream,
                                   struct snd_pcm_hw_params *hw_params)
      {
              return snd_pcm_lib_malloc_pages(substream,
                                         params_buffer_bytes(hw_params));
      }

      /* hw_free callback */
      static int snd_mychip_pcm_hw_free(struct snd_pcm_substream *substream)
      {
              return snd_pcm_lib_free_pages(substream);
      }

      /* prepare callback */
      static int snd_mychip_pcm_prepare(struct snd_pcm_substream *substream)
      {
              struct mychip *chip = snd_pcm_substream_chip(substream);
              struct snd_pcm_runtime *runtime = substream->runtime;

              /* set up the hardware with the current configuration
               * for example...
               */
              mychip_set_sample_format(chip, runtime->format);
              mychip_set_sample_rate(chip, runtime->rate);
              mychip_set_channels(chip, runtime->channels);
              mychip_set_dma_setup(chip, runtime->dma_addr,
                                   chip->buffer_size,
                                   chip->period_size);
              return 0;
      }

      /* trigger callback */
      static int snd_mychip_pcm_trigger(struct snd_pcm_substream *substream,
                                        int cmd)
      {
              switch (cmd) {
              case SNDRV_PCM_TRIGGER_START:
                      /* do something to start the PCM engine */
                      ....
                      break;
              case SNDRV_PCM_TRIGGER_STOP:
                      /* do something to stop the PCM engine */
                      ....
                      break;
              default:
                      return -EINVAL;
              }
      }

      /* pointer callback */
      static snd_pcm_uframes_t
      snd_mychip_pcm_pointer(struct snd_pcm_substream *substream)
      {
              struct mychip *chip = snd_pcm_substream_chip(substream);
              unsigned int current_ptr;

              /* get the current hardware pointer */
              current_ptr = mychip_get_hw_pointer(chip);
              return current_ptr;
      }

      /* operators */
      static struct snd_pcm_ops snd_mychip_playback_ops = {
              .open =        snd_mychip_playback_open,
              .close =       snd_mychip_playback_close,
              .ioctl =       snd_pcm_lib_ioctl,
              .hw_params =   snd_mychip_pcm_hw_params,
              .hw_free =     snd_mychip_pcm_hw_free,
              .prepare =     snd_mychip_pcm_prepare,
              .trigger =     snd_mychip_pcm_trigger,
              .pointer =     snd_mychip_pcm_pointer,
      };

      /* operators */
      static struct snd_pcm_ops snd_mychip_capture_ops = {
              .open =        snd_mychip_capture_open,
              .close =       snd_mychip_capture_close,
              .ioctl =       snd_pcm_lib_ioctl,
              .hw_params =   snd_mychip_pcm_hw_params,
              .hw_free =     snd_mychip_pcm_hw_free,
              .prepare =     snd_mychip_pcm_prepare,
              .trigger =     snd_mychip_pcm_trigger,
              .pointer =     snd_mychip_pcm_pointer,
      };

      /*
       *  definitions of capture are omitted here...
       */

      /* create a pcm device */
      static int snd_mychip_new_pcm(struct mychip *chip)
      {
              struct snd_pcm *pcm;
              int err;

              err = snd_pcm_new(chip->card, "My Chip", 0, 1, 1, &pcm);
              if (err < 0)
                      return err;
              pcm->private_data = chip;
              strcpy(pcm->name, "My Chip");
              chip->pcm = pcm;
              /* set operators */
              snd_pcm_set_ops(pcm, SNDRV_PCM_STREAM_PLAYBACK,
                              &snd_mychip_playback_ops);
              snd_pcm_set_ops(pcm, SNDRV_PCM_STREAM_CAPTURE,
                              &snd_mychip_capture_ops);
              /* pre-allocation of buffers */
              /* NOTE: this may fail */
              snd_pcm_lib_preallocate_pages_for_all(pcm, SNDRV_DMA_TYPE_DEV,
                                                    snd_dma_pci_data(chip->pci),
                                                    64*1024, 64*1024);
              return 0;
      }


.. _pcm-interface-constructor:

Constructor
===========

A pcm instance is allocated by the ``snd_pcm_new()`` function. It would
be better to create a constructor for pcm, namely,


.. code-block:: c

      static int snd_mychip_new_pcm(struct mychip *chip)
      {
              struct snd_pcm *pcm;
              int err;

              err = snd_pcm_new(chip->card, "My Chip", 0, 1, 1, &pcm);
              if (err < 0)
                      return err;
              pcm->private_data = chip;
              strcpy(pcm->name, "My Chip");
              chip->pcm = pcm;
          ....
              return 0;
      }

The ``snd_pcm_new()`` function takes four arguments. The first argument
is the card pointer to which this pcm is assigned, and the second is the
ID string.

The third argument (``index``, 0 in the above) is the index of this new
pcm. It begins from zero. If you create more than one pcm instances,
specify the different numbers in this argument. For example, ``index`` =
1 for the second PCM device.

The fourth and fifth arguments are the number of substreams for playback
and capture, respectively. Here 1 is used for both arguments. When no
playback or capture substreams are available, pass 0 to the
corresponding argument.

If a chip supports multiple playbacks or captures, you can specify more
numbers, but they must be handled properly in open/close, etc.
callbacks. When you need to know which substream you are referring to,
then it can be obtained from struct ``snd_pcm_substream`` data passed to
each callback as follows:


.. code-block:: c

      struct snd_pcm_substream *substream;
      int index = substream->number;

After the pcm is created, you need to set operators for each pcm stream.


.. code-block:: c

      snd_pcm_set_ops(pcm, SNDRV_PCM_STREAM_PLAYBACK,
                      &snd_mychip_playback_ops);
      snd_pcm_set_ops(pcm, SNDRV_PCM_STREAM_CAPTURE,
                      &snd_mychip_capture_ops);

The operators are defined typically like this:


.. code-block:: c

      static struct snd_pcm_ops snd_mychip_playback_ops = {
              .open =        snd_mychip_pcm_open,
              .close =       snd_mychip_pcm_close,
              .ioctl =       snd_pcm_lib_ioctl,
              .hw_params =   snd_mychip_pcm_hw_params,
              .hw_free =     snd_mychip_pcm_hw_free,
              .prepare =     snd_mychip_pcm_prepare,
              .trigger =     snd_mychip_pcm_trigger,
              .pointer =     snd_mychip_pcm_pointer,
      };

All the callbacks are described in the
:ref:`Operators <pcm-interface-operators>` subsection.

After setting the operators, you probably will want to pre-allocate the
buffer. For the pre-allocation, simply call the following:


.. code-block:: c

      snd_pcm_lib_preallocate_pages_for_all(pcm, SNDRV_DMA_TYPE_DEV,
                                            snd_dma_pci_data(chip->pci),
                                            64*1024, 64*1024);

It will allocate a buffer up to 64kB as default. Buffer management
details will be described in the later section
:ref:`Buffer and Memory Management <buffer-and-memory>`.

Additionally, you can set some extra information for this pcm in
pcm->info_flags. The available values are defined as
``SNDRV_PCM_INFO_XXX`` in ``<sound/asound.h>``, which is used for the
hardware definition (described later). When your soundchip supports only
half-duplex, specify like this:


.. code-block:: c

      pcm->info_flags = SNDRV_PCM_INFO_HALF_DUPLEX;


.. _pcm-interface-destructor:

... And the Destructor?
=======================

The destructor for a pcm instance is not always necessary. Since the pcm
device will be released by the middle layer code automatically, you
don't have to call the destructor explicitly.

The destructor would be necessary if you created special records
internally and needed to release them. In such a case, set the
destructor function to pcm->private_free:


.. code-block:: c

      static void mychip_pcm_free(struct snd_pcm *pcm)
      {
              struct mychip *chip = snd_pcm_chip(pcm);
              /* free your own data */
              kfree(chip->my_private_pcm_data);
              /* do what you like else */
              ....
      }

      static int snd_mychip_new_pcm(struct mychip *chip)
      {
              struct snd_pcm *pcm;
              ....
              /* allocate your own data */
              chip->my_private_pcm_data = kmalloc(...);
              /* set the destructor */
              pcm->private_data = chip;
              pcm->private_free = mychip_pcm_free;
              ....
      }


.. _pcm-interface-runtime:

Runtime Pointer - The Chest of PCM Information
==============================================

When the PCM substream is opened, a PCM runtime instance is allocated
and assigned to the substream. This pointer is accessible via
``substream->runtime``. This runtime pointer holds most information you
need to control the PCM: the copy of hw_params and sw_params
configurations, the buffer pointers, mmap records, spinlocks, etc.

The definition of runtime instance is found in ``<sound/pcm.h>``. Here
are the contents of this file:


.. code-block:: c

    struct _snd_pcm_runtime {
        /* -- Status -- */
        struct snd_pcm_substream *trigger_master;
        snd_timestamp_t trigger_tstamp; /* trigger timestamp */
        int overrange;
        snd_pcm_uframes_t avail_max;
        snd_pcm_uframes_t hw_ptr_base;  /* Position at buffer restart */
        snd_pcm_uframes_t hw_ptr_interrupt; /* Position at interrupt time*/

        /* -- HW params -- */
        snd_pcm_access_t access;    /* access mode */
        snd_pcm_format_t format;    /* SNDRV_PCM_FORMAT_* */
        snd_pcm_subformat_t subformat;  /* subformat */
        unsigned int rate;      /* rate in Hz */
        unsigned int channels;      /* channels */
        snd_pcm_uframes_t period_size;  /* period size */
        unsigned int periods;       /* periods */
        snd_pcm_uframes_t buffer_size;  /* buffer size */
        unsigned int tick_time;     /* tick time */
        snd_pcm_uframes_t min_align;    /* Min alignment for the format */
        size_t byte_align;
        unsigned int frame_bits;
        unsigned int sample_bits;
        unsigned int info;
        unsigned int rate_num;
        unsigned int rate_den;

        /* -- SW params -- */
        struct timespec tstamp_mode;    /* mmap timestamp is updated */
        unsigned int period_step;
        unsigned int sleep_min;     /* min ticks to sleep */
        snd_pcm_uframes_t start_threshold;
        snd_pcm_uframes_t stop_threshold;
        snd_pcm_uframes_t silence_threshold; /* Silence filling happens when
                            noise is nearest than this */
        snd_pcm_uframes_t silence_size; /* Silence filling size */
        snd_pcm_uframes_t boundary; /* pointers wrap point */

        snd_pcm_uframes_t silenced_start;
        snd_pcm_uframes_t silenced_size;

        snd_pcm_sync_id_t sync;     /* hardware synchronization ID */

        /* -- mmap -- */
        volatile struct snd_pcm_mmap_status *status;
        volatile struct snd_pcm_mmap_control *control;
        atomic_t mmap_count;

        /* -- locking / scheduling -- */
        spinlock_t lock;
        wait_queue_head_t sleep;
        struct timer_list tick_timer;
        struct fasync_struct *fasync;

        /* -- private section -- */
        void *private_data;
        void (*private_free)(struct snd_pcm_runtime *runtime);

        /* -- hardware description -- */
        struct snd_pcm_hardware hw;
        struct snd_pcm_hw_constraints hw_constraints;

        /* -- timer -- */
        unsigned int timer_resolution;  /* timer resolution */

        /* -- DMA -- */
        unsigned char *dma_area;    /* DMA area */
        dma_addr_t dma_addr;        /* physical bus address (not accessible from main CPU) */
        size_t dma_bytes;       /* size of DMA area */

        struct snd_dma_buffer *dma_buffer_p;    /* allocated buffer */

    #if defined(CONFIG_SND_PCM_OSS) || defined(CONFIG_SND_PCM_OSS_MODULE)
        /* -- OSS things -- */
        struct snd_pcm_oss_runtime oss;
    #endif
    };

For the operators (callbacks) of each sound driver, most of these
records are supposed to be read-only. Only the PCM middle-layer changes
/ updates them. The exceptions are the hardware description (hw) DMA
buffer information and the private data. Besides, if you use the
standard buffer allocation method via ``snd_pcm_lib_malloc_pages()``,
you don't need to set the DMA buffer information by yourself.

In the sections below, important records are explained.


.. _pcm-interface-runtime-hw:

Hardware Description
--------------------

The hardware descriptor (struct ``snd_pcm_hardware``) contains the
definitions of the fundamental hardware configuration. Above all, you'll
need to define this in
:ref:`the open callback <pcm-interface-operators-open-callback>`. Note
that the runtime instance holds the copy of the descriptor, not the
pointer to the existing descriptor. That is, in the open callback, you
can modify the copied descriptor (``runtime->hw``) as you need. For
example, if the maximum number of channels is 1 only on some chip
models, you can still use the same hardware descriptor and change the
channels_max later:


.. code-block:: c

              struct snd_pcm_runtime *runtime = substream->runtime;
              ...
              runtime->hw = snd_mychip_playback_hw; /* common definition */
              if (chip->model == VERY_OLD_ONE)
                      runtime->hw.channels_max = 1;

Typically, you'll have a hardware descriptor as below:


.. code-block:: c

      static struct snd_pcm_hardware snd_mychip_playback_hw = {
              .info = (SNDRV_PCM_INFO_MMAP |
                       SNDRV_PCM_INFO_INTERLEAVED |
                       SNDRV_PCM_INFO_BLOCK_TRANSFER |
                       SNDRV_PCM_INFO_MMAP_VALID),
              .formats =          SNDRV_PCM_FMTBIT_S16_LE,
              .rates =            SNDRV_PCM_RATE_8000_48000,
              .rate_min =         8000,
              .rate_max =         48000,
              .channels_min =     2,
              .channels_max =     2,
              .buffer_bytes_max = 32768,
              .period_bytes_min = 4096,
              .period_bytes_max = 32768,
              .periods_min =      1,
              .periods_max =      1024,
      };

-  The ``info`` field contains the type and capabilities of this pcm.
   The bit flags are defined in ``<sound/asound.h>`` as
   ``SNDRV_PCM_INFO_XXX``. Here, at least, you have to specify whether
   the mmap is supported and which interleaved format is supported. When
   the hardware supports mmap, add the ``SNDRV_PCM_INFO_MMAP`` flag
   here. When the hardware supports the interleaved or the
   non-interleaved formats, ``SNDRV_PCM_INFO_INTERLEAVED`` or
   ``SNDRV_PCM_INFO_NONINTERLEAVED`` flag must be set, respectively. If
   both are supported, you can set both, too.

   In the above example, ``MMAP_VALID`` and ``BLOCK_TRANSFER`` are
   specified for the OSS mmap mode. Usually both are set. Of course,
   ``MMAP_VALID`` is set only if the mmap is really supported.

   The other possible flags are ``SNDRV_PCM_INFO_PAUSE`` and
   ``SNDRV_PCM_INFO_RESUME``. The ``PAUSE`` bit means that the pcm
   supports the “pause” operation, while the ``RESUME`` bit means that
   the pcm supports the full “suspend/resume” operation. If the
   ``PAUSE`` flag is set, the ``trigger`` callback below must handle the
   corresponding (pause push/release) commands. The suspend/resume
   trigger commands can be defined even without the ``RESUME`` flag. See
   :ref:`Power Management <power-management>` section for details.

   When the PCM substreams can be synchronized (typically, synchronized
   start/stop of a playback and a capture streams), you can give
   ``SNDRV_PCM_INFO_SYNC_START``, too. In this case, you'll need to
   check the linked-list of PCM substreams in the trigger callback. This
   will be described in the later section.

-  ``formats`` field contains the bit-flags of supported formats
   (``SNDRV_PCM_FMTBIT_XXX``). If the hardware supports more than one
   format, give all or'ed bits. In the example above, the signed 16bit
   little-endian format is specified.

-  ``rates`` field contains the bit-flags of supported rates
   (``SNDRV_PCM_RATE_XXX``). When the chip supports continuous rates,
   pass ``CONTINUOUS`` bit additionally. The pre-defined rate bits are
   provided only for typical rates. If your chip supports unconventional
   rates, you need to add the ``KNOT`` bit and set up the hardware
   constraint manually (explained later).

-  ``rate_min`` and ``rate_max`` define the minimum and maximum sample
   rate. This should correspond somehow to ``rates`` bits.

-  ``channel_min`` and ``channel_max`` define, as you might already
   expected, the minimum and maximum number of channels.

-  ``buffer_bytes_max`` defines the maximum buffer size in bytes. There
   is no ``buffer_bytes_min`` field, since it can be calculated from the
   minimum period size and the minimum number of periods. Meanwhile,
   ``period_bytes_min`` and define the minimum and maximum size of the
   period in bytes. ``periods_max`` and ``periods_min`` define the
   maximum and minimum number of periods in the buffer.

   The “period” is a term that corresponds to a fragment in the OSS
   world. The period defines the size at which a PCM interrupt is
   generated. This size strongly depends on the hardware. Generally, the
   smaller period size will give you more interrupts, that is, more
   controls. In the case of capture, this size defines the input
   latency. On the other hand, the whole buffer size defines the output
   latency for the playback direction.

-  There is also a field ``fifo_size``. This specifies the size of the
   hardware FIFO, but currently it is neither used in the driver nor in
   the alsa-lib. So, you can ignore this field.


.. _pcm-interface-runtime-config:

PCM Configurations
------------------

Ok, let's go back again to the PCM runtime records. The most frequently
referred records in the runtime instance are the PCM configurations. The
PCM configurations are stored in the runtime instance after the
application sends ``hw_params`` data via alsa-lib. There are many fields
copied from hw_params and sw_params structs. For example, ``format``
holds the format type chosen by the application. This field contains the
enum value ``SNDRV_PCM_FORMAT_XXX``.

One thing to be noted is that the configured buffer and period sizes are
stored in “frames” in the runtime. In the ALSA world, 1 frame = channels
* samples-size. For conversion between frames and bytes, you can use the
``frames_to_bytes()`` and ``bytes_to_frames()`` helper functions.


.. code-block:: c

      period_bytes = frames_to_bytes(runtime, runtime->period_size);

Also, many software parameters (sw_params) are stored in frames, too.
Please check the type of the field. ``snd_pcm_uframes_t`` is for the
frames as unsigned integer while ``snd_pcm_sframes_t`` is for the frames
as signed integer.


.. _pcm-interface-runtime-dma:

DMA Buffer Information
----------------------

The DMA buffer is defined by the following four fields, ``dma_area``,
``dma_addr``, ``dma_bytes`` and ``dma_private``. The ``dma_area`` holds
the buffer pointer (the logical address). You can call ``memcpy``
from/to this pointer. Meanwhile, ``dma_addr`` holds the physical address
of the buffer. This field is specified only when the buffer is a linear
buffer. ``dma_bytes`` holds the size of buffer in bytes. ``dma_private``
is used for the ALSA DMA allocator.

If you use a standard ALSA function, ``snd_pcm_lib_malloc_pages()``, for
allocating the buffer, these fields are set by the ALSA middle layer,
and you should *not* change them by yourself. You can read them but not
write them. On the other hand, if you want to allocate the buffer by
yourself, you'll need to manage it in hw_params callback. At least,
``dma_bytes`` is mandatory. ``dma_area`` is necessary when the buffer is
mmapped. If your driver doesn't support mmap, this field is not
necessary. ``dma_addr`` is also optional. You can use ``dma_private`` as
you like, too.


.. _pcm-interface-runtime-status:

Running Status
--------------

The running status can be referred via ``runtime->status``. This is the
pointer to the struct ``snd_pcm_mmap_status`` record. For example, you
can get the current DMA hardware pointer via
``runtime->status->hw_ptr``.

The DMA application pointer can be referred via ``runtime->control``,
which points to the struct ``snd_pcm_mmap_control`` record. However,
accessing directly to this value is not recommended.


.. _pcm-interface-runtime-private:

Private Data
------------

You can allocate a record for the substream and store it in
``runtime->private_data``. Usually, this is done in
:ref:`the open callback <pcm-interface-operators-open-callback>`.
Don't mix this with ``pcm->private_data``. The ``pcm->private_data``
usually points to the chip instance assigned statically at the creation
of PCM, while the ``runtime->private_data`` points to a dynamic data
structure created at the PCM open callback.


.. code-block:: c

      static int snd_xxx_open(struct snd_pcm_substream *substream)
      {
              struct my_pcm_data *data;
              ....
              data = kmalloc(sizeof(*data), GFP_KERNEL);
              substream->runtime->private_data = data;
              ....
      }

The allocated object must be released in
:ref:`the close callback <pcm-interface-operators-open-callback>`.


.. _pcm-interface-operators:

Operators
=========

OK, now let me give details about each pcm callback (``ops``). In
general, every callback must return 0 if successful, or a negative error
number such as ``-EINVAL``. To choose an appropriate error number, it is
advised to check what value other parts of the kernel return when the
same kind of request fails.

The callback function takes at least the argument with
``snd_pcm_substream`` pointer. To retrieve the chip record from the
given substream instance, you can use the following macro.


.. code-block:: c

      int xxx() {
              struct mychip *chip = snd_pcm_substream_chip(substream);
              ....
      }

The macro reads ``substream->private_data``, which is a copy of
``pcm->private_data``. You can override the former if you need to assign
different data records per PCM substream. For example, the cmi8330
driver assigns different private_data for playback and capture
directions, because it uses two different codecs (SB- and AD-compatible)
for different directions.


.. _pcm-interface-operators-open-callback:

open callback
-------------


.. code-block:: c

      static int snd_xxx_open(struct snd_pcm_substream *substream);

This is called when a pcm substream is opened.

At least, here you have to initialize the runtime->hw record. Typically,
this is done by like this:


.. code-block:: c

      static int snd_xxx_open(struct snd_pcm_substream *substream)
      {
              struct mychip *chip = snd_pcm_substream_chip(substream);
              struct snd_pcm_runtime *runtime = substream->runtime;

              runtime->hw = snd_mychip_playback_hw;
              return 0;
      }

where ``snd_mychip_playback_hw`` is the pre-defined hardware
description.

You can allocate a private data in this callback, as described in
:ref:`Private Data <pcm-interface-runtime-private>` section.

If the hardware configuration needs more constraints, set the hardware
constraints here, too. See
:ref:`Constraints <pcm-interface-constraints>` for more details.


.. _pcm-interface-operators-close-callback:

close callback
--------------


.. code-block:: c

      static int snd_xxx_close(struct snd_pcm_substream *substream);

Obviously, this is called when a pcm substream is closed.

Any private instance for a pcm substream allocated in the open callback
will be released here.


.. code-block:: c

      static int snd_xxx_close(struct snd_pcm_substream *substream)
      {
              ....
              kfree(substream->runtime->private_data);
              ....
      }


.. _pcm-interface-operators-ioctl-callback:

ioctl callback
--------------

This is used for any special call to pcm ioctls. But usually you can
pass a generic ioctl callback, ``snd_pcm_lib_ioctl``.


.. _pcm-interface-operators-hw-params-callback:

hw_params callback
------------------


.. code-block:: c

      static int snd_xxx_hw_params(struct snd_pcm_substream *substream,
                                   struct snd_pcm_hw_params *hw_params);

This is called when the hardware parameter (``hw_params``) is set up by
the application, that is, once when the buffer size, the period size,
the format, etc. are defined for the pcm substream.

Many hardware setups should be done in this callback, including the
allocation of buffers.

Parameters to be initialized are retrieved by ``params_xxx()`` macros.
To allocate buffer, you can call a helper function,


.. code-block:: c

      snd_pcm_lib_malloc_pages(substream, params_buffer_bytes(hw_params));

``snd_pcm_lib_malloc_pages()`` is available only when the DMA buffers
have been pre-allocated. See the section
:ref:`Buffer Types <buffer-and-memory-buffer-types>` for more details.

Note that this and ``prepare`` callbacks may be called multiple times
per initialization. For example, the OSS emulation may call these
callbacks at each change via its ioctl.

Thus, you need to be careful not to allocate the same buffers many
times, which will lead to memory leaks! Calling the helper function
above many times is OK. It will release the previous buffer
automatically when it was already allocated.

Another note is that this callback is non-atomic (schedulable) as
default, i.e. when no ``nonatomic`` flag set. This is important, because
the ``trigger`` callback is atomic (non-schedulable). That is, mutexes
or any schedule-related functions are not available in ``trigger``
callback. Please see the subsection
:ref:`Atomicity <pcm-interface-atomicity>` for details.


.. _pcm-interface-operators-hw-free-callback:

hw_free callback
----------------


.. code-block:: c

      static int snd_xxx_hw_free(struct snd_pcm_substream *substream);

This is called to release the resources allocated via ``hw_params``. For
example, releasing the buffer via ``snd_pcm_lib_malloc_pages()`` is done
by calling the following:


.. code-block:: c

      snd_pcm_lib_free_pages(substream);

This function is always called before the close callback is called.
Also, the callback may be called multiple times, too. Keep track whether
the resource was already released.


.. _pcm-interface-operators-prepare-callback:

prepare callback
----------------


.. code-block:: c

      static int snd_xxx_prepare(struct snd_pcm_substream *substream);

This callback is called when the pcm is “prepared”. You can set the
format type, sample rate, etc. here. The difference from ``hw_params``
is that the ``prepare`` callback will be called each time
``snd_pcm_prepare()`` is called, i.e. when recovering after underruns,
etc.

Note that this callback is now non-atomic. You can use schedule-related
functions safely in this callback.

In this and the following callbacks, you can refer to the values via the
runtime record, substream->runtime. For example, to get the current
rate, format or channels, access to runtime->rate, runtime->format or
runtime->channels, respectively. The physical address of the allocated
buffer is set to runtime->dma_area. The buffer and period sizes are in
runtime->buffer_size and runtime->period_size, respectively.

Be careful that this callback will be called many times at each setup,
too.


.. _pcm-interface-operators-trigger-callback:

trigger callback
----------------


.. code-block:: c

      static int snd_xxx_trigger(struct snd_pcm_substream *substream, int cmd);

This is called when the pcm is started, stopped or paused.

Which action is specified in the second argument,
``SNDRV_PCM_TRIGGER_XXX`` in ``<sound/pcm.h>``. At least, the ``START``
and ``STOP`` commands must be defined in this callback.


.. code-block:: c

      switch (cmd) {
      case SNDRV_PCM_TRIGGER_START:
              /* do something to start the PCM engine */
              break;
      case SNDRV_PCM_TRIGGER_STOP:
              /* do something to stop the PCM engine */
              break;
      default:
              return -EINVAL;
      }

When the pcm supports the pause operation (given in the info field of
the hardware table), the ``PAUSE_PUSH`` and ``PAUSE_RELEASE`` commands
must be handled here, too. The former is the command to pause the pcm,
and the latter to restart the pcm again.

When the pcm supports the suspend/resume operation, regardless of full
or partial suspend/resume support, the ``SUSPEND`` and ``RESUME``
commands must be handled, too. These commands are issued when the
power-management status is changed. Obviously, the ``SUSPEND`` and
``RESUME`` commands suspend and resume the pcm substream, and usually,
they are identical to the ``STOP`` and ``START`` commands, respectively.
See the :ref:`Power Management <power-management>` section for
details.

As mentioned, this callback is atomic as default unless ``nonatomic``
flag set, and you cannot call functions which may sleep. The trigger
callback should be as minimal as possible, just really triggering the
DMA. The other stuff should be initialized hw_params and prepare
callbacks properly beforehand.


.. _pcm-interface-operators-pointer-callback:

pointer callback
----------------


.. code-block:: c

      static snd_pcm_uframes_t snd_xxx_pointer(struct snd_pcm_substream *substream)

This callback is called when the PCM middle layer inquires the current
hardware position on the buffer. The position must be returned in
frames, ranging from 0 to buffer_size - 1.

This is called usually from the buffer-update routine in the pcm middle
layer, which is invoked when ``snd_pcm_period_elapsed()`` is called in
the interrupt routine. Then the pcm middle layer updates the position
and calculates the available space, and wakes up the sleeping poll
threads, etc.

This callback is also atomic as default.


.. _pcm-interface-operators-copy-silence:

copy and silence callbacks
--------------------------

These callbacks are not mandatory, and can be omitted in most cases.
These callbacks are used when the hardware buffer cannot be in the
normal memory space. Some chips have their own buffer on the hardware
which is not mappable. In such a case, you have to transfer the data
manually from the memory buffer to the hardware buffer. Or, if the
buffer is non-contiguous on both physical and virtual memory spaces,
these callbacks must be defined, too.

If these two callbacks are defined, copy and set-silence operations are
done by them. The detailed will be described in the later section
:ref:`Buffer and Memory Management <buffer-and-memory>`.


.. _pcm-interface-operators-ack:

ack callback
------------

This callback is also not mandatory. This callback is called when the
appl_ptr is updated in read or write operations. Some drivers like
emu10k1-fx and cs46xx need to track the current appl_ptr for the
internal buffer, and this callback is useful only for such a purpose.

This callback is atomic as default.


.. _pcm-interface-operators-page-callback:

page callback
-------------

This callback is optional too. This callback is used mainly for
non-contiguous buffers. The mmap calls this callback to get the page
address. Some examples will be explained in the later section
:ref:`Buffer and Memory Management <buffer-and-memory>`, too.


.. _pcm-interface-interrupt-handler:

Interrupt Handler
=================

The rest of pcm stuff is the PCM interrupt handler. The role of PCM
interrupt handler in the sound driver is to update the buffer position
and to tell the PCM middle layer when the buffer position goes across
the prescribed period size. To inform this, call the
``snd_pcm_period_elapsed()`` function.

There are several types of sound chips to generate the interrupts.


.. _pcm-interface-interrupt-handler-boundary:

Interrupts at the period (fragment) boundary
--------------------------------------------

This is the most frequently found type: the hardware generates an
interrupt at each period boundary. In this case, you can call
``snd_pcm_period_elapsed()`` at each interrupt.

``snd_pcm_period_elapsed()`` takes the substream pointer as its
argument. Thus, you need to keep the substream pointer accessible from
the chip instance. For example, define substream field in the chip
record to hold the current running substream pointer, and set the
pointer value at open callback (and reset at close callback).

If you acquire a spinlock in the interrupt handler, and the lock is used
in other pcm callbacks, too, then you have to release the lock before
calling ``snd_pcm_period_elapsed()``, because
``snd_pcm_period_elapsed()`` calls other pcm callbacks inside.

Typical code would be like:


.. code-block:: c

      static irqreturn_t snd_mychip_interrupt(int irq, void *dev_id)
      {
              struct mychip *chip = dev_id;
              spin_lock(&chip->lock);
              ....
              if (pcm_irq_invoked(chip)) {
                      /* call updater, unlock before it */
                      spin_unlock(&chip->lock);
                      snd_pcm_period_elapsed(chip->substream);
                      spin_lock(&chip->lock);
                      /* acknowledge the interrupt if necessary */
              }
              ....
              spin_unlock(&chip->lock);
              return IRQ_HANDLED;
      }


.. _pcm-interface-interrupt-handler-timer:

High frequency timer interrupts
-------------------------------

This happens when the hardware doesn't generate interrupts at the period
boundary but issues timer interrupts at a fixed timer rate (e.g. es1968
or ymfpci drivers). In this case, you need to check the current hardware
position and accumulate the processed sample length at each interrupt.
When the accumulated size exceeds the period size, call
``snd_pcm_period_elapsed()`` and reset the accumulator.

Typical code would be like the following.


.. code-block:: c

      static irqreturn_t snd_mychip_interrupt(int irq, void *dev_id)
      {
              struct mychip *chip = dev_id;
              spin_lock(&chip->lock);
              ....
              if (pcm_irq_invoked(chip)) {
                      unsigned int last_ptr, size;
                      /* get the current hardware pointer (in frames) */
                      last_ptr = get_hw_ptr(chip);
                      /* calculate the processed frames since the
                       * last update
                       */
                      if (last_ptr < chip->last_ptr)
                              size = runtime->buffer_size + last_ptr
                                       - chip->last_ptr;
                      else
                              size = last_ptr - chip->last_ptr;
                      /* remember the last updated point */
                      chip->last_ptr = last_ptr;
                      /* accumulate the size */
                      chip->size += size;
                      /* over the period boundary? */
                      if (chip->size >= runtime->period_size) {
                              /* reset the accumulator */
                              chip->size %= runtime->period_size;
                              /* call updater */
                              spin_unlock(&chip->lock);
                              snd_pcm_period_elapsed(substream);
                              spin_lock(&chip->lock);
                      }
                      /* acknowledge the interrupt if necessary */
              }
              ....
              spin_unlock(&chip->lock);
              return IRQ_HANDLED;
      }


.. _pcm-interface-interrupt-handler-both:

On calling snd_pcm_period_elapsed()
-----------------------------------

In both cases, even if more than one period are elapsed, you don't have
to call ``snd_pcm_period_elapsed()`` many times. Call only once. And the
pcm layer will check the current hardware pointer and update to the
latest status.


.. _pcm-interface-atomicity:

Atomicity
=========

One of the most important (and thus difficult to debug) problems in
kernel programming are race conditions. In the Linux kernel, they are
usually avoided via spin-locks, mutexes or semaphores. In general, if a
race condition can happen in an interrupt handler, it has to be managed
atomically, and you have to use a spinlock to protect the critical
session. If the critical section is not in interrupt handler code and if
taking a relatively long time to execute is acceptable, you should use
mutexes or semaphores instead.

As already seen, some pcm callbacks are atomic and some are not. For
example, the ``hw_params`` callback is non-atomic, while ``trigger``
callback is atomic. This means, the latter is called already in a
spinlock held by the PCM middle layer. Please take this atomicity into
account when you choose a locking scheme in the callbacks.

In the atomic callbacks, you cannot use functions which may call
``schedule`` or go to ``sleep``. Semaphores and mutexes can sleep, and
hence they cannot be used inside the atomic callbacks (e.g. ``trigger``
callback). To implement some delay in such a callback, please use
``udelay()`` or ``mdelay()``.

All three atomic callbacks (trigger, pointer, and ack) are called with
local interrupts disabled.

The recent changes in PCM core code, however, allow all PCM operations
to be non-atomic. This assumes that the all caller sides are in
non-atomic contexts. For example, the function
``snd_pcm_period_elapsed()`` is called typically from the interrupt
handler. But, if you set up the driver to use a threaded interrupt
handler, this call can be in non-atomic context, too. In such a case,
you can set ``nonatomic`` filed of ``snd_pcm`` object after creating it.
When this flag is set, mutex and rwsem are used internally in the PCM
core instead of spin and rwlocks, so that you can call all PCM functions
safely in a non-atomic context.


.. _pcm-interface-constraints:

Constraints
===========

If your chip supports unconventional sample rates, or only the limited
samples, you need to set a constraint for the condition.

For example, in order to restrict the sample rates in the some supported
values, use ``snd_pcm_hw_constraint_list()``. You need to call this
function in the open callback.


.. code-block:: c

      static unsigned int rates[] =
              {4000, 10000, 22050, 44100};
      static struct snd_pcm_hw_constraint_list constraints_rates = {
              .count = ARRAY_SIZE(rates),
              .list = rates,
              .mask = 0,
      };

      static int snd_mychip_pcm_open(struct snd_pcm_substream *substream)
      {
              int err;
              ....
              err = snd_pcm_hw_constraint_list(substream->runtime, 0,
                                               SNDRV_PCM_HW_PARAM_RATE,
                                               &constraints_rates);
              if (err < 0)
                      return err;
              ....
      }

There are many different constraints. Look at ``sound/pcm.h`` for a
complete list. You can even define your own constraint rules. For
example, let's suppose my_chip can manage a substream of 1 channel if
and only if the format is S16_LE, otherwise it supports any format
specified in the ``snd_pcm_hardware`` structure (or in any other
constraint_list). You can build a rule like this:


.. code-block:: c

      static int hw_rule_channels_by_format(struct snd_pcm_hw_params *params,
                                            struct snd_pcm_hw_rule *rule)
      {
              struct snd_interval *c = hw_param_interval(params,
                            SNDRV_PCM_HW_PARAM_CHANNELS);
              struct snd_mask *f = hw_param_mask(params, SNDRV_PCM_HW_PARAM_FORMAT);
              struct snd_interval ch;

              snd_interval_any(&ch);
              if (f->bits[0] == SNDRV_PCM_FMTBIT_S16_LE) {
                      ch.min = ch.max = 1;
                      ch.integer = 1;
                      return snd_interval_refine(c, &ch);
              }
              return 0;
      }

Then you need to call this function to add your rule:


.. code-block:: c

      snd_pcm_hw_rule_add(substream->runtime, 0, SNDRV_PCM_HW_PARAM_CHANNELS,
                          hw_rule_channels_by_format, NULL,
                          SNDRV_PCM_HW_PARAM_FORMAT, -1);

The rule function is called when an application sets the PCM format, and
it refines the number of channels accordingly. But an application may
set the number of channels before setting the format. Thus you also need
to define the inverse rule:


.. code-block:: c

      static int hw_rule_format_by_channels(struct snd_pcm_hw_params *params,
                                            struct snd_pcm_hw_rule *rule)
      {
              struct snd_interval *c = hw_param_interval(params,
                    SNDRV_PCM_HW_PARAM_CHANNELS);
              struct snd_mask *f = hw_param_mask(params, SNDRV_PCM_HW_PARAM_FORMAT);
              struct snd_mask fmt;

              snd_mask_any(&fmt);    /* Init the struct */
              if (c->min < 2) {
                      fmt.bits[0] &= SNDRV_PCM_FMTBIT_S16_LE;
                      return snd_mask_refine(f, &fmt);
              }
              return 0;
      }

...and in the open callback:


.. code-block:: c

      snd_pcm_hw_rule_add(substream->runtime, 0, SNDRV_PCM_HW_PARAM_FORMAT,
                          hw_rule_format_by_channels, NULL,
                          SNDRV_PCM_HW_PARAM_CHANNELS, -1);

I won't give more details here, rather I would like to say, “Luke, use
the source.”


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
