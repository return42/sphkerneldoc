.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/scif.h

.. _`scif_range`:

struct scif_range
=================

.. c:type:: struct scif_range

    SCIF registered range used in kernel mode

.. _`scif_range.definition`:

Definition
----------

.. code-block:: c

    struct scif_range {
        void *cookie;
        int nr_pages;
        int prot_flags;
        dma_addr_t *phys_addr;
        void __iomem **va;
    }

.. _`scif_range.members`:

Members
-------

cookie
    cookie used internally by SCIF

nr_pages
    number of pages of PAGE_SIZE

prot_flags
    R/W protection

phys_addr
    Array of bus addresses

va
    Array of kernel virtual addresses backed by the pages in the phys_addr
    array. The va is populated only when called on the host for a remote
    SCIF connection on MIC. This is required to support the use case of DMA
    between MIC and another device which is not a SCIF node e.g., an IB or
    ethernet NIC.

.. _`scif_pollepd`:

struct scif_pollepd
===================

.. c:type:: struct scif_pollepd

    SCIF endpoint to be monitored via scif_poll

.. _`scif_pollepd.definition`:

Definition
----------

.. code-block:: c

    struct scif_pollepd {
        scif_epd_t epd;
        __poll_t events;
        __poll_t revents;
    }

.. _`scif_pollepd.members`:

Members
-------

epd
    SCIF endpoint

events
    requested events

revents
    returned events

.. _`scif_open`:

scif_open
=========

.. c:function:: scif_epd_t scif_open( void)

    Create an endpoint

    :param void:
        no arguments
    :type void: 

.. _`scif_open.return`:

Return
------

Upon successful completion, \ :c:func:`scif_open`\  returns an endpoint descriptor to
be used in subsequent SCIF functions calls to refer to that endpoint;
otherwise in user mode SCIF_OPEN_FAILED (that is ((scif_epd_t)-1)) is
returned and errno is set to indicate the error; in kernel mode a NULL
scif_epd_t is returned.

.. _`scif_open.errors`:

Errors
------

ENOMEM - Insufficient kernel memory was available

.. _`scif_bind`:

scif_bind
=========

.. c:function:: int scif_bind(scif_epd_t epd, u16 pn)

    Bind an endpoint to a port

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param pn:
        port number
    :type pn: u16

.. _`scif_bind.description`:

Description
-----------

\ :c:func:`scif_bind`\  binds endpoint epd to port pn, where pn is a port number on the
local node. If pn is zero, a port number greater than or equal to
SCIF_PORT_RSVD is assigned and returned. Each endpoint may be bound to
exactly one local port. Ports less than 1024 when requested can only be bound
by system (or root) processes or by processes executed by privileged users.

.. _`scif_bind.return`:

Return
------

Upon successful completion, \ :c:func:`scif_bind`\  returns the port number to which epd
is bound; otherwise in user mode -1 is returned and errno is set to
indicate the error; in kernel mode the negative of one of the following
errors is returned.

.. _`scif_bind.errors`:

Errors
------

EBADF, ENOTTY - epd is not a valid endpoint descriptor
EINVAL - the endpoint or the port is already bound
EISCONN - The endpoint is already connected
ENOSPC - No port number available for assignment
EACCES - The port requested is protected and the user is not the superuser

.. _`scif_listen`:

scif_listen
===========

.. c:function:: int scif_listen(scif_epd_t epd, int backlog)

    Listen for connections on an endpoint

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param backlog:
        maximum pending connection requests
    :type backlog: int

.. _`scif_listen.description`:

Description
-----------

\ :c:func:`scif_listen`\  marks the endpoint epd as a listening endpoint - that is, as
an endpoint that will be used to accept incoming connection requests. Once
so marked, the endpoint is said to be in the listening state and may not be
used as the endpoint of a connection.

The endpoint, epd, must have been bound to a port.

The backlog argument defines the maximum length to which the queue of
pending connections for epd may grow. If a connection request arrives when
the queue is full, the client may receive an error with an indication that
the connection was refused.

.. _`scif_listen.return`:

Return
------

Upon successful completion, \ :c:func:`scif_listen`\  returns 0; otherwise in user mode
-1 is returned and errno is set to indicate the error; in kernel mode the
negative of one of the following errors is returned.

.. _`scif_listen.errors`:

Errors
------

EBADF, ENOTTY - epd is not a valid endpoint descriptor
EINVAL - the endpoint is not bound to a port
EISCONN - The endpoint is already connected or listening

.. _`scif_connect`:

scif_connect
============

.. c:function:: int scif_connect(scif_epd_t epd, struct scif_port_id *dst)

    Initiate a connection on a port

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param dst:
        global id of port to which to connect
    :type dst: struct scif_port_id \*

.. _`scif_connect.description`:

Description
-----------

The \ :c:func:`scif_connect`\  function requests the connection of endpoint epd to remote
port dst. If the connection is successful, a peer endpoint, bound to dst, is
created on node dst.node. On successful return, the connection is complete.

If the endpoint epd has not already been bound to a port, \ :c:func:`scif_connect`\ 
will bind it to an unused local port.

A connection is terminated when an endpoint of the connection is closed,
either explicitly by \ :c:func:`scif_close`\ , or when a process that owns one of the
endpoints of the connection is terminated.

In user space, \ :c:func:`scif_connect`\  supports an asynchronous connection mode
if the application has set the O_NONBLOCK flag on the endpoint via the
\ :c:func:`fcntl`\  system call. Setting this flag will result in the calling process
not to wait during \ :c:func:`scif_connect`\ .

.. _`scif_connect.return`:

Return
------

Upon successful completion, \ :c:func:`scif_connect`\  returns the port ID to which the
endpoint, epd, is bound; otherwise in user mode -1 is returned and errno is
set to indicate the error; in kernel mode the negative of one of the
following errors is returned.

.. _`scif_connect.errors`:

Errors
------

EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNREFUSED - The destination was not listening for connections or refused
the connection request
EINVAL - dst.port is not a valid port ID
EISCONN - The endpoint is already connected
ENOMEM - No buffer space is available
ENODEV - The destination node does not exist, or the node is lost or existed,
but is not currently in the network since it may have crashed
ENOSPC - No port number available for assignment
EOPNOTSUPP - The endpoint is listening and cannot be connected

.. _`scif_accept`:

scif_accept
===========

.. c:function:: int scif_accept(scif_epd_t epd, struct scif_port_id *peer, scif_epd_t *newepd, int flags)

    Accept a connection on an endpoint

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param peer:
        global id of port to which connected
    :type peer: struct scif_port_id \*

    :param newepd:
        new connected endpoint descriptor
    :type newepd: scif_epd_t \*

    :param flags:
        flags
    :type flags: int

.. _`scif_accept.description`:

Description
-----------

