
.. _dvb_frontend:

================
DVB Frontend API
================

The DVB frontend API was designed to support three types of delivery systems:

-  Terrestrial systems: DVB-T, DVB-T2, ATSC, ATSC M/H, ISDB-T, DVB-H, DTMB, CMMB

-  Cable systems: DVB-C Annex A/C, ClearQAM (DVB-C Annex B), ISDB-C

-  Satellite systems: DVB-S, DVB-S2, DVB Turbo, ISDB-S, DSS

The DVB frontend controls several sub-devices including:

-  Tuner

-  Digital TV demodulator

-  Low noise amplifier (LNA)

-  Satellite Equipment Control (SEC) hardware (only for Satellite).

The frontend can be accessed through ``/dev/dvb/adapter?/frontend?``. Data types and ioctl definitions can be accessed by including ``linux/dvb/frontend.h`` in your application.

NOTE: Transmission via the internet (DVB-IP) is not yet handled by this API but a future extension is possible.

On Satellite systems, the API support for the Satellite Equipment Control (SEC) allows to power control and to send/receive signals to control the antenna subsystem, selecting the
polarization and choosing the Intermediate Frequency IF) of the Low Noise Block Converter Feed Horn (LNBf). It supports the DiSEqC and V-SEC protocols. The DiSEqC (digital SEC)
specification is available at `Eutelsat`_.


.. _query-dvb-frontend-info:

Querying frontend information
=============================

Usually, the first thing to do when the frontend is opened is to check the frontend capabilities. This is done using :ref:`FE_GET_INFO <FE_GET_INFO>`. This ioctl will
enumerate the DVB API version and other characteristics about the frontend, and can be opened either in read only or read/write mode.


.. _dvb-fe-read-status:

Querying frontend status and statistics
=======================================

Once :ref:`FE_SET_PROPERTY <FE_GET_PROPERTY>` is called, the frontend will run a kernel thread that will periodically check for the tuner lock status and provide statistics
about the quality of the signal.

The information about the frontend tuner locking status can be queried using :ref:`FE_READ_STATUS <FE_READ_STATUS>`.

Signal statistics are provided via :ref:`FE_GET_PROPERTY <FE_GET_PROPERTY>`. Please note that several statistics require the demodulator to be fully locked (e. g. with
FE_HAS_LOCK bit set). See :ref:`Frontend statistics indicators <frontend-stat-properties>` for more details.


.. toctree::
    :maxdepth: 1

    dvbproperty

.. _frontend_fcalls:

Frontend Function Calls
=======================


.. _frontend_f_open:

===================
DVB frontend open()
===================

*man fe-open(2)*

Open a frontend device


Synopsis
========

.. code-block:: c

    #include <fcntl.h>


.. c:function:: int open( const char *device_name, int flags )

Arguments
=========

``device_name``
    Device to be opened.

``flags``
    Open flags. Access can either be ``O_RDWR`` or ``O_RDONLY``.

    Multiple opens are allowed with ``O_RDONLY``. In this mode, only query and read ioctls are allowed.

    Only one open is allowed in ``O_RDWR``. In this mode, all ioctls are allowed.

    When the ``O_NONBLOCK`` flag is given, the system calls may return EAGAIN error code when no data is available or when the device driver is temporarily busy.

    Other flags have no effect.


Description
===========

This system call opens a named frontend device (``/dev/dvb/adapter?/frontend?``) for subsequent use. Usually the first thing to do after a successful open is to find out the
frontend type with :ref:`FE_GET_INFO <FE_GET_INFO>`.

The device can be opened in read-only mode, which only allows monitoring of device status and statistics, or read/write mode, which allows any kind of use (e.g. performing tuning
operations.)

In a system with multiple front-ends, it is usually the case that multiple devices cannot be open in read/write mode simultaneously. As long as a front-end device is opened in
read/write mode, other open() calls in read/write mode will either fail or block, depending on whether non-blocking or blocking mode was specified. A front-end device opened in
blocking mode can later be put into non-blocking mode (and vice versa) using the F_SETFL command of the fcntl system call. This is a standard system call, documented in the Linux
manual page for fcntl. When an open() call has succeeded, the device will be ready for use in the specified mode. This implies that the corresponding hardware is powered up, and
that other front-ends may have been powered down to make that possible.


Return Value
============

On success ``open`` returns the new file descriptor. On error -1 is returned, and the ``errno`` variable is set appropriately. Possible error codes are:

EACCES
    The caller has no permission to access the device.

EBUSY
    The the device driver is already in use.

ENXIO
    No device corresponding to this device special file exists.

ENOMEM
    Not enough kernel memory was available to complete the request.

EMFILE
    The process already has the maximum number of files open.

ENFILE
    The limit on the total number of files open on the system has been reached.

ENODEV
    The device got removed.


.. _frontend_f_close:

====================
DVB frontend close()
====================

*man fe-close(2)*

Close a frontend device


Synopsis
========

.. code-block:: c

    #include <unistd.h>


.. c:function:: int close( int fd )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.


Description
===========

This system call closes a previously opened front-end device. After closing a front-end device, its corresponding hardware might be powered down automatically.


Return Value
============

The function returns 0 on success, -1 on failure and the ``errno`` is set appropriately. Possible error codes:

EBADF
    ``fd`` is not a valid open file descriptor.


.. toctree::
    :maxdepth: 1

    fe-get-info
    fe-read-status
    fe-get-property
    fe-diseqc-reset-overload
    fe-diseqc-send-master-cmd
    fe-diseqc-recv-slave-reply
    fe-diseqc-send-burst
    fe-set-tone
    fe-set-voltage
    fe-enable-high-lnb-voltage
    fe-set-frontend-tune-mode

.. _frontend_legacy_dvbv3_api:

DVB Frontend legacy API (a. k. a. DVBv3)
========================================

The usage of this API is deprecated, as it doesn't support all digital TV standards, doesn't provide good statistics measurements and provides incomplete information. This is kept
only to support legacy applications.


.. toctree::
    :maxdepth: 1

    frontend_legacy_api

.. _Eutelsat: http://www.eutelsat.com/satellites/4_5_5.html
