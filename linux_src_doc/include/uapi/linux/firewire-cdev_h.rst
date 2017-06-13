.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/firewire-cdev.h

.. _`fw_cdev_event_common`:

struct fw_cdev_event_common
===========================

.. c:type:: struct fw_cdev_event_common

    Common part of all fw_cdev_event\_ types

.. _`fw_cdev_event_common.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_event_common {
        __u64 closure;
        __u32 type;
    }

.. _`fw_cdev_event_common.members`:

Members
-------

closure
    For arbitrary use by userspace

type
    Discriminates the fw_cdev_event\_ types

.. _`fw_cdev_event_common.description`:

Description
-----------

This struct may be used to access generic members of all fw_cdev_event\_
types regardless of the specific type.

Data passed in the \ ``closure``\  field for a request will be returned in the
corresponding event.  It is big enough to hold a pointer on all platforms.
The ioctl used to set \ ``closure``\  depends on the \ ``type``\  of event.

.. _`fw_cdev_event_bus_reset`:

struct fw_cdev_event_bus_reset
==============================

.. c:type:: struct fw_cdev_event_bus_reset

    Sent when a bus reset occurred

.. _`fw_cdev_event_bus_reset.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_event_bus_reset {
        __u64 closure;
        __u32 type;
        __u32 node_id;
        __u32 local_node_id;
        __u32 bm_node_id;
        __u32 irm_node_id;
        __u32 root_node_id;
        __u32 generation;
    }

.. _`fw_cdev_event_bus_reset.members`:

Members
-------

closure
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ; set by \ ``FW_CDEV_IOC_GET_INFO``\  ioctl

type
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ; always \ ``FW_CDEV_EVENT_BUS_RESET``\ 

node_id
    New node ID of this node

local_node_id
    Node ID of the local node, i.e. of the controller

bm_node_id
    Node ID of the bus manager

irm_node_id
    Node ID of the iso resource manager

root_node_id
    Node ID of the root node

generation
    New bus generation

.. _`fw_cdev_event_bus_reset.description`:

Description
-----------

This event is sent when the bus the device belongs to goes through a bus
reset.  It provides information about the new bus configuration, such as
new node ID for this device, new root ID, and others.

If \ ``bm_node_id``\  is 0xffff right after bus reset it can be reread by an
\ ``FW_CDEV_IOC_GET_INFO``\  ioctl after bus manager selection was finished.
Kernels with ABI version < 4 do not set \ ``bm_node_id``\ .

.. _`fw_cdev_event_response`:

struct fw_cdev_event_response
=============================

.. c:type:: struct fw_cdev_event_response

    Sent when a response packet was received

.. _`fw_cdev_event_response.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_event_response {
        __u64 closure;
        __u32 type;
        __u32 rcode;
        __u32 length;
        __u32 data;
    }

.. _`fw_cdev_event_response.members`:

Members
-------

closure
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ; set by \ ``FW_CDEV_IOC_SEND_REQUEST``\ 
    or \ ``FW_CDEV_IOC_SEND_BROADCAST_REQUEST``\ 
    or \ ``FW_CDEV_IOC_SEND_STREAM_PACKET``\  ioctl

type
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ; always \ ``FW_CDEV_EVENT_RESPONSE``\ 

rcode
    Response code returned by the remote node

length
    Data length, i.e. the response's payload size in bytes

data
    Payload data, if any

.. _`fw_cdev_event_response.description`:

Description
-----------

This event is sent when the stack receives a response to an outgoing request
sent by \ ``FW_CDEV_IOC_SEND_REQUEST``\  ioctl.  The payload data for responses
carrying data (read and lock responses) follows immediately and can be
accessed through the \ ``data``\  field.

The event is also generated after conclusions of transactions that do not
involve response packets.  This includes unified write transactions,
broadcast write transactions, and transmission of asynchronous stream
packets.  \ ``rcode``\  indicates success or failure of such transmissions.

.. _`fw_cdev_event_request`:

struct fw_cdev_event_request
============================

.. c:type:: struct fw_cdev_event_request

    Old version of \ :c:type:`struct fw_cdev_event_request2 <fw_cdev_event_request2>`\ 

.. _`fw_cdev_event_request.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_event_request {
        __u64 closure;
        __u32 type;
        __u32 tcode;
        __u64 offset;
        __u32 handle;
        __u32 length;
        __u32 data;
    }

.. _`fw_cdev_event_request.members`:

Members
-------

closure
    *undescribed*

type
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ; always \ ``FW_CDEV_EVENT_REQUEST``\ 

tcode
    *undescribed*

offset
    *undescribed*

handle
    *undescribed*

length
    *undescribed*

data
    *undescribed*

.. _`fw_cdev_event_request.description`:

Description
-----------

This event is sent instead of \ :c:type:`struct fw_cdev_event_request2 <fw_cdev_event_request2>`\  if the kernel or
the client implements ABI version <= 3.  \ :c:type:`struct fw_cdev_event_request <fw_cdev_event_request>`\  lacks
essential information; use \ :c:type:`struct fw_cdev_event_request2 <fw_cdev_event_request2>`\  instead.

.. _`fw_cdev_event_request2`:

struct fw_cdev_event_request2
=============================

.. c:type:: struct fw_cdev_event_request2

    Sent on incoming request to an address region

