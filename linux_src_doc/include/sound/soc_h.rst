.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/soc.h

.. _`snd_soc_jack_pin`:

struct snd_soc_jack_pin
=======================

.. c:type:: struct snd_soc_jack_pin

    Describes a pin to update based on jack detection

.. _`snd_soc_jack_pin.definition`:

Definition
----------

.. code-block:: c

    struct snd_soc_jack_pin {
        struct list_head list;
        const char *pin;
        int mask;
        bool invert;
    }

.. _`snd_soc_jack_pin.members`:

Members
-------

list
    internal list entry

pin
    name of the pin to update

mask
    bits to check for in reported jack status

invert
    if non-zero then pin is enabled when status is not reported

.. _`snd_soc_jack_zone`:

struct snd_soc_jack_zone
========================

.. c:type:: struct snd_soc_jack_zone

    Describes voltage zones of jack detection

.. _`snd_soc_jack_zone.definition`:

Definition
----------

.. code-block:: c

    struct snd_soc_jack_zone {
        unsigned int min_mv;
        unsigned int max_mv;
        unsigned int jack_type;
        unsigned int debounce_time;
        struct list_head list;
    }

.. _`snd_soc_jack_zone.members`:

Members
-------

min_mv
    start voltage in mv

max_mv
    end voltage in mv

jack_type
    type of jack that is expected for this voltage

debounce_time
    debounce_time for jack, codec driver should wait for this
    duration before reading the adc for voltages

list
    internal list entry

.. _`snd_soc_jack_gpio`:

struct snd_soc_jack_gpio
========================

.. c:type:: struct snd_soc_jack_gpio

    Describes a gpio pin for jack detection

.. _`snd_soc_jack_gpio.definition`:

Definition
----------

.. code-block:: c

    struct snd_soc_jack_gpio {
        unsigned int gpio;
        unsigned int idx;
        struct device *gpiod_dev;
        const char *name;
        int report;
        int invert;
        int debounce_time;
        bool wake;
        int (*jack_status_check)(void *data);
    }

.. _`snd_soc_jack_gpio.members`:

Members
-------

gpio
    legacy gpio number

idx
    gpio descriptor index within the function of the GPIO
    consumer device

gpiod_dev
    GPIO consumer device

name
    gpio name. Also as connection ID for the GPIO consumer
    device function name lookup

report
    value to report when jack detected

invert
    report presence in low state

debounce_time
    debounce time in ms

wake
    enable as wake source

jack_status_check
    callback function which overrides the detection
    to provide more complex checks (eg, reading an
    ADC).

.. _`snd_soc_dapm_to_component`:

snd_soc_dapm_to_component
=========================

.. c:function:: struct snd_soc_component *snd_soc_dapm_to_component(struct snd_soc_dapm_context *dapm)

    Casts a DAPM context to the component it is embedded in

    :param struct snd_soc_dapm_context \*dapm:
        The DAPM context to cast to the component

.. _`snd_soc_dapm_to_component.description`:

Description
-----------

This function must only be used on DAPM contexts that are known to be part of
a component (e.g. in a component driver). Otherwise the behavior is
undefined.

.. _`snd_soc_component_get_dapm`:

snd_soc_component_get_dapm
==========================

.. c:function:: struct snd_soc_dapm_context *snd_soc_component_get_dapm(struct snd_soc_component *component)

    Returns the DAPM context associated with a component

    :param struct snd_soc_component \*component:
        The component for which to get the DAPM context

.. _`snd_soc_component_init_bias_level`:

snd_soc_component_init_bias_level
=================================

.. c:function:: void snd_soc_component_init_bias_level(struct snd_soc_component *component, enum snd_soc_bias_level level)

    Initialize COMPONENT DAPM bias level

    :param struct snd_soc_component \*component:
        The COMPONENT for which to initialize the DAPM bias level

    :param enum snd_soc_bias_level level:
        The DAPM level to initialize to

.. _`snd_soc_component_init_bias_level.description`:

Description
-----------

Initializes the COMPONENT DAPM bias level. See \ :c:func:`snd_soc_dapm_init_bias_level`\ .

.. _`snd_soc_component_get_bias_level`:

snd_soc_component_get_bias_level
================================

.. c:function:: enum snd_soc_bias_level snd_soc_component_get_bias_level(struct snd_soc_component *component)

    Get current COMPONENT DAPM bias level

    :param struct snd_soc_component \*component:
        The COMPONENT for which to get the DAPM bias level

.. _`snd_soc_component_get_bias_level.return`:

Return
------

The current DAPM bias level of the COMPONENT.

.. _`snd_soc_component_force_bias_level`:

snd_soc_component_force_bias_level
==================================

.. c:function:: int snd_soc_component_force_bias_level(struct snd_soc_component *component, enum snd_soc_bias_level level)

    Set the COMPONENT DAPM bias level

    :param struct snd_soc_component \*component:
        The COMPONENT for which to set the level

    :param enum snd_soc_bias_level level:
        The level to set to

.. _`snd_soc_component_force_bias_level.description`:

Description
-----------

Forces the COMPONENT bias level to a specific state. See
\ :c:func:`snd_soc_dapm_force_bias_level`\ .

.. _`snd_soc_dapm_kcontrol_component`:

snd_soc_dapm_kcontrol_component
===============================

.. c:function:: struct snd_soc_component *snd_soc_dapm_kcontrol_component(struct snd_kcontrol *kcontrol)

    Returns the component associated to a kcontrol

    :param struct snd_kcontrol \*kcontrol:
        The kcontrol

.. _`snd_soc_dapm_kcontrol_component.description`:

Description
-----------

This function must only be used on DAPM contexts that are known to be part of
a COMPONENT (e.g. in a COMPONENT driver). Otherwise the behavior is undefined.

.. _`snd_soc_component_cache_sync`:

snd_soc_component_cache_sync
============================

.. c:function:: int snd_soc_component_cache_sync(struct snd_soc_component *component)

    Sync the register cache with the hardware

    :param struct snd_soc_component \*component:
        COMPONENT to sync

.. _`snd_soc_component_cache_sync.note`:

Note
----

This function will call \ :c:func:`regcache_sync`\ 

.. _`snd_soc_kcontrol_component`:

snd_soc_kcontrol_component
==========================

.. c:function:: struct snd_soc_component *snd_soc_kcontrol_component(struct snd_kcontrol *kcontrol)

    Returns the component that registered the control

    :param struct snd_kcontrol \*kcontrol:
        The control for which to get the component

.. _`snd_soc_kcontrol_component.note`:

Note
----

This function will work correctly if the control has been registered
for a component. With \ :c:func:`snd_soc_add_codec_controls`\  or via table based
setup for either a CODEC or component driver. Otherwise the behavior is
undefined.

.. This file was automatic generated / don't edit.

