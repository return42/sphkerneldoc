.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-core/demux.h

.. _`ts_filter_type`:

enum ts_filter_type
===================

.. c:type:: enum ts_filter_type

    filter type bitmap for dmx_ts_feed.set(\)

.. _`ts_filter_type.definition`:

Definition
----------

.. code-block:: c

    enum ts_filter_type {
        TS_PACKET,
        TS_PAYLOAD_ONLY,
        TS_DECODER,
        TS_DEMUX
    };

.. _`ts_filter_type.constants`:

Constants
---------

TS_PACKET
    Send TS packets (188 bytes) to callback (default).

TS_PAYLOAD_ONLY
    In case TS_PACKET is set, only send the TS payload
    (<=184 bytes per packet) to callback

TS_DECODER
    Send stream to built-in decoder (if present).

TS_DEMUX
    In case TS_PACKET is set, send the TS to the demux
    device, not to the dvr device

.. _`dmx_ts_feed`:

struct dmx_ts_feed
==================

.. c:type:: struct dmx_ts_feed

    Structure that contains a TS feed filter

.. _`dmx_ts_feed.definition`:

Definition
----------

.. code-block:: c

    struct dmx_ts_feed {
        int is_filtering;
        struct dmx_demux *parent;
        void *priv;
        int (*set)(struct dmx_ts_feed *feed,u16 pid,int type,enum dmx_ts_pes pes_type, ktime_t timeout);
        int (*start_filtering)(struct dmx_ts_feed *feed);
        int (*stop_filtering)(struct dmx_ts_feed *feed);
    }

.. _`dmx_ts_feed.members`:

Members
-------

is_filtering
    Set to non-zero when filtering in progress

parent
    pointer to struct dmx_demux

priv
    pointer to private data of the API client

set
    sets the TS filter

start_filtering
    starts TS filtering

stop_filtering
    stops TS filtering

.. _`dmx_ts_feed.description`:

Description
-----------

A TS feed is typically mapped to a hardware PID filter on the demux chip.
Using this API, the client can set the filtering properties to start/stop
filtering TS packets on a particular TS feed.

.. _`dmx_section_filter`:

struct dmx_section_filter
=========================

.. c:type:: struct dmx_section_filter

    Structure that describes a section filter

.. _`dmx_section_filter.definition`:

Definition
----------

.. code-block:: c

    struct dmx_section_filter {
        u8 filter_value;
        u8 filter_mask;
        u8 filter_mode;
        struct dmx_section_feed *parent;
        void *priv;
    }

.. _`dmx_section_filter.members`:

Members
-------

filter_value
    Contains up to 16 bytes (128 bits) of the TS section header
    that will be matched by the section filter

filter_mask
    Contains a 16 bytes (128 bits) filter mask with the bits
    specified by \ ``filter_value``\  that will be used on the filter
    match logic.

filter_mode
    Contains a 16 bytes (128 bits) filter mode.

parent
    Pointer to struct dmx_section_feed.

priv
    Pointer to private data of the API client.

.. _`dmx_section_filter.description`:

Description
-----------


The \ ``filter_mask``\  controls which bits of \ ``filter_value``\  are compared with
the section headers/payload. On a binary value of 1 in filter_mask, the
corresponding bits are compared. The filter only accepts sections that are
equal to filter_value in all the tested bit positions.

.. _`dmx_section_feed`:

struct dmx_section_feed
=======================

.. c:type:: struct dmx_section_feed

    Structure that contains a section feed filter

.. _`dmx_section_feed.definition`:

Definition
----------

.. code-block:: c

    struct dmx_section_feed {
        int is_filtering;
        struct dmx_demux *parent;
        void *priv;
        int check_crc;
        int (*set)(struct dmx_section_feed *feed,u16 pid, int check_crc);
        int (*allocate_filter)(struct dmx_section_feed *feed, struct dmx_section_filter **filter);
        int (*release_filter)(struct dmx_section_feed *feed, struct dmx_section_filter *filter);
        int (*start_filtering)(struct dmx_section_feed *feed);
        int (*stop_filtering)(struct dmx_section_feed *feed);
    }

.. _`dmx_section_feed.members`:

Members
-------

is_filtering
    Set to non-zero when filtering in progress

parent
    pointer to struct dmx_demux

priv
    pointer to private data of the API client