The \ :c:func:`scif_accept`\  call extracts the first connection request from the queue
of pending connections for the port on which epd is listening. \ :c:func:`scif_accept`\ 
creates a new endpoint, bound to the same port as epd, and allocates a new
SCIF endpoint descriptor, returned in newepd, for the endpoint. The new
endpoint is connected to the endpoint through which the connection was
requested. epd is unaffected by this call, and remains in the listening
state.

On successful return, peer holds the global port identifier (node id and
local port number) of the port which requested the connection.

A connection is terminated when an endpoint of the connection is closed,
either explicitly by \ :c:func:`scif_close`\ , or when a process that owns one of the
endpoints of the connection is terminated.

The number of connections that can (subsequently) be accepted on epd is only
limited by system resources (memory).

The flags argument is formed by OR'ing together zero or more of the
following values.
SCIF_ACCEPT_SYNC - block until a connection request is presented. If
SCIF_ACCEPT_SYNC is not in flags, and no pending
connections are present on the queue, \ :c:func:`scif_accept`\ 
fails with an EAGAIN error

In user mode, the \ :c:func:`select`\  and \ :c:func:`poll`\  functions can be used to determine
when there is a connection request. In kernel mode, the \ :c:func:`scif_poll`\ 
function may be used for this purpose. A readable event will be delivered
when a connection is requested.

.. _`scif_accept.return`:

Return
------

Upon successful completion, \ :c:func:`scif_accept`\  returns 0; otherwise in user mode
-1 is returned and errno is set to indicate the error; in kernel mode the
negative of one of the following errors is returned.

.. _`scif_accept.errors`:

Errors
------

EAGAIN - SCIF_ACCEPT_SYNC is not set and no connections are present to be
accepted or SCIF_ACCEPT_SYNC is not set and remote node failed to complete
its connection request
EBADF, ENOTTY - epd is not a valid endpoint descriptor
EINTR - Interrupted function
EINVAL - epd is not a listening endpoint, or flags is invalid, or peer is
NULL, or newepd is NULL
ENODEV - The requesting node is lost or existed, but is not currently in the
network since it may have crashed
ENOMEM - Not enough space
ENOENT - Secondary part of epd registration failed

.. _`scif_close`:

scif_close
==========

.. c:function:: int scif_close(scif_epd_t epd)

    Close an endpoint

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

.. _`scif_close.description`:

Description
-----------

\ :c:func:`scif_close`\  closes an endpoint and performs necessary teardown of
facilities associated with that endpoint.

If epd is a listening endpoint then it will no longer accept connection
requests on the port to which it is bound. Any pending connection requests
are rejected.

If epd is a connected endpoint, then its peer endpoint is also closed. RMAs
which are in-process through epd or its peer endpoint will complete before
\ :c:func:`scif_close`\  returns. Registered windows of the local and peer endpoints are
released as if \ :c:func:`scif_unregister`\  was called against each window.

Closing a SCIF endpoint does not affect local registered memory mapped by
a SCIF endpoint on a remote node. The local memory remains mapped by the peer
SCIF endpoint explicitly removed by calling munmap(..) by the peer.

If the peer endpoint's receive queue is not empty at the time that epd is
closed, then the peer endpoint can be passed as the endpoint parameter to
\ :c:func:`scif_recv`\  until the receive queue is empty.

epd is freed and may no longer be accessed.

.. _`scif_close.return`:

Return
------

Upon successful completion, \ :c:func:`scif_close`\  returns 0; otherwise in user mode
-1 is returned and errno is set to indicate the error; in kernel mode the
negative of one of the following errors is returned.

.. _`scif_close.errors`:

Errors
------

EBADF, ENOTTY - epd is not a valid endpoint descriptor

.. _`scif_send`:

scif_send
=========

.. c:function:: int scif_send(scif_epd_t epd, void *msg, int len, int flags)

    Send a message

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param msg:
        message buffer address
    :type msg: void \*

    :param len:
        message length
    :type len: int

    :param flags:
        blocking mode flags
    :type flags: int

.. _`scif_send.description`:

Description
-----------

\ :c:func:`scif_send`\  sends data to the peer of endpoint epd. Up to len bytes of data
are copied from memory starting at address msg. On successful execution the
return value of \ :c:func:`scif_send`\  is the number of bytes that were sent, and is
zero if no bytes were sent because len was zero. \ :c:func:`scif_send`\  may be called
only when the endpoint is in a connected state.

If a \ :c:func:`scif_send`\  call is non-blocking, then it sends only those bytes which
can be sent without waiting, up to a maximum of len bytes.

If a \ :c:func:`scif_send`\  call is blocking, then it normally returns after sending
all len bytes. If a blocking call is interrupted or the connection is
reset, the call is considered successful if some bytes were sent or len is
zero, otherwise the call is considered unsuccessful.

In user mode, the \ :c:func:`select`\  and \ :c:func:`poll`\  functions can be used to determine
when the send queue is not full. In kernel mode, the \ :c:func:`scif_poll`\  function
may be used for this purpose.

It is recommended that \ :c:func:`scif_send`\ /scif_recv() only be used for short
control-type message communication between SCIF endpoints. The SCIF RMA
APIs are expected to provide better performance for transfer sizes of
1024 bytes or longer for the current MIC hardware and software
implementation.

\ :c:func:`scif_send`\  will block until the entire message is sent if SCIF_SEND_BLOCK
is passed as the flags argument.

.. _`scif_send.return`:

Return
------

Upon successful completion, \ :c:func:`scif_send`\  returns the number of bytes sent;
otherwise in user mode -1 is returned and errno is set to indicate the
error; in kernel mode the negative of one of the following errors is
returned.

.. _`scif_send.errors`:

Errors
------

EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - flags is invalid, or len is negative
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOMEM - Not enough space
ENOTCONN - The endpoint is not connected

.. _`scif_recv`:

scif_recv
=========

.. c:function:: int scif_recv(scif_epd_t epd, void *msg, int len, int flags)

    Receive a message

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param msg:
        message buffer address
    :type msg: void \*

    :param len:
        message buffer length
    :type len: int

    :param flags:
        blocking mode flags
    :type flags: int

.. _`scif_recv.description`:

Description
-----------

\ :c:func:`scif_recv`\  receives data from the peer of endpoint epd. Up to len bytes of
data are copied to memory starting at address msg. On successful execution
the return value of \ :c:func:`scif_recv`\  is the number of bytes that were received,
and is zero if no bytes were received because len was zero. \ :c:func:`scif_recv`\  may
be called only when the endpoint is in a connected state.

If a \ :c:func:`scif_recv`\  call is non-blocking, then it receives only those bytes
which can be received without waiting, up to a maximum of len bytes.

If a \ :c:func:`scif_recv`\  call is blocking, then it normally returns after receiving
all len bytes. If the blocking call was interrupted due to a disconnection,
subsequent calls to \ :c:func:`scif_recv`\  will copy all bytes received upto the point
of disconnection.

In user mode, the \ :c:func:`select`\  and \ :c:func:`poll`\  functions can be used to determine
when data is available to be received. In kernel mode, the \ :c:func:`scif_poll`\ 
function may be used for this purpose.

