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
        int (* jack_status_check) (void *data);
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

.. _`snd_soc_component_to_codec`:

snd_soc_component_to_codec
==========================

.. c:function:: struct snd_soc_codec *snd_soc_component_to_codec(struct snd_soc_component *component)

    Casts a component to the CODEC it is embedded in

    :param struct snd_soc_component \*component:
        The component to cast to a CODEC

.. _`snd_soc_component_to_codec.description`:

Description
-----------

This function must only be used on components that are known to be CODECs.
Otherwise the behavior is undefined.

.. _`snd_soc_component_to_platform`:

snd_soc_component_to_platform
=============================

.. c:function:: struct snd_soc_platform *snd_soc_component_to_platform(struct snd_soc_component *component)

    Casts a component to the platform it is embedded in

    :param struct snd_soc_component \*component:
        The component to cast to a platform

.. _`snd_soc_component_to_platform.description`:

Description
-----------

This function must only be used on components that are known to be platforms.
Otherwise the behavior is undefined.

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

.. _`snd_soc_dapm_to_codec`:

snd_soc_dapm_to_codec
=====================

.. c:function:: struct snd_soc_codec *snd_soc_dapm_to_codec(struct snd_soc_dapm_context *dapm)

    Casts a DAPM context to the CODEC it is embedded in

    :param struct snd_soc_dapm_context \*dapm:
        The DAPM context to cast to the CODEC

.. _`snd_soc_dapm_to_codec.description`:

Description
-----------

This function must only be used on DAPM contexts that are known to be part of
a CODEC (e.g. in a CODEC driver). Otherwise the behavior is undefined.

.. _`snd_soc_dapm_to_platform`:

snd_soc_dapm_to_platform
========================

.. c:function:: struct snd_soc_platform *snd_soc_dapm_to_platform(struct snd_soc_dapm_context *dapm)

    Casts a DAPM context to the platform it is embedded in

    :param struct snd_soc_dapm_context \*dapm:
        The DAPM context to cast to the platform.

.. _`snd_soc_dapm_to_platform.description`:

Description
-----------

This function must only be used on DAPM contexts that are known to be part of
a platform (e.g. in a platform driver). Otherwise the behavior is undefined.

.. _`snd_soc_component_get_dapm`:

snd_soc_component_get_dapm
==========================

.. c:function:: struct snd_soc_dapm_context *snd_soc_component_get_dapm(struct snd_soc_component *component)

    Returns the DAPM context associated with a component

    :param struct snd_soc_component \*component:
        The component for which to get the DAPM context

.. _`snd_soc_codec_get_dapm`:

snd_soc_codec_get_dapm
======================

.. c:function:: struct snd_soc_dapm_context *snd_soc_codec_get_dapm(struct snd_soc_codec *codec)

    Returns the DAPM context for the CODEC

    :param struct snd_soc_codec \*codec:
        The CODEC for which to get the DAPM context

.. _`snd_soc_codec_get_dapm.note`:

Note
----

Use this function instead of directly accessing the CODEC's dapm field

.. _`snd_soc_codec_init_bias_level`:

snd_soc_codec_init_bias_level
=============================

.. c:function:: void snd_soc_codec_init_bias_level(struct snd_soc_codec *codec, enum snd_soc_bias_level level)

    Initialize CODEC DAPM bias level

    :param struct snd_soc_codec \*codec:
        The CODEC for which to initialize the DAPM bias level

    :param enum snd_soc_bias_level level:
        The DAPM level to initialize to

.. _`snd_soc_codec_init_bias_level.description`:

Description
-----------

Initializes the CODEC DAPM bias level. See \ :c:func:`snd_soc_dapm_init_bias_level`\ .

.. _`snd_soc_codec_get_bias_level`:

snd_soc_codec_get_bias_level
============================

.. c:function:: enum snd_soc_bias_level snd_soc_codec_get_bias_level(struct snd_soc_codec *codec)

    Get current CODEC DAPM bias level

    :param struct snd_soc_codec \*codec:
        The CODEC for which to get the DAPM bias level

.. _`snd_soc_codec_get_bias_level.return`:

Return
------

The current DAPM bias level of the CODEC.

.. _`snd_soc_codec_force_bias_level`:

snd_soc_codec_force_bias_level
==============================