check_crc
    If non-zero, check the CRC values of filtered sections.

set
    sets the section filter

allocate_filter
    This function is used to allocate a section filter on
    the demux. It should only be called when no filtering
    is in progress on this section feed. If a filter cannot
    be allocated, the function fails with -ENOSPC.

release_filter
    This function releases all the resources of a
    previously allocated section filter. The function
    should not be called while filtering is in progress
    on this section feed. After calling this function,
    the caller should not try to dereference the filter
    pointer.

start_filtering
    starts section filtering

stop_filtering
    stops section filtering

.. _`dmx_section_feed.description`:

Description
-----------

A TS feed is typically mapped to a hardware PID filter on the demux chip.
Using this API, the client can set the filtering properties to start/stop
filtering TS packets on a particular TS feed.

.. _`dmx_ts_cb`:

dmx_ts_cb
=========

.. c:function:: int dmx_ts_cb(const u8 *buffer1, size_t buffer1_length, const u8 *buffer2, size_t buffer2_length, struct dmx_ts_feed *source)

    DVB demux TS filter callback function prototype

    :param const u8 \*buffer1:
        Pointer to the start of the filtered TS packets.

    :param size_t buffer1_length:
        Length of the TS data in buffer1.

    :param const u8 \*buffer2:
        Pointer to the tail of the filtered TS packets, or NULL.

    :param size_t buffer2_length:
        Length of the TS data in buffer2.

    :param struct dmx_ts_feed \*source:
        Indicates which TS feed is the source of the callback.

.. _`dmx_ts_cb.description`:

Description
-----------

This function callback prototype, provided by the client of the demux API,
is called from the demux code. The function is only called when filtering
on a TS feed has been enabled using the start_filtering(\) function at
the \ :c:type:`struct dmx_demux <dmx_demux>`\ .
Any TS packets that match the filter settings are copied to a circular
buffer. The filtered TS packets are delivered to the client using this
callback function.
It is expected that the \ ``buffer1``\  and \ ``buffer2``\  callback parameters point to
addresses within the circular buffer, but other implementations are also
possible. Note that the called party should not try to free the memory
the \ ``buffer1``\  and \ ``buffer2``\  parameters point to.

When this function is called, the \ ``buffer1``\  parameter typically points to
the start of the first undelivered TS packet within a circular buffer.
The \ ``buffer2``\  buffer parameter is normally NULL, except when the received
TS packets have crossed the last address of the circular buffer and
”wrapped” to the beginning of the buffer. In the latter case the \ ``buffer1``\ 
parameter would contain an address within the circular buffer, while the
\ ``buffer2``\  parameter would contain the first address of the circular buffer.
The number of bytes delivered with this function (i.e. \ ``buffer1_length``\  +
\ ``buffer2_length``\ ) is usually equal to the value of callback_length parameter
given in the \ :c:func:`set`\  function, with one exception: if a timeout occurs before
receiving callback_length bytes of TS data, any undelivered packets are
immediately delivered to the client by calling this function. The timeout
duration is controlled by the \ :c:func:`set`\  function in the TS Feed API.

If a TS packet is received with errors that could not be fixed by the
TS-level forward error correction (FEC), the Transport_error_indicator
flag of the TS packet header should be set. The TS packet should not be
discarded, as the error can possibly be corrected by a higher layer
protocol. If the called party is slow in processing the callback, it
is possible that the circular buffer eventually fills up. If this happens,
the demux driver should discard any TS packets received while the buffer
is full and return -EOVERFLOW.

The type of data returned to the callback can be selected by the
\ :c:type:`struct dmx_ts_feed <dmx_ts_feed>`\ .@set function. The type parameter decides if the raw
TS packet (TS_PACKET) or just the payload (TS_PACKET|TS_PAYLOAD_ONLY)
should be returned. If additionally the TS_DECODER bit is set the stream
will also be sent to the hardware MPEG decoder.

.. _`dmx_ts_cb.return`:

Return
------


- 0, on success;

- -EOVERFLOW, on buffer overflow.

.. _`dmx_section_cb`:

dmx_section_cb
==============

