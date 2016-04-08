
.. _API-enum-snd-jack-types:

===================
enum snd_jack_types
===================

*man enum snd_jack_types(9)*

*4.6.0-rc1*

Jack types which can be reported


Synopsis
========

.. code-block:: c

    enum snd_jack_types {
      SND_JACK_HEADPHONE,
      SND_JACK_MICROPHONE,
      SND_JACK_HEADSET,
      SND_JACK_LINEOUT,
      SND_JACK_MECHANICAL,
      SND_JACK_VIDEOOUT,
      SND_JACK_AVOUT,
      SND_JACK_LINEIN,
      SND_JACK_BTN_0,
      SND_JACK_BTN_1,
      SND_JACK_BTN_2,
      SND_JACK_BTN_3,
      SND_JACK_BTN_4,
      SND_JACK_BTN_5
    };


Constants
=========

SND_JACK_HEADPHONE
    Headphone

SND_JACK_MICROPHONE
    Microphone

SND_JACK_HEADSET
    Headset

SND_JACK_LINEOUT
    Line out

SND_JACK_MECHANICAL
    Mechanical switch

SND_JACK_VIDEOOUT
    Video out

SND_JACK_AVOUT
    AV (Audio Video) out

SND_JACK_LINEIN
    Line in

SND_JACK_BTN_0
    Button 0

SND_JACK_BTN_1
    Button 1

SND_JACK_BTN_2
    Button 2

SND_JACK_BTN_3
    Button 3

SND_JACK_BTN_4
    Button 4

SND_JACK_BTN_5
    Button 5


Description
===========

These values are used as a bitmask.

Note that this must be kept in sync with the lookup table in sound/core/jack.c.
