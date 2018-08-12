.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-jack.c

.. _`snd_soc_component_set_jack`:

snd_soc_component_set_jack
==========================

.. c:function:: int snd_soc_component_set_jack(struct snd_soc_component *component, struct snd_soc_jack *jack, void *data)

    configure component jack.

    :param struct snd_soc_component \*component:
        COMPONENTs

    :param struct snd_soc_jack \*jack:
        structure to use for the jack

    :param void \*data:
        can be used if codec driver need extra data for configuring jack

.. _`snd_soc_component_set_jack.description`:

Description
-----------

Configures and enables jack detection function.

.. _`snd_soc_card_jack_new`:

snd_soc_card_jack_new
=====================

.. c:function:: int snd_soc_card_jack_new(struct snd_soc_card *card, const char *id, int type, struct snd_soc_jack *jack, struct snd_soc_jack_pin *pins, unsigned int num_pins)

    Create a new jack

    :param struct snd_soc_card \*card:
        ASoC card

    :param const char \*id:
        an identifying string for this jack

    :param int type:
        a bitmask of enum snd_jack_type values that can be detected by
        this jack

    :param struct snd_soc_jack \*jack:
        structure to use for the jack

    :param struct snd_soc_jack_pin \*pins:
        Array of jack pins to be added to the jack or NULL

    :param unsigned int num_pins:
        Number of elements in the \ ``pins``\  array

.. _`snd_soc_card_jack_new.description`:

Description
-----------

Creates a new jack object.

Returns zero if successful, or a negative error code on failure.
On success jack will be initialised.

.. _`snd_soc_jack_report`:

snd_soc_jack_report
===================

.. c:function:: void snd_soc_jack_report(struct snd_soc_jack *jack, int status, int mask)

    Report the current status for a jack

    :param struct snd_soc_jack \*jack:
        the jack

    :param int status:
        a bitmask of enum snd_jack_type values that are currently detected.

    :param int mask:
        a bitmask of enum snd_jack_type values that being reported.

.. _`snd_soc_jack_report.description`:

Description
-----------

If configured using \ :c:func:`snd_soc_jack_add_pins`\  then the associated
DAPM pins will be enabled or disabled as appropriate and DAPM
synchronised.

.. _`snd_soc_jack_report.note`:

Note
----

This function uses mutexes and should be called from a
context which can sleep (such as a workqueue).

.. _`snd_soc_jack_add_zones`:

snd_soc_jack_add_zones
======================

.. c:function:: int snd_soc_jack_add_zones(struct snd_soc_jack *jack, int count, struct snd_soc_jack_zone *zones)

    Associate voltage zones with jack

    :param struct snd_soc_jack \*jack:
        ASoC jack

    :param int count:
        Number of zones

    :param struct snd_soc_jack_zone \*zones:
        Array of zones

.. _`snd_soc_jack_add_zones.description`:

Description
-----------

After this function has been called the zones specified in the
array will be associated with the jack.

.. _`snd_soc_jack_get_type`:

snd_soc_jack_get_type
=====================

.. c:function:: int snd_soc_jack_get_type(struct snd_soc_jack *jack, int micbias_voltage)

    Based on the mic bias value, this function returns the type of jack from the zones declared in the jack type

    :param struct snd_soc_jack \*jack:
        ASoC jack

    :param int micbias_voltage:
        mic bias voltage at adc channel when jack is plugged in

.. _`snd_soc_jack_get_type.description`:

Description
-----------

Based on the mic bias value passed, this function helps identify
the type of jack from the already declared jack zones

.. _`snd_soc_jack_add_pins`:

snd_soc_jack_add_pins
=====================

.. c:function:: int snd_soc_jack_add_pins(struct snd_soc_jack *jack, int count, struct snd_soc_jack_pin *pins)

    Associate DAPM pins with an ASoC jack

    :param struct snd_soc_jack \*jack:
        ASoC jack

    :param int count:
        Number of pins

    :param struct snd_soc_jack_pin \*pins:
        Array of pins

.. _`snd_soc_jack_add_pins.description`:

Description
-----------

After this function has been called the DAPM pins specified in the
pins array will have their status updated to reflect the current
state of the jack whenever the jack status is updated.

.. _`snd_soc_jack_notifier_register`:

snd_soc_jack_notifier_register
==============================

.. c:function:: void snd_soc_jack_notifier_register(struct snd_soc_jack *jack, struct notifier_block *nb)

    Register a notifier for jack status

    :param struct snd_soc_jack \*jack:
        ASoC jack

    :param struct notifier_block \*nb:
        Notifier block to register

.. _`snd_soc_jack_notifier_register.description`:

Description
-----------

Register for notification of the current status of the jack.  Note
that it is not possible to report additional jack events in the
callback from the notifier, this is intended to support
applications such as enabling electrical detection only when a
mechanical detection event has occurred.

.. _`snd_soc_jack_notifier_unregister`:

snd_soc_jack_notifier_unregister
================================

.. c:function:: void snd_soc_jack_notifier_unregister(struct snd_soc_jack *jack, struct notifier_block *nb)

    Unregister a notifier for jack status

    :param struct snd_soc_jack \*jack:
        ASoC jack

    :param struct notifier_block \*nb:
        Notifier block to unregister

.. _`snd_soc_jack_notifier_unregister.description`:

Description
-----------

Stop notifying for status changes.

.. _`snd_soc_jack_add_gpios`:

snd_soc_jack_add_gpios
======================

.. c:function:: int snd_soc_jack_add_gpios(struct snd_soc_jack *jack, int count, struct snd_soc_jack_gpio *gpios)

    Associate GPIO pins with an ASoC jack

    :param struct snd_soc_jack \*jack:
        ASoC jack

    :param int count:
        number of pins

    :param struct snd_soc_jack_gpio \*gpios:
        array of gpio pins

.. _`snd_soc_jack_add_gpios.description`:

Description
-----------

This function will request gpio, set data direction and request irq
for each gpio in the array.

.. _`snd_soc_jack_add_gpiods`:

snd_soc_jack_add_gpiods
=======================

.. c:function:: int snd_soc_jack_add_gpiods(struct device *gpiod_dev, struct snd_soc_jack *jack, int count, struct snd_soc_jack_gpio *gpios)

    Associate GPIO descriptor pins with an ASoC jack

    :param struct device \*gpiod_dev:
        GPIO consumer device

    :param struct snd_soc_jack \*jack:
        ASoC jack

    :param int count:
        number of pins

    :param struct snd_soc_jack_gpio \*gpios:
        array of gpio pins

.. _`snd_soc_jack_add_gpiods.description`:

Description
-----------

This function will request gpio, set data direction and request irq
for each gpio in the array.

.. _`snd_soc_jack_free_gpios`:

snd_soc_jack_free_gpios
=======================

.. c:function:: void snd_soc_jack_free_gpios(struct snd_soc_jack *jack, int count, struct snd_soc_jack_gpio *gpios)

    Release GPIO pins' resources of an ASoC jack

    :param struct snd_soc_jack \*jack:
        ASoC jack

    :param int count:
        number of pins

    :param struct snd_soc_jack_gpio \*gpios:
        array of gpio pins

.. _`snd_soc_jack_free_gpios.description`:

Description
-----------

Release gpio and irq resources for gpio pins associated with an ASoC jack.

.. This file was automatic generated / don't edit.

