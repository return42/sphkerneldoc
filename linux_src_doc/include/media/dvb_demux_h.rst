.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/dvb_demux.h

.. _`dvb_dmx_filter_type`:

enum dvb_dmx_filter_type
========================

.. c:type:: enum dvb_dmx_filter_type

    type of demux feed.

.. _`dvb_dmx_filter_type.definition`:

Definition
----------

.. code-block:: c

    enum dvb_dmx_filter_type {
        DMX_TYPE_TS,
        DMX_TYPE_SEC
    };

.. _`dvb_dmx_filter_type.constants`:

Constants
---------

DMX_TYPE_TS
    feed is in TS mode.

DMX_TYPE_SEC
    feed is in Section mode.

.. _`dvb_dmx_state`:

enum dvb_dmx_state
==================

.. c:type:: enum dvb_dmx_state

    state machine for a demux filter.

.. _`dvb_dmx_state.definition`:

Definition
----------

.. code-block:: c

    enum dvb_dmx_state {
        DMX_STATE_FREE,
        DMX_STATE_ALLOCATED,
        DMX_STATE_READY,
        DMX_STATE_GO
    };

.. _`dvb_dmx_state.constants`:

Constants
---------

DMX_STATE_FREE
    indicates that the filter is freed.

DMX_STATE_ALLOCATED
    indicates that the filter was allocated
    to be used.

DMX_STATE_READY
    indicates that the filter is ready
    to be used.

DMX_STATE_GO
    indicates that the filter is running.

.. _`dvb_demux_filter`:

struct dvb_demux_filter
=======================

.. c:type:: struct dvb_demux_filter

    Describes a DVB demux section filter.

.. _`dvb_demux_filter.definition`:

Definition
----------

.. code-block:: c

    struct dvb_demux_filter {
        struct dmx_section_filter filter;
        u8 maskandmode[DMX_MAX_FILTER_SIZE];
        u8 maskandnotmode[DMX_MAX_FILTER_SIZE];
        bool doneq;
        struct dvb_demux_filter *next;
        struct dvb_demux_feed *feed;
        int index;
        enum dvb_dmx_state state;
        enum dvb_dmx_filter_type type;
    }

.. _`dvb_demux_filter.members`:

Members
-------

filter
    Section filter as defined by \ :c:type:`struct dmx_section_filter <dmx_section_filter>`\ .

maskandmode
    logical ``and`` bit mask.

maskandnotmode
    logical ``and not`` bit mask.

doneq
    flag that indicates when a filter is ready.

next
    pointer to the next section filter.

feed
    \ :c:type:`struct dvb_demux_feed <dvb_demux_feed>`\  pointer.

index
    index of the used demux filter.

state
    state of the filter as described by \ :c:type:`enum dvb_dmx_state <dvb_dmx_state>`\ .

type
    type of the filter as described
    by \ :c:type:`enum dvb_dmx_filter_type <dvb_dmx_filter_type>`\ .

.. _`dvb_demux_feed`:

struct dvb_demux_feed
=====================

.. c:type:: struct dvb_demux_feed

    describes a DVB field

.. _`dvb_demux_feed.definition`:

Definition
----------

.. code-block:: c

    struct dvb_demux_feed {
        union {
            struct dmx_ts_feed ts;
            struct dmx_section_feed sec;
        } feed;
        union {
            dmx_ts_cb ts;
            dmx_section_cb sec;
        } cb;
        struct dvb_demux *demux;
        void *priv;
        enum dvb_dmx_filter_type type;
        enum dvb_dmx_state state;
        u16 pid;
        ktime_t timeout;
        struct dvb_demux_filter *filter;
        enum ts_filter_type ts_type;
        enum dmx_ts_pes pes_type;
        int cc;
        bool pusi_seen;
        u16 peslen;
        struct list_head list_head;
        unsigned int index;
    }

.. _`dvb_demux_feed.members`:

Members
-------

feed
    a union describing a digital TV feed.
    Depending on the feed type, it can be either
    \ ``feed``\ .ts or \ ``feed``\ .sec.

feed.ts
    a \ :c:type:`struct dmx_ts_feed <dmx_ts_feed>`\  pointer.
    For TS feed only.

feed.sec
    a \ :c:type:`struct dmx_section_feed <dmx_section_feed>`\  pointer.
    For section feed only.

cb
    a union describing digital TV callbacks.
    Depending on the feed type, it can be either
    \ ``cb``\ .ts or \ ``cb``\ .sec.

cb.ts
    a \ :c:func:`dmx_ts_cb`\  calback function pointer.
    For TS feed only.

cb.sec
    a \ :c:func:`dmx_section_cb`\  callback function pointer.
    For section feed only.

demux
    pointer to \ :c:type:`struct dvb_demux <dvb_demux>`\ .

priv
    private data that can optionally be used by a DVB driver.

type
    type of the filter, as defined by \ :c:type:`enum dvb_dmx_filter_type <dvb_dmx_filter_type>`\ .

