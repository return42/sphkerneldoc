.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/tuner-core.c

.. _`tuner_pad_index`:

enum tuner_pad_index
====================

.. c:type:: enum tuner_pad_index

    tuner pad index for MEDIA_ENT_F_TUNER

.. _`tuner_pad_index.definition`:

Definition
----------

.. code-block:: c

    enum tuner_pad_index {
        TUNER_PAD_RF_INPUT,
        TUNER_PAD_OUTPUT,
        TUNER_PAD_AUD_OUT,
        TUNER_NUM_PADS
    };

.. _`tuner_pad_index.constants`:

Constants
---------

TUNER_PAD_RF_INPUT
    Radiofrequency (RF) sink pad, usually linked to a RF connector entity.

TUNER_PAD_OUTPUT
    tuner video output source pad. Contains the video chrominance
    and luminance or the hole bandwidth of the signal converted to
    an Intermediate Frequency (IF) or to baseband (on zero-IF tuners).

TUNER_PAD_AUD_OUT
    Tuner audio output source pad. Tuners used to decode analog TV
    signals have an extra pad for audio output. Old tuners use an
    analog stage with a saw filter for the audio IF frequency. The
    output of the pad is, in this case, the audio IF, with should be
    decoded either by the bridge chipset (that's the case of cx2388x
    chipsets) or may require an external IF sound processor, like
    msp34xx. On modern silicon tuners, the audio IF decoder is usually
    incorporated at the tuner. On such case, the output of this pad
    is an audio sampled data.

TUNER_NUM_PADS
    Number of pads of the tuner.

.. _`if_vid_dec_pad_index`:

enum if_vid_dec_pad_index
=========================

.. c:type:: enum if_vid_dec_pad_index

    video IF-PLL pad index for MEDIA_ENT_F_IF_VID_DECODER

.. _`if_vid_dec_pad_index.definition`:

Definition
----------

.. code-block:: c

    enum if_vid_dec_pad_index {
        IF_VID_DEC_PAD_IF_INPUT,
        IF_VID_DEC_PAD_OUT,
        IF_VID_DEC_PAD_NUM_PADS
    };

.. _`if_vid_dec_pad_index.constants`:

Constants
---------

IF_VID_DEC_PAD_IF_INPUT
    video Intermediate Frequency (IF) sink pad

IF_VID_DEC_PAD_OUT
    IF-PLL video output source pad. Contains the video chrominance
    and luminance IF signals.

IF_VID_DEC_PAD_NUM_PADS
    Number of pads of the video IF-PLL.

.. _`set_type`:

set_type
========

.. c:function:: void set_type(struct i2c_client *c, unsigned int type, unsigned int new_mode_mask, void *new_config, int (*tuner_callback)(void *dev, int component, int cmd, int arg))

    Sets the tuner type for a given device

    :param c:
        i2c_client descriptor
    :type c: struct i2c_client \*

    :param type:
        type of the tuner (e. g. tuner number)
    :type type: unsigned int

    :param new_mode_mask:
        Indicates if tuner supports TV and/or Radio
    :type new_mode_mask: unsigned int

    :param new_config:
        an optional parameter used by a few tuners to adjust
        internal parameters, like LNA mode
    :type new_config: void \*

    :param int (\*tuner_callback)(void \*dev, int component, int cmd, int arg):
        an optional function to be called when switching
        to analog mode

.. _`set_type.description`:

Description
-----------

This function applies the tuner config to tuner specified
by tun_setup structure. It contains several per-tuner initialization "magic"

.. _`tuner_s_type_addr`:

tuner_s_type_addr
=================

.. c:function:: int tuner_s_type_addr(struct v4l2_subdev *sd, struct tuner_setup *tun_setup)

    Sets the tuner type for a device

    :param sd:
        subdev descriptor
    :type sd: struct v4l2_subdev \*

    :param tun_setup:
        type to be associated to a given tuner i2c address
    :type tun_setup: struct tuner_setup \*

.. _`tuner_s_type_addr.description`:

Description
-----------

This function applies the tuner config to tuner specified
by tun_setup structure.
If tuner I2C address is UNSET, then it will only set the device
if the tuner supports the mode specified in the call.
If the address is specified, the change will be applied only if
tuner I2C address matches.
The call can change the tuner number and the tuner mode.

.. _`tuner_s_config`:

tuner_s_config
==============