.. c:function:: int dmx_section_cb(const u8 *buffer1, size_t buffer1_len, const u8 *buffer2, size_t buffer2_len, struct dmx_section_filter *source)

    DVB demux TS filter callback function prototype

    :param const u8 \*buffer1:
        Pointer to the start of the filtered section, e.g.
        within the circular buffer of the demux driver.

    :param size_t buffer1_len:
        Length of the filtered section data in \ ``buffer1``\ ,
        including headers and CRC.

    :param const u8 \*buffer2:
        Pointer to the tail of the filtered section data,
        or NULL. Useful to handle the wrapping of a
        circular buffer.

    :param size_t buffer2_len:
        Length of the filtered section data in \ ``buffer2``\ ,
        including headers and CRC.

    :param struct dmx_section_filter \*source:
        Indicates which section feed is the source of the
        callback.

.. _`dmx_section_cb.description`:

Description
-----------

This function callback prototype, provided by the client of the demux API,
is called from the demux code. The function is only called when
filtering of sections has been enabled using the function
\ :c:type:`struct dmx_ts_feed <dmx_ts_feed>`\ .@start_filtering. When the demux driver has received a
complete section that matches at least one section filter, the client
is notified via this callback function. Normally this function is called
for each received section; however, it is also possible to deliver
multiple sections with one callback, for example when the system load
is high. If an error occurs while receiving a section, this
function should be called with the corresponding error type set in the
success field, whether or not there is data to deliver. The Section Feed
implementation should maintain a circular buffer for received sections.
However, this is not necessary if the Section Feed API is implemented as
a client of the TS Feed API, because the TS Feed implementation then
buffers the received data. The size of the circular buffer can be
configured using the \ :c:type:`struct dmx_ts_feed <dmx_ts_feed>`\ .@set function in the Section Feed API.
If there is no room in the circular buffer when a new section is received,
the section must be discarded. If this happens, the value of the success
parameter should be DMX_OVERRUN_ERROR on the next callback.

.. _`dmx_frontend_source`:

enum dmx_frontend_source
========================

.. c:type:: enum dmx_frontend_source

    Used to identify the type of frontend

.. _`dmx_frontend_source.definition`:

Definition
----------

.. code-block:: c

    enum dmx_frontend_source {
        DMX_MEMORY_FE,
        DMX_FRONTEND_0
    };

.. _`dmx_frontend_source.constants`:

Constants
---------

DMX_MEMORY_FE
    The source of the demux is memory. It means that
    the MPEG-TS to be filtered comes from userspace,
    via \ :c:func:`write`\  syscall.

DMX_FRONTEND_0
    The source of the demux is a frontend connected
    to the demux.

.. _`dmx_frontend`:

struct dmx_frontend
===================

.. c:type:: struct dmx_frontend

    Structure that lists the frontends associated with a demux

.. _`dmx_frontend.definition`:

Definition
----------

.. code-block:: c

    struct dmx_frontend {
        struct list_head connectivity_list;
        enum dmx_frontend_source source;
    }

.. _`dmx_frontend.members`:

Members
-------

connectivity_list
    List of front-ends that can be connected to a
    particular demux;

source
    Type of the frontend.

.. _`dmx_frontend.description`:

Description
-----------

FIXME: this structure should likely be replaced soon by some
     media-controller based logic.

.. _`dmx_demux_caps`:

enum dmx_demux_caps
===================

.. c:type:: enum dmx_demux_caps

    MPEG-2 TS Demux capabilities bitmap

.. _`dmx_demux_caps.definition`:

Definition
----------

.. code-block:: c

    enum dmx_demux_caps {
        DMX_TS_FILTERING,
        DMX_SECTION_FILTERING,
        DMX_MEMORY_BASED_FILTERING
    };

.. _`dmx_demux_caps.constants`:

Constants
---------

DMX_TS_FILTERING
    set if TS filtering is supported;

DMX_SECTION_FILTERING
    set if section filtering is supported;

DMX_MEMORY_BASED_FILTERING
    set if \ :c:func:`write`\  available.

.. _`dmx_demux_caps.description`:

Description
-----------

Those flags are OR'ed in the \ :c:type:`dmx_demux.capabilities <dmx_demux>`\  field

.. _`dmx_fe_entry`:

DMX_FE_ENTRY
============

.. c:function::  DMX_FE_ENTRY( list)

    Casts elements in the list of registered front-ends from the generic type struct list_head to the type * struct dmx_frontend

    :param  list:
        list of struct dmx_frontend

