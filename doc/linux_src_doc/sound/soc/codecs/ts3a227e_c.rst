.. -*- coding: utf-8; mode: rst -*-

==========
ts3a227e.c
==========


.. _`ts3a227e_enable_jack_detect`:

ts3a227e_enable_jack_detect
===========================

.. c:function:: int ts3a227e_enable_jack_detect (struct snd_soc_component *component, struct snd_soc_jack *jack)

    Specify a jack for event reporting

    :param struct snd_soc_component \*component:
        component to register the jack with

    :param struct snd_soc_jack \*jack:
        jack to use to report headset and button events on



.. _`ts3a227e_enable_jack_detect.description`:

Description
-----------

After this function has been called the headset insert/remove and button
events 0-3 will be routed to the given jack.  Jack can be null to stop
reporting.