It is recommended that \ :c:func:`scif_send`\ /scif_recv() only be used for short
control-type message communication between SCIF endpoints. The SCIF RMA
APIs are expected to provide better performance for transfer sizes of
1024 bytes or longer for the current MIC hardware and software
implementation.

\ :c:func:`scif_recv`\  will block until the entire message is received if
SCIF_RECV_BLOCK is passed as the flags argument.

.. _`scif_recv.return`:

Return
------

Upon successful completion, \ :c:func:`scif_recv`\  returns the number of bytes
received; otherwise in user mode -1 is returned and errno is set to
indicate the error; in kernel mode the negative of one of the following
errors is returned.

.. _`scif_recv.errors`:

Errors
------

EAGAIN - The destination node is returning from a low power state
EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - flags is invalid, or len is negative
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOMEM - Not enough space
ENOTCONN - The endpoint is not connected

.. _`scif_register`:

scif_register
=============

.. c:function:: off_t scif_register(scif_epd_t epd, void *addr, size_t len, off_t offset, int prot_flags, int map_flags)

    Mark a memory region for remote access.

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param addr:
        starting virtual address
    :type addr: void \*

    :param len:
        length of range
    :type len: size_t

    :param offset:
        offset of window
    :type offset: off_t

    :param prot_flags:
        read/write protection flags
    :type prot_flags: int

    :param map_flags:
        mapping flags
    :type map_flags: int

.. _`scif_register.description`:

Description
-----------

The \ :c:func:`scif_register`\  function opens a window, a range of whole pages of the
registered address space of the endpoint epd, starting at offset po and
continuing for len bytes. The value of po, further described below, is a
function of the parameters offset and len, and the value of map_flags. Each
page of the window represents the physical memory page which backs the
corresponding page of the range of virtual address pages starting at addr
and continuing for len bytes. addr and len are constrained to be multiples
of the page size. A successful \ :c:func:`scif_register`\  call returns po.

When SCIF_MAP_FIXED is set in the map_flags argument, po will be offset
exactly, and offset is constrained to be a multiple of the page size. The
mapping established by \ :c:func:`scif_register`\  will not replace any existing
registration; an error is returned if any page within the range [offset,
offset + len - 1] intersects an existing window.

When SCIF_MAP_FIXED is not set, the implementation uses offset in an
implementation-defined manner to arrive at po. The po value so chosen will
be an area of the registered address space that the implementation deems
suitable for a mapping of len bytes. An offset value of 0 is interpreted as
granting the implementation complete freedom in selecting po, subject to
constraints described below. A non-zero value of offset is taken to be a
suggestion of an offset near which the mapping should be placed. When the
implementation selects a value for po, it does not replace any extant
window. In all cases, po will be a multiple of the page size.

The physical pages which are so represented by a window are available for
access in calls to \ :c:func:`mmap`\ , \ :c:func:`scif_readfrom`\ , \ :c:func:`scif_writeto`\ ,
\ :c:func:`scif_vreadfrom`\ , and \ :c:func:`scif_vwriteto`\ . While a window is registered, the
physical pages represented by the window will not be reused by the memory
subsystem for any other purpose. Note that the same physical page may be
represented by multiple windows.

Subsequent operations which change the memory pages to which virtual
addresses are mapped (such as \ :c:func:`mmap`\ , \ :c:func:`munmap`\ ) have no effect on
existing window.

If the process will \ :c:func:`fork`\ , it is recommended that the registered
virtual address range be marked with MADV_DONTFORK. Doing so will prevent
problems due to copy-on-write semantics.

The prot_flags argument is formed by OR'ing together one or more of the
following values.
SCIF_PROT_READ - allow read operations from the window
SCIF_PROT_WRITE - allow write operations to the window

.. _`scif_register.return`:

Return
------

Upon successful completion, \ :c:func:`scif_register`\  returns the offset at which the
mapping was placed (po); otherwise in user mode SCIF_REGISTER_FAILED (that
is (off_t \*)-1) is returned and errno is set to indicate the error; in
kernel mode the negative of one of the following errors is returned.

.. _`scif_register.errors`:

Errors
------

EADDRINUSE - SCIF_MAP_FIXED is set in map_flags, and pages in the range
[offset, offset + len -1] are already registered
EAGAIN - The mapping could not be performed due to lack of resources
EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - map_flags is invalid, or prot_flags is invalid, or SCIF_MAP_FIXED is
set in flags, and offset is not a multiple of the page size, or addr is not a
multiple of the page size, or len is not a multiple of the page size, or is
0, or offset is negative
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOMEM - Not enough space
ENOTCONN -The endpoint is not connected

.. _`scif_unregister`:

scif_unregister
===============

.. c:function:: int scif_unregister(scif_epd_t epd, off_t offset, size_t len)

    Mark a memory region for remote access.

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param offset:
        start of range to unregister
    :type offset: off_t

    :param len:
        length of range to unregister
    :type len: size_t

.. _`scif_unregister.description`:

Description
-----------

The \ :c:func:`scif_unregister`\  function closes those previously registered windows
which are entirely within the range [offset, offset + len - 1]. It is an
error to specify a range which intersects only a subrange of a window.

On a successful return, pages within the window may no longer be specified
in calls to \ :c:func:`mmap`\ , \ :c:func:`scif_readfrom`\ , \ :c:func:`scif_writeto`\ , \ :c:func:`scif_vreadfrom`\ ,
\ :c:func:`scif_vwriteto`\ , scif_get_pages, and \ :c:func:`scif_fence_signal`\ . The window,
however, continues to exist until all previous references against it are
removed. A window is referenced if there is a mapping to it created by
\ :c:func:`mmap`\ , or if \ :c:func:`scif_get_pages`\  was called against the window
(and the pages have not been returned via \ :c:func:`scif_put_pages`\ ). A window is
also referenced while an RMA, in which some range of the window is a source
or destination, is in progress. Finally a window is referenced while some
offset in that window was specified to \ :c:func:`scif_fence_signal`\ , and the RMAs
marked by that call to \ :c:func:`scif_fence_signal`\  have not completed. While a
window is in this state, its registered address space pages are not
available for use in a new registered window.

When all such references to the window have been removed, its references to
all the physical pages which it represents are removed. Similarly, the
registered address space pages of the window become available for
registration in a new window.

.. _`scif_unregister.return`:

Return
------

Upon successful completion, \ :c:func:`scif_unregister`\  returns 0; otherwise in user
mode -1 is returned and errno is set to indicate the error; in kernel mode
the negative of one of the following errors is returned. In the event of an
error, no windows are unregistered.

.. _`scif_unregister.errors`:

Errors
------

EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - the range [offset, offset + len - 1] intersects a subrange of a
window, or offset is negative
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected
ENXIO - Offsets in the range [offset, offset + len - 1] are invalid for the
registered address space of epd

.. _`scif_readfrom`:

scif_readfrom
=============

.. c:function:: int scif_readfrom(scif_epd_t epd, off_t loffset, size_t len, off_t roffset, int rma_flags)

    Copy from a remote address space

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param loffset:
        offset in local registered address space to
        which to copy
    :type loffset: off_t

    :param len:
        length of range to copy
    :type len: size_t

    :param roffset:
        offset in remote registered address space
        from which to copy
    :type roffset: off_t

    :param rma_flags:
        transfer mode flags
    :type rma_flags: int

.. _`scif_readfrom.description`:

Description
-----------

\ :c:func:`scif_readfrom`\  copies len bytes from the remote registered address space of
the peer of endpoint epd, starting at the offset roffset to the local
registered address space of epd, starting at the offset loffset.

Each of the specified ranges [loffset, loffset + len - 1] and [roffset,
roffset + len - 1] must be within some registered window or windows of the
local and remote nodes. A range may intersect multiple registered windows,
but only if those windows are contiguous in the registered address space.

If rma_flags includes SCIF_RMA_USECPU, then the data is copied using
programmed read/writes. Otherwise the data is copied using DMA. If rma_-
flags includes SCIF_RMA_SYNC, then \ :c:func:`scif_readfrom`\  will return after the
transfer is complete. Otherwise, the transfer may be performed asynchron-
ously. The order in which any two asynchronous RMA operations complete
is non-deterministic. The synchronization functions, \ :c:func:`scif_fence_mark`\ /
\ :c:func:`scif_fence_wait`\  and \ :c:func:`scif_fence_signal`\ , can be used to synchronize to
the completion of asynchronous RMA operations on the same endpoint.

The DMA transfer of individual bytes is not guaranteed to complete in
address order. If rma_flags includes SCIF_RMA_ORDERED, then the last
cacheline or partial cacheline of the source range will become visible on
the destination node after all other transferred data in the source
range has become visible on the destination node.

The optimal DMA performance will likely be realized if both
loffset and roffset are cacheline aligned (are a multiple of 64). Lower
performance will likely be realized if loffset and roffset are not
cacheline aligned but are separated by some multiple of 64. The lowest level
of performance is likely if loffset and roffset are not separated by a
multiple of 64.

The rma_flags argument is formed by ORing together zero or more of the
following values.
SCIF_RMA_USECPU - perform the transfer using the CPU, otherwise use the DMA
engine.
SCIF_RMA_SYNC - perform the transfer synchronously, returning after the
transfer has completed. Passing this flag results in the
current implementation busy waiting and consuming CPU cycles
while the DMA transfer is in progress for best performance by
avoiding the interrupt latency.
SCIF_RMA_ORDERED - ensure that the last cacheline or partial cacheline of
the source range becomes visible on the destination node
after all other transferred data in the source range has
become visible on the destination

.. _`scif_readfrom.return`:

Return
------

Upon successful completion, \ :c:func:`scif_readfrom`\  returns 0; otherwise in user
mode -1 is returned and errno is set to indicate the error; in kernel mode
the negative of one of the following errors is returned.

.. _`scif_readfrom.errors`:

Errors
------

EACCESS - Attempt to write to a read-only range
EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - rma_flags is invalid
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected
ENXIO - The range [loffset, loffset + len - 1] is invalid for the registered
address space of epd, or, The range [roffset, roffset + len - 1] is invalid
for the registered address space of the peer of epd, or loffset or roffset
is negative

.. _`scif_writeto`:

scif_writeto
============

.. c:function:: int scif_writeto(scif_epd_t epd, off_t loffset, size_t len, off_t roffset, int rma_flags)

    Copy to a remote address space

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param loffset:
        offset in local registered address space
        from which to copy
    :type loffset: off_t

    :param len:
        length of range to copy
    :type len: size_t

    :param roffset:
        offset in remote registered address space to
        which to copy
    :type roffset: off_t

    :param rma_flags:
        transfer mode flags
    :type rma_flags: int

.. _`scif_writeto.description`:

Description
-----------

\ :c:func:`scif_writeto`\  copies len bytes from the local registered address space of
epd, starting at the offset loffset to the remote registered address space
of the peer of endpoint epd, starting at the offset roffset.

Each of the specified ranges [loffset, loffset + len - 1] and [roffset,
roffset + len - 1] must be within some registered window or windows of the
local and remote nodes. A range may intersect multiple registered windows,
but only if those windows are contiguous in the registered address space.

If rma_flags includes SCIF_RMA_USECPU, then the data is copied using
programmed read/writes. Otherwise the data is copied using DMA. If rma_-
flags includes SCIF_RMA_SYNC, then \ :c:func:`scif_writeto`\  will return after the
transfer is complete. Otherwise, the transfer may be performed asynchron-
ously. The order in which any two asynchronous RMA operations complete
is non-deterministic. The synchronization functions, \ :c:func:`scif_fence_mark`\ /
\ :c:func:`scif_fence_wait`\  and \ :c:func:`scif_fence_signal`\ , can be used to synchronize to
the completion of asynchronous RMA operations on the same endpoint.

The DMA transfer of individual bytes is not guaranteed to complete in
address order. If rma_flags includes SCIF_RMA_ORDERED, then the last
cacheline or partial cacheline of the source range will become visible on
the destination node after all other transferred data in the source
range has become visible on the destination node.

The optimal DMA performance will likely be realized if both
loffset and roffset are cacheline aligned (are a multiple of 64). Lower
performance will likely be realized if loffset and roffset are not cacheline
aligned but are separated by some multiple of 64. The lowest level of
performance is likely if loffset and roffset are not separated by a multiple
of 64.

The rma_flags argument is formed by ORing together zero or more of the
following values.
SCIF_RMA_USECPU - perform the transfer using the CPU, otherwise use the DMA
engine.
SCIF_RMA_SYNC - perform the transfer synchronously, returning after the
transfer has completed. Passing this flag results in the
current implementation busy waiting and consuming CPU cycles
while the DMA transfer is in progress for best performance by
avoiding the interrupt latency.
SCIF_RMA_ORDERED - ensure that the last cacheline or partial cacheline of
the source range becomes visible on the destination node
after all other transferred data in the source range has
become visible on the destination

.. _`scif_writeto.return`:

Return
------

Upon successful completion, \ :c:func:`scif_readfrom`\  returns 0; otherwise in user
mode -1 is returned and errno is set to indicate the error; in kernel mode
the negative of one of the following errors is returned.

.. _`scif_writeto.errors`:

Errors
------

EACCESS - Attempt to write to a read-only range
EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - rma_flags is invalid
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected
ENXIO - The range [loffset, loffset + len - 1] is invalid for the registered
address space of epd, or, The range [roffset , roffset + len -1] is invalid
for the registered address space of the peer of epd, or loffset or roffset
is negative

.. _`scif_vreadfrom`:

scif_vreadfrom
==============