.. _`fw_cdev_event_request2.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_event_request2 {
        __u64 closure;
        __u32 type;
        __u32 tcode;
        __u64 offset;
        __u32 source_node_id;
        __u32 destination_node_id;
        __u32 card;
        __u32 generation;
        __u32 handle;
        __u32 length;
        __u32 data;
    }

.. _`fw_cdev_event_request2.members`:

Members
-------

closure
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ; set by \ ``FW_CDEV_IOC_ALLOCATE``\  ioctl

type
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ; always \ ``FW_CDEV_EVENT_REQUEST2``\ 

tcode
    Transaction code of the incoming request

offset
    The offset into the 48-bit per-node address space

source_node_id
    Sender node ID

destination_node_id
    Destination node ID

card
    The index of the card from which the request came

generation
    Bus generation in which the request is valid

handle
    Reference to the kernel-side pending request

length
    Data length, i.e. the request's payload size in bytes

data
    Incoming data, if any

.. _`fw_cdev_event_request2.description`:

Description
-----------

This event is sent when the stack receives an incoming request to an address
region registered using the \ ``FW_CDEV_IOC_ALLOCATE``\  ioctl.  The request is
guaranteed to be completely contained in the specified region.  Userspace is
responsible for sending the response by \ ``FW_CDEV_IOC_SEND_RESPONSE``\  ioctl,
using the same \ ``handle``\ .

The payload data for requests carrying data (write and lock requests)
follows immediately and can be accessed through the \ ``data``\  field.

Unlike \ :c:type:`struct fw_cdev_event_request <fw_cdev_event_request>`\ , \ ``tcode``\  of lock requests is one of the
firewire-core specific \ ``TCODE_LOCK_MASK_SWAP``\ ...%TCODE_LOCK_VENDOR_DEPENDENT,
i.e. encodes the extended transaction code.

\ ``card``\  may differ from \ :c:type:`fw_cdev_get_info.card <fw_cdev_get_info>`\  because requests are received
from all cards of the Linux host.  \ ``source_node_id``\ , \ ``destination_node_id``\ , and
\ ``generation``\  pertain to that card.  Destination node ID and bus generation may
therefore differ from the corresponding fields of the last
\ :c:type:`struct fw_cdev_event_bus_reset <fw_cdev_event_bus_reset>`\ .

\ ``destination_node_id``\  may also differ from the current node ID because of a
non-local bus ID part or in case of a broadcast write request.  Note, a
client must call an \ ``FW_CDEV_IOC_SEND_RESPONSE``\  ioctl even in case of a
broadcast write request; the kernel will then release the kernel-side pending
request but will not actually send a response packet.

In case of a write request to FCP_REQUEST or FCP_RESPONSE, the kernel already
sent a write response immediately after the request was received; in this
case the client must still call an \ ``FW_CDEV_IOC_SEND_RESPONSE``\  ioctl to
release the kernel-side pending request, though another response won't be
sent.

If the client subsequently needs to initiate requests to the sender node of
an \ :c:type:`struct fw_cdev_event_request2 <fw_cdev_event_request2>`\ , it needs to use a device file with matching
card index, node ID, and generation for outbound requests.

.. _`fw_cdev_event_iso_interrupt`:

struct fw_cdev_event_iso_interrupt
==================================

.. c:type:: struct fw_cdev_event_iso_interrupt

    Sent when an iso packet was completed

.. _`fw_cdev_event_iso_interrupt.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_event_iso_interrupt {
        __u64 closure;
        __u32 type;
        __u32 cycle;
        __u32 header_length;
        __u32 header;
    }

.. _`fw_cdev_event_iso_interrupt.members`:

Members
-------

closure
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ;
    set by \ ``FW_CDEV_CREATE_ISO_CONTEXT``\  ioctl

type
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ; always \ ``FW_CDEV_EVENT_ISO_INTERRUPT``\ 

cycle
    Cycle counter of the last completed packet

header_length
    Total length of following headers, in bytes

header
    Stripped headers, if any

.. _`fw_cdev_event_iso_interrupt.description`:

Description
-----------

This event is sent when the controller has completed an \ :c:type:`struct fw_cdev_iso_packet <fw_cdev_iso_packet>`\ 
with the \ ``FW_CDEV_ISO_INTERRUPT``\  bit set, when explicitly requested with
\ ``FW_CDEV_IOC_FLUSH_ISO``\ , or when there have been so many completed packets
without the interrupt bit set that the kernel's internal buffer for \ ``header``\ 
is about to overflow.  (In the last case, ABI versions < 5 drop header data
up to the next interrupt packet.)

Isochronous transmit events (context type \ ``FW_CDEV_ISO_CONTEXT_TRANSMIT``\ ):

In version 3 and some implementations of version 2 of the ABI, \ :c:type:`struct header_length <header_length>`\ 
is a multiple of 4 and \ :c:type:`struct header <header>`\  contains timestamps of all packets up until
the interrupt packet.  The format of the timestamps is as described below for
isochronous reception.  In version 1 of the ABI, \ :c:type:`struct header_length <header_length>`\  was 0.

Isochronous receive events (context type \ ``FW_CDEV_ISO_CONTEXT_RECEIVE``\ ):

The headers stripped of all packets up until and including the interrupt
packet are returned in the \ ``header``\  field.  The amount of header data per
packet is as specified at iso context creation by
\ :c:type:`fw_cdev_create_iso_context.header_size <fw_cdev_create_iso_context>`\ .

Hence, \_interrupt.header_length / \_context.header_size is the number of
packets received in this interrupt event.  The client can now iterate
through the \ :c:func:`mmap`\ 'ed DMA buffer according to this number of packets and
to the buffer sizes as the client specified in \ :c:type:`struct fw_cdev_queue_iso <fw_cdev_queue_iso>`\ .

Since version 2 of this ABI, the portion for each packet in \_interrupt.header
consists of the 1394 isochronous packet header, followed by a timestamp
quadlet if \ :c:type:`fw_cdev_create_iso_context.header_size <fw_cdev_create_iso_context>`\  > 4, followed by quadlets
from the packet payload if \ :c:type:`fw_cdev_create_iso_context.header_size <fw_cdev_create_iso_context>`\  > 8.

.. _`fw_cdev_event_iso_interrupt.format-of-1394-iso-packet-header`:

Format of 1394 iso packet header
--------------------------------

16 bits data_length, 2 bits tag, 6 bits
channel, 4 bits tcode, 4 bits sy, in big endian byte order.
data_length is the actual received size of the packet without the four
1394 iso packet header bytes.

.. _`fw_cdev_event_iso_interrupt.format-of-timestamp`:

Format of timestamp
-------------------

16 bits invalid, 3 bits cycleSeconds, 13 bits
cycleCount, in big endian byte order.

In version 1 of the ABI, no timestamp quadlet was inserted; instead, payload
data followed directly after the 1394 is header if header_size > 4.
Behaviour of ver. 1 of this ABI is no longer available since ABI ver. 2.

.. _`fw_cdev_event_iso_interrupt_mc`:

struct fw_cdev_event_iso_interrupt_mc
=====================================

.. c:type:: struct fw_cdev_event_iso_interrupt_mc

    An iso buffer chunk was completed