state
    state of the filter as defined by \ :c:type:`enum dvb_dmx_state <dvb_dmx_state>`\ .

pid
    PID to be filtered.

timeout
    feed timeout.

filter
    pointer to \ :c:type:`struct dvb_demux_filter <dvb_demux_filter>`\ .

ts_type
    type of TS, as defined by \ :c:type:`enum ts_filter_type <ts_filter_type>`\ .

pes_type
    type of PES, as defined by \ :c:type:`enum dmx_ts_pes <dmx_ts_pes>`\ .

cc
    MPEG-TS packet continuity counter

pusi_seen
    if true, indicates that a discontinuity was detected.
    it is used to prevent feeding of garbage from previous section.

peslen
    length of the PES (Packet Elementary Stream).

list_head
    head for the list of digital TV demux feeds.

index
    a unique index for each feed. Can be used as hardware
    pid filter index.

.. _`dvb_demux`:

struct dvb_demux
================

.. c:type:: struct dvb_demux

    represents a digital TV demux

.. _`dvb_demux.definition`:

Definition
----------

.. code-block:: c

    struct dvb_demux {
        struct dmx_demux dmx;
        void *priv;
        int filternum;
        int feednum;
        int (*start_feed)(struct dvb_demux_feed *feed);
        int (*stop_feed)(struct dvb_demux_feed *feed);
        int (*write_to_decoder)(struct dvb_demux_feed *feed, const u8 *buf, size_t len);
        u32 (*check_crc32)(struct dvb_demux_feed *feed, const u8 *buf, size_t len);
        void (*memcopy)(struct dvb_demux_feed *feed, u8 *dst, const u8 *src, size_t len);
        int users;
    #define MAX_DVB_DEMUX_USERS 10
        struct dvb_demux_filter *filter;
        struct dvb_demux_feed *feed;
        struct list_head frontend_list;
        struct dvb_demux_feed *pesfilter[DMX_PES_OTHER];
        u16 pids[DMX_PES_OTHER];
    #define DMX_MAX_PID 0x2000
        struct list_head feed_list;
        u8 tsbuf[204];
        int tsbufp;
        struct mutex mutex;
        spinlock_t lock;
        uint8_t *cnt_storage;
        ktime_t speed_last_time;
        uint32_t speed_pkts_cnt;
    }

.. _`dvb_demux.members`:

Members
-------

dmx
    embedded \ :c:type:`struct dmx_demux <dmx_demux>`\  with demux capabilities
    and callbacks.

priv
    private data that can optionally be used by
    a DVB driver.

filternum
    maximum amount of DVB filters.

feednum
    maximum amount of DVB feeds.

start_feed
    callback routine to be called in order to start
    a DVB feed.

stop_feed
    callback routine to be called in order to stop
    a DVB feed.

write_to_decoder
    callback routine to be called if the feed is TS and
    it is routed to an A/V decoder, when a new TS packet
    is received.
    Used only on av7110-av.c.

check_crc32
    callback routine to check CRC. If not initialized,
    dvb_demux will use an internal one.

memcopy
    callback routine to memcopy received data.
    If not initialized, dvb_demux will default to \ :c:func:`memcpy`\ .

users
    counter for the number of demux opened file descriptors.
    Currently, it is limited to 10 users.

filter
    pointer to \ :c:type:`struct dvb_demux_filter <dvb_demux_filter>`\ .

feed
    pointer to \ :c:type:`struct dvb_demux_feed <dvb_demux_feed>`\ .

frontend_list
    \ :c:type:`struct list_head <list_head>`\  with frontends used by the demux.

pesfilter
    array of \ :c:type:`struct dvb_demux_feed <dvb_demux_feed>`\  with the PES types
    that will be filtered.

pids
    list of filtered program IDs.

feed_list
    \ :c:type:`struct list_head <list_head>`\  with feeds.

tsbuf
    temporary buffer used internally to store TS packets.

tsbufp
    temporary buffer index used internally.

mutex
    pointer to \ :c:type:`struct mutex <mutex>`\  used to protect feed set
    logic.

lock
    pointer to \ :c:type:`struct spinlock_t <spinlock_t>`\ , used to protect buffer handling.

cnt_storage
    buffer used for TS/TEI continuity check.

speed_last_time
    \ :c:type:`struct ktime_t <ktime_t>`\  used for TS speed check.

speed_pkts_cnt
    packets count used for TS speed check.

.. _`dvb_dmx_init`:

dvb_dmx_init
============

.. c:function:: int dvb_dmx_init(struct dvb_demux *demux)

    initialize a digital TV demux struct.

    :param struct dvb_demux \*demux:
        \ :c:type:`struct dvb_demux <dvb_demux>`\  to be initialized.

.. _`dvb_dmx_init.description`:

Description
-----------

Before being able to register a digital TV demux struct, drivers
should call this routine. On its typical usage, some fields should
be initialized at the driver before calling it.

