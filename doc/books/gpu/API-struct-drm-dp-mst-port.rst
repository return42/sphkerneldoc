
.. _API-struct-drm-dp-mst-port:

======================
struct drm_dp_mst_port
======================

*man struct drm_dp_mst_port(9)*

*4.6.0-rc1*

MST port


Synopsis
========

.. code-block:: c

    struct drm_dp_mst_port {
      struct kref kref;
      u8 port_num;
      bool input;
      bool mcs;
      bool ddps;
      u8 pdt;
      bool ldps;
      u8 dpcd_rev;
      u8 num_sdp_streams;
      u8 num_sdp_stream_sinks;
      uint16_t available_pbn;
      struct list_head next;
      struct drm_dp_mst_branch * mstb;
      struct drm_dp_aux aux;
      struct drm_dp_mst_branch * parent;
      struct drm_dp_vcpi vcpi;
      struct drm_connector * connector;
      struct drm_dp_mst_topology_mgr * mgr;
    };


Members
=======

kref
    reference count for this port.

port_num
    port number

input
    if this port is an input port.

mcs
    message capability status - DP 1.2 spec.

ddps
    DisplayPort Device Plug Status - DP 1.2

pdt
    Peer Device Type

ldps
    Legacy Device Plug Status

dpcd_rev
    DPCD revision of device on this port

num_sdp_streams
    Number of simultaneous streams

num_sdp_stream_sinks
    Number of stream sinks

available_pbn
    Available bandwidth for this port.

next
    link to next port on this branch device

mstb
    branch device attach below this port

aux
    i2c aux transport to talk to device connected to this port.

parent
    branch device parent of this port

vcpi
    Virtual Channel Payload info for this port.

connector
    DRM connector this port is connected to.

mgr
    topology manager this port lives under.


Description
===========

This structure represents an MST port endpoint on a device somewhere in the MST topology.
