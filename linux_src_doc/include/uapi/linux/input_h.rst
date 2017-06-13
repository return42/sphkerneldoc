.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/input.h

.. _`input_absinfo`:

struct input_absinfo
====================

.. c:type:: struct input_absinfo

    used by EVIOCGABS/EVIOCSABS ioctls

.. _`input_absinfo.definition`:

Definition
----------

.. code-block:: c

    struct input_absinfo {
        __s32 value;
        __s32 minimum;
        __s32 maximum;
        __s32 fuzz;
        __s32 flat;
        __s32 resolution;
    }

.. _`input_absinfo.members`:

Members
-------

value
    latest reported value for the axis.

minimum
    specifies minimum value for the axis.

maximum
    specifies maximum value for the axis.

fuzz
    specifies fuzz value that is used to filter noise from
    the event stream.

flat
    values that are within this value will be discarded by
    joydev interface and reported as 0 instead.

resolution
    specifies resolution for the values reported for
    the axis.

.. _`input_absinfo.description`:

Description
-----------

Note that input core does not clamp reported values to the
[minimum, maximum] limits, such task is left to userspace.

The default resolution for main axes (ABS_X, ABS_Y, ABS_Z)
is reported in units per millimeter (units/mm), resolution
for rotational axes (ABS_RX, ABS_RY, ABS_RZ) is reported
in units per radian.
When INPUT_PROP_ACCELEROMETER is set the resolution changes.
The main axes (ABS_X, ABS_Y, ABS_Z) are then reported in
in units per g (units/g) and in units per degree per second
(units/deg/s) for rotational axes (ABS_RX, ABS_RY, ABS_RZ).

.. _`input_keymap_entry`:

struct input_keymap_entry
=========================

.. c:type:: struct input_keymap_entry

    used by EVIOCGKEYCODE/EVIOCSKEYCODE ioctls

.. _`input_keymap_entry.definition`:

Definition
----------

.. code-block:: c

    struct input_keymap_entry {
    #define INPUT_KEYMAP_BY_INDEX (1 << 0)
        __u8 flags;
        __u8 len;
        __u16 index;
        __u32 keycode;
        __u8 scancode[32];
    }

.. _`input_keymap_entry.members`:

Members
-------

flags
    allows to specify how kernel should handle the request. For
    example, setting INPUT_KEYMAP_BY_INDEX flag indicates that kernel
    should perform lookup in keymap by \ ``index``\  instead of \ ``scancode``\ 

len
    length of the scancode that resides in \ ``scancode``\  buffer.

index
    index in the keymap, may be used instead of scancode

keycode
    key code assigned to this scancode

scancode
    scancode represented in machine-endian form.

.. _`input_keymap_entry.description`:

Description
-----------

The structure is used to retrieve and modify keymap data. Users have
option of performing lookup either by \ ``scancode``\  itself or by \ ``index``\ 
in keymap entry. EVIOCGKEYCODE will also return scancode or index
(depending on which element was used to perform lookup).

.. _`eviocgmtslots`:

EVIOCGMTSLOTS
=============

.. c:function::  EVIOCGMTSLOTS( len)

    get MT slot values

    :param  len:
        size of the data buffer in bytes

.. _`eviocgmtslots.description`:

Description
-----------

The ioctl buffer argument should be binary equivalent to

struct input_mt_request_layout {
\__u32 code;
\__s32 values[num_slots];
};

where num_slots is the (arbitrary) number of MT slots to extract.

The ioctl size argument (len) is the size of the buffer, which
should satisfy len = (num_slots + 1) \* sizeof(__s32).  If len is
too small to fit all available slots, the first num_slots are
returned.

Before the call, code is set to the wanted ABS_MT event type. On
return, values[] is filled with the slot values for the specified
ABS_MT code.

If the request code is not an ABS_MT value, -EINVAL is returned.

.. _`eviocgmask`:

EVIOCGMASK
==========

.. c:function::  EVIOCGMASK()

    Retrieve current event mask

.. _`eviocgmask.description`:

Description
-----------

This ioctl allows user to retrieve the current event mask for specific
event type. The argument must be of type "struct input_mask" and
specifies the event type to query, the address of the receive buffer and
the size of the receive buffer.

The event mask is a per-client mask that specifies which events are
forwarded to the client. Each event code is represented by a single bit
in the event mask. If the bit is set, the event is passed to the client
normally. Otherwise, the event is filtered and will never be queued on
the client's receive buffer.

