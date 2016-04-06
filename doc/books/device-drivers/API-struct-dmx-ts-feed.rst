
.. _API-struct-dmx-ts-feed:

==================
struct dmx_ts_feed
==================

*man struct dmx_ts_feed(9)*

*4.6.0-rc1*

Structure that contains a TS feed filter


Synopsis
========

.. code-block:: c

    struct dmx_ts_feed {
      int is_filtering;
      struct dmx_demux * parent;
      void * priv;
      int (* set) (struct dmx_ts_feed *feed,u16 pid,int type,enum dmx_ts_pes pes_type,size_t circular_buffer_size,struct timespec timeout);
      int (* start_filtering) (struct dmx_ts_feed *feed);
      int (* stop_filtering) (struct dmx_ts_feed *feed);
    };


Members
=======

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


Description
===========

A TS feed is typically mapped to a hardware PID filter on the demux chip. Using this API, the client can set the filtering properties to start/stop filtering TS packets on a
particular TS feed.
