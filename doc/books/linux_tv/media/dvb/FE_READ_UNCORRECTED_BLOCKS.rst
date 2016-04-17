
.. _FE_READ_UNCORRECTED_BLOCKS:

==========================
FE_READ_UNCORRECTED_BLOCKS
==========================

DESCRIPTION

This ioctl call returns the number of uncorrected blocks detected by the device driver during its lifetime. For meaningful measurements, the increment in block count during a
specific time interval should be calculated. For this command, read-only access to the device is sufficient.

Note that the counter will wrap to zero after its maximum count has been reached.

SYNOPSIS

int ioctl( int fd, int request = :ref:`FE_READ_UNCORRECTED_BLOCKS <FE_READ_UNCORRECTED_BLOCKS>`, uint32_t ⋆ublocks);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_READ_UNCORRECTED_BLOCKS     <FE_READ_UNCORRECTED_BLOCKS>`     for this     |
    |                                                                                            | command.                                                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | uint32_t  ⋆ublocks                                                                         | The total number of uncorrected blocks seen by the driver so far.                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.
