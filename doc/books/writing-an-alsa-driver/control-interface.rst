.. -*- coding: utf-8; mode: rst -*-

.. _control-interface:

*****************
Control Interface
*****************


.. _control-interface-general:

General
=======

The control interface is used widely for many switches, sliders, etc.
which are accessed from user-space. Its most important use is the mixer
interface. In other words, since ALSA 0.9.x, all the mixer stuff is
implemented on the control kernel API.

ALSA has a well-defined AC97 control module. If your chip supports only
the AC97 and nothing else, you can skip this section.

The control API is defined in ``<sound/control.h>``. Include this file
if you want to add your own controls.


.. _control-interface-definition:

Definition of Controls
======================

To create a new control, you need to define the following three
callbacks: ``info``, ``get`` and ``put``. Then, define a struct
``snd_kcontrol_new`` record, such as:


.. code-block:: c

      static struct snd_kcontrol_new my_control = {
              .iface = SNDRV_CTL_ELEM_IFACE_MIXER,
              .name = "PCM Playback Switch",
              .index = 0,
              .access = SNDRV_CTL_ELEM_ACCESS_READWRITE,
              .private_value = 0xffff,
              .info = my_control_info,
              .get = my_control_get,
              .put = my_control_put
      };

The ``iface`` field specifies the control type,
``SNDRV_CTL_ELEM_IFACE_XXX``, which is usually ``MIXER``. Use ``CARD``
for global controls that are not logically part of the mixer. If the
control is closely associated with some specific device on the sound
card, use ``HWDEP``, ``PCM``, ``RAWMIDI``, ``TIMER``, or ``SEQUENCER``,
and specify the device number with the ``device`` and ``subdevice``
fields.

The ``name`` is the name identifier string. Since ALSA 0.9.x, the
control name is very important, because its role is classified from its
name. There are pre-defined standard control names. The details are
described in the
:ref:`Control Names <control-interface-control-names>` subsection.

The ``index`` field holds the index number of this control. If there are
several different controls with the same name, they can be distinguished
by the index number. This is the case when several codecs exist on the
card. If the index is zero, you can omit the definition above.

The ``access`` field contains the access type of this control. Give the
combination of bit masks, ``SNDRV_CTL_ELEM_ACCESS_XXX``, there. The
details will be explained in the
:ref:`Access Flags <control-interface-access-flags>` subsection.

The ``private_value`` field contains an arbitrary long integer value for
this record. When using the generic ``info``, ``get`` and ``put``
callbacks, you can pass a value through this field. If several small
numbers are necessary, you can combine them in bitwise. Or, it's
possible to give a pointer (casted to unsigned long) of some record to
this field, too.

The ``tlv`` field can be used to provide metadata about the control; see
the :ref:`Metadata <control-interface-tlv>` subsection.

The other three are
:ref:`callback functions <control-interface-callbacks>`.


.. _control-interface-control-names:

Control Names
=============

There are some standards to define the control names. A control is
usually defined from the three parts as “SOURCE DIRECTION FUNCTION”.

The first, ``SOURCE``, specifies the source of the control, and is a
string such as “Master”, “PCM”, “CD” and “Line”. There are many
pre-defined sources.

The second, ``DIRECTION``, is one of the following strings according to
the direction of the control: “Playback”, “Capture”, “Bypass Playback”
and “Bypass Capture”. Or, it can be omitted, meaning both playback and
capture directions.

The third, ``FUNCTION``, is one of the following strings according to
the function of the control: “Switch”, “Volume” and “Route”.

The example of control names are, thus, “Master Capture Switch” or “PCM
Playback Volume”.

There are some exceptions:


.. _control-interface-control-names-global:

Global capture and playback
---------------------------

“Capture Source”, “Capture Switch” and “Capture Volume” are used for the
global capture (input) source, switch and volume. Similarly, “Playback
Switch” and “Playback Volume” are used for the global output gain switch
and volume.


.. _control-interface-control-names-tone:

Tone-controls
-------------

tone-control switch and volumes are specified like “Tone Control - XXX”,
e.g. “Tone Control - Switch”, “Tone Control - Bass”, “Tone Control -
Center”.


.. _control-interface-control-names-3d:

3D controls
-----------

3D-control switches and volumes are specified like “3D Control - XXX”,
e.g. “3D Control - Switch”, “3D Control - Center”, “3D Control - Space”.


.. _control-interface-control-names-mic:

Mic boost
---------

