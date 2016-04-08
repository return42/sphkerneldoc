
.. _API-struct-mpath-info:

=================
struct mpath_info
=================

*man struct mpath_info(9)*

*4.6.0-rc1*

mesh path information


Synopsis
========

.. code-block:: c

    struct mpath_info {
      u32 filled;
      u32 frame_qlen;
      u32 sn;
      u32 metric;
      u32 exptime;
      u32 discovery_timeout;
      u8 discovery_retries;
      u8 flags;
      int generation;
    };


Members
=======

filled
    bitfield of flags from ``enum`` mpath_info_flags

frame_qlen
    number of queued frames for this destination

sn
    target sequence number

metric
    metric (cost) of this mesh path

exptime
    expiration time for the mesh path from now, in msecs

discovery_timeout
    total mesh path discovery timeout, in msecs

discovery_retries
    mesh path discovery retries

flags
    mesh path flags

generation
    generation number for nl80211 dumps. This number should increase every time the list of mesh paths changes, i.e. when a station is added or removed, so that userspace can tell
    whether it got a consistent snapshot.


Description
===========

Mesh path information filled by driver for ``get_mpath`` and ``dump_mpath``.
