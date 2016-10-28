.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fwserial/fwserial.c

.. _`list_head`:

LIST_HEAD
=========

.. c:function::  LIST_HEAD( fwserial_list)

    list of every fw_serial created for each fw_card See discussion in fwserial_probe.

    :param  fwserial_list:
        *undescribed*

.. _`fwtty_update_port_status`:

fwtty_update_port_status
========================

.. c:function:: void fwtty_update_port_status(struct fwtty_port *port, unsigned int status)

    decodes & dispatches line status changes

    :param struct fwtty_port \*port:
        *undescribed*

    :param unsigned int status:
        *undescribed*

.. _`fwtty_update_port_status.note`:

Note
----

in loopback, the port->lock is being held. Only use functions that
don't attempt to reclaim the port->lock.

.. _`__fwtty_port_line_status`:

__fwtty_port_line_status
========================

.. c:function:: unsigned int __fwtty_port_line_status(struct fwtty_port *port)

    generate 'line status' for indicated port

    :param struct fwtty_port \*port:
        *undescribed*

.. _`__fwtty_port_line_status.description`:

Description
-----------

This function returns a remote 'MSR' state based on the local 'MCR' state,
as if a null modem cable was attached. The actual status is a mangling
of TIOCM\_\* bits suitable for sending to a peer's status_addr.

.. _`__fwtty_port_line_status.note`:

Note
----

caller must be holding port lock

.. _`__fwtty_write_port_status`:

__fwtty_write_port_status
=========================

.. c:function:: int __fwtty_write_port_status(struct fwtty_port *port)

    send the port line status to peer

    :param struct fwtty_port \*port:
        *undescribed*

.. _`__fwtty_write_port_status.note`:

Note
----

caller must be holding the port lock.

.. _`fwtty_write_port_status`:

fwtty_write_port_status
=======================

.. c:function:: int fwtty_write_port_status(struct fwtty_port *port)

    same as above but locked by port lock

    :param struct fwtty_port \*port:
        *undescribed*

.. _`fwtty_do_hangup`:

fwtty_do_hangup
===============

.. c:function:: void fwtty_do_hangup(struct work_struct *work)

    wait for ldisc to deliver all pending rx; only then hangup

    :param struct work_struct \*work:
        *undescribed*

.. _`fwtty_do_hangup.description`:

Description
-----------

When the remote has finished tx, and all in-flight rx has been received and
and pushed to the flip buffer, the remote may close its device. This will
drop DTR on the remote which will drop carrier here. Typically, the tty is
hung up when carrier is dropped or lost.

However, there is a race between the hang up and the line discipline
delivering its data to the reader. A hangup will cause the ldisc to flush
(ie., clear) the read buffer and flip buffer. Because of firewire's
relatively high throughput, the ldisc frequently lags well behind the driver,
resulting in lost data (which has already been received and written to
the flip buffer) when the remote closes its end.

Unfortunately, since the flip buffer offers no direct method for determining
if it holds data, ensuring the ldisc has delivered all data is problematic.

.. _`fwtty_port_handler`:

fwtty_port_handler
==================

.. c:function:: void fwtty_port_handler(struct fw_card *card, struct fw_request *request, int tcode, int destination, int source, int generation, unsigned long long addr, void *data, size_t len, void *callback_data)

    bus address handler for port reads/writes

    :param struct fw_card \*card:
        *undescribed*

    :param struct fw_request \*request:
        *undescribed*

    :param int tcode:
        *undescribed*

    :param int destination:
        *undescribed*

    :param int source:
        *undescribed*

    :param int generation:
        *undescribed*

    :param unsigned long long addr:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param size_t len:
        *undescribed*

    :param void \*callback_data:
        *undescribed*

.. _`fwtty_port_handler.description`:

Description
-----------

This handler is responsible for handling inbound read/write dma from remotes.

.. _`fwtty_tx_complete`:

fwtty_tx_complete
=================

.. c:function:: void fwtty_tx_complete(struct fw_card *card, int rcode, void *data, size_t length, struct fwtty_transaction *txn)

    callback for tx dma

    :param struct fw_card \*card:
        *undescribed*

    :param int rcode:
        *undescribed*

    :param void \*data:
        ignored, has no meaning for write txns

    :param size_t length:
        ignored, has no meaning for write txns

    :param struct fwtty_transaction \*txn:
        *undescribed*

