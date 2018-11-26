.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/n_gsm.c

.. _`gsm_mux_net`:

struct gsm_mux_net
==================

.. c:type:: struct gsm_mux_net

    network interface \ ``struct``\  gsm_dlci\* dlci

.. _`gsm_mux_net.definition`:

Definition
----------

.. code-block:: c

    struct gsm_mux_net {
        struct kref ref;
        struct gsm_dlci *dlci;
    }

.. _`gsm_mux_net.members`:

Members
-------

ref
    *undescribed*

dlci
    *undescribed*

.. _`gsm_mux_net.description`:

Description
-----------

Created when net interface is initialized.

.. _`gsm_fcs_add`:

gsm_fcs_add
===========

.. c:function:: u8 gsm_fcs_add(u8 fcs, u8 c)

    update FCS

    :param fcs:
        Current FCS
    :type fcs: u8

    :param c:
        Next data
    :type c: u8

.. _`gsm_fcs_add.description`:

Description
-----------

Update the FCS to include c. Uses the algorithm in the specification
notes.

.. _`gsm_fcs_add_block`:

gsm_fcs_add_block
=================

.. c:function:: u8 gsm_fcs_add_block(u8 fcs, u8 *c, int len)

    update FCS for a block

    :param fcs:
        Current FCS
    :type fcs: u8

    :param c:
        buffer of data
    :type c: u8 \*

    :param len:
        length of buffer
    :type len: int

.. _`gsm_fcs_add_block.description`:

Description
-----------

Update the FCS to include c. Uses the algorithm in the specification
notes.

.. _`gsm_read_ea`:

gsm_read_ea
===========

.. c:function:: int gsm_read_ea(unsigned int *val, u8 c)

    read a byte into an EA

    :param val:
        variable holding value
        c: byte going into the EA
    :type val: unsigned int \*

    :param c:
        *undescribed*
    :type c: u8

.. _`gsm_read_ea.description`:

Description
-----------

Processes one byte of an EA. Updates the passed variable
and returns 1 if the EA is now completely read

.. _`gsm_encode_modem`:

gsm_encode_modem
================

.. c:function:: u8 gsm_encode_modem(const struct gsm_dlci *dlci)

    encode modem data bits

    :param dlci:
        DLCI to encode from
    :type dlci: const struct gsm_dlci \*

.. _`gsm_encode_modem.description`:

Description
-----------

Returns the correct GSM encoded modem status bits (6 bit field) for
the current status of the DLCI and attached tty object

.. _`gsm_print_packet`:

gsm_print_packet
================

.. c:function:: void gsm_print_packet(const char *hdr, int addr, int cr, u8 control, const u8 *data, int dlen)

    display a frame for debug

    :param hdr:
        header to print before decode
    :type hdr: const char \*

    :param addr:
        address EA from the frame
    :type addr: int

    :param cr:
        C/R bit from the frame
    :type cr: int

    :param control:
        control including PF bit
    :type control: u8

    :param data:
        following data bytes
    :type data: const u8 \*

    :param dlen:
        length of data
    :type dlen: int

.. _`gsm_print_packet.description`:

Description
-----------

Displays a packet in human readable format for debugging purposes. The
style is based on amateur radio LAP-B dump display.

.. _`gsm_stuff_frame`:

gsm_stuff_frame
===============

.. c:function:: int gsm_stuff_frame(const u8 *input, u8 *output, int len)

    bytestuff a packet

    :param input:
        *undescribed*
    :type input: const u8 \*

    :param output:
        *undescribed*
    :type output: u8 \*

    :param len:
        length of input
    :type len: int

.. _`gsm_stuff_frame.description`:

Description
-----------

Expand a buffer by bytestuffing it. The worst case size change
is doubling and the caller is responsible for handing out
suitable sized buffers.

.. _`gsm_send`:

gsm_send
========

