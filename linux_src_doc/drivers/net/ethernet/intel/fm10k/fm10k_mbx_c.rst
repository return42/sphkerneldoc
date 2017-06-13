.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_mbx.c

.. _`fm10k_fifo_init`:

fm10k_fifo_init
===============

.. c:function:: void fm10k_fifo_init(struct fm10k_mbx_fifo *fifo, u32 *buffer, u16 size)

    Initialize a message FIFO

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

    :param u32 \*buffer:
        pointer to memory to be used to store FIFO

    :param u16 size:
        maximum message size to store in FIFO, must be 2^n - 1

.. _`fm10k_fifo_used`:

fm10k_fifo_used
===============

.. c:function:: u16 fm10k_fifo_used(struct fm10k_mbx_fifo *fifo)

    Retrieve used space in FIFO

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

.. _`fm10k_fifo_used.description`:

Description
-----------

This function returns the number of DWORDs used in the FIFO

.. _`fm10k_fifo_unused`:

fm10k_fifo_unused
=================

.. c:function:: u16 fm10k_fifo_unused(struct fm10k_mbx_fifo *fifo)

    Retrieve unused space in FIFO

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

.. _`fm10k_fifo_unused.description`:

Description
-----------

This function returns the number of unused DWORDs in the FIFO

.. _`fm10k_fifo_empty`:

fm10k_fifo_empty
================

.. c:function:: bool fm10k_fifo_empty(struct fm10k_mbx_fifo *fifo)

    Test to verify if FIFO is empty

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

.. _`fm10k_fifo_empty.description`:

Description
-----------

This function returns true if the FIFO is empty, else false

.. _`fm10k_fifo_head_offset`:

fm10k_fifo_head_offset
======================

.. c:function:: u16 fm10k_fifo_head_offset(struct fm10k_mbx_fifo *fifo, u16 offset)

    returns indices of head with given offset

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

    :param u16 offset:
        offset to add to head

.. _`fm10k_fifo_head_offset.description`:

Description
-----------

This function returns the indices into the FIFO based on head + offset

.. _`fm10k_fifo_tail_offset`:

fm10k_fifo_tail_offset
======================

.. c:function:: u16 fm10k_fifo_tail_offset(struct fm10k_mbx_fifo *fifo, u16 offset)

    returns indices of tail with given offset

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

    :param u16 offset:
        offset to add to tail

.. _`fm10k_fifo_tail_offset.description`:

Description
-----------

This function returns the indices into the FIFO based on tail + offset

.. _`fm10k_fifo_head_len`:

fm10k_fifo_head_len
===================

.. c:function:: u16 fm10k_fifo_head_len(struct fm10k_mbx_fifo *fifo)

    Retrieve length of first message in FIFO

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

.. _`fm10k_fifo_head_len.description`:

Description
-----------

This function returns the size of the first message in the FIFO

.. _`fm10k_fifo_head_drop`:

fm10k_fifo_head_drop
====================

.. c:function:: u16 fm10k_fifo_head_drop(struct fm10k_mbx_fifo *fifo)

    Drop the first message in FIFO

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

.. _`fm10k_fifo_head_drop.description`:

Description
-----------

This function returns the size of the message dropped from the FIFO

.. _`fm10k_fifo_drop_all`:

fm10k_fifo_drop_all
===================

.. c:function:: void fm10k_fifo_drop_all(struct fm10k_mbx_fifo *fifo)

    Drop all messages in FIFO

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

.. _`fm10k_fifo_drop_all.description`:

Description
-----------

This function resets the head pointer to drop all messages in the FIFO and
ensure the FIFO is empty.

.. _`fm10k_mbx_index_len`:

fm10k_mbx_index_len
===================

.. c:function:: u16 fm10k_mbx_index_len(struct fm10k_mbx_info *mbx, u16 head, u16 tail)

    Convert a head/tail index into a length value

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 head:
        head index

    :param u16 tail:
        head index