.. c:function:: int scif_vreadfrom(scif_epd_t epd, void *addr, size_t len, off_t roffset, int rma_flags)

    Copy from a remote address space

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param addr:
        address to which to copy
    :type addr: void \*

    :param len:
        length of range to copy
    :type len: size_t

    :param roffset:
        offset in remote registered address space
        from which to copy
    :type roffset: off_t

    :param rma_flags:
        transfer mode flags
    :type rma_flags: int

.. _`scif_vreadfrom.description`:

Description
-----------

\ :c:func:`scif_vreadfrom`\  copies len bytes from the remote registered address
space of the peer of endpoint epd, starting at the offset roffset, to local
memory, starting at addr.

The specified range [roffset, roffset + len - 1] must be within some
registered window or windows of the remote nodes. The range may
intersect multiple registered windows, but only if those windows are
contiguous in the registered address space.

If rma_flags includes SCIF_RMA_USECPU, then the data is copied using
programmed read/writes. Otherwise the data is copied using DMA. If rma_-
flags includes SCIF_RMA_SYNC, then \ :c:func:`scif_vreadfrom`\  will return after the
transfer is complete. Otherwise, the transfer may be performed asynchron-
ously. The order in which any two asynchronous RMA operations complete
is non-deterministic. The synchronization functions, \ :c:func:`scif_fence_mark`\ /
\ :c:func:`scif_fence_wait`\  and \ :c:func:`scif_fence_signal`\ , can be used to synchronize to
the completion of asynchronous RMA operations on the same endpoint.

The DMA transfer of individual bytes is not guaranteed to complete in
address order. If rma_flags includes SCIF_RMA_ORDERED, then the last
cacheline or partial cacheline of the source range will become visible on
the destination node after all other transferred data in the source
range has become visible on the destination node.

If rma_flags includes SCIF_RMA_USECACHE, then the physical pages which back
the specified local memory range may be remain in a pinned state even after
the specified transfer completes. This may reduce overhead if some or all of
the same virtual address range is referenced in a subsequent call of
\ :c:func:`scif_vreadfrom`\  or \ :c:func:`scif_vwriteto`\ .

The optimal DMA performance will likely be realized if both
addr and roffset are cacheline aligned (are a multiple of 64). Lower
performance will likely be realized if addr and roffset are not
cacheline aligned but are separated by some multiple of 64. The lowest level
of performance is likely if addr and roffset are not separated by a
multiple of 64.

The rma_flags argument is formed by ORing together zero or more of the
following values.
SCIF_RMA_USECPU - perform the transfer using the CPU, otherwise use the DMA
engine.
SCIF_RMA_USECACHE - enable registration caching
SCIF_RMA_SYNC - perform the transfer synchronously, returning after the
transfer has completed. Passing this flag results in the
current implementation busy waiting and consuming CPU cycles
while the DMA transfer is in progress for best performance by
avoiding the interrupt latency.
SCIF_RMA_ORDERED - ensure that the last cacheline or partial cacheline of
the source range becomes visible on the destination node
after all other transferred data in the source range has
become visible on the destination

.. _`scif_vreadfrom.return`:

Return
------

Upon successful completion, \ :c:func:`scif_vreadfrom`\  returns 0; otherwise in user
mode -1 is returned and errno is set to indicate the error; in kernel mode
the negative of one of the following errors is returned.

.. _`scif_vreadfrom.errors`:

Errors
------

EACCESS - Attempt to write to a read-only range
EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - rma_flags is invalid
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected
ENXIO - Offsets in the range [roffset, roffset + len - 1] are invalid for the
registered address space of epd

.. _`scif_vwriteto`:

scif_vwriteto
=============

.. c:function:: int scif_vwriteto(scif_epd_t epd, void *addr, size_t len, off_t roffset, int rma_flags)

    Copy to a remote address space

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param addr:
        address from which to copy
    :type addr: void \*

    :param len:
        length of range to copy
    :type len: size_t

    :param roffset:
        offset in remote registered address space to
        which to copy
    :type roffset: off_t

    :param rma_flags:
        transfer mode flags
    :type rma_flags: int

.. _`scif_vwriteto.description`:

Description
-----------

\ :c:func:`scif_vwriteto`\  copies len bytes from the local memory, starting at addr, to
the remote registered address space of the peer of endpoint epd, starting at
the offset roffset.

The specified range [roffset, roffset + len - 1] must be within some
registered window or windows of the remote nodes. The range may intersect
multiple registered windows, but only if those windows are contiguous in the
registered address space.

If rma_flags includes SCIF_RMA_USECPU, then the data is copied using
programmed read/writes. Otherwise the data is copied using DMA. If rma_-
flags includes SCIF_RMA_SYNC, then \ :c:func:`scif_vwriteto`\  will return after the
transfer is complete. Otherwise, the transfer may be performed asynchron-
ously. The order in which any two asynchronous RMA operations complete
is non-deterministic. The synchronization functions, \ :c:func:`scif_fence_mark`\ /
\ :c:func:`scif_fence_wait`\  and \ :c:func:`scif_fence_signal`\ , can be used to synchronize to
the completion of asynchronous RMA operations on the same endpoint.

The DMA transfer of individual bytes is not guaranteed to complete in
address order. If rma_flags includes SCIF_RMA_ORDERED, then the last
cacheline or partial cacheline of the source range will become visible on
the destination node after all other transferred data in the source
range has become visible on the destination node.

If rma_flags includes SCIF_RMA_USECACHE, then the physical pages which back
the specified local memory range may be remain in a pinned state even after
the specified transfer completes. This may reduce overhead if some or all of
the same virtual address range is referenced in a subsequent call of
\ :c:func:`scif_vreadfrom`\  or \ :c:func:`scif_vwriteto`\ .

The optimal DMA performance will likely be realized if both
addr and offset are cacheline aligned (are a multiple of 64). Lower
performance will likely be realized if addr and offset are not cacheline
aligned but are separated by some multiple of 64. The lowest level of
performance is likely if addr and offset are not separated by a multiple of
64.

The rma_flags argument is formed by ORing together zero or more of the
following values.
SCIF_RMA_USECPU - perform the transfer using the CPU, otherwise use the DMA
engine.
SCIF_RMA_USECACHE - allow registration caching
SCIF_RMA_SYNC - perform the transfer synchronously, returning after the
transfer has completed. Passing this flag results in the
current implementation busy waiting and consuming CPU cycles
while the DMA transfer is in progress for best performance by
avoiding the interrupt latency.
SCIF_RMA_ORDERED - ensure that the last cacheline or partial cacheline of
the source range becomes visible on the destination node
after all other transferred data in the source range has
become visible on the destination

.. _`scif_vwriteto.return`:

Return
------

Upon successful completion, \ :c:func:`scif_vwriteto`\  returns 0; otherwise in user
mode -1 is returned and errno is set to indicate the error; in kernel mode
the negative of one of the following errors is returned.

.. _`scif_vwriteto.errors`:

Errors
------

