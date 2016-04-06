
.. _API-struct-dmx-section-feed:

=======================
struct dmx_section_feed
=======================

*man struct dmx_section_feed(9)*

*4.6.0-rc1*

Structure that contains a section feed filter


Synopsis
========

.. code-block:: c

    struct dmx_section_feed {
      int is_filtering;
      struct dmx_demux * parent;
      void * priv;
      int check_crc;
      int (* set) (struct dmx_section_feed *feed,u16 pid,size_t circular_buffer_size,int check_crc);
      int (* allocate_filter) (struct dmx_section_feed *feed,struct dmx_section_filter **filter);
      int (* release_filter) (struct dmx_section_feed *feed,struct dmx_section_filter *filter);
      int (* start_filtering) (struct dmx_section_feed *feed);
      int (* stop_filtering) (struct dmx_section_feed *feed);
    };


Members
=======

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
    This function is used to allocate a section filter on the demux. It should only be called when no filtering is in progress on this section feed. If a filter cannot be
    allocated, the function fails with -ENOSPC.

release_filter
    This function releases all the resources of a previously allocated section filter. The function should not be called while filtering is in progress on this section feed. After
    calling this function, the caller should not try to dereference the filter pointer.

start_filtering
    starts section filtering

stop_filtering
    stops section filtering


Description
===========

A TS feed is typically mapped to a hardware PID filter on the demux chip. Using this API, the client can set the filtering properties to start/stop filtering TS packets on a
particular TS feed.