.. c:function:: int tuner_s_config(struct v4l2_subdev *sd, const struct v4l2_priv_tun_config *cfg)

    Sets tuner configuration

    :param sd:
        subdev descriptor
    :type sd: struct v4l2_subdev \*

    :param cfg:
        tuner configuration
    :type cfg: const struct v4l2_priv_tun_config \*

.. _`tuner_s_config.description`:

Description
-----------

Calls tuner \ :c:func:`set_config`\  private function to set some tuner-internal
parameters

.. _`tuner_lookup`:

tuner_lookup
============

.. c:function:: void tuner_lookup(struct i2c_adapter *adap, struct tuner **radio, struct tuner **tv)

    Seek for tuner adapters

    :param adap:
        i2c_adapter struct
    :type adap: struct i2c_adapter \*

    :param radio:
        pointer to be filled if the adapter is radio
    :type radio: struct tuner \*\*

    :param tv:
        pointer to be filled if the adapter is TV
    :type tv: struct tuner \*\*

.. _`tuner_lookup.description`:

Description
-----------

Search for existing radio and/or TV tuners on the given I2C adapter,
discarding demod-only adapters (tda9887).

Note that when this function is called from tuner_probe you can be
certain no other devices will be added/deleted at the same time, I2C
core protects against that.

.. _`tuner_probe`:

tuner_probe
===========

.. c:function:: int tuner_probe(struct i2c_client *client, const struct i2c_device_id *id)

    Probes the existing tuners on an I2C bus

    :param client:
        i2c_client descriptor
    :type client: struct i2c_client \*

    :param id:
        not used
    :type id: const struct i2c_device_id \*

.. _`tuner_probe.description`:

Description
-----------

This routine probes for tuners at the expected I2C addresses. On most
cases, if a device answers to a given I2C address, it assumes that the
device is a tuner. On a few cases, however, an additional logic is needed
to double check if the device is really a tuner, or to identify the tuner
type, like on tea5767/5761 devices.

During client attach, set_type is called by adapter's attach_inform callback.
set_type must then be completed by tuner_probe.

.. _`tuner_remove`:

tuner_remove
============

.. c:function:: int tuner_remove(struct i2c_client *client)

    detaches a tuner

    :param client:
        i2c_client descriptor
    :type client: struct i2c_client \*

.. _`check_mode`:

check_mode
==========

.. c:function:: int check_mode(struct tuner *t, enum v4l2_tuner_type mode)

    Verify if tuner supports the requested mode

    :param t:
        a pointer to the module's internal struct_tuner
    :type t: struct tuner \*

    :param mode:
        mode of the tuner, as defined by \ :c:type:`enum v4l2_tuner_type <v4l2_tuner_type>`\ .
    :type mode: enum v4l2_tuner_type

.. _`check_mode.description`:

Description
-----------

This function checks if the tuner is capable of tuning analog TV,
digital TV or radio, depending on what the caller wants. If the
tuner can't support that mode, it returns -EINVAL. Otherwise, it
returns 0.
This function is needed for boards that have a separate tuner for
radio (like devices with tea5767).

.. _`check_mode.note`:

NOTE
----

mt20xx uses V4L2_TUNER_DIGITAL_TV and calls set_tv_freq to
select a TV frequency. So, t_mode = T_ANALOG_TV could actually
be used to represent a Digital TV too.

.. _`set_mode`:

set_mode
========

.. c:function:: int set_mode(struct tuner *t, enum v4l2_tuner_type mode)

    Switch tuner to other mode.

    :param t:
        a pointer to the module's internal struct_tuner
    :type t: struct tuner \*

    :param mode:
        enum v4l2_type (radio or TV)
    :type mode: enum v4l2_tuner_type

.. _`set_mode.description`:

Description
-----------

If tuner doesn't support the needed mode (radio or TV), prints a
debug message and returns -EINVAL, changing its state to standby.
Otherwise, changes the mode and returns 0.

.. _`set_freq`:

set_freq
========

.. c:function:: void set_freq(struct tuner *t, unsigned int freq)

    Set the tuner to the desired frequency.

    :param t:
        a pointer to the module's internal struct_tuner
    :type t: struct tuner \*

    :param freq:
        frequency to set (0 means to use the current frequency)
    :type freq: unsigned int

.. _`set_tv_freq`:

set_tv_freq
===========