.. _`fwtty_tx_complete.description`:

Description
-----------

The writer must be woken here if the fifo has been emptied because it
may have slept if chars_in_buffer was != 0

.. _`fwtty_port_carrier_raised`:

fwtty_port_carrier_raised
=========================

.. c:function:: int fwtty_port_carrier_raised(struct tty_port *tty_port)

    required tty_port operation

    :param struct tty_port \*tty_port:
        *undescribed*

.. _`fwtty_port_carrier_raised.description`:

Description
-----------

This port operation is polled after a tty has been opened and is waiting for
carrier detect -- see drivers/tty/tty_port:\ :c:func:`tty_port_block_til_ready`\ .

.. _`fwtty_port_shutdown`:

fwtty_port_shutdown
===================

.. c:function:: void fwtty_port_shutdown(struct tty_port *tty_port)

    :param struct tty_port \*tty_port:
        *undescribed*

.. _`fwtty_port_shutdown.note`:

Note
----

the tty port core ensures this is not the console and
manages TTY_IO_ERROR properly

.. _`fwtty_break_ctl`:

fwtty_break_ctl
===============

.. c:function:: int fwtty_break_ctl(struct tty_struct *tty, int state)

    start/stop sending breaks

    :param struct tty_struct \*tty:
        *undescribed*

    :param int state:
        *undescribed*

.. _`fwtty_break_ctl.description`:

Description
-----------

Signals the remote to start or stop generating simulated breaks.
First, stop dequeueing from the fifo and wait for writer/drain to leave tx
before signalling the break line status. This guarantees any pending rx will
be queued to the line discipline before break is simulated on the remote.
Conversely, turning off break_ctl requires signalling the line status change,
then enabling tx.

.. _`fwserial_claim_port`:

fwserial_claim_port
===================

.. c:function:: struct fwtty_port *fwserial_claim_port(struct fwtty_peer *peer, int index)

    attempt to claim port @ index for peer

    :param struct fwtty_peer \*peer:
        *undescribed*

    :param int index:
        *undescribed*

.. _`fwserial_claim_port.description`:

Description
-----------

Returns ptr to claimed port or error code (as \ :c:func:`ERR_PTR`\ )
Can sleep - must be called from process context

.. _`fwserial_find_port`:

fwserial_find_port
==================

.. c:function:: struct fwtty_port *fwserial_find_port(struct fwtty_peer *peer)

    find avail port and claim for peer

    :param struct fwtty_peer \*peer:
        *undescribed*

.. _`fwserial_find_port.description`:

Description
-----------

Returns ptr to claimed port or NULL if none avail
Can sleep - must be called from process context

.. _`fwserial_connect_peer`:

fwserial_connect_peer
=====================

.. c:function:: int fwserial_connect_peer(struct fwtty_peer *peer)

    initiate virtual cable with peer

    :param struct fwtty_peer \*peer:
        *undescribed*

.. _`fwserial_connect_peer.description`:

Description
-----------

Returns 0 if VIRT_CABLE_PLUG request was successfully sent,
otherwise error code.  Must be called from process context.

.. _`fwserial_close_port`:

fwserial_close_port
===================

.. c:function:: void fwserial_close_port(struct tty_driver *driver, struct fwtty_port *port)

    HUP the tty (if the tty exists) and unregister the tty device. Only used by the unit driver upon unit removal to disconnect and cleanup all attached ports

    :param struct tty_driver \*driver:
        *undescribed*

    :param struct fwtty_port \*port:
        *undescribed*

.. _`fwserial_close_port.description`:

Description
-----------

The port reference is put by fwtty_cleanup (if a reference was
ever taken).

.. _`fwserial_lookup`:

fwserial_lookup
===============

.. c:function:: struct fw_serial *fwserial_lookup(struct fw_card *card)

    finds first fw_serial associated with card

    :param struct fw_card \*card:
        fw_card to match

.. _`fwserial_lookup.description`:

Description
-----------

NB: caller must be holding fwserial_list_mutex

.. _`__fwserial_lookup_rcu`:

__fwserial_lookup_rcu
=====================

.. c:function:: struct fw_serial *__fwserial_lookup_rcu(struct fw_card *card)

    finds first fw_serial associated with card

    :param struct fw_card \*card:
        fw_card to match