.. c:function:: void gsm_send(struct gsm_mux *gsm, int addr, int cr, int control)

    send a control frame

    :param gsm:
        our GSM mux
    :type gsm: struct gsm_mux \*

    :param addr:
        address for control frame
    :type addr: int

    :param cr:
        command/response bit
    :type cr: int

    :param control:
        control byte including PF bit
    :type control: int

.. _`gsm_send.description`:

Description
-----------

Format up and transmit a control frame. These do not go via the
queueing logic as they should be transmitted ahead of data when
they are needed.

.. _`gsm_send.fixme`:

FIXME
-----

Lock versus data TX path

.. _`gsm_response`:

gsm_response
============

.. c:function:: void gsm_response(struct gsm_mux *gsm, int addr, int control)

    send a control response

    :param gsm:
        our GSM mux
    :type gsm: struct gsm_mux \*

    :param addr:
        address for control frame
    :type addr: int

    :param control:
        control byte including PF bit
    :type control: int

.. _`gsm_response.description`:

Description
-----------

Format up and transmit a link level response frame.

.. _`gsm_command`:

gsm_command
===========

.. c:function:: void gsm_command(struct gsm_mux *gsm, int addr, int control)

    send a control command

    :param gsm:
        our GSM mux
    :type gsm: struct gsm_mux \*

    :param addr:
        address for control frame
    :type addr: int

    :param control:
        control byte including PF bit
    :type control: int

.. _`gsm_command.description`:

Description
-----------

Format up and transmit a link level command frame.

.. _`gsm_data_alloc`:

gsm_data_alloc
==============

.. c:function:: struct gsm_msg *gsm_data_alloc(struct gsm_mux *gsm, u8 addr, int len, u8 ctrl)

    allocate data frame

    :param gsm:
        GSM mux
    :type gsm: struct gsm_mux \*

    :param addr:
        DLCI address
    :type addr: u8

    :param len:
        length excluding header and FCS
    :type len: int

    :param ctrl:
        control byte
    :type ctrl: u8

.. _`gsm_data_alloc.description`:

Description
-----------

Allocate a new data buffer for sending frames with data. Space is left
at the front for header bytes but that is treated as an implementation
detail and not for the high level code to use

.. _`gsm_data_kick`:

gsm_data_kick
=============

.. c:function:: void gsm_data_kick(struct gsm_mux *gsm)

    poke the queue

    :param gsm:
        GSM Mux
    :type gsm: struct gsm_mux \*

.. _`gsm_data_kick.description`:

Description
-----------

The tty device has called us to indicate that room has appeared in
the transmit queue. Ram more data into the pipe if we have any
If we have been flow-stopped by a CMD_FCOFF, then we can only
send messages on DLCI0 until CMD_FCON

.. _`gsm_data_kick.fixme`:

FIXME
-----

lock against link layer control transmissions

.. _`__gsm_data_queue`:

\__gsm_data_queue
=================

.. c:function:: void __gsm_data_queue(struct gsm_dlci *dlci, struct gsm_msg *msg)

    queue a UI or UIH frame

    :param dlci:
        DLCI sending the data
    :type dlci: struct gsm_dlci \*

    :param msg:
        message queued
    :type msg: struct gsm_msg \*

.. _`__gsm_data_queue.description`:

Description
-----------

Add data to the transmit queue and try and get stuff moving
out of the mux tty if not already doing so. The Caller must hold
the gsm tx lock.

.. _`gsm_data_queue`:

gsm_data_queue
==============

.. c:function:: void gsm_data_queue(struct gsm_dlci *dlci, struct gsm_msg *msg)

    queue a UI or UIH frame

    :param dlci:
        DLCI sending the data
    :type dlci: struct gsm_dlci \*

    :param msg:
        message queued
    :type msg: struct gsm_msg \*

.. _`gsm_data_queue.description`:

Description
-----------

Add data to the transmit queue and try and get stuff moving
out of the mux tty if not already doing so. Take the
the gsm tx lock and dlci lock.