.. c:function:: int snd_soc_codec_force_bias_level(struct snd_soc_codec *codec, enum snd_soc_bias_level level)

    Set the CODEC DAPM bias level

    :param struct snd_soc_codec \*codec:
        The CODEC for which to set the level

    :param enum snd_soc_bias_level level:
        The level to set to

.. _`snd_soc_codec_force_bias_level.description`:

Description
-----------

Forces the CODEC bias level to a specific state. See
\ :c:func:`snd_soc_dapm_force_bias_level`\ .

.. _`snd_soc_dapm_kcontrol_codec`:

snd_soc_dapm_kcontrol_codec
===========================

.. c:function:: struct snd_soc_codec *snd_soc_dapm_kcontrol_codec(struct snd_kcontrol *kcontrol)

    Returns the codec associated to a kcontrol

    :param struct snd_kcontrol \*kcontrol:
        The kcontrol

.. _`snd_soc_dapm_kcontrol_codec.description`:

Description
-----------

This function must only be used on DAPM contexts that are known to be part of
a CODEC (e.g. in a CODEC driver). Otherwise the behavior is undefined.

.. _`snd_soc_cache_sync`:

snd_soc_cache_sync
==================

.. c:function:: int snd_soc_cache_sync(struct snd_soc_codec *codec)

    Sync the register cache with the hardware

    :param struct snd_soc_codec \*codec:
        CODEC to sync

.. _`snd_soc_cache_sync.note`:

Note
----

This function will call \ :c:func:`regcache_sync`\ 

.. _`snd_soc_codec_init_regmap`:

snd_soc_codec_init_regmap
=========================

.. c:function:: void snd_soc_codec_init_regmap(struct snd_soc_codec *codec, struct regmap *regmap)

    Initialize regmap instance for the CODEC

    :param struct snd_soc_codec \*codec:
        The CODEC for which to initialize the regmap instance

    :param struct regmap \*regmap:
        The regmap instance that should be used by the CODEC

.. _`snd_soc_codec_init_regmap.description`:

Description
-----------

This function allows deferred assignment of the regmap instance that is
associated with the CODEC. Only use this if the regmap instance is not yet
ready when the CODEC is registered. The function must also be called before
the first IO attempt of the CODEC.

.. _`snd_soc_codec_exit_regmap`:

snd_soc_codec_exit_regmap
=========================

.. c:function:: void snd_soc_codec_exit_regmap(struct snd_soc_codec *codec)

    De-initialize regmap instance for the CODEC

    :param struct snd_soc_codec \*codec:
        The CODEC for which to de-initialize the regmap instance

.. _`snd_soc_codec_exit_regmap.description`:

Description
-----------

Calls \ :c:func:`regmap_exit`\  on the regmap instance associated to the CODEC and
removes the regmap instance from the CODEC.

This function should only be used if \ :c:func:`snd_soc_codec_init_regmap`\  was used to
initialize the regmap instance.

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
for a component. Either with \ :c:func:`snd_soc_add_codec_controls`\  or
\ :c:func:`snd_soc_add_platform_controls`\  or via  table based setup for either a
CODEC, a platform or component driver. Otherwise the behavior is undefined.

.. _`snd_soc_kcontrol_codec`:

snd_soc_kcontrol_codec
======================

.. c:function:: struct snd_soc_codec *snd_soc_kcontrol_codec(struct snd_kcontrol *kcontrol)

    Returns the CODEC that registered the control

    :param struct snd_kcontrol \*kcontrol:
        The control for which to get the CODEC

.. _`snd_soc_kcontrol_codec.note`:

Note
----

This function will only work correctly if the control has been
registered with \ :c:func:`snd_soc_add_codec_controls`\  or via table based setup of
snd_soc_codec_driver. Otherwise the behavior is undefined.

.. _`snd_soc_kcontrol_platform`:

snd_soc_kcontrol_platform
=========================

.. c:function:: struct snd_soc_platform *snd_soc_kcontrol_platform(struct snd_kcontrol *kcontrol)

    Returns the platform that registered the control

    :param struct snd_kcontrol \*kcontrol:
        The control for which to get the platform

.. _`snd_soc_kcontrol_platform.note`:

Note
----

This function will only work correctly if the control has been
registered with \ :c:func:`snd_soc_add_platform_controls`\  or via table based setup of
a snd_soc_platform_driver. Otherwise the behavior is undefined.

.. This file was automatic generated / don't edit.

