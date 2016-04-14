.. -*- coding: utf-8; mode: rst -*-

======
jack.h
======

.. _`snd_jack_types`:

enum snd_jack_types
===================

.. c:type:: enum snd_jack_types

    Jack types which can be reported



Constants
---------

:``SND_JACK_HEADPHONE``:
    Headphone

:``SND_JACK_MICROPHONE``:
    Microphone

:``SND_JACK_HEADSET``:
    Headset

:``SND_JACK_LINEOUT``:
    Line out

:``SND_JACK_MECHANICAL``:
    Mechanical switch

:``SND_JACK_VIDEOOUT``:
    Video out

:``SND_JACK_AVOUT``:
    AV (Audio Video) out

:``SND_JACK_LINEIN``:
    Line in

:``SND_JACK_BTN_0``:
    Button 0

:``SND_JACK_BTN_1``:
    Button 1

:``SND_JACK_BTN_2``:
    Button 2

:``SND_JACK_BTN_3``:
    Button 3

:``SND_JACK_BTN_4``:
    Button 4

:``SND_JACK_BTN_5``:
    Button 5


Description
-----------

These values are used as a bitmask.

Note that this must be kept in sync with the lookup table in
sound/core/jack.c.