.. _`dmx_demux`:

struct dmx_demux
================

.. c:type:: struct dmx_demux

    Structure that contains the demux capabilities and callbacks.

.. _`dmx_demux.definition`:

Definition
----------

.. code-block:: c

    struct dmx_demux {
        enum dmx_demux_caps capabilities;
        struct dmx_frontend *frontend;
        void *priv;
        int (*open)(struct dmx_demux *demux);
        int (*close)(struct dmx_demux *demux);
        int (*write)(struct dmx_demux *demux, const char __user *buf, size_t count);
        int (*allocate_ts_feed)(struct dmx_demux *demux,struct dmx_ts_feed **feed, dmx_ts_cb callback);
        int (*release_ts_feed)(struct dmx_demux *demux, struct dmx_ts_feed *feed);
        int (*allocate_section_feed)(struct dmx_demux *demux,struct dmx_section_feed **feed, dmx_section_cb callback);
        int (*release_section_feed)(struct dmx_demux *demux, struct dmx_section_feed *feed);
        int (*add_frontend)(struct dmx_demux *demux, struct dmx_frontend *frontend);
        int (*remove_frontend)(struct dmx_demux *demux, struct dmx_frontend *frontend);
        struct list_head *(*get_frontends)(struct dmx_demux *demux);
        int (*connect_frontend)(struct dmx_demux *demux, struct dmx_frontend *frontend);
        int (*disconnect_frontend)(struct dmx_demux *demux);
        int (*get_pes_pids)(struct dmx_demux *demux, u16 *pids);
    }

.. _`dmx_demux.members`:

Members
-------

capabilities
    Bitfield of capability flags.

frontend
    Front-end connected to the demux

priv
    Pointer to private data of the API client

open
    This function reserves the demux for use by the caller and, if
    necessary, initializes the demux. When the demux is no longer needed,
    the function \ ``close``\  should be called. It should be possible for
    multiple clients to access the demux at the same time. Thus, the
    function implementation should increment the demux usage count when
    \ ``open``\  is called and decrement it when \ ``close``\  is called.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.

    It returns:

    0 on success;
    -EUSERS, if maximum usage count was reached;
    -EINVAL, on bad parameter.

close
    This function reserves the demux for use by the caller and, if
    necessary, initializes the demux. When the demux is no longer needed,
    the function \ ``close``\  should be called. It should be possible for
    multiple clients to access the demux at the same time. Thus, the
    function implementation should increment the demux usage count when
    \ ``open``\  is called and decrement it when \ ``close``\  is called.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.

    It returns:

    0 on success;
    -ENODEV, if demux was not in use (e. g. no users);
    -EINVAL, on bad parameter.

write
    This function provides the demux driver with a memory buffer
    containing TS packets. Instead of receiving TS packets from the DVB
    front-end, the demux driver software will read packets from memory.
    Any clients of this demux with active TS, PES or Section filters will
    receive filtered data via the Demux callback API (see 0). The function
    returns when all the data in the buffer has been consumed by the demux.
    Demux hardware typically cannot read TS from memory. If this is the
    case, memory-based filtering has to be implemented entirely in software.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    The \ ``buf``\  function parameter contains a pointer to the TS data in
    kernel-space memory.
    The \ ``count``\  function parameter contains the length of the TS data.

    It returns:

    0 on success;
    -ERESTARTSYS, if mutex lock was interrupted;
    -EINTR, if a signal handling is pending;
    -ENODEV, if demux was removed;
    -EINVAL, on bad parameter.

allocate_ts_feed
    Allocates a new TS feed, which is used to filter the TS
    packets carrying a certain PID. The TS feed normally corresponds to a
    hardware PID filter on the demux chip.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    The \ ``feed``\  function parameter contains a pointer to the TS feed API and
    instance data.
    The \ ``callback``\  function parameter contains a pointer to the callback
    function for passing received TS packet.

    It returns:

    0 on success;
    -ERESTARTSYS, if mutex lock was interrupted;
    -EBUSY, if no more TS feeds is available;
    -EINVAL, on bad parameter.

release_ts_feed
    Releases the resources allocated with \ ``allocate_ts_feed``\ .
    Any filtering in progress on the TS feed should be stopped before
    calling this function.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    The \ ``feed``\  function parameter contains a pointer to the TS feed API and
    instance data.

    It returns:

    0 on success;
    -EINVAL on bad parameter.

