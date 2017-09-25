.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/alps.h

.. _`alps_protocol_info`:

struct alps_protocol_info
=========================

.. c:type:: struct alps_protocol_info

    information about protocol used by a device

.. _`alps_protocol_info.definition`:

Definition
----------

.. code-block:: c

    struct alps_protocol_info {
        u16 version;
        u8 byte0, mask0;
        unsigned int flags;
    }

.. _`alps_protocol_info.members`:

Members
-------

version
    Indicates V1/V2/V3/...

byte0
    Helps figure out whether a position report packet matches the
    known format for this model.  The first byte of the report, ANDed with
    mask0, should match byte0.

mask0
    The mask used to check the first byte of the report.

flags
    Additional device capabilities (passthrough port, trackstick, etc.).

.. _`alps_model_info`:

struct alps_model_info
======================

.. c:type:: struct alps_model_info

    touchpad ID table

.. _`alps_model_info.definition`:

Definition
----------

.. code-block:: c

    struct alps_model_info {
        u8 signature[3];
        struct alps_protocol_info protocol_info;
    }

.. _`alps_model_info.members`:

Members
-------

signature
    E7 response string to match.

protocol_info
    information about protocol used by the device.

.. _`alps_model_info.description`:

Description
-----------

Many (but not all) ALPS touchpads can be identified by looking at the
values returned in the "E7 report" and/or the "EC report."  This table
lists a number of such touchpads.

.. _`alps_nibble_commands`:

struct alps_nibble_commands
===========================

.. c:type:: struct alps_nibble_commands

    encodings for register accesses

.. _`alps_nibble_commands.definition`:

Definition
----------

.. code-block:: c

    struct alps_nibble_commands {
        int command;
        unsigned char data;
    }

.. _`alps_nibble_commands.members`:

Members
-------

command
    PS/2 command used for the nibble

data
    Data supplied as an argument to the PS/2 command, if applicable

.. _`alps_nibble_commands.description`:

Description
-----------

The ALPS protocol uses magic sequences to transmit binary data to the
touchpad, as it is generally not OK to send arbitrary bytes out the
PS/2 port.  Each of the sequences in this table sends one nibble of the
register address or (write) data.  Different versions of the ALPS protocol
use slightly different encodings.

.. _`alps_fields`:

struct alps_fields
==================

.. c:type:: struct alps_fields

    decoded version of the report packet

.. _`alps_fields.definition`:

Definition
----------

.. code-block:: c

    struct alps_fields {
        unsigned int x_map;
        unsigned int y_map;
        unsigned int fingers;
        int pressure;
        struct input_mt_pos st;
        struct input_mt_pos mt[MAX_TOUCHES];
        unsigned int first_mp:1;
        unsigned int is_mp:1;
        unsigned int left:1;
        unsigned int right:1;
        unsigned int middle:1;
        unsigned int ts_left:1;
        unsigned int ts_right:1;
        unsigned int ts_middle:1;
    }

.. _`alps_fields.members`:

Members
-------

x_map
    Bitmap of active X positions for MT.

y_map
    Bitmap of active Y positions for MT.

fingers
    Number of fingers for MT.

pressure
    Pressure.

st
    position for ST.

mt
    position for MT.

first_mp
    Packet is the first of a multi-packet report.

is_mp
    Packet is part of a multi-packet report.

left
    Left touchpad button is active.

right
    Right touchpad button is active.

middle
    Middle touchpad button is active.

ts_left
    Left trackstick button is active.

ts_right
    Right trackstick button is active.

ts_middle
    Middle trackstick button is active.

.. _`alps_data`:

struct alps_data
================

.. c:type:: struct alps_data

    private data structure for the ALPS driver

.. _`alps_data.definition`:

Definition
----------

.. code-block:: c

    struct alps_data {
        struct psmouse *psmouse;
        struct input_dev *dev2;
        struct input_dev *dev3;
        char phys2[32];
        char phys3[32];
        struct delayed_work dev3_register_work;
        const struct alps_nibble_commands *nibble_commands;
        int addr_command;
        u16 proto_version;
        u8 byte0, mask0;
        u8 dev_id[3];
        u8 fw_ver[3];
        int flags;
        int x_max;
        int y_max;
        int x_bits;
        int y_bits;
        unsigned int x_res;
        unsigned int y_res;
        int (*hw_init)(struct psmouse *psmouse);
        void (*process_packet)(struct psmouse *psmouse);
        int (*decode_fields)(struct alps_fields *f, unsigned char *p, struct psmouse *psmouse);
        void (*set_abs_params)(struct alps_data *priv, struct input_dev *dev1);
        int prev_fin;
        int multi_packet;
        int second_touch;
        unsigned char multi_data[6];
        struct alps_fields f;
        u8 quirks;
        struct timer_list timer;
    }

.. _`alps_data.members`:

Members
-------

psmouse
    Pointer to parent psmouse device

dev2
    Trackstick device (can be NULL).

dev3
    Generic PS/2 mouse (can be NULL, delayed registering).

phys2
    Physical path for the trackstick device.

phys3
    Physical path for the generic PS/2 mouse.

dev3_register_work
    Delayed work for registering PS/2 mouse.

nibble_commands
    Command mapping used for touchpad register accesses.

addr_command
    Command used to tell the touchpad that a register address
    follows.

proto_version
    Indicates V1/V2/V3/...

byte0
    Helps figure out whether a position report packet matches the
    known format for this model.  The first byte of the report, ANDed with
    mask0, should match byte0.

mask0
    The mask used to check the first byte of the report.

dev_id
    *undescribed*

fw_ver
    cached copy of firmware version (EC report)

flags
    Additional device capabilities (passthrough port, trackstick, etc.).

x_max
    Largest possible X position value.

y_max
    Largest possible Y position value.

x_bits
    Number of X bits in the MT bitmap.

y_bits
    Number of Y bits in the MT bitmap.

x_res
    *undescribed*

y_res
    *undescribed*

hw_init
    Protocol-specific hardware init function.

process_packet
    Protocol-specific function to process a report packet.

decode_fields
    Protocol-specific function to read packet bitfields.

set_abs_params
    Protocol-specific function to configure the input_dev.

prev_fin
    Finger bit from previous packet.

multi_packet
    Multi-packet data in progress.

second_touch
    *undescribed*

multi_data
    Saved multi-packet data.

f
    Decoded packet data fields.

quirks
    Bitmap of ALPS_QUIRK\_\*.

timer
    Timer for flushing out the final report packet in the stream.

.. This file was automatic generated / don't edit.

