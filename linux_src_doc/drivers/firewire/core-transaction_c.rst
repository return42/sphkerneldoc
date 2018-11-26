.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firewire/core-transaction.c

.. _`fw_send_request`:

fw_send_request
===============

.. c:function:: void fw_send_request(struct fw_card *card, struct fw_transaction *t, int tcode, int destination_id, int generation, int speed, unsigned long long offset, void *payload, size_t length, fw_transaction_callback_t callback, void *callback_data)

    submit a request packet for transmission

    :param card:
        interface to send the request at
    :type card: struct fw_card \*

    :param t:
        transaction instance to which the request belongs
    :type t: struct fw_transaction \*

    :param tcode:
        transaction code
    :type tcode: int

    :param destination_id:
        destination node ID, consisting of bus_ID and phy_ID
    :type destination_id: int

    :param generation:
        bus generation in which request and response are valid
    :type generation: int

    :param speed:
        transmission speed
    :type speed: int

    :param offset:
        48bit wide offset into destination's address space
    :type offset: unsigned long long

    :param payload:
        data payload for the request subaction
    :type payload: void \*

    :param length:
        length of the payload, in bytes
    :type length: size_t

    :param callback:
        function to be called when the transaction is completed
    :type callback: fw_transaction_callback_t

    :param callback_data:
        data to be passed to the transaction completion callback
    :type callback_data: void \*

.. _`fw_send_request.description`:

Description
-----------

Submit a request packet into the asynchronous request transmission queue.
Can be called from atomic context.  If you prefer a blocking API, use
\ :c:func:`fw_run_transaction`\  in a context that can sleep.

In case of lock requests, specify one of the firewire-core specific \ ``TCODE_``\ 
constants instead of \ ``TCODE_LOCK_REQUEST``\  in \ ``tcode``\ .

Make sure that the value in \ ``destination_id``\  is not older than the one in
\ ``generation``\ .  Otherwise the request is in danger to be sent to a wrong node.

In case of asynchronous stream packets i.e. \ ``TCODE_STREAM_DATA``\ , the caller
needs to synthesize \ ``destination_id``\  with \ :c:func:`fw_stream_packet_destination_id`\ .
It will contain tag, channel, and sy data instead of a node ID then.

The payload buffer at \ ``data``\  is going to be DMA-mapped except in case of
\ ``length``\  <= 8 or of local (loopback) requests.  Hence make sure that the
buffer complies with the restrictions of the streaming DMA mapping API.
\ ``payload``\  must not be freed before the \ ``callback``\  is called.

In case of request types without payload, \ ``data``\  is NULL and \ ``length``\  is 0.

After the transaction is completed successfully or unsuccessfully, the
\ ``callback``\  will be called.  Among its parameters is the response code which
is either one of the rcodes per IEEE 1394 or, in case of internal errors,
the firewire-core specific \ ``RCODE_SEND_ERROR``\ .  The other firewire-core
specific rcodes (%RCODE_CANCELLED, \ ``RCODE_BUSY``\ , \ ``RCODE_GENERATION``\ ,
\ ``RCODE_NO_ACK``\ ) denote transaction timeout, busy responder, stale request
generation, or missing ACK respectively.

Note some timing corner cases:  \ :c:func:`fw_send_request`\  may complete much earlier
than when the request packet actually hits the wire.  On the other hand,
transaction completion and hence execution of \ ``callback``\  may happen even
before \ :c:func:`fw_send_request`\  returns.

.. _`fw_run_transaction`:

fw_run_transaction
==================

.. c:function:: int fw_run_transaction(struct fw_card *card, int tcode, int destination_id, int generation, int speed, unsigned long long offset, void *payload, size_t length)

    send request and sleep until transaction is completed

    :param card:
        card interface for this request
    :type card: struct fw_card \*

    :param tcode:
        transaction code
    :type tcode: int

    :param destination_id:
        destination node ID, consisting of bus_ID and phy_ID
    :type destination_id: int

    :param generation:
        bus generation in which request and response are valid
    :type generation: int

    :param speed:
        transmission speed
    :type speed: int

    :param offset:
        48bit wide offset into destination's address space
    :type offset: unsigned long long

    :param payload:
        data payload for the request subaction
    :type payload: void \*

    :param length:
        length of the payload, in bytes
    :type length: size_t

.. _`fw_run_transaction.description`:

Description
-----------

Returns the RCODE.  See \ :c:func:`fw_send_request`\  for parameter documentation.
Unlike \ :c:func:`fw_send_request`\ , \ ``data``\  points to the payload of the request or/and
to the payload of the response.  DMA mapping restrictions apply to outbound
request payloads of >= 8 bytes but not to inbound response payloads.

.. _`fw_core_add_address_handler`:

fw_core_add_address_handler
===========================

.. c:function:: int fw_core_add_address_handler(struct fw_address_handler *handler, const struct fw_address_region *region)

    register for incoming requests

    :param handler:
        callback
    :type handler: struct fw_address_handler \*

    :param region:
        region in the IEEE 1212 node space address range
    :type region: const struct fw_address_region \*

.. _`fw_core_add_address_handler.description`:

Description
-----------

region->start, ->end, and handler->length have to be quadlet-aligned.

When a request is received that falls within the specified address range,
the specified callback is invoked.  The parameters passed to the callback
give the details of the particular request.

To be called in process context.
Return value:  0 on success, non-zero otherwise.

The start offset of the handler's address region is determined by
\ :c:func:`fw_core_add_address_handler`\  and is returned in handler->offset.

Address allocations are exclusive, except for the FCP registers.

.. _`fw_core_remove_address_handler`:

fw_core_remove_address_handler
==============================

.. c:function:: void fw_core_remove_address_handler(struct fw_address_handler *handler)

    unregister an address handler

    :param handler:
        callback
    :type handler: struct fw_address_handler \*

.. _`fw_core_remove_address_handler.description`:

Description
-----------

To be called in process context.

When \ :c:func:`fw_core_remove_address_handler`\  returns, \ ``handler->callback``\ () is
guaranteed to not run on any CPU anymore.

.. _`fw_get_request_speed`:

fw_get_request_speed
====================

.. c:function:: int fw_get_request_speed(struct fw_request *request)

    returns speed at which the \ ``request``\  was received

    :param request:
        firewire request data
    :type request: struct fw_request \*

.. _`fw_rcode_string`:

fw_rcode_string
===============

.. c:function:: const char *fw_rcode_string(int rcode)

    convert a firewire result code to an error description

    :param rcode:
        the result code
    :type rcode: int

.. This file was automatic generated / don't edit.

