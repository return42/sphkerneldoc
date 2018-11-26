.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/greybus/operation.c

.. _`gb_operation_request_send`:

gb_operation_request_send
=========================

.. c:function:: int gb_operation_request_send(struct gb_operation *operation, gb_operation_callback callback, unsigned int timeout, gfp_t gfp)

    send an operation request message

    :param operation:
        the operation to initiate
    :type operation: struct gb_operation \*

    :param callback:
        the operation completion callback
    :type callback: gb_operation_callback

    :param timeout:
        operation timeout in milliseconds, or zero for no timeout
    :type timeout: unsigned int

    :param gfp:
        the memory flags to use for any allocations
    :type gfp: gfp_t

.. _`gb_operation_request_send.description`:

Description
-----------

The caller has filled in any payload so the request message is ready to go.
The callback function supplied will be called when the response message has
arrived, a unidirectional request has been sent, or the operation is
cancelled, indicating that the operation is complete. The callback function
can fetch the result of the operation using \ :c:func:`gb_operation_result`\  if
desired.

.. _`gb_operation_request_send.return`:

Return
------

0 if the request was successfully queued in the host-driver queues,
or a negative errno.

.. _`gb_operation_sync_timeout`:

gb_operation_sync_timeout
=========================

.. c:function:: int gb_operation_sync_timeout(struct gb_connection *connection, int type, void *request, int request_size, void *response, int response_size, unsigned int timeout)

    implement a "simple" synchronous operation

    :param connection:
        the Greybus connection to send this to
    :type connection: struct gb_connection \*

    :param type:
        the type of operation to send
    :type type: int

    :param request:
        pointer to a memory buffer to copy the request from
    :type request: void \*

    :param request_size:
        size of \ ``request``\ 
    :type request_size: int

    :param response:
        pointer to a memory buffer to copy the response to
    :type response: void \*

    :param response_size:
        the size of \ ``response``\ .
    :type response_size: int

    :param timeout:
        operation timeout in milliseconds
    :type timeout: unsigned int

.. _`gb_operation_sync_timeout.description`:

Description
-----------

This function implements a simple synchronous Greybus operation.  It sends
the provided operation request and waits (sleeps) until the corresponding
operation response message has been successfully received, or an error
occurs.  \ ``request``\  and \ ``response``\  are buffers to hold the request and response
data respectively, and if they are not NULL, their size must be specified in
\ ``request_size``\  and \ ``response_size``\ .

If a response payload is to come back, and \ ``response``\  is not NULL,
\ ``response_size``\  number of bytes will be copied into \ ``response``\  if the operation
is successful.

If there is an error, the response buffer is left alone.

.. _`gb_operation_unidirectional_timeout`:

gb_operation_unidirectional_timeout
===================================

.. c:function:: int gb_operation_unidirectional_timeout(struct gb_connection *connection, int type, void *request, int request_size, unsigned int timeout)

    initiate a unidirectional operation

    :param connection:
        connection to use
    :type connection: struct gb_connection \*

    :param type:
        type of operation to send
    :type type: int

    :param request:
        memory buffer to copy the request from
    :type request: void \*

    :param request_size:
        size of \ ``request``\ 
    :type request_size: int

    :param timeout:
        send timeout in milliseconds
    :type timeout: unsigned int

.. _`gb_operation_unidirectional_timeout.description`:

Description
-----------

Initiate a unidirectional operation by sending a request message and
waiting for it to be acknowledged as sent by the host device.

Note that successful send of a unidirectional operation does not imply that
the request as actually reached the remote end of the connection.

.. This file was automatic generated / don't edit.