Event masks do not affect global state of the input device. They only
affect the file descriptor they are applied to.

The default event mask for a client has all bits set, i.e. all events
are forwarded to the client. If the kernel is queried for an unknown
event type or if the receive buffer is larger than the number of
event codes known to the kernel, the kernel returns all zeroes for those
codes.

At maximum, codes_size bytes are copied.

This ioctl may fail with ENODEV in case the file is revoked, EFAULT
if the receive-buffer points to invalid memory, or EINVAL if the kernel
does not implement the ioctl.

.. _`eviocsmask`:

EVIOCSMASK
==========

.. c:function::  EVIOCSMASK()

    Set event mask

.. _`eviocsmask.description`:

Description
-----------

This ioctl is the counterpart to EVIOCGMASK. Instead of receiving the
current event mask, this changes the client's event mask for a specific
type.  See EVIOCGMASK for a description of event-masks and the
argument-type.

This ioctl provides full forward compatibility. If the passed event type
is unknown to the kernel, or if the number of event codes specified in
the mask is bigger than what is known to the kernel, the ioctl is still
accepted and applied. However, any unknown codes are left untouched and
stay cleared. That means, the kernel always filters unknown codes
regardless of what the client requests.  If the new mask doesn't cover
all known event-codes, all remaining codes are automatically cleared and
thus filtered.

This ioctl may fail with ENODEV in case the file is revoked. EFAULT is
returned if the receive-buffer points to invalid memory. EINVAL is returned
if the kernel does not implement the ioctl.

.. _`ff_replay`:

struct ff_replay
================

.. c:type:: struct ff_replay

    defines scheduling of the force-feedback effect

.. _`ff_replay.definition`:

Definition
----------

.. code-block:: c

    struct ff_replay {
        __u16 length;
        __u16 delay;
    }

.. _`ff_replay.members`:

Members
-------

length
    duration of the effect

delay
    delay before effect should start playing

.. _`ff_trigger`:

struct ff_trigger
=================

.. c:type:: struct ff_trigger

    defines what triggers the force-feedback effect

.. _`ff_trigger.definition`:

Definition
----------

.. code-block:: c

    struct ff_trigger {
        __u16 button;
        __u16 interval;
    }

.. _`ff_trigger.members`:

Members
-------

button
    number of the button triggering the effect

interval
    controls how soon the effect can be re-triggered

.. _`ff_envelope`:

struct ff_envelope
==================

.. c:type:: struct ff_envelope

    generic force-feedback effect envelope

.. _`ff_envelope.definition`:

Definition
----------

.. code-block:: c

    struct ff_envelope {
        __u16 attack_length;
        __u16 attack_level;
        __u16 fade_length;
        __u16 fade_level;
    }

.. _`ff_envelope.members`:

Members
-------

attack_length
    duration of the attack (ms)

attack_level
    level at the beginning of the attack

fade_length
    duration of fade (ms)

fade_level
    level at the end of fade

.. _`ff_envelope.description`:

Description
-----------

The \ ``attack_level``\  and \ ``fade_level``\  are absolute values; when applying
envelope force-feedback core will convert to positive/negative
value based on polarity of the default level of the effect.
Valid range for the attack and fade levels is 0x0000 - 0x7fff

.. _`ff_constant_effect`:

struct ff_constant_effect
=========================

.. c:type:: struct ff_constant_effect

    defines parameters of a constant force-feedback effect

.. _`ff_constant_effect.definition`:

Definition
----------

.. code-block:: c

    struct ff_constant_effect {
        __s16 level;
        struct ff_envelope envelope;
    }

.. _`ff_constant_effect.members`:

Members
-------

level
    strength of the effect; may be negative

envelope
    envelope data

.. _`ff_ramp_effect`:

struct ff_ramp_effect
=====================

.. c:type:: struct ff_ramp_effect

    defines parameters of a ramp force-feedback effect

.. _`ff_ramp_effect.definition`:

Definition
----------

.. code-block:: c

    struct ff_ramp_effect {
        __s16 start_level;
        __s16 end_level;
        struct ff_envelope envelope;
    }

.. _`ff_ramp_effect.members`:

Members
-------

start_level
    beginning strength of the effect; may be negative

end_level
    final strength of the effect; may be negative

envelope
    envelope data

.. _`ff_condition_effect`:

struct ff_condition_effect
==========================