allocate_section_feed
    Allocates a new section feed, i.e. a demux resource
    for filtering and receiving sections. On platforms with hardware
    support for section filtering, a section feed is directly mapped to
    the demux HW. On other platforms, TS packets are first PID filtered in
    hardware and a hardware section filter then emulated in software. The
    caller obtains an API pointer of type dmx_section_feed_t as an out
    parameter. Using this API the caller can set filtering parameters and
    start receiving sections.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    The \ ``feed``\  function parameter contains a pointer to the TS feed API and
    instance data.
    The \ ``callback``\  function parameter contains a pointer to the callback
    function for passing received TS packet.

    It returns:

    0 on success;
    -EBUSY, if no more TS feeds is available;
    -EINVAL, on bad parameter.

release_section_feed
    Releases the resources allocated with
    \ ``allocate_section_feed``\ , including allocated filters. Any filtering in
    progress on the section feed should be stopped before calling this
    function.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    The \ ``feed``\  function parameter contains a pointer to the TS feed API and
    instance data.

    It returns:

    0 on success;
    -EINVAL, on bad parameter.

add_frontend
    Registers a connectivity between a demux and a front-end,
    i.e., indicates that the demux can be connected via a call to
    \ ``connect_frontend``\  to use the given front-end as a TS source. The
    client of this function has to allocate dynamic or static memory for
    the frontend structure and initialize its fields before calling this
    function. This function is normally called during the driver
    initialization. The caller must not free the memory of the frontend
    struct before successfully calling \ ``remove_frontend``\ .
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    The \ ``frontend``\  function parameter contains a pointer to the front-end
    instance data.

    It returns:

    0 on success;
    -EINVAL, on bad parameter.

remove_frontend
    Indicates that the given front-end, registered by a call
    to \ ``add_frontend``\ , can no longer be connected as a TS source by this
    demux. The function should be called when a front-end driver or a demux
    driver is removed from the system. If the front-end is in use, the
    function fails with the return value of -EBUSY. After successfully
    calling this function, the caller can free the memory of the frontend
    struct if it was dynamically allocated before the \ ``add_frontend``\ 
    operation.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    The \ ``frontend``\  function parameter contains a pointer to the front-end
    instance data.

    It returns:

    0 on success;
    -ENODEV, if the front-end was not found,
    -EINVAL, on bad parameter.

get_frontends
    Provides the APIs of the front-ends that have been
    registered for this demux. Any of the front-ends obtained with this
    call can be used as a parameter for \ ``connect_frontend``\ . The include
    file demux.h contains the macro \ :c:func:`DMX_FE_ENTRY`\  for converting an
    element of the generic type struct \ :c:type:`struct list_head <list_head>`\  * to the type
    struct \ :c:type:`struct dmx_frontend <dmx_frontend>`\  *. The caller must not free the memory of any of
    the elements obtained via this function call.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    It returns a struct list_head pointer to the list of front-end
    interfaces, or NULL in the case of an empty list.

connect_frontend
    Connects the TS output of the front-end to the input of
    the demux. A demux can only be connected to a front-end registered to
    the demux with the function \ ``add_frontend``\ . It may or may not be
    possible to connect multiple demuxes to the same front-end, depending
    on the capabilities of the HW platform. When not used, the front-end
    should be released by calling \ ``disconnect_frontend``\ .
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    The \ ``frontend``\  function parameter contains a pointer to the front-end
    instance data.

    It returns:

    0 on success;
    -EINVAL, on bad parameter.

disconnect_frontend
    Disconnects the demux and a front-end previously
    connected by a \ ``connect_frontend``\  call.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.

    It returns:

    0 on success;
    -EINVAL on bad parameter.

get_pes_pids
    Get the PIDs for DMX_PES_AUDIO0, DMX_PES_VIDEO0,
    DMX_PES_TELETEXT0, DMX_PES_SUBTITLE0 and DMX_PES_PCR0.
    The \ ``demux``\  function parameter contains a pointer to the demux API and
    instance data.
    The \ ``pids``\  function parameter contains an array with five u16 elements
    where the PIDs will be stored.

    It returns:

    0 on success;
    -EINVAL on bad parameter.

.. This file was automatic generated / don't edit.