.. _`fw_cdev_event_iso_interrupt_mc.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_event_iso_interrupt_mc {
        __u64 closure;
        __u32 type;
        __u32 completed;
    }

.. _`fw_cdev_event_iso_interrupt_mc.members`:

Members
-------

closure
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ;
    set by \ ``FW_CDEV_CREATE_ISO_CONTEXT``\  ioctl

type
    %FW_CDEV_EVENT_ISO_INTERRUPT_MULTICHANNEL

completed
    Offset into the receive buffer; data before this offset is valid

.. _`fw_cdev_event_iso_interrupt_mc.description`:

Description
-----------

This event is sent in multichannel contexts (context type
\ ``FW_CDEV_ISO_CONTEXT_RECEIVE_MULTICHANNEL``\ ) for \ :c:type:`struct fw_cdev_iso_packet <fw_cdev_iso_packet>`\  buffer
chunks that have been completely filled and that have the
\ ``FW_CDEV_ISO_INTERRUPT``\  bit set, or when explicitly requested with
\ ``FW_CDEV_IOC_FLUSH_ISO``\ .

The buffer is continuously filled with the following data, per packet:
- the 1394 iso packet header as described at \ :c:type:`struct fw_cdev_event_iso_interrupt <fw_cdev_event_iso_interrupt>`\ ,
but in little endian byte order,
- packet payload (as many bytes as specified in the data_length field of
the 1394 iso packet header) in big endian byte order,
- 0...3 padding bytes as needed to align the following trailer quadlet,
- trailer quadlet, containing the reception timestamp as described at
\ :c:type:`struct fw_cdev_event_iso_interrupt <fw_cdev_event_iso_interrupt>`\ , but in little endian byte order.

Hence the per-packet size is data_length (rounded up to a multiple of 4) + 8.
When processing the data, stop before a packet that would cross the
\ ``completed``\  offset.

A packet near the end of a buffer chunk will typically spill over into the
next queued buffer chunk.  It is the responsibility of the client to check
for this condition, assemble a broken-up packet from its parts, and not to
re-queue any buffer chunks in which as yet unread packet parts reside.

.. _`fw_cdev_event_iso_resource`:

struct fw_cdev_event_iso_resource
=================================

.. c:type:: struct fw_cdev_event_iso_resource

    Iso resources were allocated or freed

.. _`fw_cdev_event_iso_resource.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_event_iso_resource {
        __u64 closure;
        __u32 type;
        __u32 handle;
        __s32 channel;
        __s32 bandwidth;
    }

.. _`fw_cdev_event_iso_resource.members`:

Members
-------

closure
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ;
    set by \ ``FW_CDEV_IOC_``\ (DE)ALLOCATE_ISO_RESOURCE(_ONCE) ioctl

type
    %FW_CDEV_EVENT_ISO_RESOURCE_ALLOCATED or
    \ ``FW_CDEV_EVENT_ISO_RESOURCE_DEALLOCATED``\ 

handle
    Reference by which an allocated resource can be deallocated

channel
    Isochronous channel which was (de)allocated, if any

bandwidth
    Bandwidth allocation units which were (de)allocated, if any

.. _`fw_cdev_event_iso_resource.description`:

Description
-----------

An \ ``FW_CDEV_EVENT_ISO_RESOURCE_ALLOCATED``\  event is sent after an isochronous
resource was allocated at the IRM.  The client has to check \ ``channel``\  and
\ ``bandwidth``\  for whether the allocation actually succeeded.

An \ ``FW_CDEV_EVENT_ISO_RESOURCE_DEALLOCATED``\  event is sent after an isochronous
resource was deallocated at the IRM.  It is also sent when automatic
reallocation after a bus reset failed.

\ ``channel``\  is <0 if no channel was (de)allocated or if reallocation failed.
\ ``bandwidth``\  is 0 if no bandwidth was (de)allocated or if reallocation failed.

.. _`fw_cdev_event_phy_packet`:

struct fw_cdev_event_phy_packet
===============================

.. c:type:: struct fw_cdev_event_phy_packet

    A PHY packet was transmitted or received

.. _`fw_cdev_event_phy_packet.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_event_phy_packet {
        __u64 closure;
        __u32 type;
        __u32 rcode;
        __u32 length;
        __u32 data;
    }

.. _`fw_cdev_event_phy_packet.members`:

Members
-------

closure
    See \ :c:type:`struct fw_cdev_event_common <fw_cdev_event_common>`\ ; set by \ ``FW_CDEV_IOC_SEND_PHY_PACKET``\ 
    or \ ``FW_CDEV_IOC_RECEIVE_PHY_PACKETS``\  ioctl

type
    %FW_CDEV_EVENT_PHY_PACKET_SENT or %..._RECEIVED

rcode
    %RCODE_..., indicates success or failure of transmission

length
    Data length in bytes

data
    Incoming data

.. _`fw_cdev_event_phy_packet.description`:

Description
-----------

If \ ``type``\  is \ ``FW_CDEV_EVENT_PHY_PACKET_SENT``\ , \ ``length``\  is 0 and \ ``data``\  empty,

.. _`fw_cdev_event_phy_packet.except-in-case-of-a-ping-packet`:

except in case of a ping packet
-------------------------------

Then, \ ``length``\  is 4, and \ ``data``\ [0] is the
ping time in 49.152MHz clocks if \ ``rcode``\  is \ ``RCODE_COMPLETE``\ .

If \ ``type``\  is \ ``FW_CDEV_EVENT_PHY_PACKET_RECEIVED``\ , \ ``length``\  is 8 and \ ``data``\ 
consists of the two PHY packet quadlets, in host byte order.

.. _`fw_cdev_event`:

union fw_cdev_event
===================

.. c:type:: struct fw_cdev_event

    Convenience union of fw_cdev_event\_ types

.. _`fw_cdev_event.definition`:

Definition
----------

.. code-block:: c

    union fw_cdev_event {
        struct fw_cdev_event_common common;
        struct fw_cdev_event_bus_reset bus_reset;
        struct fw_cdev_event_response response;
        struct fw_cdev_event_request request;
        struct fw_cdev_event_request2 request2;
        struct fw_cdev_event_iso_interrupt iso_interrupt;
        struct fw_cdev_event_iso_interrupt_mc iso_interrupt_mc;
        struct fw_cdev_event_iso_resource iso_resource;
        struct fw_cdev_event_phy_packet phy_packet;
    }

.. _`fw_cdev_event.members`:

Members
-------

common
    Valid for all types

bus_reset
    Valid if \ ``common``\ .type == \ ``FW_CDEV_EVENT_BUS_RESET``\ 

response
    Valid if \ ``common``\ .type == \ ``FW_CDEV_EVENT_RESPONSE``\ 

request
    Valid if \ ``common``\ .type == \ ``FW_CDEV_EVENT_REQUEST``\ 

request2
    Valid if \ ``common``\ .type == \ ``FW_CDEV_EVENT_REQUEST2``\ 

iso_interrupt
    Valid if \ ``common``\ .type == \ ``FW_CDEV_EVENT_ISO_INTERRUPT``\ 

iso_interrupt_mc
    Valid if \ ``common``\ .type ==
    \ ``FW_CDEV_EVENT_ISO_INTERRUPT_MULTICHANNEL``\ 

iso_resource
    Valid if \ ``common``\ .type ==
    \ ``FW_CDEV_EVENT_ISO_RESOURCE_ALLOCATED``\  or
    \ ``FW_CDEV_EVENT_ISO_RESOURCE_DEALLOCATED``\ 

phy_packet
    Valid if \ ``common``\ .type ==
    \ ``FW_CDEV_EVENT_PHY_PACKET_SENT``\  or
    \ ``FW_CDEV_EVENT_PHY_PACKET_RECEIVED``\ 

.. _`fw_cdev_event.description`:

Description
-----------

Convenience union for userspace use.  Events could be read(2) into an
appropriately aligned char buffer and then cast to this union for further
processing.  Note that for a request, response or iso_interrupt event,
the data[] or header[] may make the size of the full event larger than
sizeof(union fw_cdev_event).  Also note that if you attempt to read(2)
an event into a buffer that is not large enough for it, the data that does
not fit will be discarded so that the next read(2) will return a new event.

.. _`fw_cdev_get_info`:

struct fw_cdev_get_info
=======================

.. c:type:: struct fw_cdev_get_info

    General purpose information ioctl

.. _`fw_cdev_get_info.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_get_info {
        __u32 version;
        __u32 rom_length;
        __u64 rom;
        __u64 bus_reset;
        __u64 bus_reset_closure;
        __u32 card;
    }

