.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/core.h

.. _`most_channel_capability`:

struct most_channel_capability
==============================

.. c:type:: struct most_channel_capability

    Channel capability

.. _`most_channel_capability.definition`:

Definition
----------

.. code-block:: c

    struct most_channel_capability {
        u16 direction;
        u16 data_type;
        u16 num_buffers_packet;
        u16 buffer_size_packet;
        u16 num_buffers_streaming;
        u16 buffer_size_streaming;
        const char *name_suffix;
    }

.. _`most_channel_capability.members`:

Members
-------

direction
    Supported channel directions.
    The value is bitwise OR-combination of the values from the
    enumeration most_channel_direction. Zero is allowed value and means
    "channel may not be used".

data_type
    Supported channel data types.
    The value is bitwise OR-combination of the values from the
    enumeration most_channel_data_type. Zero is allowed value and means
    "channel may not be used".

num_buffers_packet
    Maximum number of buffers supported by this channel
    for packet data types (Async,Control,QoS)

buffer_size_packet
    Maximum buffer size supported by this channel
    for packet data types (Async,Control,QoS)

num_buffers_streaming
    Maximum number of buffers supported by this channel
    for streaming data types (Sync,AV Packetized)

buffer_size_streaming
    Maximum buffer size supported by this channel
    for streaming data types (Sync,AV Packetized)

name_suffix
    Optional suffix providean by an HDM that is attached to the
    regular channel name.

.. _`most_channel_capability.description`:

Description
-----------

Describes the capabilities of a MOST channel like supported Data Types
and directions. This information is provided by an HDM for the MostCore.

The Core creates read only sysfs attribute files in
/sys/devices/most/mdev#/<channel>/ with the

.. _`most_channel_capability.following-attributes`:

following attributes
--------------------

-available_directions
-available_datatypes
-number_of_packet_buffers
-number_of_stream_buffers
-size_of_packet_buffer
-size_of_stream_buffer
where content of each file is a string with all supported properties of this
very channel attribute.

.. _`most_channel_config`:

struct most_channel_config
==========================

.. c:type:: struct most_channel_config

    stores channel configuration

.. _`most_channel_config.definition`:

Definition
----------

.. code-block:: c

    struct most_channel_config {
        enum most_channel_direction direction;
        enum most_channel_data_type data_type;
        u16 num_buffers;
        u16 buffer_size;
        u16 extra_len;
        u16 subbuffer_size;
        u16 packets_per_xact;
    }

.. _`most_channel_config.members`:

Members
-------

direction
    direction of the channel

data_type
    data type travelling over this channel

num_buffers
    number of buffers

buffer_size
    size of a buffer for AIM.
    Buffer size may be cutted down by HDM in a configure callback
    to match to a given interface and channel type.

extra_len
    additional buffer space for internal HDM purposes like padding.
    May be set by HDM in a configure callback if needed.

subbuffer_size
    size of a subbuffer

packets_per_xact
    number of MOST frames that are packet inside one USB
    packet. This is USB specific

.. _`most_channel_config.description`:

Description
-----------

Describes the configuration for a MOST channel. This information is
provided from the MostCore to a HDM (like the Medusa PCIe Interface) as a
parameter of the "configure" function call.

.. _`core_component`:

struct core_component
=====================

.. c:type:: struct core_component

    identifies a loadable component for the mostcore

.. _`core_component.definition`:

Definition
----------

.. code-block:: c

    struct core_component {
        struct list_head list;
        const char *name;
        int (*probe_channel)(struct most_interface *iface, int channel_idx, struct most_channel_config *cfg, char *name);
        int (*disconnect_channel)(struct most_interface *iface, int channel_idx);
        int (*rx_completion)(struct mbo *mbo);
        int (*tx_completion)(struct most_interface *iface, int channel_idx);
    }

.. _`core_component.members`:

Members
-------

list
    list_head

name
    component name

probe_channel
    function for core to notify driver about channel connection

disconnect_channel
    callback function to disconnect a certain channel

rx_completion
    completion handler for received packets

tx_completion
    completion handler for transmitted packets

.. _`most_register_interface`:

most_register_interface
=======================

.. c:function:: int most_register_interface(struct most_interface *iface)

    Registers instance of the interface.

    :param struct most_interface \*iface:
        Pointer to the interface instance description.

.. _`most_register_interface.description`:

Description
-----------

Returns a pointer to the kobject of the generated instance.

.. _`most_register_interface.note`:

Note
----

HDM has to ensure that any reference held on the kobj is
released before deregistering the interface.

.. _`most_deregister_interface`:

most_deregister_interface
=========================

.. c:function:: void most_deregister_interface(struct most_interface *iface)

    \ ``intf_instance``\  Pointer to the interface instance description.

    :param struct most_interface \*iface:
        *undescribed*

.. _`most_stop_enqueue`:

most_stop_enqueue
=================

.. c:function:: void most_stop_enqueue(struct most_interface *iface, int channel_idx)

    prevents core from enqueing MBOs

    :param struct most_interface \*iface:
        pointer to interface

    :param int channel_idx:
        channel index

.. _`most_resume_enqueue`:

most_resume_enqueue
===================

.. c:function:: void most_resume_enqueue(struct most_interface *iface, int channel_idx)

    allow core to enqueue MBOs again

    :param struct most_interface \*iface:
        pointer to interface

    :param int channel_idx:
        channel index

.. _`most_resume_enqueue.description`:

Description
-----------

This clears the enqueue halt flag and enqueues all MBOs currently
in wait fifo.

.. This file was automatic generated / don't edit.

