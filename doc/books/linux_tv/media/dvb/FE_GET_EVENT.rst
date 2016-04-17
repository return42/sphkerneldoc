
.. _FE_GET_EVENT:

============
FE_GET_EVENT
============

DESCRIPTION

This ioctl call returns a frontend event if available. If an event is not available, the behavior depends on whether the device is in blocking or non-blocking mode. In the latter
case, the call fails immediately with errno set to EWOULDBLOCK. In the former case, the call blocks until an event becomes available.

The standard Linux poll() and/or select() system calls can be used with the device file descriptor to watch for new events. For select(), the file descriptor should be included in
the exceptfds argument, and for poll(), POLLPRI should be specified as the wake-up condition. Since the event queue allocated is rather small (room for 8 events), the queue must be
serviced regularly to avoid overflow. If an overflow happens, the oldest event is discarded from the queue, and an error (EOVERFLOW) occurs the next time the queue is read. After
reporting the error condition in this fashion, subsequent :ref:`FE_GET_EVENT <FE_GET_EVENT>` calls will return events from the queue as usual.

For the sake of implementation simplicity, this command requires read/write access to the device.

SYNOPSIS

int ioctl(int fd, int request = QPSK_GET_EVENT, struct dvb_frontend_event ⋆ev);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_GET_EVENT    <FE_GET_EVENT>`    for this command.                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct dvb_frontend_event   ⋆ev                                                            | Points to the location where the event,                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | if any, is to be stored.                                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EWOULDBLOCK                                                                                | There is no event pending, and the device is in non-blocking mode.                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EOVERFLOW                                                                                  | Overflow in event queue - one or more events were lost.                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