.. _`gsm_dlci_data_output`:

gsm_dlci_data_output
====================

.. c:function:: int gsm_dlci_data_output(struct gsm_mux *gsm, struct gsm_dlci *dlci)

    try and push data out of a DLCI

    :param gsm:
        mux
    :type gsm: struct gsm_mux \*

    :param dlci:
        the DLCI to pull data from
    :type dlci: struct gsm_dlci \*

.. _`gsm_dlci_data_output.description`:

Description
-----------

Pull data from a DLCI and send it into the transmit queue if there
is data. Keep to the MRU of the mux. This path handles the usual tty
interface which is a byte stream with optional modem data.

Caller must hold the tx_lock of the mux.

.. _`gsm_dlci_data_output_framed`:

gsm_dlci_data_output_framed
===========================

.. c:function:: int gsm_dlci_data_output_framed(struct gsm_mux *gsm, struct gsm_dlci *dlci)

    try and push data out of a DLCI

    :param gsm:
        mux
    :type gsm: struct gsm_mux \*

    :param dlci:
        the DLCI to pull data from
    :type dlci: struct gsm_dlci \*

.. _`gsm_dlci_data_output_framed.description`:

Description
-----------

Pull data from a DLCI and send it into the transmit queue if there
is data. Keep to the MRU of the mux. This path handles framed data
queued as skbuffs to the DLCI.

Caller must hold the tx_lock of the mux.

.. _`gsm_dlci_data_sweep`:

gsm_dlci_data_sweep
===================

.. c:function:: void gsm_dlci_data_sweep(struct gsm_mux *gsm)

    look for data to send

    :param gsm:
        the GSM mux
    :type gsm: struct gsm_mux \*

.. _`gsm_dlci_data_sweep.description`:

Description
-----------

Sweep the GSM mux channels in priority order looking for ones with
data to send. We could do with optimising this scan a bit. We aim
to fill the queue totally or up to TX_THRESH_HI bytes. Once we hit
TX_THRESH_LO we get called again

.. _`gsm_dlci_data_sweep.fixme`:

FIXME
-----

We should round robin between groups and in theory you can
renegotiate DLCI priorities with optional stuff. Needs optimising.

.. _`gsm_dlci_data_kick`:

gsm_dlci_data_kick
==================

.. c:function:: void gsm_dlci_data_kick(struct gsm_dlci *dlci)

    transmit if possible

    :param dlci:
        DLCI to kick
    :type dlci: struct gsm_dlci \*

.. _`gsm_dlci_data_kick.description`:

Description
-----------

Transmit data from this DLCI if the queue is empty. We can't rely on
a tty wakeup except when we filled the pipe so we need to fire off
new data ourselves in other cases.

.. _`gsm_control_reply`:

gsm_control_reply
=================

.. c:function:: void gsm_control_reply(struct gsm_mux *gsm, int cmd, u8 *data, int dlen)

    send a response frame to a control

    :param gsm:
        gsm channel
    :type gsm: struct gsm_mux \*

    :param cmd:
        the command to use
    :type cmd: int

    :param data:
        data to follow encoded info
    :type data: u8 \*

    :param dlen:
        length of data
    :type dlen: int

.. _`gsm_control_reply.description`:

Description
-----------

Encode up and queue a UI/UIH frame containing our response.

.. _`gsm_process_modem`:

gsm_process_modem
=================

.. c:function:: void gsm_process_modem(struct tty_struct *tty, struct gsm_dlci *dlci, u32 modem, int clen)

    process received modem status

    :param tty:
        virtual tty bound to the DLCI
    :type tty: struct tty_struct \*

    :param dlci:
        DLCI to affect
    :type dlci: struct gsm_dlci \*

    :param modem:
        modem bits (full EA)
    :type modem: u32

    :param clen:
        *undescribed*
    :type clen: int

.. _`gsm_process_modem.description`:

Description
-----------