Mic-boost switch is set as “Mic Boost” or “Mic Boost (6dB)”.

More precise information can be found in
``Documentation/sound/alsa/ControlNames.txt``.


.. _control-interface-access-flags:

Access Flags
============

The access flag is the bitmask which specifies the access type of the
given control. The default access type is
``SNDRV_CTL_ELEM_ACCESS_READWRITE``, which means both read and write are
allowed to this control. When the access flag is omitted (i.e. = 0), it
is considered as ``READWRITE`` access as default.

When the control is read-only, pass ``SNDRV_CTL_ELEM_ACCESS_READ``
instead. In this case, you don't have to define the ``put`` callback.
Similarly, when the control is write-only (although it's a rare case),
you can use the ``WRITE`` flag instead, and you don't need the ``get``
callback.

If the control value changes frequently (e.g. the VU meter),
``VOLATILE`` flag should be given. This means that the control may be
changed without
:ref:`notification <control-interface-change-notification>`.
Applications should poll such a control constantly.

When the control is inactive, set the ``INACTIVE`` flag, too. There are
``LOCK`` and ``OWNER`` flags to change the write permissions.


.. _control-interface-callbacks:

Callbacks
=========


.. _control-interface-callbacks-info:

info callback
-------------

The ``info`` callback is used to get detailed information on this
control. This must store the values of the given struct
``snd_ctl_elem_info`` object. For example, for a boolean control with a
single element:


.. code-block:: c

      static int snd_myctl_mono_info(struct snd_kcontrol *kcontrol,
                              struct snd_ctl_elem_info *uinfo)
      {
              uinfo->type = SNDRV_CTL_ELEM_TYPE_BOOLEAN;
              uinfo->count = 1;
              uinfo->value.integer.min = 0;
              uinfo->value.integer.max = 1;
              return 0;
      }

The ``type`` field specifies the type of the control. There are
``BOOLEAN``, ``INTEGER``, ``ENUMERATED``, ``BYTES``, ``IEC958`` and
``INTEGER64``. The ``count`` field specifies the number of elements in
this control. For example, a stereo volume would have count = 2. The
``value`` field is a union, and the values stored are depending on the
type. The boolean and integer types are identical.

The enumerated type is a bit different from others. You'll need to set
the string for the currently given item index.


.. code-block:: c

      static int snd_myctl_enum_info(struct snd_kcontrol *kcontrol,
                              struct snd_ctl_elem_info *uinfo)
      {
              static char *texts[4] = {
                      "First", "Second", "Third", "Fourth"
              };
              uinfo->type = SNDRV_CTL_ELEM_TYPE_ENUMERATED;
              uinfo->count = 1;
              uinfo->value.enumerated.items = 4;
              if (uinfo->value.enumerated.item > 3)
                      uinfo->value.enumerated.item = 3;
              strcpy(uinfo->value.enumerated.name,
                     texts[uinfo->value.enumerated.item]);
              return 0;
      }

The above callback can be simplified with a helper function,
``snd_ctl_enum_info``. The final code looks like below. (You can pass
ARRAY_SIZE(texts) instead of 4 in the third argument; it's a matter of
taste.)


.. code-block:: c

      static int snd_myctl_enum_info(struct snd_kcontrol *kcontrol,
                              struct snd_ctl_elem_info *uinfo)
      {
              static char *texts[4] = {
                      "First", "Second", "Third", "Fourth"
              };
              return snd_ctl_enum_info(uinfo, 1, 4, texts);
      }

Some common info callbacks are available for your convenience:
``snd_ctl_boolean_mono_info()`` and ``snd_ctl_boolean_stereo_info()``.
Obviously, the former is an info callback for a mono channel boolean
item, just like ``snd_myctl_mono_info`` above, and the latter is for a
stereo channel boolean item.


.. _control-interface-callbacks-get:

get callback
------------

This callback is used to read the current value of the control and to
return to user-space.

For example,


.. code-block:: c

      static int snd_myctl_get(struct snd_kcontrol *kcontrol,
                               struct snd_ctl_elem_value *ucontrol)
      {
              struct mychip *chip = snd_kcontrol_chip(kcontrol);
              ucontrol->value.integer.value[0] = get_some_value(chip);
              return 0;
      }

The ``value`` field depends on the type of control as well as on the
info callback. For example, the sb driver uses this field to store the
register offset, the bit-shift and the bit-mask. The ``private_value``
field is set as follows:


.. code-block:: c

      .private_value = reg | (shift << 16) | (mask << 24)

and is retrieved in callbacks like


.. code-block:: c

      static int snd_sbmixer_get_single(struct snd_kcontrol *kcontrol,
                                        struct snd_ctl_elem_value *ucontrol)
      {
              int reg = kcontrol->private_value & 0xff;
              int shift = (kcontrol->private_value >> 16) & 0xff;
              int mask = (kcontrol->private_value >> 24) & 0xff;
              ....
      }

In the ``get`` callback, you have to fill all the elements if the
control has more than one elements, i.e. ``count`` > 1. In the example
above, we filled only one element (``value.integer.value[0]``) since
it's assumed as ``count`` = 1.


.. _control-interface-callbacks-put:

put callback
------------

This callback is used to write a value from user-space.

For example,


.. code-block:: c

      static int snd_myctl_put(struct snd_kcontrol *kcontrol,
                               struct snd_ctl_elem_value *ucontrol)
      {
              struct mychip *chip = snd_kcontrol_chip(kcontrol);
              int changed = 0;
              if (chip->current_value !=
                   ucontrol->value.integer.value[0]) {
                      change_current_value(chip,
                                  ucontrol->value.integer.value[0]);
                      changed = 1;
              }
              return changed;
      }

As seen above, you have to return 1 if the value is changed. If the
value is not changed, return 0 instead. If any fatal error happens,
return a negative error code as usual.

As in the ``get`` callback, when the control has more than one elements,
all elements must be evaluated in this callback, too.


.. _control-interface-callbacks-all:

Callbacks are not atomic
------------------------

All these three callbacks are basically not atomic.


.. _control-interface-constructor:

Constructor
===========

When everything is ready, finally we can create a new control. To create
a control, there are two functions to be called, ``snd_ctl_new1()`` and
``snd_ctl_add()``.

In the simplest way, you can do like this:


.. code-block:: c

      err = snd_ctl_add(card, snd_ctl_new1(&my_control, chip));
      if (err < 0)
              return err;

where ``my_control`` is the struct ``snd_kcontrol_new`` object defined
above, and chip is the object pointer to be passed to
kcontrol->private_data which can be referred to in callbacks.

``snd_ctl_new1()`` allocates a new ``snd_kcontrol`` instance, and
``snd_ctl_add`` assigns the given control component to the card.


.. _control-interface-change-notification:

Change Notification
===================

If you need to change and update a control in the interrupt routine, you
can call ``snd_ctl_notify()``. For example,


.. code-block:: c

      snd_ctl_notify(card, SNDRV_CTL_EVENT_MASK_VALUE, id_pointer);

This function takes the card pointer, the event-mask, and the control id
pointer for the notification. The event-mask specifies the types of
notification, for example, in the above example, the change of control
values is notified. The id pointer is the pointer of struct
``snd_ctl_elem_id`` to be notified. You can find some examples in
``es1938.c`` or ``es1968.c`` for hardware volume interrupts.


.. _control-interface-tlv:

Metadata
========

To provide information about the dB values of a mixer control, use on of
the ``DECLARE_TLV_xxx`` macros from ``<sound/tlv.h>`` to define a
variable containing this information, set the\ ``tlv.p`` field to point
to this variable, and include the ``SNDRV_CTL_ELEM_ACCESS_TLV_READ``
flag in the ``access`` field; like this:


.. code-block:: c

      static DECLARE_TLV_DB_SCALE(db_scale_my_control, -4050, 150, 0);

      static struct snd_kcontrol_new my_control = {
              ...
              .access = SNDRV_CTL_ELEM_ACCESS_READWRITE |
                        SNDRV_CTL_ELEM_ACCESS_TLV_READ,
              ...
              .tlv.p = db_scale_my_control,
      };

The ``DECLARE_TLV_DB_SCALE`` macro defines information about a mixer
control where each step in the control's value changes the dB value by a
constant dB amount. The first parameter is the name of the variable to
be defined. The second parameter is the minimum value, in units of 0.01
dB. The third parameter is the step size, in units of 0.01 dB. Set the
fourth parameter to 1 if the minimum value actually mutes the control.

The ``DECLARE_TLV_DB_LINEAR`` macro defines information about a mixer
control where the control's value affects the output linearly. The first
parameter is the name of the variable to be defined. The second
parameter is the minimum value, in units of 0.01 dB. The third parameter
is the maximum value, in units of 0.01 dB. If the minimum value mutes
the control, set the second parameter to ``TLV_DB_GAIN_MUTE``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
