.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/dmxdev.h

.. _`dmxdev_type`:

enum dmxdev_type
================

.. c:type:: enum dmxdev_type

    type of demux filter type.

.. _`dmxdev_type.definition`:

Definition
----------

.. code-block:: c

    enum dmxdev_type {
        DMXDEV_TYPE_NONE,
        DMXDEV_TYPE_SEC,
        DMXDEV_TYPE_PES
    };

.. _`dmxdev_type.constants`:

Constants
---------

DMXDEV_TYPE_NONE
    no filter set.

DMXDEV_TYPE_SEC
    section filter.

DMXDEV_TYPE_PES
    Program Elementary Stream (PES) filter.

.. _`dmxdev_state`:

enum dmxdev_state
=================

.. c:type:: enum dmxdev_state

    state machine for the dmxdev.

.. _`dmxdev_state.definition`:

Definition
----------

.. code-block:: c

    enum dmxdev_state {
        DMXDEV_STATE_FREE,
        DMXDEV_STATE_ALLOCATED,
        DMXDEV_STATE_SET,
        DMXDEV_STATE_GO,
        DMXDEV_STATE_DONE,
        DMXDEV_STATE_TIMEDOUT
    };

.. _`dmxdev_state.constants`:

Constants
---------

DMXDEV_STATE_FREE
    indicates that the filter is freed.

DMXDEV_STATE_ALLOCATED
    indicates that the filter was allocated
    to be used.

DMXDEV_STATE_SET
    indicates that the filter parameters are set.

DMXDEV_STATE_GO
    indicates that the filter is running.

DMXDEV_STATE_DONE
    indicates that a packet was already filtered
    and the filter is now disabled.
    Set only if \ ``DMX_ONESHOT``\ . See
    \ :c:type:`struct dmx_sct_filter_params <dmx_sct_filter_params>`\ .

DMXDEV_STATE_TIMEDOUT
    Indicates a timeout condition.

.. _`dmxdev_feed`:

struct dmxdev_feed
==================

.. c:type:: struct dmxdev_feed

    digital TV dmxdev feed

.. _`dmxdev_feed.definition`:

Definition
----------

.. code-block:: c

    struct dmxdev_feed {
        u16 pid;
        struct dmx_ts_feed *ts;
        struct list_head next;
    }

.. _`dmxdev_feed.members`:

Members
-------

pid
    Program ID to be filtered

ts
    pointer to \ :c:type:`struct dmx_ts_feed <dmx_ts_feed>`\ 

next
    &struct list_head pointing to the next feed.

.. _`dmxdev_filter`:

struct dmxdev_filter
====================

.. c:type:: struct dmxdev_filter

    digital TV dmxdev filter

.. _`dmxdev_filter.definition`:

Definition
----------

.. code-block:: c

    struct dmxdev_filter {
        union {
            struct dmx_section_filter *sec;
        } filter;
        union {
            struct list_head ts;
            struct dmx_section_feed *sec;
        } feed;
        union {
            struct dmx_sct_filter_params sec;
            struct dmx_pes_filter_params pes;
        } params;
        enum dmxdev_type type;
        enum dmxdev_state state;
        struct dmxdev *dev;
        struct dvb_ringbuffer buffer;
        struct dvb_vb2_ctx vb2_ctx;
        struct mutex mutex;
        struct timer_list timer;
        int todo;
        u8 secheader[3];
    }

.. _`dmxdev_filter.members`:

Members
-------

filter
    a union describing a dmxdev filter.
    Currently used only for section filters.

filter.sec
    a \ :c:type:`struct dmx_section_filter <dmx_section_filter>`\  pointer.
    For section filter only.

feed
    a union describing a dmxdev feed.
    Depending on the filter type, it can be either
    \ ``feed``\ .ts or \ ``feed``\ .sec.

feed.ts
    a \ :c:type:`struct list_head <list_head>`\  list.
    For TS and PES feeds.

feed.sec
    a \ :c:type:`struct dmx_section_feed <dmx_section_feed>`\  pointer.
    For section feed only.

params
    a union describing dmxdev filter parameters.
    Depending on the filter type, it can be either
    \ ``params``\ .sec or \ ``params``\ .pes.