Used when a modem control message or line state inline in adaption
layer 2 is processed. Sort out the local modem state and throttles

.. _`gsm_control_modem`:

gsm_control_modem
=================

.. c:function:: void gsm_control_modem(struct gsm_mux *gsm, u8 *data, int clen)

    modem status received

    :param gsm:
        GSM channel
    :type gsm: struct gsm_mux \*

    :param data:
        data following command
    :type data: u8 \*

    :param clen:
        command length
    :type clen: int

.. _`gsm_control_modem.description`:

Description
-----------

We have received a modem status control message. This is used by
the GSM mux protocol to pass virtual modem line status and optionally
to indicate break signals. Unpack it, convert to Linux representation
and if need be stuff a break message down the tty.

.. _`gsm_control_rls`:

gsm_control_rls
===============

.. c:function:: void gsm_control_rls(struct gsm_mux *gsm, u8 *data, int clen)

    remote line status

    :param gsm:
        GSM channel
    :type gsm: struct gsm_mux \*

    :param data:
        data bytes
    :type data: u8 \*

    :param clen:
        data length
    :type clen: int

.. _`gsm_control_rls.description`:

Description
-----------

The modem sends us a two byte message on the control channel whenever
it wishes to send us an error state from the virtual link. Stuff
this into the uplink tty if present

.. _`gsm_control_message`:

gsm_control_message
===================

.. c:function:: void gsm_control_message(struct gsm_mux *gsm, unsigned int command, u8 *data, int clen)

    DLCI 0 control processing

    :param gsm:
        our GSM mux
    :type gsm: struct gsm_mux \*

    :param command:
        the command EA
    :type command: unsigned int

    :param data:
        data beyond the command/length EAs
    :type data: u8 \*

    :param clen:
        length
    :type clen: int

.. _`gsm_control_message.description`:

Description
-----------

Input processor for control messages from the other end of the link.
Processes the incoming request and queues a response frame or an
NSC response if not supported

.. _`gsm_control_response`:

gsm_control_response
====================

.. c:function:: void gsm_control_response(struct gsm_mux *gsm, unsigned int command, u8 *data, int clen)

    process a response to our control

    :param gsm:
        our GSM mux
    :type gsm: struct gsm_mux \*

    :param command:
        the command (response) EA
    :type command: unsigned int

    :param data:
        data beyond the command/length EA
    :type data: u8 \*

    :param clen:
        length
    :type clen: int

.. _`gsm_control_response.description`:

Description
-----------

Process a response to an outstanding command. We only allow a single
control message in flight so this is fairly easy. All the clean up
is done by the caller, we just update the fields, flag it as done
and return

.. _`gsm_control_transmit`:

gsm_control_transmit
====================

.. c:function:: void gsm_control_transmit(struct gsm_mux *gsm, struct gsm_control *ctrl)

    send control packet

    :param gsm:
        gsm mux
    :type gsm: struct gsm_mux \*

    :param ctrl:
        frame to send
    :type ctrl: struct gsm_control \*

.. _`gsm_control_transmit.description`:

Description
-----------

Send out a pending control command (called under control lock)

.. _`gsm_control_retransmit`:

gsm_control_retransmit
======================

.. c:function:: void gsm_control_retransmit(struct timer_list *t)

    retransmit a control frame

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`gsm_control_retransmit.description`:

Description
-----------

Called off the T2 timer expiry in order to retransmit control frames
that have been lost in the system somewhere. The control_lock protects
us from colliding with another sender or a receive completion event.
In that situation the timer may still occur in a small window but
gsm->pending_cmd will be NULL and we just let the timer expire.

.. _`gsm_control_send`:

gsm_control_send
================

.. c:function:: struct gsm_control *gsm_control_send(struct gsm_mux *gsm, unsigned int command, u8 *data, int clen)

    send a control frame on DLCI 0

    :param gsm:
        the GSM channel
    :type gsm: struct gsm_mux \*

    :param command:
        command  to send including CR bit
    :type command: unsigned int

    :param data:
        bytes of data (must be kmalloced)
    :type data: u8 \*

    :param clen:
        *undescribed*
    :type clen: int