A typical usecase is::

     dvb->demux.dmx.capabilities =
             DMX_TS_FILTERING | DMX_SECTION_FILTERING |
             DMX_MEMORY_BASED_FILTERING;
     dvb->demux.priv       = dvb;
     dvb->demux.filternum  = 256;
     dvb->demux.feednum    = 256;
     dvb->demux.start_feed = driver_start_feed;
     dvb->demux.stop_feed  = driver_stop_feed;
     ret = dvb_dmx_init(&dvb->demux);
     if (ret < 0)
             return ret;

.. _`dvb_dmx_release`:

dvb_dmx_release
===============

.. c:function:: void dvb_dmx_release(struct dvb_demux *demux)

    releases a digital TV demux internal buffers.

    :param struct dvb_demux \*demux:
        \ :c:type:`struct dvb_demux <dvb_demux>`\  to be released.

.. _`dvb_dmx_release.description`:

Description
-----------

The DVB core internally allocates data at \ ``demux``\ . This routine
releases those data. Please notice that the struct itelf is not
released, as it can be embedded on other structs.

.. _`dvb_dmx_swfilter_packets`:

dvb_dmx_swfilter_packets
========================

.. c:function:: void dvb_dmx_swfilter_packets(struct dvb_demux *demux, const u8 *buf, size_t count)

    use dvb software filter for a buffer with multiple MPEG-TS packets with 188 bytes each.

    :param struct dvb_demux \*demux:
        pointer to \ :c:type:`struct dvb_demux <dvb_demux>`\ 

    :param const u8 \*buf:
        buffer with data to be filtered

    :param size_t count:
        number of MPEG-TS packets with size of 188.

.. _`dvb_dmx_swfilter_packets.description`:

Description
-----------

The routine will discard a DVB packet that don't start with 0x47.

Use this routine if the DVB demux fills MPEG-TS buffers that are
already aligned.

.. _`dvb_dmx_swfilter_packets.note`:

NOTE
----

The \ ``buf``\  size should have size equal to ``count * 188``.

.. _`dvb_dmx_swfilter`:

dvb_dmx_swfilter
================

.. c:function:: void dvb_dmx_swfilter(struct dvb_demux *demux, const u8 *buf, size_t count)

    use dvb software filter for a buffer with multiple MPEG-TS packets with 188 bytes each.

    :param struct dvb_demux \*demux:
        pointer to \ :c:type:`struct dvb_demux <dvb_demux>`\ 

    :param const u8 \*buf:
        buffer with data to be filtered

    :param size_t count:
        number of MPEG-TS packets with size of 188.

.. _`dvb_dmx_swfilter.description`:

Description
-----------

If a DVB packet doesn't start with 0x47, it will seek for the first
byte that starts with 0x47.

Use this routine if the DVB demux fill buffers that may not start with
a packet start mark (0x47).

.. _`dvb_dmx_swfilter.note`:

NOTE
----

The \ ``buf``\  size should have size equal to ``count * 188``.

.. _`dvb_dmx_swfilter_204`:

dvb_dmx_swfilter_204
====================

.. c:function:: void dvb_dmx_swfilter_204(struct dvb_demux *demux, const u8 *buf, size_t count)

    use dvb software filter for a buffer with multiple MPEG-TS packets with 204 bytes each.

    :param struct dvb_demux \*demux:
        pointer to \ :c:type:`struct dvb_demux <dvb_demux>`\ 

    :param const u8 \*buf:
        buffer with data to be filtered

    :param size_t count:
        number of MPEG-TS packets with size of 204.

.. _`dvb_dmx_swfilter_204.description`:

Description
-----------

If a DVB packet doesn't start with 0x47, it will seek for the first
byte that starts with 0x47.

Use this routine if the DVB demux fill buffers that may not start with
a packet start mark (0x47).

.. _`dvb_dmx_swfilter_204.note`:

NOTE
----

The \ ``buf``\  size should have size equal to ``count * 204``.

.. _`dvb_dmx_swfilter_raw`:

dvb_dmx_swfilter_raw
====================

.. c:function:: void dvb_dmx_swfilter_raw(struct dvb_demux *demux, const u8 *buf, size_t count)

    make the raw data available to userspace without filtering

    :param struct dvb_demux \*demux:
        pointer to \ :c:type:`struct dvb_demux <dvb_demux>`\ 

    :param const u8 \*buf:
        buffer with data

    :param size_t count:
        number of packets to be passed. The actual size of each packet
        depends on the \ :c:type:`dvb_demux->feed <dvb_demux>`\ ->cb.ts logic.

.. _`dvb_dmx_swfilter_raw.description`:

Description
-----------

Use it if the driver needs to deliver the raw payload to userspace without
passing through the kernel demux. That is meant to support some
delivery systems that aren't based on MPEG-TS.

This function relies on \ :c:type:`dvb_demux->feed <dvb_demux>`\ ->cb.ts to actually handle the
buffer.

.. This file was automatic generated / don't edit.