EACCESS - Attempt to write to a read-only range
EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - rma_flags is invalid
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected
ENXIO - Offsets in the range [roffset, roffset + len - 1] are invalid for the
registered address space of epd

.. _`scif_fence_mark`:

scif_fence_mark
===============

.. c:function:: int scif_fence_mark(scif_epd_t epd, int flags, int *mark)

    Mark previously issued RMAs

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param flags:
        control flags
    :type flags: int

    :param mark:
        marked value returned as output.
    :type mark: int \*

.. _`scif_fence_mark.description`:

Description
-----------

\ :c:func:`scif_fence_mark`\  returns after marking the current set of all uncompleted
RMAs initiated through the endpoint epd or the current set of all
uncompleted RMAs initiated through the peer of endpoint epd. The RMAs are
marked with a value returned at mark. The application may subsequently call
\ :c:func:`scif_fence_wait`\ , passing the value returned at mark, to await completion
of all RMAs so marked.

The flags argument has exactly one of the following values.
SCIF_FENCE_INIT_SELF - RMA operations initiated through endpoint
epd are marked
SCIF_FENCE_INIT_PEER - RMA operations initiated through the peer
of endpoint epd are marked

.. _`scif_fence_mark.return`:

Return
------

Upon successful completion, \ :c:func:`scif_fence_mark`\  returns 0; otherwise in user
mode -1 is returned and errno is set to indicate the error; in kernel mode
the negative of one of the following errors is returned.

.. _`scif_fence_mark.errors`:

Errors
------

EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - flags is invalid
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected
ENOMEM - Insufficient kernel memory was available

.. _`scif_fence_wait`:

scif_fence_wait
===============

.. c:function:: int scif_fence_wait(scif_epd_t epd, int mark)

    Wait for completion of marked RMAs

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param mark:
        mark request
    :type mark: int

.. _`scif_fence_wait.description`:

Description
-----------

\ :c:func:`scif_fence_wait`\  returns after all RMAs marked with mark have completed.
The value passed in mark must have been obtained in a previous call to
\ :c:func:`scif_fence_mark`\ .

.. _`scif_fence_wait.return`:

Return
------

Upon successful completion, \ :c:func:`scif_fence_wait`\  returns 0; otherwise in user
mode -1 is returned and errno is set to indicate the error; in kernel mode
the negative of one of the following errors is returned.

.. _`scif_fence_wait.errors`:

Errors
------

EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected
ENOMEM - Insufficient kernel memory was available

.. _`scif_fence_signal`:

scif_fence_signal
=================

.. c:function:: int scif_fence_signal(scif_epd_t epd, off_t loff, u64 lval, off_t roff, u64 rval, int flags)

    Request a memory update on completion of RMAs

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param loff:
        local offset
    :type loff: off_t

    :param lval:
        local value to write to loffset
    :type lval: u64

    :param roff:
        remote offset
    :type roff: off_t

    :param rval:
        remote value to write to roffset
    :type rval: u64

    :param flags:
        flags
    :type flags: int

.. _`scif_fence_signal.description`:

Description
-----------

\ :c:func:`scif_fence_signal`\  returns after marking the current set of all uncompleted
RMAs initiated through the endpoint epd or marking the current set of all
uncompleted RMAs initiated through the peer of endpoint epd.

If flags includes SCIF_SIGNAL_LOCAL, then on completion of the RMAs in the
marked set, lval is written to memory at the address corresponding to offset
loff in the local registered address space of epd. loff must be within a
registered window. If flags includes SCIF_SIGNAL_REMOTE, then on completion
of the RMAs in the marked set, rval is written to memory at the address
corresponding to offset roff in the remote registered address space of epd.
roff must be within a remote registered window of the peer of epd. Note
that any specified offset must be DWORD (4 byte / 32 bit) aligned.

The flags argument is formed by OR'ing together the following.
Exactly one of the following values.
SCIF_FENCE_INIT_SELF - RMA operations initiated through endpoint
epd are marked
SCIF_FENCE_INIT_PEER - RMA operations initiated through the peer
of endpoint epd are marked
One or more of the following values.
SCIF_SIGNAL_LOCAL - On completion of the marked set of RMAs, write lval to
memory at the address corresponding to offset loff in the local
registered address space of epd.
SCIF_SIGNAL_REMOTE - On completion of the marked set of RMAs, write rval to
memory at the address corresponding to offset roff in the remote
registered address space of epd.

.. _`scif_fence_signal.return`:

Return
------

Upon successful completion, \ :c:func:`scif_fence_signal`\  returns 0; otherwise in
user mode -1 is returned and errno is set to indicate the error; in kernel
mode the negative of one of the following errors is returned.

.. _`scif_fence_signal.errors`:

Errors
------

EBADF, ENOTTY - epd is not a valid endpoint descriptor
ECONNRESET - Connection reset by peer
EINVAL - flags is invalid, or loff or roff are not DWORD aligned
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected
ENXIO - loff is invalid for the registered address of epd, or roff is invalid
for the registered address space, of the peer of epd

.. _`scif_get_node_ids`:

scif_get_node_ids
=================

.. c:function:: int scif_get_node_ids(u16 *nodes, int len, u16 *self)

    Return information about online nodes

    :param nodes:
        array in which to return online node IDs
    :type nodes: u16 \*

    :param len:
        number of entries in the nodes array
    :type len: int

    :param self:
        address to place the node ID of the local node
    :type self: u16 \*

.. _`scif_get_node_ids.description`:

Description
-----------

\ :c:func:`scif_get_node_ids`\  fills in the nodes array with up to len node IDs of the
nodes in the SCIF network. If there is not enough space in nodes, as
indicated by the len parameter, only len node IDs are returned in nodes. The
return value of \ :c:func:`scif_get_node_ids`\  is the total number of nodes currently in
the SCIF network. By checking the return value against the len parameter,
the user may determine if enough space for nodes was allocated.

The node ID of the local node is returned at self.

.. _`scif_get_node_ids.return`:

Return
------

Upon successful completion, \ :c:func:`scif_get_node_ids`\  returns the actual number of
online nodes in the SCIF network including 'self'; otherwise in user mode
-1 is returned and errno is set to indicate the error; in kernel mode no
errors are returned.

.. _`scif_pin_pages`:

scif_pin_pages
==============

.. c:function:: int scif_pin_pages(void *addr, size_t len, int prot_flags, int map_flags, scif_pinned_pages_t *pinned_pages)

    Pin a set of pages

    :param addr:
        Virtual address of range to pin
    :type addr: void \*

    :param len:
        Length of range to pin
    :type len: size_t

    :param prot_flags:
        Page protection flags
    :type prot_flags: int

    :param map_flags:
        Page classification flags
    :type map_flags: int

    :param pinned_pages:
        Handle to pinned pages
    :type pinned_pages: scif_pinned_pages_t \*

.. _`scif_pin_pages.description`:

Description
-----------