.. _`gsm_control_send.description`:

Description
-----------

Queue and dispatch a control command. Only one command can be
active at a time. In theory more can be outstanding but the matching
gets really complicated so for now stick to one outstanding.

.. _`gsm_control_wait`:

gsm_control_wait
================

.. c:function:: int gsm_control_wait(struct gsm_mux *gsm, struct gsm_control *control)

    wait for a control to finish

    :param gsm:
        GSM mux
    :type gsm: struct gsm_mux \*

    :param control:
        control we are waiting on
    :type control: struct gsm_control \*

.. _`gsm_control_wait.description`:

Description
-----------

Waits for the control to complete or time out. Frees any used
resources and returns 0 for success, or an error if the remote
rejected or ignored the request.

.. _`gsm_dlci_close`:

gsm_dlci_close
==============

.. c:function:: void gsm_dlci_close(struct gsm_dlci *dlci)

    a DLCI has closed

    :param dlci:
        DLCI that closed
    :type dlci: struct gsm_dlci \*

.. _`gsm_dlci_close.description`:

Description
-----------

Perform processing when moving a DLCI into closed state. If there
is an attached tty this is hung up

.. _`gsm_dlci_open`:

gsm_dlci_open
=============

.. c:function:: void gsm_dlci_open(struct gsm_dlci *dlci)

    a DLCI has opened

    :param dlci:
        DLCI that opened
    :type dlci: struct gsm_dlci \*

.. _`gsm_dlci_open.description`:

Description
-----------

Perform processing when moving a DLCI into open state.

.. _`gsm_dlci_t1`:

gsm_dlci_t1
===========

.. c:function:: void gsm_dlci_t1(struct timer_list *t)

    T1 timer expiry

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`gsm_dlci_t1.description`:

Description
-----------

The T1 timer handles retransmits of control frames (essentially of
SABM and DISC). We resend the command until the retry count runs out
in which case an opening port goes back to closed and a closing port
is simply put into closed state (any further frames from the other
end will get a DM response)

Some control dlci can stay in ADM mode with other dlci working just
fine. In that case we can just keep the control dlci open after the
DLCI_OPENING retries time out.

.. _`gsm_dlci_begin_open`:

gsm_dlci_begin_open
===================

.. c:function:: void gsm_dlci_begin_open(struct gsm_dlci *dlci)

    start channel open procedure

    :param dlci:
        DLCI to open
    :type dlci: struct gsm_dlci \*

.. _`gsm_dlci_begin_open.description`:

Description
-----------

Commence opening a DLCI from the Linux side. We issue SABM messages
to the modem which should then reply with a UA or ADM, at which point
we will move into open state. Opening is done asynchronously with retry
running off timers and the responses.

.. _`gsm_dlci_begin_close`:

gsm_dlci_begin_close
====================

.. c:function:: void gsm_dlci_begin_close(struct gsm_dlci *dlci)

    start channel open procedure

    :param dlci:
        DLCI to open
    :type dlci: struct gsm_dlci \*

.. _`gsm_dlci_begin_close.description`:

Description
-----------

Commence closing a DLCI from the Linux side. We issue DISC messages
to the modem which should then reply with a UA, at which point we
will move into closed state. Closing is done asynchronously with retry
off timers. We may also receive a DM reply from the other end which
indicates the channel was already closed.

.. _`gsm_dlci_data`:

gsm_dlci_data
=============

.. c:function:: void gsm_dlci_data(struct gsm_dlci *dlci, u8 *data, int clen)

    data arrived

    :param dlci:
        channel
    :type dlci: struct gsm_dlci \*

    :param data:
        block of bytes received
    :type data: u8 \*

    :param clen:
        *undescribed*
    :type clen: int

.. _`gsm_dlci_data.description`:

Description
-----------

A UI or UIH frame has arrived which contains data for a channel
other than the control channel. If the relevant virtual tty is
open we shovel the bits down it, if not we drop them.

.. _`gsm_dlci_command`:

gsm_dlci_command
================

.. c:function:: void gsm_dlci_command(struct gsm_dlci *dlci, u8 *data, int len)

    data arrived on control channel

    :param dlci:
        channel
    :type dlci: struct gsm_dlci \*

    :param data:
        block of bytes received
    :type data: u8 \*

    :param len:
        length of received block
    :type len: int

.. _`gsm_dlci_command.description`:

Description
-----------

A UI or UIH frame has arrived which contains data for DLCI 0 the
control channel. This should contain a command EA followed by
control data bytes. The command EA contains a command/response bit
and we divide up the work accordingly.

.. _`gsm_dlci_alloc`:

gsm_dlci_alloc
==============

.. c:function:: struct gsm_dlci *gsm_dlci_alloc(struct gsm_mux *gsm, int addr)

    allocate a DLCI

    :param gsm:
        GSM mux
    :type gsm: struct gsm_mux \*

    :param addr:
        address of the DLCI
    :type addr: int

.. _`gsm_dlci_alloc.description`:

Description
-----------

Allocate and install a new DLCI object into the GSM mux.

.. _`gsm_dlci_alloc.fixme`:

FIXME
-----

review locking races

.. _`gsm_dlci_free`:

gsm_dlci_free
=============

.. c:function:: void gsm_dlci_free(struct tty_port *port)

    free DLCI

    :param port:
        *undescribed*
    :type port: struct tty_port \*

.. _`gsm_dlci_free.description`:

Description
-----------

Free up a DLCI.

Can sleep.

.. _`gsm_dlci_release`:

gsm_dlci_release
================

.. c:function:: void gsm_dlci_release(struct gsm_dlci *dlci)

    release DLCI

    :param dlci:
        DLCI to destroy
    :type dlci: struct gsm_dlci \*

.. _`gsm_dlci_release.description`:

Description
-----------

Release a DLCI. Actual free is deferred until either
mux is closed or tty is closed - whichever is last.

Can sleep.

.. _`gsm_queue`:

gsm_queue
=========

.. c:function:: void gsm_queue(struct gsm_mux *gsm)

    a GSM frame is ready to process

    :param gsm:
        pointer to our gsm mux
    :type gsm: struct gsm_mux \*

.. _`gsm_queue.description`:

Description
-----------

At this point in time a frame has arrived and been demangled from
the line encoding. All the differences between the encodings have
been handled below us and the frame is unpacked into the structures.
The fcs holds the header FCS but any data FCS must be added here.

.. _`gsm0_receive`:

gsm0_receive
============

.. c:function:: void gsm0_receive(struct gsm_mux *gsm, unsigned char c)

    perform processing for non-transparency

    :param gsm:
        gsm data for this ldisc instance
    :type gsm: struct gsm_mux \*

    :param c:
        character
    :type c: unsigned char

.. _`gsm0_receive.description`:

Description
-----------

Receive bytes in gsm mode 0

.. _`gsm1_receive`:

gsm1_receive
============

.. c:function:: void gsm1_receive(struct gsm_mux *gsm, unsigned char c)

    perform processing for non-transparency

    :param gsm:
        gsm data for this ldisc instance
    :type gsm: struct gsm_mux \*

    :param c:
        character
    :type c: unsigned char

.. _`gsm1_receive.description`:

Description
-----------

Receive bytes in mode 1 (Advanced option)

.. _`gsm_error`:

gsm_error
=========

.. c:function:: void gsm_error(struct gsm_mux *gsm, unsigned char data, unsigned char flag)

    handle tty error

    :param gsm:
        ldisc data
    :type gsm: struct gsm_mux \*

    :param data:
        byte received (may be invalid)
    :type data: unsigned char

    :param flag:
        error received
    :type flag: unsigned char