.. _`fm10k_mbx_index_len.description`:

Description
-----------

This function takes the head and tail index and determines the length
of the data indicated by this pair.

.. _`fm10k_mbx_tail_add`:

fm10k_mbx_tail_add
==================

.. c:function:: u16 fm10k_mbx_tail_add(struct fm10k_mbx_info *mbx, u16 offset)

    Determine new tail value with added offset

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 offset:
        length to add to tail offset

.. _`fm10k_mbx_tail_add.description`:

Description
-----------

This function takes the local tail index and recomputes it for
a given length added as an offset.

.. _`fm10k_mbx_tail_sub`:

fm10k_mbx_tail_sub
==================

.. c:function:: u16 fm10k_mbx_tail_sub(struct fm10k_mbx_info *mbx, u16 offset)

    Determine new tail value with subtracted offset

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 offset:
        length to add to tail offset

.. _`fm10k_mbx_tail_sub.description`:

Description
-----------

This function takes the local tail index and recomputes it for
a given length added as an offset.

.. _`fm10k_mbx_head_add`:

fm10k_mbx_head_add
==================

.. c:function:: u16 fm10k_mbx_head_add(struct fm10k_mbx_info *mbx, u16 offset)

    Determine new head value with added offset

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 offset:
        length to add to head offset

.. _`fm10k_mbx_head_add.description`:

Description
-----------

This function takes the local head index and recomputes it for
a given length added as an offset.

.. _`fm10k_mbx_head_sub`:

fm10k_mbx_head_sub
==================

.. c:function:: u16 fm10k_mbx_head_sub(struct fm10k_mbx_info *mbx, u16 offset)

    Determine new head value with subtracted offset

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 offset:
        length to add to head offset

.. _`fm10k_mbx_head_sub.description`:

Description
-----------

This function takes the local head index and recomputes it for
a given length added as an offset.

.. _`fm10k_mbx_pushed_tail_len`:

fm10k_mbx_pushed_tail_len
=========================

.. c:function:: u16 fm10k_mbx_pushed_tail_len(struct fm10k_mbx_info *mbx)

    Retrieve the length of message being pushed

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_pushed_tail_len.description`:

Description
-----------

This function will return the length of the message currently being
pushed onto the tail of the Rx queue.

.. _`fm10k_fifo_write_copy`:

fm10k_fifo_write_copy
=====================

.. c:function:: void fm10k_fifo_write_copy(struct fm10k_mbx_fifo *fifo, const u32 *msg, u16 tail_offset, u16 len)

    pulls data off of msg and places it in FIFO

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

    :param const u32 \*msg:
        message array to populate

    :param u16 tail_offset:
        additional offset to add to tail pointer

    :param u16 len:
        length of FIFO to copy into message header

.. _`fm10k_fifo_write_copy.description`:

Description
-----------

This function will take a message and copy it into a section of the
FIFO.  In order to get something into a location other than just
the tail you can use tail_offset to adjust the pointer.

.. _`fm10k_fifo_enqueue`:

fm10k_fifo_enqueue
==================

.. c:function:: s32 fm10k_fifo_enqueue(struct fm10k_mbx_fifo *fifo, const u32 *msg)

    Enqueues the message to the tail of the FIFO

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

    :param const u32 \*msg:
        message array to read

.. _`fm10k_fifo_enqueue.description`:

Description
-----------

This function enqueues a message up to the size specified by the length
contained in the first DWORD of the message and will place at the tail
of the FIFO.  It will return 0 on success, or a negative value on error.

.. _`fm10k_mbx_validate_msg_size`:

fm10k_mbx_validate_msg_size
===========================

.. c:function:: u16 fm10k_mbx_validate_msg_size(struct fm10k_mbx_info *mbx, u16 len)

    Validate incoming message based on size

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 len:
        length of data pushed onto buffer

.. _`fm10k_mbx_validate_msg_size.description`:

Description
-----------

This function analyzes the frame and will return a non-zero value when
the start of a message larger than the mailbox is detected.

.. _`fm10k_mbx_write_copy`:

fm10k_mbx_write_copy
====================

.. c:function:: void fm10k_mbx_write_copy(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    pulls data off of Tx FIFO and places it in mbmem

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_write_copy.description`:

Description
-----------

This function will take a section of the Tx FIFO and copy it into the
mailbox memory.  The offset in mbmem is based on the lower bits of the
tail and len determines the length to copy.

.. _`fm10k_mbx_pull_head`:

fm10k_mbx_pull_head
===================

.. c:function:: void fm10k_mbx_pull_head(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx, u16 head)

    Pulls data off of head of Tx FIFO

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 head:
        acknowledgement number last received

.. _`fm10k_mbx_pull_head.description`:

Description
-----------

This function will push the tail index forward based on the remote
head index.  It will then pull up to mbmem_len DWORDs off of the
head of the FIFO and will place it in the MBMEM registers
associated with the mailbox.

.. _`fm10k_mbx_read_copy`:

fm10k_mbx_read_copy
===================

.. c:function:: void fm10k_mbx_read_copy(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    pulls data off of mbmem and places it in Rx FIFO

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_read_copy.description`:

Description
-----------

This function will take a section of the mailbox memory and copy it
into the Rx FIFO.  The offset is based on the lower bits of the
head and len determines the length to copy.

.. _`fm10k_mbx_push_tail`:

fm10k_mbx_push_tail
===================

.. c:function:: s32 fm10k_mbx_push_tail(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx, u16 tail)

    Pushes up to 15 DWORDs on to tail of FIFO

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 tail:
        tail index of message

.. _`fm10k_mbx_push_tail.description`:

Description
-----------

This function will first validate the tail index and size for the
incoming message.  It then updates the acknowledgment number and
copies the data into the FIFO.  It will return the number of messages
dequeued on success and a negative value on error.

.. _`fm10k_crc_16b`:

fm10k_crc_16b
=============

.. c:function:: u16 fm10k_crc_16b(const u32 *data, u16 seed, u16 len)

    Generate a 16 bit CRC for a region of 16 bit data

    :param const u32 \*data:
        pointer to data to process

    :param u16 seed:
        seed value for CRC

    :param u16 len:
        length measured in 16 bits words

.. _`fm10k_crc_16b.description`:

Description
-----------

This function will generate a CRC based on the polynomial 0xAC9A and
whatever value is stored in the seed variable.  Note that this
value inverts the local seed and the result in order to capture all
leading and trailing zeros.

.. _`fm10k_fifo_crc`:

fm10k_fifo_crc
==============

.. c:function:: u16 fm10k_fifo_crc(struct fm10k_mbx_fifo *fifo, u16 offset, u16 len, u16 seed)

    generate a CRC based off of FIFO data

    :param struct fm10k_mbx_fifo \*fifo:
        pointer to FIFO

    :param u16 offset:
        offset point for start of FIFO

    :param u16 len:
        number of DWORDS words to process

    :param u16 seed:
        seed value for CRC

.. _`fm10k_fifo_crc.description`:

Description
-----------

This function generates a CRC for some region of the FIFO

.. _`fm10k_mbx_update_local_crc`:

fm10k_mbx_update_local_crc
==========================

.. c:function:: void fm10k_mbx_update_local_crc(struct fm10k_mbx_info *mbx, u16 head)

    Update the local CRC for outgoing data

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 head:
        head index provided by remote mailbox

.. _`fm10k_mbx_update_local_crc.description`:

Description
-----------

This function will generate the CRC for all data from the end of the
last head update to the current one.  It uses the result of the
previous CRC as the seed for this update.  The result is stored in
mbx->local.

.. _`fm10k_mbx_verify_remote_crc`:

fm10k_mbx_verify_remote_crc
===========================

.. c:function:: s32 fm10k_mbx_verify_remote_crc(struct fm10k_mbx_info *mbx)

    Verify the CRC is correct for current data

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_verify_remote_crc.description`:

Description
-----------

This function will take all data that has been provided from the remote
end and generate a CRC for it.  This is stored in mbx->remote.  The
CRC for the header is then computed and if the result is non-zero this
is an error and we signal an error dropping all data and resetting the
connection.

.. _`fm10k_mbx_rx_ready`:

fm10k_mbx_rx_ready
==================

.. c:function:: bool fm10k_mbx_rx_ready(struct fm10k_mbx_info *mbx)

    Indicates that a message is ready in the Rx FIFO

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_rx_ready.description`:

Description
-----------

This function returns true if there is a message in the Rx FIFO to dequeue.

.. _`fm10k_mbx_tx_ready`:

fm10k_mbx_tx_ready
==================

.. c:function:: bool fm10k_mbx_tx_ready(struct fm10k_mbx_info *mbx, u16 len)

    Indicates that the mailbox is in state ready for Tx

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 len:
        verify free space is >= this value

.. _`fm10k_mbx_tx_ready.description`:

Description
-----------

This function returns true if the mailbox is in a state ready to transmit.

.. _`fm10k_mbx_tx_complete`:

fm10k_mbx_tx_complete
=====================

.. c:function:: bool fm10k_mbx_tx_complete(struct fm10k_mbx_info *mbx)

    Indicates that the Tx FIFO has been emptied

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_tx_complete.description`:

Description
-----------

This function returns true if the Tx FIFO is empty.

.. _`fm10k_mbx_dequeue_rx`:

fm10k_mbx_dequeue_rx
====================

.. c:function:: u16 fm10k_mbx_dequeue_rx(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Dequeues the message from the head in the Rx FIFO

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_dequeue_rx.description`:

Description
-----------

This function dequeues messages and hands them off to the TLV parser.
It will return the number of messages processed when called.

.. _`fm10k_mbx_enqueue_tx`:

fm10k_mbx_enqueue_tx
====================

.. c:function:: s32 fm10k_mbx_enqueue_tx(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx, const u32 *msg)

    Enqueues the message to the tail of the Tx FIFO

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param const u32 \*msg:
        message array to read

.. _`fm10k_mbx_enqueue_tx.description`:

Description
-----------

This function enqueues a message up to the size specified by the length
contained in the first DWORD of the message and will place at the tail
of the FIFO.  It will return 0 on success, or a negative value on error.

.. _`fm10k_mbx_read`:

fm10k_mbx_read
==============

.. c:function:: s32 fm10k_mbx_read(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Copies the mbmem to local message buffer

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_read.description`:

Description
-----------

This function copies the message from the mbmem to the message array

.. _`fm10k_mbx_write`:

fm10k_mbx_write
===============

.. c:function:: void fm10k_mbx_write(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Copies the local message buffer to mbmem

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_write.description`:

Description
-----------

This function copies the message from the the message array to mbmem

.. _`fm10k_mbx_create_connect_hdr`:

fm10k_mbx_create_connect_hdr
============================

.. c:function:: void fm10k_mbx_create_connect_hdr(struct fm10k_mbx_info *mbx)

    Generate a connect mailbox header

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_create_connect_hdr.description`:

Description
-----------

This function returns a connection mailbox header

.. _`fm10k_mbx_create_data_hdr`:

fm10k_mbx_create_data_hdr
=========================

.. c:function:: void fm10k_mbx_create_data_hdr(struct fm10k_mbx_info *mbx)

    Generate a data mailbox header

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_create_data_hdr.description`:

Description
-----------

This function returns a data mailbox header

.. _`fm10k_mbx_create_disconnect_hdr`:

fm10k_mbx_create_disconnect_hdr
===============================

.. c:function:: void fm10k_mbx_create_disconnect_hdr(struct fm10k_mbx_info *mbx)

    Generate a disconnect mailbox header

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_create_disconnect_hdr.description`:

Description
-----------

This function returns a disconnect mailbox header

.. _`fm10k_mbx_create_fake_disconnect_hdr`:

fm10k_mbx_create_fake_disconnect_hdr
====================================

.. c:function:: void fm10k_mbx_create_fake_disconnect_hdr(struct fm10k_mbx_info *mbx)

    Generate a false disconnect mbox hdr

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_create_fake_disconnect_hdr.description`:

Description
-----------

This function creates a fake disconnect header for loading into remote
mailbox header. The primary purpose is to prevent errors on immediate
start up after mbx->connect.

.. _`fm10k_mbx_create_error_msg`:

fm10k_mbx_create_error_msg
==========================

.. c:function:: void fm10k_mbx_create_error_msg(struct fm10k_mbx_info *mbx, s32 err)

    Generate an error message

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param s32 err:
        local error encountered

.. _`fm10k_mbx_create_error_msg.description`:

Description
-----------

This function will interpret the error provided by err, and based on
that it may shift the message by 1 DWORD and then place an error header
at the start of the message.

.. _`fm10k_mbx_validate_msg_hdr`:

fm10k_mbx_validate_msg_hdr
==========================

.. c:function:: s32 fm10k_mbx_validate_msg_hdr(struct fm10k_mbx_info *mbx)

    Validate common fields in the message header

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_validate_msg_hdr.description`:

Description
-----------

This function will parse up the fields in the mailbox header and return
an error if the header contains any of a number of invalid configurations
including unrecognized type, invalid route, or a malformed message.

.. _`fm10k_mbx_create_reply`:

fm10k_mbx_create_reply
======================

.. c:function:: s32 fm10k_mbx_create_reply(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx, u16 head)

    Generate reply based on state and remote head

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 head:
        acknowledgement number

.. _`fm10k_mbx_create_reply.description`:

Description
-----------

This function will generate an outgoing message based on the current
mailbox state and the remote FIFO head.  It will return the length
of the outgoing message excluding header on success, and a negative value
on error.

.. _`fm10k_mbx_reset_work`:

fm10k_mbx_reset_work
====================

.. c:function:: void fm10k_mbx_reset_work(struct fm10k_mbx_info *mbx)

    Reset internal pointers for any pending work

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_reset_work.description`:

Description
-----------

This function will reset all internal pointers so any work in progress
is dropped.  This call should occur every time we transition from the
open state to the connect state.

.. _`fm10k_mbx_update_max_size`:

fm10k_mbx_update_max_size
=========================

.. c:function:: void fm10k_mbx_update_max_size(struct fm10k_mbx_info *mbx, u16 size)

    Update the max_size and drop any large messages

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 size:
        new value for max_size

.. _`fm10k_mbx_update_max_size.description`:

Description
-----------

This function updates the max_size value and drops any outgoing messages
at the head of the Tx FIFO if they are larger than max_size. It does not
drop all messages, as this is too difficult to parse and remove them from
the FIFO. Instead, rely on the checking to ensure that messages larger
than max_size aren't pushed into the memory buffer.

.. _`fm10k_mbx_connect_reset`:

fm10k_mbx_connect_reset
=======================

.. c:function:: void fm10k_mbx_connect_reset(struct fm10k_mbx_info *mbx)

    Reset following request for reset

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_connect_reset.description`:

Description
-----------

This function resets the mailbox to either a disconnected state
or a connect state depending on the current mailbox state

.. _`fm10k_mbx_process_connect`:

fm10k_mbx_process_connect
=========================

.. c:function:: s32 fm10k_mbx_process_connect(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Process connect header

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_process_connect.description`:

Description
-----------

This function will read an incoming connect header and reply with the
appropriate message.  It will return a value indicating the number of
data DWORDs on success, or will return a negative value on failure.

.. _`fm10k_mbx_process_data`:

fm10k_mbx_process_data
======================

.. c:function:: s32 fm10k_mbx_process_data(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Process data header

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_process_data.description`:

Description
-----------

This function will read an incoming data header and reply with the
appropriate message.  It will return a value indicating the number of
data DWORDs on success, or will return a negative value on failure.

.. _`fm10k_mbx_process_disconnect`:

fm10k_mbx_process_disconnect
============================

.. c:function:: s32 fm10k_mbx_process_disconnect(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Process disconnect header

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_process_disconnect.description`:

Description
-----------

This function will read an incoming disconnect header and reply with the
appropriate message.  It will return a value indicating the number of
data DWORDs on success, or will return a negative value on failure.

.. _`fm10k_mbx_process_error`:

fm10k_mbx_process_error
=======================

.. c:function:: s32 fm10k_mbx_process_error(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Process error header

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_process_error.description`:

Description
-----------

This function will read an incoming error header and reply with the
appropriate message.  It will return a value indicating the number of
data DWORDs on success, or will return a negative value on failure.

.. _`fm10k_mbx_process`:

fm10k_mbx_process
=================

.. c:function:: s32 fm10k_mbx_process(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Process mailbox interrupt

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_process.description`:

Description
-----------

This function will process incoming mailbox events and generate mailbox
replies.  It will return a value indicating the number of DWORDs
transmitted excluding header on success or a negative value on error.

.. _`fm10k_mbx_disconnect`:

fm10k_mbx_disconnect
====================

.. c:function:: void fm10k_mbx_disconnect(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Shutdown mailbox connection

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_disconnect.description`:

Description
-----------

This function will shut down the mailbox.  It places the mailbox first
in the disconnect state, it then allows up to a predefined timeout for
the mailbox to transition to close on its own.  If this does not occur
then the mailbox will be forced into the closed state.

Any mailbox transactions not completed before calling this function
are not guaranteed to complete and may be dropped.

.. _`fm10k_mbx_connect`:

fm10k_mbx_connect
=================

.. c:function:: s32 fm10k_mbx_connect(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Start mailbox connection

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_mbx_connect.description`:

Description
-----------

This function will initiate a mailbox connection.  It will populate the
mailbox with a broadcast connect message and then initialize the lock.
This is safe since the connect message is a single DWORD so the mailbox
transaction is guaranteed to be atomic.

This function will return an error if the mailbox has not been initiated
or is currently in use.

.. _`fm10k_mbx_validate_handlers`:

fm10k_mbx_validate_handlers
===========================

.. c:function:: s32 fm10k_mbx_validate_handlers(const struct fm10k_msg_data *msg_data)

    Validate layout of message parsing data

    :param const struct fm10k_msg_data \*msg_data:
        handlers for mailbox events

.. _`fm10k_mbx_validate_handlers.description`:

Description
-----------

This function validates the layout of the message parsing data.  This
should be mostly static, but it is important to catch any errors that
are made when constructing the parsers.

.. _`fm10k_mbx_register_handlers`:

fm10k_mbx_register_handlers
===========================

.. c:function:: s32 fm10k_mbx_register_handlers(struct fm10k_mbx_info *mbx, const struct fm10k_msg_data *msg_data)

    Register a set of handler ops for mailbox

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param const struct fm10k_msg_data \*msg_data:
        handlers for mailbox events

.. _`fm10k_mbx_register_handlers.description`:

Description
-----------

This function associates a set of message handling ops with a mailbox.

.. _`fm10k_pfvf_mbx_init`:

fm10k_pfvf_mbx_init
===================

.. c:function:: s32 fm10k_pfvf_mbx_init(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx, const struct fm10k_msg_data *msg_data, u8 id)

    Initialize mailbox memory for PF/VF mailbox

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param const struct fm10k_msg_data \*msg_data:
        handlers for mailbox events

    :param u8 id:
        ID reference for PF as it supports up to 64 PF/VF mailboxes

.. _`fm10k_pfvf_mbx_init.description`:

Description
-----------

This function initializes the mailbox for use.  It will split the
buffer provided and use that to populate both the Tx and Rx FIFO by
evenly splitting it.  In order to allow for easy masking of head/tail
the value reported in size must be a power of 2 and is reported in
DWORDs, not bytes.  Any invalid values will cause the mailbox to return
error.

.. _`fm10k_sm_mbx_create_data_hdr`:

fm10k_sm_mbx_create_data_hdr
============================

.. c:function:: void fm10k_sm_mbx_create_data_hdr(struct fm10k_mbx_info *mbx)

    Generate a mailbox header for local FIFO

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_sm_mbx_create_data_hdr.description`:

Description
-----------

This function returns a data mailbox header

.. _`fm10k_sm_mbx_create_connect_hdr`:

fm10k_sm_mbx_create_connect_hdr
===============================

.. c:function:: void fm10k_sm_mbx_create_connect_hdr(struct fm10k_mbx_info *mbx, u8 err)

    Generate a mailbox header for local FIFO

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u8 err:
        error flags to report if any

.. _`fm10k_sm_mbx_create_connect_hdr.description`:

Description
-----------

This function returns a connection mailbox header

.. _`fm10k_sm_mbx_connect_reset`:

fm10k_sm_mbx_connect_reset
==========================

.. c:function:: void fm10k_sm_mbx_connect_reset(struct fm10k_mbx_info *mbx)

    Reset following request for reset

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_sm_mbx_connect_reset.description`:

Description
-----------

This function resets the mailbox to a just connected state

.. _`fm10k_sm_mbx_connect`:

fm10k_sm_mbx_connect
====================

.. c:function:: s32 fm10k_sm_mbx_connect(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Start switch manager mailbox connection

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_sm_mbx_connect.description`:

Description
-----------

This function will initiate a mailbox connection with the switch
manager.  To do this it will first disconnect the mailbox, and then
reconnect it in order to complete a reset of the mailbox.

This function will return an error if the mailbox has not been initiated
or is currently in use.

.. _`fm10k_sm_mbx_disconnect`:

fm10k_sm_mbx_disconnect
=======================

.. c:function:: void fm10k_sm_mbx_disconnect(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Shutdown mailbox connection

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_sm_mbx_disconnect.description`:

Description
-----------

This function will shut down the mailbox.  It places the mailbox first
in the disconnect state, it then allows up to a predefined timeout for
the mailbox to transition to close on its own.  If this does not occur
then the mailbox will be forced into the closed state.

Any mailbox transactions not completed before calling this function
are not guaranteed to complete and may be dropped.

.. _`fm10k_sm_mbx_validate_fifo_hdr`:

fm10k_sm_mbx_validate_fifo_hdr
==============================

.. c:function:: s32 fm10k_sm_mbx_validate_fifo_hdr(struct fm10k_mbx_info *mbx)

    Validate fields in the remote FIFO header

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_sm_mbx_validate_fifo_hdr.description`:

Description
-----------

This function will parse up the fields in the mailbox header and return
an error if the header contains any of a number of invalid configurations
including unrecognized offsets or version numbers.

.. _`fm10k_sm_mbx_process_error`:

fm10k_sm_mbx_process_error
==========================

.. c:function:: void fm10k_sm_mbx_process_error(struct fm10k_mbx_info *mbx)

    Process header with error flag set

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_sm_mbx_process_error.description`:

Description
-----------

This function is meant to respond to a request where the error flag
is set.  As a result we will terminate a connection if one is present
and fall back into the reset state with a connection header of version
0 (RESET).

.. _`fm10k_sm_mbx_create_error_msg`:

fm10k_sm_mbx_create_error_msg
=============================

.. c:function:: void fm10k_sm_mbx_create_error_msg(struct fm10k_mbx_info *mbx, s32 err)

    Process an error in FIFO header

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param s32 err:
        local error encountered

.. _`fm10k_sm_mbx_create_error_msg.description`:

Description
-----------

This function will interpret the error provided by err, and based on
that it may set the error bit in the local message header

.. _`fm10k_sm_mbx_receive`:

fm10k_sm_mbx_receive
====================

.. c:function:: s32 fm10k_sm_mbx_receive(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx, u16 tail)

    Take message from Rx mailbox FIFO and put it in Rx

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 tail:
        tail index of message

.. _`fm10k_sm_mbx_receive.description`:

Description
-----------

This function will dequeue one message from the Rx switch manager mailbox
FIFO and place it in the Rx mailbox FIFO for processing by software.

.. _`fm10k_sm_mbx_transmit`:

fm10k_sm_mbx_transmit
=====================

.. c:function:: void fm10k_sm_mbx_transmit(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx, u16 head)

    Take message from Tx and put it in Tx mailbox FIFO

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 head:
        head index of message

.. _`fm10k_sm_mbx_transmit.description`:

Description
-----------

This function will dequeue one message from the Tx mailbox FIFO and place
it in the Tx switch manager mailbox FIFO for processing by hardware.

.. _`fm10k_sm_mbx_create_reply`:

fm10k_sm_mbx_create_reply
=========================

.. c:function:: void fm10k_sm_mbx_create_reply(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx, u16 head)

    Generate reply based on state and remote head

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param u16 head:
        acknowledgement number

.. _`fm10k_sm_mbx_create_reply.description`:

Description
-----------

This function will generate an outgoing message based on the current
mailbox state and the remote FIFO head.  It will return the length
of the outgoing message excluding header on success, and a negative value
on error.

.. _`fm10k_sm_mbx_process_reset`:

fm10k_sm_mbx_process_reset
==========================

.. c:function:: s32 fm10k_sm_mbx_process_reset(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Process header with version == 0 (RESET)

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_sm_mbx_process_reset.description`:

Description
-----------

This function is meant to respond to a request where the version data
is set to 0.  As such we will either terminate the connection or go
into the connect state in order to re-establish the connection.  This
function can also be used to respond to an error as the connection
resetting would also be a means of dealing with errors.

.. _`fm10k_sm_mbx_process_version_1`:

fm10k_sm_mbx_process_version_1
==============================

.. c:function:: s32 fm10k_sm_mbx_process_version_1(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Process header with version == 1

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_sm_mbx_process_version_1.description`:

Description
-----------

This function is meant to process messages received when the remote
mailbox is active.

.. _`fm10k_sm_mbx_process`:

fm10k_sm_mbx_process
====================

.. c:function:: s32 fm10k_sm_mbx_process(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx)

    Process switch manager mailbox interrupt

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

.. _`fm10k_sm_mbx_process.description`:

Description
-----------

This function will process incoming mailbox events and generate mailbox
replies.  It will return a value indicating the number of DWORDs
transmitted excluding header on success or a negative value on error.

.. _`fm10k_sm_mbx_init`:

fm10k_sm_mbx_init
=================

.. c:function:: s32 fm10k_sm_mbx_init(struct fm10k_hw *hw, struct fm10k_mbx_info *mbx, const struct fm10k_msg_data *msg_data)

    Initialize mailbox memory for PF/SM mailbox

    :param struct fm10k_hw \*hw:
        pointer to hardware structure

    :param struct fm10k_mbx_info \*mbx:
        pointer to mailbox

    :param const struct fm10k_msg_data \*msg_data:
        handlers for mailbox events

.. _`fm10k_sm_mbx_init.description`:

Description
-----------

This function initializes the PF/SM mailbox for use.  It will split the
buffer provided and use that to populate both the Tx and Rx FIFO by
evenly splitting it.  In order to allow for easy masking of head/tail
the value reported in size must be a power of 2 and is reported in
DWORDs, not bytes.  Any invalid values will cause the mailbox to return
error.

.. This file was automatic generated / don't edit.

