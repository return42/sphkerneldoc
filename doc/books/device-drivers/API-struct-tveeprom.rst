.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-tveeprom:

===============
struct tveeprom
===============

*man struct tveeprom(9)*

*4.6.0-rc5*

Contains the fields parsed from Hauppauge eeproms


Synopsis
========

.. code-block:: c

    struct tveeprom {
      u32 has_radio;
      u32 has_ir;
      u32 has_MAC_address;
      u32 tuner_type;
      u32 tuner_formats;
      u32 tuner_hauppauge_model;
      u32 tuner2_type;
      u32 tuner2_formats;
      u32 tuner2_hauppauge_model;
      u32 audio_processor;
      u32 decoder_processor;
      u32 model;
      u32 revision;
      u32 serial_number;
      char rev_str[5];
      u8 MAC_address[ETH_ALEN];
    };


Members
=======

has_radio
    1 if the device has radio; 0 otherwise.

has_ir
    If has_ir == 0, then it is unknown what the IR capabilities are.
    Otherwise: bit 0) 1 (= IR capabilities are known); bit 1) IR
    receiver present; bit 2) IR transmitter (blaster) present.

has_MAC_address
    0: no MAC, 1: MAC present, 2: unknown.

tuner_type
    type of the tuner (TUNER_*, as defined at include/media/tuner.h).

tuner_formats
    Supported analog TV standards (V4L2_STD_*).

tuner_hauppauge_model
    Hauppauge's code for the device model number.

tuner2_type
    type of the second tuner (TUNER_*, as defined at
    include/media/tuner.h).

tuner2_formats
    Tuner 2 supported analog TV standards (V4L2_STD_*).

tuner2_hauppauge_model
    tuner 2 Hauppauge's code for the device model number.

audio_processor
    analog audio decoder, as defined by enum tveeprom_audio_processor.

decoder_processor
    Hauppauge's code for the decoder chipset. Unused by the drivers, as
    they probe the decoder based on the PCI or USB ID.

model
    Hauppauge's model number

revision
    Card revision number

serial_number
    Card's serial number

rev_str[5]
    Card revision converted to number

MAC_address[ETH_ALEN]
    MAC address for the network interface


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