.. _`fw_cdev_get_info.members`:

Members
-------

version
    The version field is just a running serial number.  Both an
    input parameter (ABI version implemented by the client) and
    output parameter (ABI version implemented by the kernel).
    A client shall fill in the ABI \ ``version``\  for which the client
    was implemented.  This is necessary for forward compatibility.

rom_length
    If \ ``rom``\  is non-zero, up to \ ``rom_length``\  bytes of Configuration
    ROM will be copied into that user space address.  In either
    case, \ ``rom_length``\  is updated with the actual length of the
    Configuration ROM.

rom
    If non-zero, address of a buffer to be filled by a copy of the
    device's Configuration ROM

bus_reset
    If non-zero, address of a buffer to be filled by a
    \ :c:type:`struct fw_cdev_event_bus_reset <fw_cdev_event_bus_reset>`\  with the current state
    of the bus.  This does not cause a bus reset to happen.

bus_reset_closure
    Value of \ :c:type:`struct closure <closure>`\  in this and subsequent bus reset events

card
    The index of the card this device belongs to

.. _`fw_cdev_get_info.description`:

Description
-----------

The \ ``FW_CDEV_IOC_GET_INFO``\  ioctl is usually the very first one which a client
performs right after it opened a /dev/fw\* file.

As a side effect, reception of \ ``FW_CDEV_EVENT_BUS_RESET``\  events to be read(2)
is started by this ioctl.

.. _`fw_cdev_send_request`:

struct fw_cdev_send_request
===========================

.. c:type:: struct fw_cdev_send_request

    Send an asynchronous request packet

.. _`fw_cdev_send_request.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_send_request {
        __u32 tcode;
        __u32 length;
        __u64 offset;
        __u64 closure;
        __u64 data;
        __u32 generation;
    }

.. _`fw_cdev_send_request.members`:

Members
-------

tcode
    Transaction code of the request

length
    Length of outgoing payload, in bytes

offset
    48-bit offset at destination node

closure
    Passed back to userspace in the response event

data
    Userspace pointer to payload

generation
    The bus generation where packet is valid

.. _`fw_cdev_send_request.description`:

Description
-----------

Send a request to the device.  This ioctl implements all outgoing requests.
Both quadlet and block request specify the payload as a pointer to the data
in the \ ``data``\  field.  Once the transaction completes, the kernel writes an
\ :c:type:`struct fw_cdev_event_response <fw_cdev_event_response>`\  event back.  The \ ``closure``\  field is passed back to
user space in the response event.

.. _`fw_cdev_send_response`:

struct fw_cdev_send_response
============================

.. c:type:: struct fw_cdev_send_response

    Send an asynchronous response packet

.. _`fw_cdev_send_response.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_send_response {
        __u32 rcode;
        __u32 length;
        __u64 data;
        __u32 handle;
    }

.. _`fw_cdev_send_response.members`:

Members
-------

rcode
    Response code as determined by the userspace handler

length
    Length of outgoing payload, in bytes

data
    Userspace pointer to payload

handle
    The handle from the \ :c:type:`struct fw_cdev_event_request <fw_cdev_event_request>`\ 

.. _`fw_cdev_send_response.description`:

Description
-----------

Send a response to an incoming request.  By setting up an address range using
the \ ``FW_CDEV_IOC_ALLOCATE``\  ioctl, userspace can listen for incoming requests.  An
incoming request will generate an \ ``FW_CDEV_EVENT_REQUEST``\ , and userspace must
send a reply using this ioctl.  The event has a handle to the kernel-side
pending transaction, which should be used with this ioctl.

.. _`fw_cdev_allocate`:

struct fw_cdev_allocate
=======================

.. c:type:: struct fw_cdev_allocate

    Allocate a CSR in an address range

