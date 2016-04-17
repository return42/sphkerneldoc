
.. _FE_GET_FRONTEND:

===============
FE_GET_FRONTEND
===============

DESCRIPTION

This ioctl call queries the currently effective frontend parameters. For this command, read-only access to the device is sufficient.

SYNOPSIS

int ioctl(int fd, int request = :ref:`FE_GET_FRONTEND <FE_GET_FRONTEND>`, struct dvb_frontend_parameters ⋆p);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_SET_FRONTEND    <FE_SET_FRONTEND>`    for this command.                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct dvb_frontend_parameters   ⋆p                                                        | Points to parameters for tuning operation.                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | Maximum supported symbol rate reached.                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


