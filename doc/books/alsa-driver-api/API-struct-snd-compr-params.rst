
.. _API-struct-snd-compr-params:

=======================
struct snd_compr_params
=======================

*man struct snd_compr_params(9)*

*4.6.0-rc1*

compressed stream params


Synopsis
========

.. code-block:: c

    struct snd_compr_params {
      struct snd_compressed_buffer buffer;
      struct snd_codec codec;
      __u8 no_wake_mode;
    };


Members
=======

buffer
    buffer description

codec
    codec parameters

no_wake_mode
    dont wake on fragment elapsed