.. _`fw_cdev_allocate.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_allocate {
        __u64 offset;
        __u64 closure;
        __u32 length;
        __u32 handle;
        __u64 region_end;
    }

.. _`fw_cdev_allocate.members`:

Members
-------

offset
    Start offset of the address range

closure
    To be passed back to userspace in request events

length
    Length of the CSR, in bytes

handle
    Handle to the allocation, written by the kernel

region_end
    First address above the address range (added in ABI v4, 2.6.36)

.. _`fw_cdev_allocate.description`:

Description
-----------

Allocate an address range in the 48-bit address space on the local node
(the controller).  This allows userspace to listen for requests with an
offset within that address range.  Every time when the kernel receives a
request within the range, an \ :c:type:`struct fw_cdev_event_request2 <fw_cdev_event_request2>`\  event will be emitted.
(If the kernel or the client implements ABI version <= 3, an
\ :c:type:`struct fw_cdev_event_request <fw_cdev_event_request>`\  will be generated instead.)

The \ ``closure``\  field is passed back to userspace in these request events.
The \ ``handle``\  field is an out parameter, returning a handle to the allocated
range to be used for later deallocation of the range.

The address range is allocated on all local nodes.  The address allocation
is exclusive except for the FCP command and response registers.  If an
exclusive address region is already in use, the ioctl fails with errno set
to \ ``EBUSY``\ .

If kernel and client implement ABI version >= 4, the kernel looks up a free
spot of size \ ``length``\  inside [@offset..@region_end) and, if found, writes
the start address of the new CSR back in \ ``offset``\ .  I.e. \ ``offset``\  is an
in and out parameter.  If this automatic placement of a CSR in a bigger
address range is not desired, the client simply needs to set \ ``region_end``\ 
= \ ``offset``\  + \ ``length``\ .

If the kernel or the client implements ABI version <= 3, \ ``region_end``\  is
ignored and effectively assumed to be \ ``offset``\  + \ ``length``\ .

\ ``region_end``\  is only present in a kernel header >= 2.6.36.  If necessary,
this can for example be tested by #ifdef FW_CDEV_EVENT_REQUEST2.

.. _`fw_cdev_deallocate`:

struct fw_cdev_deallocate
=========================

.. c:type:: struct fw_cdev_deallocate

    Free a CSR address range or isochronous resource

.. _`fw_cdev_deallocate.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_deallocate {
        __u32 handle;
    }

.. _`fw_cdev_deallocate.members`:

Members
-------

handle
    Handle to the address range or iso resource, as returned by the
    kernel when the range or resource was allocated

.. _`fw_cdev_initiate_bus_reset`:

struct fw_cdev_initiate_bus_reset
=================================

.. c:type:: struct fw_cdev_initiate_bus_reset

    Initiate a bus reset

.. _`fw_cdev_initiate_bus_reset.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_initiate_bus_reset {
        __u32 type;
    }

.. _`fw_cdev_initiate_bus_reset.members`:

Members
-------

type
    %FW_CDEV_SHORT_RESET or \ ``FW_CDEV_LONG_RESET``\ 

.. _`fw_cdev_initiate_bus_reset.description`:

Description
-----------

Initiate a bus reset for the bus this device is on.  The bus reset can be
either the original (long) bus reset or the arbitrated (short) bus reset
introduced in 1394a-2000.

The ioctl returns immediately.  A subsequent \ :c:type:`struct fw_cdev_event_bus_reset <fw_cdev_event_bus_reset>`\ 
indicates when the reset actually happened.  Since ABI v4, this may be
considerably later than the ioctl because the kernel ensures a grace period
between subsequent bus resets as per IEEE 1394 bus management specification.

.. _`fw_cdev_add_descriptor`:

struct fw_cdev_add_descriptor
=============================

.. c:type:: struct fw_cdev_add_descriptor

    Add contents to the local node's config ROM

.. _`fw_cdev_add_descriptor.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_add_descriptor {
        __u32 immediate;
        __u32 key;
        __u64 data;
        __u32 length;
        __u32 handle;
    }

.. _`fw_cdev_add_descriptor.members`:

Members
-------

immediate
    If non-zero, immediate key to insert before pointer

key
    Upper 8 bits of root directory pointer

data
    Userspace pointer to contents of descriptor block

length
    Length of descriptor block data, in quadlets

handle
    Handle to the descriptor, written by the kernel

.. _`fw_cdev_add_descriptor.description`:

Description
-----------

Add a descriptor block and optionally a preceding immediate key to the local
node's Configuration ROM.

The \ ``key``\  field specifies the upper 8 bits of the descriptor root directory
pointer and the \ ``data``\  and \ ``length``\  fields specify the contents. The \ ``key``\ 
should be of the form 0xXX000000. The offset part of the root directory entry
will be filled in by the kernel.

If not 0, the \ ``immediate``\  field specifies an immediate key which will be
inserted before the root directory pointer.

\ ``immediate``\ , \ ``key``\ , and \ ``data``\  array elements are CPU-endian quadlets.

If successful, the kernel adds the descriptor and writes back a \ ``handle``\  to
the kernel-side object to be used for later removal of the descriptor block
and immediate key.  The kernel will also generate a bus reset to signal the
change of the Configuration ROM to other nodes.

This ioctl affects the Configuration ROMs of all local nodes.
The ioctl only succeeds on device files which represent a local node.

.. _`fw_cdev_remove_descriptor`:

struct fw_cdev_remove_descriptor
================================

.. c:type:: struct fw_cdev_remove_descriptor

    Remove contents from the Configuration ROM

.. _`fw_cdev_remove_descriptor.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_remove_descriptor {
        __u32 handle;
    }

.. _`fw_cdev_remove_descriptor.members`:

Members
-------

handle
    Handle to the descriptor, as returned by the kernel when the
    descriptor was added

.. _`fw_cdev_remove_descriptor.description`:

Description
-----------

Remove a descriptor block and accompanying immediate key from the local
nodes' Configuration ROMs.  The kernel will also generate a bus reset to
signal the change of the Configuration ROM to other nodes.

.. _`fw_cdev_create_iso_context`:

struct fw_cdev_create_iso_context
=================================

.. c:type:: struct fw_cdev_create_iso_context

    Create a context for isochronous I/O

.. _`fw_cdev_create_iso_context.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_create_iso_context {
        __u32 type;
        __u32 header_size;
        __u32 channel;
        __u32 speed;
        __u64 closure;
        __u32 handle;
    }

.. _`fw_cdev_create_iso_context.members`:

Members
-------

type
    %FW_CDEV_ISO_CONTEXT_TRANSMIT or \ ``FW_CDEV_ISO_CONTEXT_RECEIVE``\  or
    \ ``FW_CDEV_ISO_CONTEXT_RECEIVE_MULTICHANNEL``\ 

header_size
    Header size to strip in single-channel reception

channel
    Channel to bind to in single-channel reception or transmission

speed
    Transmission speed

closure
    To be returned in \ :c:type:`struct fw_cdev_event_iso_interrupt <fw_cdev_event_iso_interrupt>`\  or
    \ :c:type:`struct fw_cdev_event_iso_interrupt_multichannel <fw_cdev_event_iso_interrupt_multichannel>`\ 

handle
    Handle to context, written back by kernel

.. _`fw_cdev_create_iso_context.description`:

Description
-----------