\ :c:func:`scif_pin_pages`\  pins (locks in physical memory) the physical pages which
back the range of virtual address pages starting at addr and continuing for
len bytes. addr and len are constrained to be multiples of the page size. A
successful \ :c:func:`scif_pin_pages`\  call returns a handle to pinned_pages which may
be used in subsequent calls to \ :c:func:`scif_register_pinned_pages`\ .

The pages will remain pinned as long as there is a reference against the
scif_pinned_pages_t value returned by \ :c:func:`scif_pin_pages`\  and until
\ :c:func:`scif_unpin_pages`\  is called, passing the scif_pinned_pages_t value. A
reference is added to a scif_pinned_pages_t value each time a window is
created by calling \ :c:func:`scif_register_pinned_pages`\  and passing the
scif_pinned_pages_t value. A reference is removed from a
scif_pinned_pages_t value each time such a window is deleted.

Subsequent operations which change the memory pages to which virtual
addresses are mapped (such as \ :c:func:`mmap`\ , \ :c:func:`munmap`\ ) have no effect on the
scif_pinned_pages_t value or windows created against it.

If the process will \ :c:func:`fork`\ , it is recommended that the registered
virtual address range be marked with MADV_DONTFORK. Doing so will prevent
problems due to copy-on-write semantics.

The prot_flags argument is formed by OR'ing together one or more of the
following values.
SCIF_PROT_READ - allow read operations against the pages
SCIF_PROT_WRITE - allow write operations against the pages
The map_flags argument can be set as SCIF_MAP_KERNEL to interpret addr as a
kernel space address. By default, addr is interpreted as a user space
address.

.. _`scif_pin_pages.return`:

Return
------

Upon successful completion, \ :c:func:`scif_pin_pages`\  returns 0; otherwise the
negative of one of the following errors is returned.

.. _`scif_pin_pages.errors`:

Errors
------

EINVAL - prot_flags is invalid, map_flags is invalid, or offset is negative
ENOMEM - Not enough space

.. _`scif_unpin_pages`:

scif_unpin_pages
================

.. c:function:: int scif_unpin_pages(scif_pinned_pages_t pinned_pages)

    Unpin a set of pages

    :param pinned_pages:
        Handle to pinned pages to be unpinned
    :type pinned_pages: scif_pinned_pages_t

.. _`scif_unpin_pages.description`:

Description
-----------

