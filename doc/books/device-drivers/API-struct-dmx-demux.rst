
.. _API-struct-dmx-demux:

================
struct dmx_demux
================

*man struct dmx_demux(9)*

*4.6.0-rc1*

Structure that contains the demux capabilities and callbacks.


Synopsis
========

.. code-block:: c

    struct dmx_demux {
      enum dmx_demux_caps capabilities;
      struct dmx_frontend * frontend;
      void * priv;
      int (* open) (struct dmx_demux *demux);
      int (* close) (struct dmx_demux *demux);
      int (* write) (struct dmx_demux *demux, const char __user *buf,size_t count);
      int (* allocate_ts_feed) (struct dmx_demux *demux,struct dmx_ts_feed **feed,dmx_ts_cb callback);
      int (* release_ts_feed) (struct dmx_demux *demux,struct dmx_ts_feed *feed);
      int (* allocate_section_feed) (struct dmx_demux *demux,struct dmx_section_feed **feed,dmx_section_cb callback);
      int (* release_section_feed) (struct dmx_demux *demux,struct dmx_section_feed *feed);
      int (* add_frontend) (struct dmx_demux *demux,struct dmx_frontend *frontend);
      int (* remove_frontend) (struct dmx_demux *demux,struct dmx_frontend *frontend);
      struct list_head *(* get_frontends) (struct dmx_demux *demux);
      int (* connect_frontend) (struct dmx_demux *demux,struct dmx_frontend *frontend);
      int (* disconnect_frontend) (struct dmx_demux *demux);
      int (* get_pes_pids) (struct dmx_demux *demux, u16 *pids);
    };


Members
=======

capabilities
    Bitfield of capability flags.

frontend
    Front-end connected to the demux

priv
    Pointer to private data of the API client

open
    This function reserves the demux for use by the caller and, if necessary, initializes the demux. When the demux is no longer needed, the function ``close`` should be called. It
    should be possible for multiple clients to access the demux at the same time. Thus, the function implementation should increment the demux usage count when ``open`` is called
    and decrement it when ``close`` is called. The ``demux`` function parameter contains a pointer to the demux API and instance data. It returns 0 on success; -EUSERS, if maximum
    usage count was reached; -EINVAL, on bad parameter.

close
    This function reserves the demux for use by the caller and, if necessary, initializes the demux. When the demux is no longer needed, the function ``close`` should be called. It
    should be possible for multiple clients to access the demux at the same time. Thus, the function implementation should increment the demux usage count when ``open`` is called
    and decrement it when ``close`` is called. The ``demux`` function parameter contains a pointer to the demux API and instance data. It returns 0 on success; -ENODEV, if demux
    was not in use (e. g. no users); -EINVAL, on bad parameter.

write
    This function provides the demux driver with a memory buffer containing TS packets. Instead of receiving TS packets from the DVB front-end, the demux driver software will read
    packets from memory. Any clients of this demux with active TS, PES or Section filters will receive filtered data via the Demux callback API (see 0). The function returns when
    all the data in the buffer has been consumed by the demux. Demux hardware typically cannot read TS from memory. If this is the case, memory-based filtering has to be
    implemented entirely in software. The ``demux`` function parameter contains a pointer to the demux API and instance data. The ``buf`` function parameter contains a pointer to
    the TS data in kernel-space memory. The ``count`` function parameter contains the length of the TS data. It returns 0 on success; -ERESTARTSYS, if mutex lock was interrupted;
    -EINTR, if a signal handling is pending; -ENODEV, if demux was removed; -EINVAL, on bad parameter.

allocate_ts_feed
    Allocates a new TS feed, which is used to filter the TS packets carrying a certain PID. The TS feed normally corresponds to a hardware PID filter on the demux chip. The
    ``demux`` function parameter contains a pointer to the demux API and instance data. The ``feed`` function parameter contains a pointer to the TS feed API and instance data. The
    ``callback`` function parameter contains a pointer to the callback function for passing received TS packet. It returns 0 on success; -ERESTARTSYS, if mutex lock was
    interrupted; -EBUSY, if no more TS feeds is available; -EINVAL, on bad parameter.

release_ts_feed
    Releases the resources allocated with ``allocate_ts_feed``. Any filtering in progress on the TS feed should be stopped before calling this function. The ``demux`` function
    parameter contains a pointer to the demux API and instance data. The ``feed`` function parameter contains a pointer to the TS feed API and instance data. It returns 0 on
    success; -EINVAL on bad parameter.