.. _`__fwserial_lookup_rcu.description`:

Description
-----------

NB: caller must be inside \ :c:func:`rcu_read_lock`\  section

.. _`__fwserial_peer_by_node_id`:

__fwserial_peer_by_node_id
==========================

.. c:function:: struct fwtty_peer *__fwserial_peer_by_node_id(struct fw_card *card, int generation, int id)

    finds a peer matching the given generation + id

    :param struct fw_card \*card:
        *undescribed*

    :param int generation:
        *undescribed*

    :param int id:
        *undescribed*

.. _`__fwserial_peer_by_node_id.description`:

Description
-----------

If a matching peer could not be found for the specified generation/node id,

.. _`__fwserial_peer_by_node_id.this-could-be-because`:

this could be because
---------------------

a) the generation has changed and one of the nodes hasn't updated yet
b) the remote node has created its remote unit device before this
local node has created its corresponding remote unit device
In either case, the remote node should retry

.. _`__fwserial_peer_by_node_id.note`:

Note
----

caller must be in \ :c:func:`rcu_read_lock`\  section

.. _`fwserial_add_peer`:

fwserial_add_peer
=================

.. c:function:: int fwserial_add_peer(struct fw_serial *serial, struct fw_unit *unit)

    add a newly probed 'serial' unit device as a 'peer'

    :param struct fw_serial \*serial:
        aggregate representing the specific fw_card to add the peer to

    :param struct fw_unit \*unit:
        'peer' to create and add to peer_list of serial

.. _`fwserial_add_peer.description`:

Description
-----------

Adds a 'peer' (ie, a local or remote 'serial' unit device) to the list of
peers for a specific fw_card. Optionally, auto-attach this peer to an
available tty port. This function is called either directly or indirectly
as a result of a 'serial' unit device being created & probed.

.. _`fwserial_add_peer.note`:

Note
----

this function is serialized with \ :c:func:`fwserial_remove_peer`\  by the
fwserial_list_mutex held in \ :c:func:`fwserial_probe`\ .

A 1:1 correspondence between an fw_unit and an fwtty_peer is maintained
via the \ :c:func:`dev_set_drvdata`\  for the device of the fw_unit.

.. _`fwserial_remove_peer`:

fwserial_remove_peer
====================

.. c:function:: void fwserial_remove_peer(struct fwtty_peer *peer)

    remove a 'serial' unit device as a 'peer'

    :param struct fwtty_peer \*peer:
        *undescribed*

.. _`fwserial_remove_peer.description`:

Description
-----------

Remove a 'peer' from its list of peers. This function is only
called by \ :c:func:`fwserial_remove`\  on bus removal of the unit device.

.. _`fwserial_remove_peer.note`:

Note
----

this function is serialized with \ :c:func:`fwserial_add_peer`\  by the
fwserial_list_mutex held in \ :c:func:`fwserial_remove`\ .

.. _`fwserial_create`:

fwserial_create
===============

.. c:function:: int fwserial_create(struct fw_unit *unit)

    init everything to create TTYs for a specific fw_card

    :param struct fw_unit \*unit:
        fw_unit for first 'serial' unit device probed for this fw_card

.. _`fwserial_create.description`:

Description
-----------

This function inits the aggregate structure (an fw_serial instance)
used to manage the TTY ports registered by a specific fw_card. Also, the
unit device is added as the first 'peer'.