\ :c:func:`scif_unpin_pages`\  prevents \ :c:func:`scif_register_pinned_pages`\  from registering new
windows against pinned_pages. The physical pages represented by pinned_pages
will remain pinned until all windows previously registered against
pinned_pages are deleted (the window is \ :c:func:`scif_unregister`\ 'd and all
references to the window are removed (see \ :c:func:`scif_unregister`\ ).

pinned_pages must have been obtain from a previous call to \ :c:func:`scif_pin_pages`\ .
After calling \ :c:func:`scif_unpin_pages`\ , it is an error to pass pinned_pages to
\ :c:func:`scif_register_pinned_pages`\ .

.. _`scif_unpin_pages.return`:

Return
------

Upon successful completion, \ :c:func:`scif_unpin_pages`\  returns 0; otherwise the
negative of one of the following errors is returned.

.. _`scif_unpin_pages.errors`:

Errors
------

EINVAL - pinned_pages is not valid

.. _`scif_register_pinned_pages`:

scif_register_pinned_pages
==========================

.. c:function:: off_t scif_register_pinned_pages(scif_epd_t epd, scif_pinned_pages_t pinned_pages, off_t offset, int map_flags)

    Mark a memory region for remote access.

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param pinned_pages:
        Handle to pinned pages
    :type pinned_pages: scif_pinned_pages_t

    :param offset:
        Registered address space offset
    :type offset: off_t

    :param map_flags:
        Flags which control where pages are mapped
    :type map_flags: int

.. _`scif_register_pinned_pages.description`:

Description
-----------

The \ :c:func:`scif_register_pinned_pages`\  function opens a window, a range of whole
pages of the registered address space of the endpoint epd, starting at
offset po. The value of po, further described below, is a function of the
parameters offset and pinned_pages, and the value of map_flags. Each page of
the window represents a corresponding physical memory page of the range
represented by pinned_pages; the length of the window is the same as the
length of range represented by pinned_pages. A successful
\ :c:func:`scif_register_pinned_pages`\  call returns po as the return value.

When SCIF_MAP_FIXED is set in the map_flags argument, po will be offset
exactly, and offset is constrained to be a multiple of the page size. The
mapping established by \ :c:func:`scif_register_pinned_pages`\  will not replace any
existing registration; an error is returned if any page of the new window
would intersect an existing window.

When SCIF_MAP_FIXED is not set, the implementation uses offset in an
implementation-defined manner to arrive at po. The po so chosen will be an
area of the registered address space that the implementation deems suitable
for a mapping of the required size. An offset value of 0 is interpreted as
granting the implementation complete freedom in selecting po, subject to
constraints described below. A non-zero value of offset is taken to be a
suggestion of an offset near which the mapping should be placed. When the
implementation selects a value for po, it does not replace any extant
window. In all cases, po will be a multiple of the page size.

The physical pages which are so represented by a window are available for
access in calls to \ :c:func:`scif_get_pages`\ , \ :c:func:`scif_readfrom`\ , \ :c:func:`scif_writeto`\ ,
\ :c:func:`scif_vreadfrom`\ , and \ :c:func:`scif_vwriteto`\ . While a window is registered, the
physical pages represented by the window will not be reused by the memory
subsystem for any other purpose. Note that the same physical page may be
represented by multiple windows.

Windows created by \ :c:func:`scif_register_pinned_pages`\  are unregistered by
\ :c:func:`scif_unregister`\ .

The map_flags argument can be set to SCIF_MAP_FIXED which interprets a
fixed offset.

.. _`scif_register_pinned_pages.return`:

Return
------

Upon successful completion, \ :c:func:`scif_register_pinned_pages`\  returns the offset
at which the mapping was placed (po); otherwise the negative of one of the
following errors is returned.

.. _`scif_register_pinned_pages.errors`:

Errors
------

EADDRINUSE - SCIF_MAP_FIXED is set in map_flags and pages in the new window
would intersect an existing window
EAGAIN - The mapping could not be performed due to lack of resources
ECONNRESET - Connection reset by peer
EINVAL - map_flags is invalid, or SCIF_MAP_FIXED is set in map_flags, and
offset is not a multiple of the page size, or offset is negative
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOMEM - Not enough space
ENOTCONN - The endpoint is not connected

.. _`scif_get_pages`:

scif_get_pages
==============

.. c:function:: int scif_get_pages(scif_epd_t epd, off_t offset, size_t len, struct scif_range **pages)

    Add references to remote registered pages

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

    :param offset:
        remote registered offset
    :type offset: off_t

    :param len:
        length of range of pages
    :type len: size_t

    :param pages:
        returned scif_range structure
    :type pages: struct scif_range \*\*

.. _`scif_get_pages.description`:

Description
-----------

\ :c:func:`scif_get_pages`\  returns the addresses of the physical pages represented by
those pages of the registered address space of the peer of epd, starting at
offset and continuing for len bytes. offset and len are constrained to be
multiples of the page size.

All of the pages in the specified range [offset, offset + len - 1] must be
within a single window of the registered address space of the peer of epd.

The addresses are returned as a virtually contiguous array pointed to by the
phys_addr component of the scif_range structure whose address is returned in
pages. The nr_pages component of scif_range is the length of the array. The
prot_flags component of scif_range holds the protection flag value passed
when the pages were registered.

Each physical page whose address is returned by \ :c:func:`scif_get_pages`\  remains
available and will not be released for reuse until the scif_range structure
is returned in a call to \ :c:func:`scif_put_pages`\ . The scif_range structure returned
by \ :c:func:`scif_get_pages`\  must be unmodified.

It is an error to call \ :c:func:`scif_close`\  on an endpoint on which a scif_range
structure of that endpoint has not been returned to \ :c:func:`scif_put_pages`\ .

.. _`scif_get_pages.return`:

Return
------

Upon successful completion, \ :c:func:`scif_get_pages`\  returns 0; otherwise the
negative of one of the following errors is returned.

.. _`scif_get_pages.errors`:

Errors
------

ECONNRESET - Connection reset by peer.
EINVAL - offset is not a multiple of the page size, or offset is negative, or
len is not a multiple of the page size
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected
ENXIO - Offsets in the range [offset, offset + len - 1] are invalid
for the registered address space of the peer epd

.. _`scif_put_pages`:

scif_put_pages
==============

.. c:function:: int scif_put_pages(struct scif_range *pages)

    Remove references from remote registered pages

    :param pages:
        pages to be returned
    :type pages: struct scif_range \*

.. _`scif_put_pages.description`:

Description
-----------

\ :c:func:`scif_put_pages`\  releases a scif_range structure previously obtained by
calling \ :c:func:`scif_get_pages`\ . The physical pages represented by pages may
be reused when the window which represented those pages is unregistered.
Therefore, those pages must not be accessed after calling \ :c:func:`scif_put_pages`\ .

.. _`scif_put_pages.return`:

Return
------

Upon successful completion, \ :c:func:`scif_put_pages`\  returns 0; otherwise the
negative of one of the following errors is returned.

.. _`scif_put_pages.errors`:

Errors
------

EINVAL - pages does not point to a valid scif_range structure, or
the scif_range structure pointed to by pages was already returned
ENODEV - The remote node is lost or existed, but is not currently in the
network since it may have crashed
ENOTCONN - The endpoint is not connected

.. _`scif_poll`:

scif_poll
=========

.. c:function:: int scif_poll(struct scif_pollepd *epds, unsigned int nepds, long timeout)

    Wait for some event on an endpoint

    :param epds:
        Array of endpoint descriptors
    :type epds: struct scif_pollepd \*

    :param nepds:
        Length of epds
    :type nepds: unsigned int

    :param timeout:
        Upper limit on time for which \ :c:func:`scif_poll`\  will block
    :type timeout: long

.. _`scif_poll.description`:

Description
-----------

\ :c:func:`scif_poll`\  waits for one of a set of endpoints to become ready to perform
an I/O operation.

The epds argument specifies the endpoint descriptors to be examined and the
events of interest for each endpoint descriptor. epds is a pointer to an
array with one member for each open endpoint descriptor of interest.

The number of items in the epds array is specified in nepds. The epd field
of scif_pollepd is an endpoint descriptor of an open endpoint. The field
events is a bitmask specifying the events which the application is
interested in. The field revents is an output parameter, filled by the
kernel with the events that actually occurred. The bits returned in revents
can include any of those specified in events, or one of the values EPOLLERR,
EPOLLHUP, or EPOLLNVAL. (These three bits are meaningless in the events
field, and will be set in the revents field whenever the corresponding
condition is true.)

If none of the events requested (and no error) has occurred for any of the
endpoint descriptors, then \ :c:func:`scif_poll`\  blocks until one of the events occurs.

The timeout argument specifies an upper limit on the time for which
\ :c:func:`scif_poll`\  will block, in milliseconds. Specifying a negative value in
timeout means an infinite timeout.

The following bits may be set in events and returned in revents.
EPOLLIN - Data may be received without blocking. For a connected
endpoint, this means that \ :c:func:`scif_recv`\  may be called without blocking. For a
listening endpoint, this means that \ :c:func:`scif_accept`\  may be called without
blocking.
EPOLLOUT - Data may be sent without blocking. For a connected endpoint, this
means that \ :c:func:`scif_send`\  may be called without blocking. EPOLLOUT may also be
used to block waiting for a non-blocking connect to complete. This bit value
has no meaning for a listening endpoint and is ignored if specified.

The following bits are only returned in revents, and are ignored if set in
events.
EPOLLERR - An error occurred on the endpoint
EPOLLHUP - The connection to the peer endpoint was disconnected
EPOLLNVAL - The specified endpoint descriptor is invalid.

.. _`scif_poll.return`:

Return
------

Upon successful completion, \ :c:func:`scif_poll`\  returns a non-negative value. A
positive value indicates the total number of endpoint descriptors that have
been selected (that is, endpoint descriptors for which the revents member is
non-zero). A value of 0 indicates that the call timed out and no endpoint
descriptors have been selected. Otherwise in user mode -1 is returned and
errno is set to indicate the error; in kernel mode the negative of one of
the following errors is returned.

.. _`scif_poll.errors`:

Errors
------

EINTR - A signal occurred before any requested event
EINVAL - The nepds argument is greater than {OPEN_MAX}
ENOMEM - There was no space to allocate file descriptor tables

.. _`scif_client_register`:

scif_client_register
====================

.. c:function:: int scif_client_register(struct scif_client *client)

    Register a SCIF client

    :param client:
        client to be registered
    :type client: struct scif_client \*

.. _`scif_client_register.description`:

Description
-----------

\ :c:func:`scif_client_register`\  registers a SCIF client. The \ :c:func:`probe`\  method
of the client is called when SCIF peer devices come online and the
\ :c:func:`remove`\  method is called when the peer devices disappear.

.. _`scif_client_register.return`:

Return
------

Upon successful completion, \ :c:func:`scif_client_register`\  returns a non-negative
value. Otherwise the return value is the same as \ :c:func:`subsys_interface_register`\ 
in the kernel.

.. _`scif_client_unregister`:

scif_client_unregister
======================

.. c:function:: void scif_client_unregister(struct scif_client *client)

    Unregister a SCIF client

    :param client:
        client to be unregistered
    :type client: struct scif_client \*

.. _`scif_client_unregister.description`:

Description
-----------

\ :c:func:`scif_client_unregister`\  unregisters a SCIF client.

.. _`scif_client_unregister.return`:

Return
------

None

.. This file was automatic generated / don't edit.