params.sec
    a \ :c:type:`struct dmx_sct_filter_params <dmx_sct_filter_params>`\  embedded struct.
    For section filter only.

params.pes
    a \ :c:type:`struct dmx_pes_filter_params <dmx_pes_filter_params>`\  embedded struct.
    For PES filter only.

type
    type of the dmxdev filter, as defined by \ :c:type:`enum dmxdev_type <dmxdev_type>`\ .

state
    state of the dmxdev filter, as defined by \ :c:type:`enum dmxdev_state <dmxdev_state>`\ .

dev
    pointer to \ :c:type:`struct dmxdev <dmxdev>`\ .

buffer
    an embedded \ :c:type:`struct dvb_ringbuffer <dvb_ringbuffer>`\  buffer.

vb2_ctx
    control struct for VB2 handler

mutex
    protects the access to \ :c:type:`struct dmxdev_filter <dmxdev_filter>`\ .

timer
    &struct timer_list embedded timer, used to check for
    feed timeouts.
    Only for section filter.

todo
    index for the \ ``secheader``\ .
    Only for section filter.

secheader
    buffer cache to parse the section header.
    Only for section filter.

.. _`dmxdev`:

struct dmxdev
=============

.. c:type:: struct dmxdev

    Describes a digital TV demux device.

.. _`dmxdev.definition`:

Definition
----------

.. code-block:: c

    struct dmxdev {
        struct dvb_device *dvbdev;
        struct dvb_device *dvr_dvbdev;
        struct dmxdev_filter *filter;
        struct dmx_demux *demux;
        int filternum;
        int capabilities;
        unsigned int exit:1;
    #define DMXDEV_CAP_DUPLEX 1
        struct dmx_frontend *dvr_orig_fe;
        struct dvb_ringbuffer dvr_buffer;
    #define DVR_BUFFER_SIZE (10*188*1024)
        struct dvb_vb2_ctx dvr_vb2_ctx;
        struct mutex mutex;
        spinlock_t lock;
    }

.. _`dmxdev.members`:

Members
-------

dvbdev
    pointer to \ :c:type:`struct dvb_device <dvb_device>`\  associated with
    the demux device node.

dvr_dvbdev
    pointer to \ :c:type:`struct dvb_device <dvb_device>`\  associated with
    the dvr device node.

filter
    pointer to \ :c:type:`struct dmxdev_filter <dmxdev_filter>`\ .

demux
    pointer to \ :c:type:`struct dmx_demux <dmx_demux>`\ .

filternum
    number of filters.

capabilities
    demux capabilities as defined by \ :c:type:`enum dmx_demux_caps <dmx_demux_caps>`\ .

exit
    flag to indicate that the demux is being released.

dvr_orig_fe
    pointer to \ :c:type:`struct dmx_frontend <dmx_frontend>`\ .

dvr_buffer
    embedded \ :c:type:`struct dvb_ringbuffer <dvb_ringbuffer>`\  for DVB output.

dvr_vb2_ctx
    control struct for VB2 handler

mutex
    protects the usage of this structure.

lock
    protects access to \ :c:type:`dmxdev->filter <dmxdev>`\ ->data.

.. _`dvb_dmxdev_init`:

dvb_dmxdev_init
===============

.. c:function:: int dvb_dmxdev_init(struct dmxdev *dmxdev, struct dvb_adapter *adap)

    initializes a digital TV demux and registers both demux and DVR devices.

    :param struct dmxdev \*dmxdev:
        pointer to \ :c:type:`struct dmxdev <dmxdev>`\ .

    :param struct dvb_adapter \*adap:
        pointer to \ :c:type:`struct dvb_adapter <dvb_adapter>`\ .

.. _`dvb_dmxdev_release`:

dvb_dmxdev_release
==================

.. c:function:: void dvb_dmxdev_release(struct dmxdev *dmxdev)

    releases a digital TV demux and unregisters it.

    :param struct dmxdev \*dmxdev:
        pointer to \ :c:type:`struct dmxdev <dmxdev>`\ .

.. This file was automatic generated / don't edit.