Prior to sending or receiving isochronous I/O, a context must be created.
The context records information about the transmit or receive configuration
and typically maps to an underlying hardware resource.  A context is set up
for either sending or receiving.  It is bound to a specific isochronous
\ ``channel``\ .

In case of multichannel reception, \ ``header_size``\  and \ ``channel``\  are ignored
and the channels are selected by \ ``FW_CDEV_IOC_SET_ISO_CHANNELS``\ .

For \ ``FW_CDEV_ISO_CONTEXT_RECEIVE``\  contexts, \ ``header_size``\  must be at least 4
and must be a multiple of 4.  It is ignored in other context types.

\ ``speed``\  is ignored in receive context types.

If a context was successfully created, the kernel writes back a handle to the
context, which must be passed in for subsequent operations on that context.

.. _`fw_cdev_create_iso_context.limitations`:

Limitations
-----------

No more than one iso context can be created per fd.
The total number of contexts that all userspace and kernelspace drivers can
create on a card at a time is a hardware limit, typically 4 or 8 contexts per
direction, and of them at most one multichannel receive context.

.. _`fw_cdev_set_iso_channels`:

struct fw_cdev_set_iso_channels
===============================

.. c:type:: struct fw_cdev_set_iso_channels

    Select channels in multichannel reception

.. _`fw_cdev_set_iso_channels.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_set_iso_channels {
        __u64 channels;
        __u32 handle;
    }

.. _`fw_cdev_set_iso_channels.members`:

Members
-------

channels
    Bitmask of channels to listen to

handle
    Handle of the mutichannel receive context

.. _`fw_cdev_set_iso_channels.description`:

Description
-----------

@channels is the bitwise or of 1ULL << n for each channel n to listen to.

The ioctl fails with errno \ ``EBUSY``\  if there is already another receive context
on a channel in \ ``channels``\ .  In that case, the bitmask of all unoccupied
channels is returned in \ ``channels``\ .

.. _`fw_cdev_iso_packet`:

struct fw_cdev_iso_packet
=========================

.. c:type:: struct fw_cdev_iso_packet

    Isochronous packet

.. _`fw_cdev_iso_packet.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_iso_packet {
        __u32 control;
        __u32 header;
    }

.. _`fw_cdev_iso_packet.members`:

Members
-------

control
    Contains the header length (8 uppermost bits),
    the sy field (4 bits), the tag field (2 bits), a sync flag
    or a skip flag (1 bit), an interrupt flag (1 bit), and the
    payload length (16 lowermost bits)

header
    Header and payload in case of a transmit context.

.. _`fw_cdev_iso_packet.description`:

Description
-----------

&struct fw_cdev_iso_packet is used to describe isochronous packet queues.
Use the FW_CDEV_ISO\_ macros to fill in \ ``control``\ .
The \ ``header``\  array is empty in case of receive contexts.

Context type \ ``FW_CDEV_ISO_CONTEXT_TRANSMIT``\ :

\ ``control``\ .HEADER_LENGTH must be a multiple of 4.  It specifies the numbers of
bytes in \ ``header``\  that will be prepended to the packet's payload.  These bytes
are copied into the kernel and will not be accessed after the ioctl has
returned.

The \ ``control``\ .SY and TAG fields are copied to the iso packet header.  These
fields are specified by IEEE 1394a and IEC 61883-1.

The \ ``control``\ .SKIP flag specifies that no packet is to be sent in a frame.
When using this, all other fields except \ ``control``\ .INTERRUPT must be zero.

When a packet with the \ ``control``\ .INTERRUPT flag set has been completed, an
\ :c:type:`struct fw_cdev_event_iso_interrupt <fw_cdev_event_iso_interrupt>`\  event will be sent.

Context type \ ``FW_CDEV_ISO_CONTEXT_RECEIVE``\ :

\ ``control``\ .HEADER_LENGTH must be a multiple of the context's header_size.
If the HEADER_LENGTH is larger than the context's header_size, multiple
packets are queued for this entry.

The \ ``control``\ .SY and TAG fields are ignored.

If the \ ``control``\ .SYNC flag is set, the context drops all packets until a
packet with a sy field is received which matches \ :c:type:`fw_cdev_start_iso.sync <fw_cdev_start_iso>`\ .

\ ``control``\ .PAYLOAD_LENGTH defines how many payload bytes can be received for
one packet (in addition to payload quadlets that have been defined as headers
and are stripped and returned in the \ :c:type:`struct fw_cdev_event_iso_interrupt <fw_cdev_event_iso_interrupt>`\  structure).
If more bytes are received, the additional bytes are dropped.  If less bytes
are received, the remaining bytes in this part of the payload buffer will not
be written to, not even by the next packet.  I.e., packets received in
consecutive frames will not necessarily be consecutive in memory.  If an
entry has queued multiple packets, the PAYLOAD_LENGTH is divided equally
among them.

When a packet with the \ ``control``\ .INTERRUPT flag set has been completed, an
\ :c:type:`struct fw_cdev_event_iso_interrupt <fw_cdev_event_iso_interrupt>`\  event will be sent.  An entry that has queued
multiple receive packets is completed when its last packet is completed.

Context type \ ``FW_CDEV_ISO_CONTEXT_RECEIVE_MULTICHANNEL``\ :

Here, \ :c:type:`struct fw_cdev_iso_packet <fw_cdev_iso_packet>`\  would be more aptly named \_iso_buffer_chunk since
it specifies a chunk of the \ :c:func:`mmap`\ 'ed buffer, while the number and alignment
of packets to be placed into the buffer chunk is not known beforehand.

\ ``control``\ .PAYLOAD_LENGTH is the size of the buffer chunk and specifies room
for header, payload, padding, and trailer bytes of one or more packets.
It must be a multiple of 4.

\ ``control``\ .HEADER_LENGTH, TAG and SY are ignored.  SYNC is treated as described
for single-channel reception.

When a buffer chunk with the \ ``control``\ .INTERRUPT flag set has been filled
entirely, an \ :c:type:`struct fw_cdev_event_iso_interrupt_mc <fw_cdev_event_iso_interrupt_mc>`\  event will be sent.

.. _`fw_cdev_queue_iso`:

struct fw_cdev_queue_iso
========================

.. c:type:: struct fw_cdev_queue_iso

    Queue isochronous packets for I/O

