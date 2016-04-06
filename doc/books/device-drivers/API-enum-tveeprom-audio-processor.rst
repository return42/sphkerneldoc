
.. _API-enum-tveeprom-audio-processor:

=============================
enum tveeprom_audio_processor
=============================

*man enum tveeprom_audio_processor(9)*

*4.6.0-rc1*

Specifies the type of audio processor used on a Hauppauge device.


Synopsis
========

.. code-block:: c

    enum tveeprom_audio_processor {
      TVEEPROM_AUDPROC_NONE,
      TVEEPROM_AUDPROC_INTERNAL,
      TVEEPROM_AUDPROC_MSP,
      TVEEPROM_AUDPROC_OTHER
    };


Constants
=========

TVEEPROM_AUDPROC_NONE
    No audio processor present

TVEEPROM_AUDPROC_INTERNAL
    The audio processor is internal to the video processor

TVEEPROM_AUDPROC_MSP
    The audio processor is a MSPXXXX device

TVEEPROM_AUDPROC_OTHER
    The audio processor is another device