This unit device may represent a local unit device (as specified by the
config ROM unit directory) or it may represent a remote unit device
(as specified by the reading of the remote node's config ROM).

Returns 0 to indicate "ownership" of the unit device, or a negative errno
value to indicate which error.

.. _`fwserial_probe`:

fwserial_probe
==============

.. c:function:: int fwserial_probe(struct fw_unit *unit, const struct ieee1394_device_id *id)

    bus probe function for firewire 'serial' unit devices

    :param struct fw_unit \*unit:
        *undescribed*

    :param const struct ieee1394_device_id \*id:
        *undescribed*

.. _`fwserial_probe.description`:

Description
-----------

A 'serial' unit device is created and probed as a result of:
- declaring a ieee1394 bus id table for 'devices' matching a fabricated
'serial' unit specifier id
- adding a unit directory to the config ROM(s) for a 'serial' unit

The firewire core registers unit devices by enumerating unit directories
of a node's config ROM after reading the config ROM when a new node is
added to the bus topology after a bus reset.

.. _`fwserial_probe.the-practical-implications-of-this-are`:

The practical implications of this are
--------------------------------------

- this probe is called for both local and remote nodes that have a 'serial'
unit directory in their config ROM (that matches the specifiers in
fwserial_id_table).
- no specific order is enforced for local vs. remote unit devices

This unit driver copes with the lack of specific order in the same way the
firewire net driver does -- each probe, for either a local or remote unit
device, is treated as a 'peer' (has a struct fwtty_peer instance) and the
first peer created for a given fw_card (tracked by the global fwserial_list)
creates the underlying TTYs (aggregated in a fw_serial instance).

NB: an early attempt to differentiate local & remote unit devices by creating
peers only for remote units and fw_serial instances (with their
associated TTY devices) only for local units was discarded. Managing
the peer lifetimes on device removal proved too complicated.

fwserial_probe/fwserial_remove are effectively serialized by the
fwserial_list_mutex. This is necessary because the addition of the first peer
for a given fw_card will trigger the creation of the fw_serial for that
fw_card, which must not simultaneously contend with the removal of the
last peer for a given fw_card triggering the destruction of the same
fw_serial for the same fw_card.

.. _`fwserial_remove`:

fwserial_remove
===============

.. c:function:: void fwserial_remove(struct fw_unit *unit)

    bus removal function for firewire 'serial' unit devices

    :param struct fw_unit \*unit:
        *undescribed*

.. _`fwserial_remove.description`:

Description
-----------

The corresponding 'peer' for this unit device is removed from the list of
peers for the associated fw_serial (which has a 1:1 correspondence with a
specific fw_card). If this is the last peer being removed, then trigger
the destruction of the underlying TTYs.

.. _`fwserial_update`:

fwserial_update
===============

.. c:function:: void fwserial_update(struct fw_unit *unit)

    bus update function for 'firewire' serial unit devices

    :param struct fw_unit \*unit:
        *undescribed*

.. _`fwserial_update.description`:

Description
-----------

Updates the new node_id and bus generation for this peer. Note that locking
is unnecessary; but careful memory barrier usage is important to enforce the
load and store order of generation & node_id.

The fw-core orders the write of node_id before generation in the parent
fw_device to ensure that a stale node_id cannot be used with a current
bus generation. So the generation value must be read before the node_id.

In turn, this orders the write of node_id before generation in the peer to
also ensure a stale node_id cannot be used with a current bus generation.

.. _`fwserial_handle_plug_req`:

fwserial_handle_plug_req
========================

.. c:function:: void fwserial_handle_plug_req(struct work_struct *work)

    handle VIRT_CABLE_PLUG request work

    :param struct work_struct \*work:
        ptr to peer->work

.. _`fwserial_handle_plug_req.description`:

Description
-----------

Attempts to complete the VIRT_CABLE_PLUG handshake sequence for this peer.

This checks for a collided request-- ie, that a VIRT_CABLE_PLUG request was
already sent to this peer. If so, the collision is resolved by comparing
guid values; the loser sends the plug response.

.. _`fwserial_handle_plug_req.note`:

Note
----

if an error prevents a response, don't do anything -- the
remote will timeout its request.

.. _`fwserial_mgmt_handler`:

fwserial_mgmt_handler
=====================

.. c:function:: void fwserial_mgmt_handler(struct fw_card *card, struct fw_request *request, int tcode, int destination, int source, int generation, unsigned long long addr, void *data, size_t len, void *callback_data)

    bus address handler for mgmt requests

    :param struct fw_card \*card:
        *undescribed*

    :param struct fw_request \*request:
        *undescribed*

    :param int tcode:
        *undescribed*

    :param int destination:
        *undescribed*

    :param int source:
        *undescribed*

    :param int generation:
        *undescribed*

    :param unsigned long long addr:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param size_t len:
        *undescribed*

    :param void \*callback_data:
        *undescribed*

.. _`fwserial_mgmt_handler.description`:

Description
-----------

This handler is responsible for handling virtual cable requests from remotes
for all cards.

.. This file was automatic generated / don't edit.