.. _`fw_cdev_queue_iso.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_queue_iso {
        __u64 packets;
        __u64 data;
        __u32 size;
        __u32 handle;
    }

.. _`fw_cdev_queue_iso.members`:

Members
-------

packets
    Userspace pointer to an array of \ :c:type:`struct fw_cdev_iso_packet <fw_cdev_iso_packet>`\ 

data
    Pointer into \ :c:func:`mmap`\ 'ed payload buffer

size
    Size of the \ ``packets``\  array, in bytes

handle
    Isochronous context handle

.. _`fw_cdev_queue_iso.description`:

Description
-----------

Queue a number of isochronous packets for reception or transmission.
This ioctl takes a pointer to an array of \ :c:type:`struct fw_cdev_iso_packet <fw_cdev_iso_packet>`\  structs,
which describe how to transmit from or receive into a contiguous region
of a \ :c:func:`mmap`\ 'ed payload buffer.  As part of transmit packet descriptors,
a series of headers can be supplied, which will be prepended to the
payload during DMA.

The kernel may or may not queue all packets, but will write back updated
values of the \ ``packets``\ , \ ``data``\  and \ ``size``\  fields, so the ioctl can be
resubmitted easily.

In case of a multichannel receive context, \ ``data``\  must be quadlet-aligned
relative to the buffer start.

.. _`fw_cdev_start_iso`:

struct fw_cdev_start_iso
========================

.. c:type:: struct fw_cdev_start_iso

    Start an isochronous transmission or reception

.. _`fw_cdev_start_iso.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_start_iso {
        __s32 cycle;
        __u32 sync;
        __u32 tags;
        __u32 handle;
    }

.. _`fw_cdev_start_iso.members`:

Members
-------

cycle
    Cycle in which to start I/O.  If \ ``cycle``\  is greater than or
    equal to 0, the I/O will start on that cycle.

sync
    Determines the value to wait for for receive packets that have
    the \ ``FW_CDEV_ISO_SYNC``\  bit set

tags
    Tag filter bit mask.  Only valid for isochronous reception.
    Determines the tag values for which packets will be accepted.
    Use FW_CDEV_ISO_CONTEXT_MATCH\_ macros to set \ ``tags``\ .

handle
    Isochronous context handle within which to transmit or receive

.. _`fw_cdev_stop_iso`:

struct fw_cdev_stop_iso
=======================

.. c:type:: struct fw_cdev_stop_iso

    Stop an isochronous transmission or reception

.. _`fw_cdev_stop_iso.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_stop_iso {
        __u32 handle;
    }

.. _`fw_cdev_stop_iso.members`:

Members
-------

handle
    Handle of isochronous context to stop

.. _`fw_cdev_flush_iso`:

struct fw_cdev_flush_iso
========================

.. c:type:: struct fw_cdev_flush_iso

    flush completed iso packets

.. _`fw_cdev_flush_iso.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_flush_iso {
        __u32 handle;
    }

.. _`fw_cdev_flush_iso.members`:

Members
-------

handle
    handle of isochronous context to flush

.. _`fw_cdev_flush_iso.description`:

Description
-----------

For \ ``FW_CDEV_ISO_CONTEXT_TRANSMIT``\  or \ ``FW_CDEV_ISO_CONTEXT_RECEIVE``\  contexts,
report any completed packets.

For \ ``FW_CDEV_ISO_CONTEXT_RECEIVE_MULTICHANNEL``\  contexts, report the current
offset in the receive buffer, if it has changed; this is typically in the
middle of some buffer chunk.

Any \ ``FW_CDEV_EVENT_ISO_INTERRUPT``\  or \ ``FW_CDEV_EVENT_ISO_INTERRUPT_MULTICHANNEL``\ 
events generated by this ioctl are sent synchronously, i.e., are available
for reading from the file descriptor when this ioctl returns.

.. _`fw_cdev_get_cycle_timer`:

struct fw_cdev_get_cycle_timer
==============================

.. c:type:: struct fw_cdev_get_cycle_timer

    read cycle timer register

.. _`fw_cdev_get_cycle_timer.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_get_cycle_timer {
        __u64 local_time;
        __u32 cycle_timer;
    }

.. _`fw_cdev_get_cycle_timer.members`:

Members
-------

local_time
    system time, in microseconds since the Epoch

cycle_timer
    Cycle Time register contents

.. _`fw_cdev_get_cycle_timer.description`:

Description
-----------

Same as \ ``FW_CDEV_IOC_GET_CYCLE_TIMER2``\ , but fixed to use \ ``CLOCK_REALTIME``\ 
and only with microseconds resolution.

In version 1 and 2 of the ABI, this ioctl returned unreliable (non-
monotonic) \ ``cycle_timer``\  values on certain controllers.

.. _`fw_cdev_get_cycle_timer2`:

struct fw_cdev_get_cycle_timer2
===============================

.. c:type:: struct fw_cdev_get_cycle_timer2

    read cycle timer register

.. _`fw_cdev_get_cycle_timer2.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_get_cycle_timer2 {
        __s64 tv_sec;
        __s32 tv_nsec;
        __s32 clk_id;
        __u32 cycle_timer;
    }

.. _`fw_cdev_get_cycle_timer2.members`:

Members
-------

tv_sec
    system time, seconds

tv_nsec
    system time, sub-seconds part in nanoseconds

clk_id
    input parameter, clock from which to get the system time

cycle_timer
    Cycle Time register contents

.. _`fw_cdev_get_cycle_timer2.description`:

Description
-----------

The \ ``FW_CDEV_IOC_GET_CYCLE_TIMER2``\  ioctl reads the isochronous cycle timer
and also the system clock.  This allows to correlate reception time of
isochronous packets with system time.

\ ``clk_id``\  lets you choose a clock like with POSIX' clock_gettime function.
Supported \ ``clk_id``\  values are POSIX' \ ``CLOCK_REALTIME``\  and \ ``CLOCK_MONOTONIC``\ 
and Linux' \ ``CLOCK_MONOTONIC_RAW``\ .

\ ``cycle_timer``\  consists of 7 bits cycleSeconds, 13 bits cycleCount, and
12 bits cycleOffset, in host byte order.  Cf. the Cycle Time register
per IEEE 1394 or Isochronous Cycle Timer register per OHCI-1394.

.. _`fw_cdev_allocate_iso_resource`:

struct fw_cdev_allocate_iso_resource
====================================

.. c:type:: struct fw_cdev_allocate_iso_resource

    (De)allocate a channel or bandwidth