allocate_section_feed
    Allocates a new section feed, i.e. a demux resource for filtering and receiving sections. On platforms with hardware support for section filtering, a section feed is directly
    mapped to the demux HW. On other platforms, TS packets are first PID filtered in hardware and a hardware section filter then emulated in software. The caller obtains an API
    pointer of type dmx_section_feed_t as an out parameter. Using this API the caller can set filtering parameters and start receiving sections. The ``demux`` function parameter
    contains a pointer to the demux API and instance data. The ``feed`` function parameter contains a pointer to the TS feed API and instance data. The ``callback`` function
    parameter contains a pointer to the callback function for passing received TS packet. It returns 0 on success; -EBUSY, if no more TS feeds is available; -EINVAL, on bad
    parameter.

release_section_feed
    Releases the resources allocated with ``allocate_section_feed``, including allocated filters. Any filtering in progress on the section feed should be stopped before calling
    this function. The ``demux`` function parameter contains a pointer to the demux API and instance data. The ``feed`` function parameter contains a pointer to the TS feed API and
    instance data. It returns 0 on success; -EINVAL, on bad parameter.

add_frontend
    Registers a connectivity between a demux and a front-end, i.e., indicates that the demux can be connected via a call to ``connect_frontend`` to use the given front-end as a TS
    source. The client of this function has to allocate dynamic or static memory for the frontend structure and initialize its fields before calling this function. This function is
    normally called during the driver initialization. The caller must not free the memory of the frontend struct before successfully calling ``remove_frontend``. The ``demux``
    function parameter contains a pointer to the demux API and instance data. The ``frontend`` function parameter contains a pointer to the front-end instance data. It returns 0 on
    success; -EINVAL, on bad parameter.

remove_frontend
    Indicates that the given front-end, registered by a call to ``add_frontend``, can no longer be connected as a TS source by this demux. The function should be called when a
    front-end driver or a demux driver is removed from the system. If the front-end is in use, the function fails with the return value of -EBUSY. After successfully calling this
    function, the caller can free the memory of the frontend struct if it was dynamically allocated before the ``add_frontend`` operation. The ``demux`` function parameter contains
    a pointer to the demux API and instance data. The ``frontend`` function parameter contains a pointer to the front-end instance data. It returns 0 on success; -ENODEV, if the
    front-end was not found, -EINVAL, on bad parameter.

get_frontends
    Provides the APIs of the front-ends that have been registered for this demux. Any of the front-ends obtained with this call can be used as a parameter for ``connect_frontend``.
    The include file demux.h contains the macro ``DMX_FE_ENTRY`` for converting an element of the generic type struct ``list_head`` ⋆ to the type struct ``dmx_frontend`` ⋆. The
    caller must not free the memory of any of the elements obtained via this function call. The ``demux`` function parameter contains a pointer to the demux API and instance data.
    It returns a struct list_head pointer to the list of front-end interfaces, or NULL in the case of an empty list.

connect_frontend
    Connects the TS output of the front-end to the input of the demux. A demux can only be connected to a front-end registered to the demux with the function ``add_frontend``. It
    may or may not be possible to connect multiple demuxes to the same front-end, depending on the capabilities of the HW platform. When not used, the front-end should be released
    by calling ``disconnect_frontend``. The ``demux`` function parameter contains a pointer to the demux API and instance data. The ``frontend`` function parameter contains a
    pointer to the front-end instance data. It returns 0 on success; -EINVAL, on bad parameter.

disconnect_frontend
    Disconnects the demux and a front-end previously connected by a ``connect_frontend`` call. The ``demux`` function parameter contains a pointer to the demux API and instance
    data. It returns 0 on success; -EINVAL on bad parameter.

get_pes_pids
    Get the PIDs for DMX_PES_AUDIO0, DMX_PES_VIDEO0, DMX_PES_TELETEXT0, DMX_PES_SUBTITLE0 and DMX_PES_PCR0. The ``demux`` function parameter contains a pointer to the
    demux API and instance data. The ``pids`` function parameter contains an array with five u16 elements where the PIDs will be stored. It returns 0 on success; -EINVAL on bad
    parameter.
