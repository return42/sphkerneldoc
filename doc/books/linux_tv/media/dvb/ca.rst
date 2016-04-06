
.. _dvb_ca:

=============
DVB CA Device
=============

The DVB CA device controls the conditional access hardware. It can be accessed through ``/dev/dvb/adapter?/ca?``. Data types and and ioctl definitions can be accessed by including
``linux/dvb/ca.h`` in your application.


.. _ca_data_types:

CA Data Types
=============


.. _ca-slot-info:

ca_slot_info_t
==============


.. code-block:: c

    typedef struct ca_slot_info {
        int num;               /* slot number */

        int type;              /* CA interface this slot supports */
    #define CA_CI            1     /* CI high level interface */
    #define CA_CI_LINK       2     /* CI link layer level interface */
    #define CA_CI_PHYS       4     /* CI physical layer level interface */
    #define CA_DESCR         8     /* built-in descrambler */
    #define CA_SC          128     /* simple smart card interface */

        unsigned int flags;
    #define CA_CI_MODULE_PRESENT 1 /* module (or card) inserted */
    #define CA_CI_MODULE_READY   2
    } ca_slot_info_t;


.. _ca-descr-info:

ca_descr_info_t
===============


.. code-block:: c

    typedef struct ca_descr_info {
        unsigned int num;  /* number of available descramblers (keys) */
        unsigned int type; /* type of supported scrambling system */
    #define CA_ECD           1
    #define CA_NDS           2
    #define CA_DSS           4
    } ca_descr_info_t;


.. _ca-caps:

ca_caps_t
=========


.. code-block:: c

    typedef struct ca_caps {
        unsigned int slot_num;  /* total number of CA card and module slots */
        unsigned int slot_type; /* OR of all supported types */
        unsigned int descr_num; /* total number of descrambler slots (keys) */
        unsigned int descr_type;/* OR of all supported types */
     } ca_cap_t;


.. _ca-msg:

ca_msg_t
========


.. code-block:: c

    /* a message to/from a CI-CAM */
    typedef struct ca_msg {
        unsigned int index;
        unsigned int type;
        unsigned int length;
        unsigned char msg[256];
    } ca_msg_t;


.. _ca-descr:

ca_descr_t
==========


.. code-block:: c

    typedef struct ca_descr {
        unsigned int index;
        unsigned int parity;
        unsigned char cw[8];
    } ca_descr_t;


.. _ca-pid:

ca-pid
======


.. code-block:: c

    typedef struct ca_pid {
        unsigned int pid;
        int index;      /* -1 == disable*/
    } ca_pid_t;


.. _ca_function_calls:

CA Function Calls
=================


.. _ca_fopen:

open()
======

DESCRIPTION

This system call opens a named ca device (e.g. /dev/ost/ca) for subsequent use.

When an open() call has succeeded, the device will be ready for use. The significance of blocking or non-blocking mode is described in the documentation for functions where there
is a difference. It does not affect the semantics of the open() call itself. A device opened in blocking mode can later be put into non-blocking mode (and vice versa) using the
F_SETFL command of the fcntl system call. This is a standard system call, documented in the Linux manual page for fcntl. Only one user can open the CA Device in O_RDWR mode. All
other attempts to open the device in this mode will fail, and an error code will be returned.

SYNOPSIS

int open(const char ⋆deviceName, int flags);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | const char ⋆deviceName                                                                     | Name of specific video device.                                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int flags                                                                                  | A bit-wise OR of the following flags:                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | O_RDONLY  read-only access                                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | O_RDWR  read/write access                                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | O_NONBLOCK  open in non-blocking mode                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | (blocking mode is the default)                                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ENODEV                                                                                     | Device driver not loaded/available.                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINTERNAL                                                                                  | Internal error.                                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EBUSY                                                                                      | Device or resource busy.                                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | Invalid argument.                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _ca_fclose:

close()
=======

DESCRIPTION

This system call closes a previously opened audio device.

SYNOPSIS

int close(int fd);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EBADF                                                                                      | fd is not a valid open file descriptor.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _CA_RESET:

CA_RESET
========

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = CA_RESET);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals CA_RESET  for this command.                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _CA_GET_CAP:

CA_GET_CAP
==========

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = CA_GET_CAP, ca_caps_t ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals CA_GET_CAP   for this command.                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ca_caps_t   ⋆                                                                              | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _CA_GET_SLOT_INFO:

CA_GET_SLOT_INFO
================

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = CA_GET_SLOT_INFO, ca_slot_info_t ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals CA_GET_SLOT_INFO    for this command.                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ca_slot_info_t    ⋆                                                                        | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _CA_GET_DESCR_INFO:

CA_GET_DESCR_INFO
=================

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = CA_GET_DESCR_INFO, ca_descr_info_t ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals CA_GET_DESCR_INFO    for this command.                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ca_descr_info_t    ⋆                                                                       | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _CA_GET_MSG:

CA_GET_MSG
==========

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = CA_GET_MSG, ca_msg_t ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals CA_GET_MSG   for this command.                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ca_msg_t   ⋆                                                                               | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _CA_SEND_MSG:

CA_SEND_MSG
===========

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = CA_SEND_MSG, ca_msg_t ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals CA_SEND_MSG   for this command.                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ca_msg_t   ⋆                                                                               | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _CA_SET_DESCR:

CA_SET_DESCR
============

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = CA_SET_DESCR, ca_descr_t ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals CA_SET_DESCR   for this command.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ca_descr_t   ⋆                                                                             | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _CA_SET_PID:

CA_SET_PID
==========

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = CA_SET_PID, ca_pid_t ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals CA_SET_PID   for this command.                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ca_pid_t   ⋆                                                                               | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.