.. _`fw_cdev_allocate_iso_resource.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_allocate_iso_resource {
        __u64 closure;
        __u64 channels;
        __u32 bandwidth;
        __u32 handle;
    }

.. _`fw_cdev_allocate_iso_resource.members`:

Members
-------

closure
    Passed back to userspace in corresponding iso resource events

channels
    Isochronous channels of which one is to be (de)allocated

bandwidth
    Isochronous bandwidth units to be (de)allocated

handle
    Handle to the allocation, written by the kernel (only valid in
    case of \ ``FW_CDEV_IOC_ALLOCATE_ISO_RESOURCE``\  ioctls)

.. _`fw_cdev_allocate_iso_resource.description`:

Description
-----------

The \ ``FW_CDEV_IOC_ALLOCATE_ISO_RESOURCE``\  ioctl initiates allocation of an
isochronous channel and/or of isochronous bandwidth at the isochronous
resource manager (IRM).  Only one of the channels specified in \ ``channels``\  is
allocated.  An \ ``FW_CDEV_EVENT_ISO_RESOURCE_ALLOCATED``\  is sent after
communication with the IRM, indicating success or failure in the event data.
The kernel will automatically reallocate the resources after bus resets.
Should a reallocation fail, an \ ``FW_CDEV_EVENT_ISO_RESOURCE_DEALLOCATED``\  event
will be sent.  The kernel will also automatically deallocate the resources
when the file descriptor is closed.

The \ ``FW_CDEV_IOC_DEALLOCATE_ISO_RESOURCE``\  ioctl can be used to initiate
deallocation of resources which were allocated as described above.
An \ ``FW_CDEV_EVENT_ISO_RESOURCE_DEALLOCATED``\  event concludes this operation.

The \ ``FW_CDEV_IOC_ALLOCATE_ISO_RESOURCE_ONCE``\  ioctl is a variant of allocation
without automatic re- or deallocation.
An \ ``FW_CDEV_EVENT_ISO_RESOURCE_ALLOCATED``\  event concludes this operation,
indicating success or failure in its data.

The \ ``FW_CDEV_IOC_DEALLOCATE_ISO_RESOURCE_ONCE``\  ioctl works like
\ ``FW_CDEV_IOC_ALLOCATE_ISO_RESOURCE_ONCE``\  except that resources are freed
instead of allocated.
An \ ``FW_CDEV_EVENT_ISO_RESOURCE_DEALLOCATED``\  event concludes this operation.

To summarize, \ ``FW_CDEV_IOC_ALLOCATE_ISO_RESOURCE``\  allocates iso resources
for the lifetime of the fd or \ ``handle``\ .
In contrast, \ ``FW_CDEV_IOC_ALLOCATE_ISO_RESOURCE_ONCE``\  allocates iso resources
for the duration of a bus generation.

\ ``channels``\  is a host-endian bitfield with the least significant bit

.. _`fw_cdev_allocate_iso_resource.representing-channel-0-and-the-most-significant-bit-representing-channel-63`:

representing channel 0 and the most significant bit representing channel 63
---------------------------------------------------------------------------

1ULL << c for each channel c that is a candidate for (de)allocation.

\ ``bandwidth``\  is expressed in bandwidth allocation units, i.e. the time to send
one quadlet of data (payload or header data) at speed S1600.

.. _`fw_cdev_send_stream_packet`:

struct fw_cdev_send_stream_packet
=================================

.. c:type:: struct fw_cdev_send_stream_packet

    send an asynchronous stream packet

.. _`fw_cdev_send_stream_packet.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_send_stream_packet {
        __u32 length;
        __u32 tag;
        __u32 channel;
        __u32 sy;
        __u64 closure;
        __u64 data;
        __u32 generation;
        __u32 speed;
    }

.. _`fw_cdev_send_stream_packet.members`:

Members
-------

length
    Length of outgoing payload, in bytes

tag
    Data format tag

channel
    Isochronous channel to transmit to

sy
    Synchronization code

closure
    Passed back to userspace in the response event

data
    Userspace pointer to payload

generation
    The bus generation where packet is valid

speed
    Speed to transmit at

.. _`fw_cdev_send_stream_packet.description`:

Description
-----------

The \ ``FW_CDEV_IOC_SEND_STREAM_PACKET``\  ioctl sends an asynchronous stream packet
to every device which is listening to the specified channel.  The kernel
writes an \ :c:type:`struct fw_cdev_event_response <fw_cdev_event_response>`\  event which indicates success or failure of
the transmission.

.. _`fw_cdev_send_phy_packet`:

struct fw_cdev_send_phy_packet
==============================

.. c:type:: struct fw_cdev_send_phy_packet

    send a PHY packet

.. _`fw_cdev_send_phy_packet.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_send_phy_packet {
        __u64 closure;
        __u32 data;
        __u32 generation;
    }

.. _`fw_cdev_send_phy_packet.members`:

Members
-------

closure
    Passed back to userspace in the PHY-packet-sent event

data
    First and second quadlet of the PHY packet

generation
    The bus generation where packet is valid

.. _`fw_cdev_send_phy_packet.description`:

Description
-----------

The \ ``FW_CDEV_IOC_SEND_PHY_PACKET``\  ioctl sends a PHY packet to all nodes
on the same card as this device.  After transmission, an
\ ``FW_CDEV_EVENT_PHY_PACKET_SENT``\  event is generated.

The payload \ ``data``\ [] shall be specified in host byte order.  Usually,
\ ``data``\ [1] needs to be the bitwise inverse of \ ``data``\ [0].  VersaPHY packets
are an exception to this rule.

The ioctl is only permitted on device files which represent a local node.

.. _`fw_cdev_receive_phy_packets`:

struct fw_cdev_receive_phy_packets
==================================

.. c:type:: struct fw_cdev_receive_phy_packets

    start reception of PHY packets

.. _`fw_cdev_receive_phy_packets.definition`:

Definition
----------

.. code-block:: c

    struct fw_cdev_receive_phy_packets {
        __u64 closure;
    }

.. _`fw_cdev_receive_phy_packets.members`:

Members
-------

closure
    Passed back to userspace in phy packet events

.. _`fw_cdev_receive_phy_packets.description`:

Description
-----------

This ioctl activates issuing of \ ``FW_CDEV_EVENT_PHY_PACKET_RECEIVED``\  due to
incoming PHY packets from any node on the same bus as the device.

The ioctl is only permitted on device files which represent a local node.

.. This file was automatic generated / don't edit.

