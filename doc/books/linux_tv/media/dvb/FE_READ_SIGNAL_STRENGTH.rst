
.. _FE_READ_SIGNAL_STRENGTH:

=======================
FE_READ_SIGNAL_STRENGTH
=======================

DESCRIPTION

This ioctl call returns the signal strength value for the signal currently received by the front-end. For this command, read-only access to the device is sufficient.

SYNOPSIS

int ioctl( int fd, int request = :ref:`FE_READ_SIGNAL_STRENGTH <FE_READ_SIGNAL_STRENGTH>`, uint16_t ⋆strength);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_READ_SIGNAL_STRENGTH     <FE_READ_SIGNAL_STRENGTH>`     for this command.  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | uint16_t  ⋆strength                                                                        | The signal strength value is stored into ⋆strength.                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.
