
.. _API-struct-snd-compr:

================
struct snd_compr
================

*man struct snd_compr(9)*

*4.6.0-rc1*


Synopsis
========

.. code-block:: c

    struct snd_compr {
      const char * name;
      struct device dev;
      struct snd_compr_ops * ops;
      void * private_data;
      struct snd_card * card;
      unsigned int direction;
      struct mutex lock;
      int device;
    #ifdef CONFIG_SND_VERBOSE_PROCFS
    #endif
    };


Members
=======

name
    DSP device name

dev
    associated device instance

ops
    pointer to DSP callbacks

private_data
    pointer to DSP pvt data

card
    sound card pointer

direction
    Playback or capture direction

lock
    device lock

device
    device id