.. c:type:: struct ff_condition_effect

    defines a spring or friction force-feedback effect

.. _`ff_condition_effect.definition`:

Definition
----------

.. code-block:: c

    struct ff_condition_effect {
        __u16 right_saturation;
        __u16 left_saturation;
        __s16 right_coeff;
        __s16 left_coeff;
        __u16 deadband;
        __s16 center;
    }

.. _`ff_condition_effect.members`:

Members
-------

right_saturation
    maximum level when joystick moved all way to the right

left_saturation
    same for the left side

right_coeff
    controls how fast the force grows when the joystick moves
    to the right

left_coeff
    same for the left side

deadband
    size of the dead zone, where no force is produced

center
    position of the dead zone

.. _`ff_periodic_effect`:

struct ff_periodic_effect
=========================

.. c:type:: struct ff_periodic_effect

    defines parameters of a periodic force-feedback effect

.. _`ff_periodic_effect.definition`:

Definition
----------

.. code-block:: c

    struct ff_periodic_effect {
        __u16 waveform;
        __u16 period;
        __s16 magnitude;
        __s16 offset;
        __u16 phase;
        struct ff_envelope envelope;
        __u32 custom_len;
        __s16 __user *custom_data;
    }

.. _`ff_periodic_effect.members`:

Members
-------

waveform
    kind of the effect (wave)

period
    period of the wave (ms)

magnitude
    peak value

offset
    mean value of the wave (roughly)

phase
    'horizontal' shift

envelope
    envelope data

custom_len
    number of samples (FF_CUSTOM only)

custom_data
    buffer of samples (FF_CUSTOM only)

.. _`ff_periodic_effect.description`:

Description
-----------

Known waveforms - FF_SQUARE, FF_TRIANGLE, FF_SINE, FF_SAW_UP,
FF_SAW_DOWN, FF_CUSTOM. The exact syntax FF_CUSTOM is undefined
for the time being as no driver supports it yet.

.. _`ff_periodic_effect.note`:

Note
----

the data pointed by custom_data is copied by the driver.
You can therefore dispose of the memory after the upload/update.

.. _`ff_rumble_effect`:

struct ff_rumble_effect
=======================

.. c:type:: struct ff_rumble_effect

    defines parameters of a periodic force-feedback effect

.. _`ff_rumble_effect.definition`:

Definition
----------

.. code-block:: c

    struct ff_rumble_effect {
        __u16 strong_magnitude;
        __u16 weak_magnitude;
    }

.. _`ff_rumble_effect.members`:

Members
-------

strong_magnitude
    magnitude of the heavy motor

weak_magnitude
    magnitude of the light one

.. _`ff_rumble_effect.description`:

Description
-----------

Some rumble pads have two motors of different weight. Strong_magnitude
represents the magnitude of the vibration generated by the heavy one.

.. _`ff_effect`:

struct ff_effect
================

.. c:type:: struct ff_effect

    defines force feedback effect

.. _`ff_effect.definition`:

Definition
----------

.. code-block:: c

    struct ff_effect {
        __u16 type;
        __s16 id;
        __u16 direction;
        struct ff_trigger trigger;
        struct ff_replay replay;
        union u;
    }

.. _`ff_effect.members`:

Members
-------

type
    type of the effect (FF_CONSTANT, FF_PERIODIC, FF_RAMP, FF_SPRING,
    FF_FRICTION, FF_DAMPER, FF_RUMBLE, FF_INERTIA, or FF_CUSTOM)

id
    an unique id assigned to an effect

direction
    direction of the effect

trigger
    trigger conditions (struct ff_trigger)

replay
    scheduling of the effect (struct ff_replay)

u
    effect-specific structure (one of ff_constant_effect, ff_ramp_effect,
    ff_periodic_effect, ff_condition_effect, ff_rumble_effect) further
    defining effect parameters

.. _`ff_effect.description`:

Description
-----------

This structure is sent through ioctl from the application to the driver.
To create a new effect application should set its \ ``id``\  to -1; the kernel
will return assigned \ ``id``\  which can later be used to update or delete
this effect.

.. _`ff_effect.direction-of-the-effect-is-encoded-as-follows`:

Direction of the effect is encoded as follows
---------------------------------------------

0 deg -> 0x0000 (down)
90 deg -> 0x4000 (left)
180 deg -> 0x8000 (up)
270 deg -> 0xC000 (right)

.. This file was automatic generated / don't edit.