.. c:function:: void set_tv_freq(struct i2c_client *c, unsigned int freq)

    Set tuner frequency,  freq in Units of 62.5 kHz = 1/16MHz

    :param c:
        i2c_client descriptor
    :type c: struct i2c_client \*

    :param freq:
        frequency
    :type freq: unsigned int

.. _`tuner_fixup_std`:

tuner_fixup_std
===============

.. c:function:: v4l2_std_id tuner_fixup_std(struct tuner *t, v4l2_std_id std)

    force a given video standard variant

    :param t:
        tuner internal struct
    :type t: struct tuner \*

    :param std:
        TV standard
    :type std: v4l2_std_id

.. _`tuner_fixup_std.description`:

Description
-----------

A few devices or drivers have problem to detect some standard variations.
On other operational systems, the drivers generally have a per-country
code, and some logic to apply per-country hacks. V4L2 API doesn't provide
such hacks. Instead, it relies on a proper video standard selection from
the userspace application. However, as some apps are buggy, not allowing
to distinguish all video standard variations, a modprobe parameter can
be used to force a video standard match.

.. _`set_radio_freq`:

set_radio_freq
==============

.. c:function:: void set_radio_freq(struct i2c_client *c, unsigned int freq)

    Set tuner frequency,  freq in Units of 62.5 Hz  = 1/16kHz

    :param c:
        i2c_client descriptor
    :type c: struct i2c_client \*

    :param freq:
        frequency
    :type freq: unsigned int

.. _`tuner_status`:

tuner_status
============

.. c:function:: void tuner_status(struct dvb_frontend *fe)

    Dumps the current tuner status at dmesg

    :param fe:
        pointer to struct dvb_frontend
    :type fe: struct dvb_frontend \*

.. _`tuner_status.description`:

Description
-----------

This callback is used only for driver debug purposes, answering to
VIDIOC_LOG_STATUS. No changes should happen on this call.

.. _`tuner_standby`:

tuner_standby
=============

.. c:function:: int tuner_standby(struct v4l2_subdev *sd)

    places the tuner in standby mode

    :param sd:
        pointer to struct v4l2_subdev
    :type sd: struct v4l2_subdev \*

.. _`tuner_g_frequency`:

tuner_g_frequency
=================

.. c:function:: int tuner_g_frequency(struct v4l2_subdev *sd, struct v4l2_frequency *f)

    Get the tuned frequency for the tuner

    :param sd:
        pointer to struct v4l2_subdev
    :type sd: struct v4l2_subdev \*

    :param f:
        pointer to struct v4l2_frequency
    :type f: struct v4l2_frequency \*

.. _`tuner_g_frequency.description`:

Description
-----------

At return, the structure f will be filled with tuner frequency
if the tuner matches the f->type.

.. _`tuner_g_frequency.note`:

Note
----

f->type should be initialized before calling it.
This is done by either video_ioctl2 or by the bridge driver.

.. _`tuner_g_tuner`:

tuner_g_tuner
=============

.. c:function:: int tuner_g_tuner(struct v4l2_subdev *sd, struct v4l2_tuner *vt)

    Fill in tuner information

    :param sd:
        pointer to struct v4l2_subdev
    :type sd: struct v4l2_subdev \*

    :param vt:
        pointer to struct v4l2_tuner
    :type vt: struct v4l2_tuner \*

.. _`tuner_g_tuner.description`:

Description
-----------

At return, the structure vt will be filled with tuner information
if the tuner matches vt->type.

.. _`tuner_g_tuner.note`:

Note
----

vt->type should be initialized before calling it.
This is done by either video_ioctl2 or by the bridge driver.

.. _`tuner_s_tuner`:

tuner_s_tuner
=============

.. c:function:: int tuner_s_tuner(struct v4l2_subdev *sd, const struct v4l2_tuner *vt)

    Set the tuner's audio mode

    :param sd:
        pointer to struct v4l2_subdev
    :type sd: struct v4l2_subdev \*

    :param vt:
        pointer to struct v4l2_tuner
    :type vt: const struct v4l2_tuner \*

.. _`tuner_s_tuner.description`:

Description
-----------

Sets the audio mode if the tuner matches vt->type.

.. _`tuner_s_tuner.note`:

Note
----

vt->type should be initialized before calling it.
This is done by either video_ioctl2 or by the bridge driver.

.. This file was automatic generated / don't edit.