.. _`gsm_error.description`:

Description
-----------

Handle an error in the receipt of data for a frame. Currently we just
go back to hunting for a SOF.

.. _`gsm_error.fixme`:

FIXME
-----

better diagnostics ?

.. _`gsm_cleanup_mux`:

gsm_cleanup_mux
===============

.. c:function:: void gsm_cleanup_mux(struct gsm_mux *gsm)

    generic GSM protocol cleanup

    :param gsm:
        our mux
    :type gsm: struct gsm_mux \*

.. _`gsm_cleanup_mux.description`:

Description
-----------

Clean up the bits of the mux which are the same for all framing
protocols. Remove the mux from the mux table, stop all the timers
and then shut down each device hanging up the channels as we go.

.. _`gsm_activate_mux`:

gsm_activate_mux
================

.. c:function:: int gsm_activate_mux(struct gsm_mux *gsm)

    generic GSM setup

    :param gsm:
        our mux
    :type gsm: struct gsm_mux \*

.. _`gsm_activate_mux.description`:

Description
-----------

Set up the bits of the mux which are the same for all framing
protocols. Add the mux to the mux table so it can be opened and
finally kick off connecting to DLCI 0 on the modem.

.. _`gsm_free_mux`:

gsm_free_mux
============

.. c:function:: void gsm_free_mux(struct gsm_mux *gsm)

    free up a mux

    :param gsm:
        *undescribed*
    :type gsm: struct gsm_mux \*

.. _`gsm_free_mux.description`:

Description
-----------

Dispose of allocated resources for a dead mux

.. _`gsm_free_muxr`:

gsm_free_muxr
=============

.. c:function:: void gsm_free_muxr(struct kref *ref)

    free up a mux

    :param ref:
        *undescribed*
    :type ref: struct kref \*

.. _`gsm_free_muxr.description`:

Description
-----------

Dispose of allocated resources for a dead mux

.. _`gsm_alloc_mux`:

gsm_alloc_mux
=============

.. c:function:: struct gsm_mux *gsm_alloc_mux( void)

    allocate a mux

    :param void:
        no arguments
    :type void: 

.. _`gsm_alloc_mux.description`:

Description
-----------

Creates a new mux ready for activation.

.. _`gsmld_output`:

gsmld_output
============

.. c:function:: int gsmld_output(struct gsm_mux *gsm, u8 *data, int len)

    write to link

    :param gsm:
        our mux
    :type gsm: struct gsm_mux \*

    :param data:
        bytes to output
    :type data: u8 \*

    :param len:
        size
    :type len: int

.. _`gsmld_output.description`:

Description
-----------

Write a block of data from the GSM mux to the data channel. This
will eventually be serialized from above but at the moment isn't.

.. _`gsmld_attach_gsm`:

gsmld_attach_gsm
================

.. c:function:: int gsmld_attach_gsm(struct tty_struct *tty, struct gsm_mux *gsm)

    mode set up

    :param tty:
        our tty structure
    :type tty: struct tty_struct \*

    :param gsm:
        our mux
    :type gsm: struct gsm_mux \*

.. _`gsmld_attach_gsm.description`:

Description
-----------

Set up the MUX for basic mode and commence connecting to the
modem. Currently called from the line discipline set up but
will need moving to an ioctl path.

.. _`gsmld_detach_gsm`:

gsmld_detach_gsm
================

.. c:function:: void gsmld_detach_gsm(struct tty_struct *tty, struct gsm_mux *gsm)

    stop doing 0710 mux

    :param tty:
        tty attached to the mux
    :type tty: struct tty_struct \*

    :param gsm:
        mux
    :type gsm: struct gsm_mux \*

.. _`gsmld_detach_gsm.description`:

Description
-----------

Shutdown and then clean up the resources used by the line discipline

.. _`gsmld_flush_buffer`:

gsmld_flush_buffer
==================

.. c:function:: void gsmld_flush_buffer(struct tty_struct *tty)

    clean input queue

    :param tty:
        terminal device
    :type tty: struct tty_struct \*

.. _`gsmld_flush_buffer.description`:

Description
-----------

Flush the input buffer. Called when the line discipline is
being closed, when the tty layer wants the buffer flushed (eg
at hangup).

.. _`gsmld_close`:

gsmld_close
===========

.. c:function:: void gsmld_close(struct tty_struct *tty)

    close the ldisc for this tty

    :param tty:
        device
    :type tty: struct tty_struct \*

.. _`gsmld_close.description`:

Description
-----------

Called from the terminal layer when this line discipline is
being shut down, either because of a close or becsuse of a
discipline change. The function will not be called while other
ldisc methods are in progress.

.. _`gsmld_open`:

gsmld_open
==========

.. c:function:: int gsmld_open(struct tty_struct *tty)

    open an ldisc

    :param tty:
        terminal to open
    :type tty: struct tty_struct \*

.. _`gsmld_open.description`:

Description
-----------

Called when this line discipline is being attached to the
terminal device. Can sleep. Called serialized so that no
other events will occur in parallel. No further open will occur
until a close.

.. _`gsmld_write_wakeup`:

gsmld_write_wakeup
==================

.. c:function:: void gsmld_write_wakeup(struct tty_struct *tty)

    asynchronous I/O notifier

    :param tty:
        tty device
    :type tty: struct tty_struct \*

.. _`gsmld_write_wakeup.description`:

Description
-----------

Required for the ptys, serial driver etc. since processes
that attach themselves to the master and rely on ASYNC
IO must be woken up

.. _`gsmld_read`:

gsmld_read
==========

.. c:function:: ssize_t gsmld_read(struct tty_struct *tty, struct file *file, unsigned char __user *buf, size_t nr)

    read function for tty

    :param tty:
        tty device
    :type tty: struct tty_struct \*

    :param file:
        file object
    :type file: struct file \*

    :param buf:
        userspace buffer pointer
    :type buf: unsigned char __user \*

    :param nr:
        size of I/O
    :type nr: size_t

.. _`gsmld_read.description`:

Description
-----------

Perform reads for the line discipline. We are guaranteed that the
line discipline will not be closed under us but we may get multiple
parallel readers and must handle this ourselves. We may also get
a hangup. Always called in user context, may sleep.

This code must be sure never to sleep through a hangup.

.. _`gsmld_write`:

gsmld_write
===========

.. c:function:: ssize_t gsmld_write(struct tty_struct *tty, struct file *file, const unsigned char *buf, size_t nr)

    write function for tty

    :param tty:
        tty device
    :type tty: struct tty_struct \*

    :param file:
        file object
    :type file: struct file \*

    :param buf:
        userspace buffer pointer
    :type buf: const unsigned char \*

    :param nr:
        size of I/O
    :type nr: size_t

.. _`gsmld_write.description`:

Description
-----------

Called when the owner of the device wants to send a frame
itself (or some other control data). The data is transferred
as-is and must be properly framed and checksummed as appropriate
by userspace. Frames are either sent whole or not at all as this
avoids pain user side.

.. _`gsmld_poll`:

gsmld_poll
==========

.. c:function:: __poll_t gsmld_poll(struct tty_struct *tty, struct file *file, poll_table *wait)

    poll method for N_GSM0710

    :param tty:
        terminal device
    :type tty: struct tty_struct \*

    :param file:
        file accessing it
    :type file: struct file \*

    :param wait:
        poll table
    :type wait: poll_table \*

.. _`gsmld_poll.description`:

Description
-----------

Called when the line discipline is asked to \ :c:func:`poll`\  for data or
for special events. This code is not serialized with respect to
other events save open/close.

This code must be sure never to sleep through a hangup.
Called without the kernel lock held - fine

.. This file was automatic generated / don't edit.

