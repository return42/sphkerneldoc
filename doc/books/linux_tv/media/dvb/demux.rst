
.. _dvb_demux:

================
DVB Demux Device
================

The DVB demux device controls the filters of the DVB hardware/software. It can be accessed through ``/dev/adapter?/demux?``. Data types and and ioctl definitions can be accessed by
including ``linux/dvb/dmx.h`` in your application.


.. _dmx_types:

Demux Data Types
================


.. _dmx-output-t:

Output for the demux
====================


.. _dmx-output:

.. table:: enum dmx_output

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | DMX_OUT_DECODER                                                                            | Streaming directly to decoder.                                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | DMX_OUT_TAP                                                                                | Output going to a memory buffer (to be retrieved via the read command). Delivers the       |
    |                                                                                            | stream output to the demux device on which the ioctl is called.                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | DMX_OUT_TS_TAP                                                                             | Output multiplexed into a new TS (to be retrieved by reading from the logical DVR device). |
    |                                                                                            | Routes output to the logical DVR device ``/dev/dvb/adapter?/dvr?``, which delivers a TS    |
    |                                                                                            | multiplexed from all filters for which ``DMX_OUT_TS_TAP`` was specified.                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | DMX_OUT_TSDEMUX_TAP                                                                        | Like :ref:`DMX_OUT_TS_TAP     <DMX-OUT-TS-TAP>`  but retrieved from the DMX device.        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _dmx-input-t:

dmx_input_t
===========


.. code-block:: c

    typedef enum
    {
        DMX_IN_FRONTEND, /* Input from a front-end device.  */
        DMX_IN_DVR       /* Input from the logical DVR device.  */
    } dmx_input_t;


.. _dmx-pes-type-t:

dmx_pes_type_t
==============


.. code-block:: c

    typedef enum
    {
        DMX_PES_AUDIO0,
        DMX_PES_VIDEO0,
        DMX_PES_TELETEXT0,
        DMX_PES_SUBTITLE0,
        DMX_PES_PCR0,

        DMX_PES_AUDIO1,
        DMX_PES_VIDEO1,
        DMX_PES_TELETEXT1,
        DMX_PES_SUBTITLE1,
        DMX_PES_PCR1,

        DMX_PES_AUDIO2,
        DMX_PES_VIDEO2,
        DMX_PES_TELETEXT2,
        DMX_PES_SUBTITLE2,
        DMX_PES_PCR2,

        DMX_PES_AUDIO3,
        DMX_PES_VIDEO3,
        DMX_PES_TELETEXT3,
        DMX_PES_SUBTITLE3,
        DMX_PES_PCR3,

        DMX_PES_OTHER
    } dmx_pes_type_t;


.. _dmx-filter:

struct dmx_filter
=================


.. code-block:: c

     typedef struct dmx_filter
    {
        __u8  filter[DMX_FILTER_SIZE];
        __u8  mask[DMX_FILTER_SIZE];
        __u8  mode[DMX_FILTER_SIZE];
    } dmx_filter_t;


.. _dmx-sct-filter-params:

struct dmx_sct_filter_params
============================


.. code-block:: c

    struct dmx_sct_filter_params
    {
        __u16          pid;
        dmx_filter_t   filter;
        __u32          timeout;
        __u32          flags;
    #define DMX_CHECK_CRC       1
    #define DMX_ONESHOT         2
    #define DMX_IMMEDIATE_START 4
    #define DMX_KERNEL_CLIENT   0x8000
    };


.. _dmx-pes-filter-params:

struct dmx_pes_filter_params
============================


.. code-block:: c

    struct dmx_pes_filter_params
    {
        __u16          pid;
        dmx_input_t    input;
        dmx_output_t   output;
        dmx_pes_type_t pes_type;
        __u32          flags;
    };


.. _dmx-event:

struct dmx_event
================


.. code-block:: c

     struct dmx_event
     {
         dmx_event_t          event;
         time_t               timeStamp;
         union
         {
             dmx_scrambling_status_t scrambling;
         } u;
     };


.. _dmx-stc:

struct dmx_stc
==============


.. code-block:: c

    struct dmx_stc {
        unsigned int num;   /* input : which STC? 0..N */
        unsigned int base;  /* output: divisor for stc to get 90 kHz clock */
        __u64 stc;      /* output: stc in 'base'*90 kHz units */
    };


.. _dmx-caps:

struct dmx_caps
===============


.. code-block:: c

     typedef struct dmx_caps {
        __u32 caps;
        int num_decoders;
    } dmx_caps_t;


.. _dmx-source-t:

enum dmx_source_t
=================


.. code-block:: c

    typedef enum {
        DMX_SOURCE_FRONT0 = 0,
        DMX_SOURCE_FRONT1,
        DMX_SOURCE_FRONT2,
        DMX_SOURCE_FRONT3,
        DMX_SOURCE_DVR0   = 16,
        DMX_SOURCE_DVR1,
        DMX_SOURCE_DVR2,
        DMX_SOURCE_DVR3
    } dmx_source_t;


.. _dmx_fcalls:

Demux Function Calls
====================


.. _dmx_fopen:

open()
======

DESCRIPTION

This system call, used with a device name of /dev/dvb/adapter0/demux0, allocates a new filter and returns a handle which can be used for subsequent control of that filter. This
call has to be made for each filter to be used, i.e. every returned file descriptor is a reference to a single filter. /dev/dvb/adapter0/dvr0 is a logical device to be used for
retrieving Transport Streams for digital video recording. When reading from this device a transport stream containing the packets from all PES filters set in the corresponding
demux device (/dev/dvb/adapter0/demux0) having the output set to DMX_OUT_TS_TAP. A recorded Transport Stream is replayed by writing to this device.

The significance of blocking or non-blocking mode is described in the documentation for functions where there is a difference. It does not affect the semantics of the open() call
itself. A device opened in blocking mode can later be put into non-blocking mode (and vice versa) using the F_SETFL command of the fcntl system call.

SYNOPSIS

int open(const char ⋆deviceName, int flags);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | const char ⋆deviceName                                                                     | Name of demux device.                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int flags                                                                                  | A bit-wise OR of the following flags:                                                      |
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
    | EINVAL                                                                                     | Invalid argument.                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EMFILE                                                                                     | “Too many open files”, i.e. no more filters available.                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ENOMEM                                                                                     | The driver failed to allocate enough memory.                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _dmx_fclose:

close()
=======

DESCRIPTION

This system call deactivates and deallocates a filter that was previously allocated via the open() call.

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



.. _dmx_fread:

read()
======

DESCRIPTION

This system call returns filtered data, which might be section or PES data. The filtered data is transferred from the driver’s internal circular buffer to buf. The maximum amount
of data to be transferred is implied by count.

When returning section data the driver always tries to return a complete single section (even though buf would provide buffer space for more data). If the size of the buffer is
smaller than the section as much as possible will be returned, and the remaining data will be provided in subsequent calls.

The size of the internal buffer is 2 ⋆ 4096 bytes (the size of two maximum sized sections) by default. The size of this buffer may be changed by using the DMX_SET_BUFFER_SIZE
function. If the buffer is not large enough, or if the read operations are not performed fast enough, this may result in a buffer overflow error. In this case EOVERFLOW will be
returned, and the circular buffer will be emptied. This call is blocking if there is no data to return, i.e. the process will be put to sleep waiting for data, unless the
O_NONBLOCK flag is specified.

Note that in order to be able to read, the filtering process has to be started by defining either a section or a PES filter by means of the ioctl functions, and then starting the
filtering process via the DMX_START ioctl function or by setting the DMX_IMMEDIATE_START flag. If the reading is done from a logical DVR demux device, the data will constitute a
Transport Stream including the packets from all PES filters in the corresponding demux device /dev/dvb/adapter0/demux0 having the output set to DMX_OUT_TS_TAP.

SYNOPSIS

size_t read(int fd, void ⋆buf, size_t count);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | void ⋆buf                                                                                  | Pointer to the buffer to be used for returned filtered data.                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | size_t  count                                                                              | Size of buf.                                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EWOULDBLOCK                                                                                | No data to return and O_NONBLOCK  was specified.                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EBADF                                                                                      | fd is not a valid open file descriptor.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ECRC                                                                                       | Last section had a CRC error - no data returned. The buffer is flushed.                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EOVERFLOW                                                                                  |                                                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | The filtered data was not read from the buffer in due time, resulting in non-read data     |
    |                                                                                            | being lost. The buffer is flushed.                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ETIMEDOUT                                                                                  | The section was not loaded within the stated timeout period. See ioctl DMX_SET_FILTER      |
    |                                                                                            | for how to set a timeout.                                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EFAULT                                                                                     | The driver failed to write to the callers buffer due to an invalid ⋆buf pointer.           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _dmx_fwrite:

write()
=======

DESCRIPTION

This system call is only provided by the logical device /dev/dvb/adapter0/dvr0, associated with the physical demux device that provides the actual DVR functionality. It is used for
replay of a digitally recorded Transport Stream. Matching filters have to be defined in the corresponding physical demux device, /dev/dvb/adapter0/demux0. The amount of data to be
transferred is implied by count.

SYNOPSIS

ssize_t write(int fd, const void ⋆buf, size_t count);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | void ⋆buf                                                                                  | Pointer to the buffer containing the Transport Stream.                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | size_t  count                                                                              | Size of buf.                                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EWOULDBLOCK                                                                                | No data was written. This might happen if O_NONBLOCK  was specified and there is no more   |
    |                                                                                            | buffer space available (if O_NONBLOCK  is not specified the function will block until      |
    |                                                                                            | buffer space is available).                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EBUSY                                                                                      | This error code indicates that there are conflicting requests. The corresponding demux     |
    |                                                                                            | device is setup to receive data from the front- end. Make sure that these filters are      |
    |                                                                                            | stopped and that the filters with input set to DMX_IN_DVR   are started.                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EBADF                                                                                      | fd is not a valid open file descriptor.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DMX_START:

DMX_START
=========

DESCRIPTION

This ioctl call is used to start the actual filtering operation defined via the ioctl calls DMX_SET_FILTER or DMX_SET_PES_FILTER.

SYNOPSIS

int ioctl( int fd, int request = DMX_START);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_START  for this command.                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | Invalid argument, i.e. no filtering parameters provided via the DMX_SET_FILTER   or        |
    |                                                                                            | DMX_SET_PES_FILTER    functions.                                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EBUSY                                                                                      | This error code indicates that there are conflicting requests. There are active filters    |
    |                                                                                            | filtering data from another input source. Make sure that these filters are stopped before  |
    |                                                                                            | starting this filter.                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DMX_STOP:

DMX_STOP
========

DESCRIPTION

This ioctl call is used to stop the actual filtering operation defined via the ioctl calls DMX_SET_FILTER or DMX_SET_PES_FILTER and started via the DMX_START command.

SYNOPSIS

int ioctl( int fd, int request = DMX_STOP);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_STOP  for this command.                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _DMX_SET_FILTER:

DMX_SET_FILTER
==============

DESCRIPTION

This ioctl call sets up a filter according to the filter and mask parameters provided. A timeout may be defined stating number of seconds to wait for a section to be loaded. A
value of 0 means that no timeout should be applied. Finally there is a flag field where it is possible to state whether a section should be CRC-checked, whether the filter should
be a ”one-shot” filter, i.e. if the filtering operation should be stopped after the first section is received, and whether the filtering operation should be started immediately
(without waiting for a DMX_START ioctl call). If a filter was previously set-up, this filter will be canceled, and the receive buffer will be flushed.

SYNOPSIS

int ioctl( int fd, int request = DMX_SET_FILTER, struct dmx_sct_filter_params ⋆params);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_SET_FILTER   for this command.                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct dmx_sct_filter_params    ⋆params                                                    | Pointer to structure containing filter parameters.                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _DMX_SET_PES_FILTER:

DMX_SET_PES_FILTER
==================

DESCRIPTION

This ioctl call sets up a PES filter according to the parameters provided. By a PES filter is meant a filter that is based just on the packet identifier (PID), i.e. no PES header
or payload filtering capability is supported.

The transport stream destination for the filtered output may be set. Also the PES type may be stated in order to be able to e.g. direct a video stream directly to the video
decoder. Finally there is a flag field where it is possible to state whether the filtering operation should be started immediately (without waiting for a DMX_START ioctl call). If
a filter was previously set-up, this filter will be cancelled, and the receive buffer will be flushed.

SYNOPSIS

int ioctl( int fd, int request = DMX_SET_PES_FILTER, struct dmx_pes_filter_params ⋆params);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_SET_PES_FILTER    for this command.                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct dmx_pes_filter_params    ⋆params                                                    | Pointer to structure containing filter parameters.                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EBUSY                                                                                      | This error code indicates that there are conflicting requests. There are active filters    |
    |                                                                                            | filtering data from another input source. Make sure that these filters are stopped before  |
    |                                                                                            | starting this filter.                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DMX_SET_BUFFER_SIZE:

DMX_SET_BUFFER_SIZE
===================

DESCRIPTION

This ioctl call is used to set the size of the circular buffer used for filtered data. The default size is two maximum sized sections, i.e. if this function is not called a buffer
size of 2 ⋆ 4096 bytes will be used.

SYNOPSIS

int ioctl( int fd, int request = DMX_SET_BUFFER_SIZE, unsigned long size);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_SET_BUFFER_SIZE    for this command.                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | unsigned long size                                                                         | Size of circular buffer.                                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _DMX_GET_EVENT:

DMX_GET_EVENT
=============

DESCRIPTION

This ioctl call returns an event if available. If an event is not available, the behavior depends on whether the device is in blocking or non-blocking mode. In the latter case, the
call fails immediately with errno set to EWOULDBLOCK. In the former case, the call blocks until an event becomes available.

The standard Linux poll() and/or select() system calls can be used with the device file descriptor to watch for new events. For select(), the file descriptor should be included in
the exceptfds argument, and for poll(), POLLPRI should be specified as the wake-up condition. Only the latest event for each filter is saved.

SYNOPSIS

int ioctl( int fd, int request = DMX_GET_EVENT, struct dmx_event ⋆ev);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_GET_EVENT   for this command.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct dmx_event  ⋆ev                                                                      | Pointer to the location where the event is to be stored.                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EWOULDBLOCK                                                                                | There is no event pending, and the device is in non-blocking mode.                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DMX_GET_STC:

DMX_GET_STC
===========

DESCRIPTION

This ioctl call returns the current value of the system time counter (which is driven by a PES filter of type DMX_PES_PCR). Some hardware supports more than one STC, so you must
specify which one by setting the num field of stc before the ioctl (range 0...n). The result is returned in form of a ratio with a 64 bit numerator and a 32 bit denominator, so the
real 90kHz STC value is stc->stc / stc->base .

SYNOPSIS

int ioctl( int fd, int request = DMX_GET_STC, struct dmx_stc ⋆stc);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_GET_STC   for this command.                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct dmx_stc  ⋆stc                                                                       | Pointer to the location where the stc is to be stored.                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | Invalid stc number.                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DMX_GET_PES_PIDS:

DMX_GET_PES_PIDS
================

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = DMX_GET_PES_PIDS, __u16[5]);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_GET_PES_PIDS    for this command.                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u16[5]                                                                                   | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _DMX_GET_CAPS:

DMX_GET_CAPS
============

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = DMX_GET_CAPS, dmx_caps_t ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_GET_CAPS   for this command.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | dmx_caps_t   ⋆                                                                             | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _DMX_SET_SOURCE:

DMX_SET_SOURCE
==============

DESCRIPTION

This ioctl is undocumented. Documentation is welcome.

SYNOPSIS

int ioctl(fd, int request = DMX_SET_SOURCE, dmx_source_t ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_SET_SOURCE   for this command.                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | dmx_source_t   ⋆                                                                           | Undocumented.                                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _DMX_ADD_PID:

DMX_ADD_PID
===========

DESCRIPTION

This ioctl call allows to add multiple PIDs to a transport stream filter previously set up with DMX_SET_PES_FILTER and output equal to DMX_OUT_TSDEMUX_TAP.

It is used by readers of /dev/dvb/adapterX/demuxY.

It may be called at any time, i.e. before or after the first filter on the shared file descriptor was started. It makes it possible to record multiple services without the need to
de-multiplex or re-multiplex TS packets.

SYNOPSIS

int ioctl(fd, int request = DMX_ADD_PID, __u16 ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_ADD_PID   for this command.                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u16   ⋆                                                                                  | PID number to be filtered.                                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _DMX_REMOVE_PID:

DMX_REMOVE_PID
==============

DESCRIPTION

This ioctl call allows to remove a PID when multiple PIDs are set on a transport stream filter, e. g. a filter previously set up with output equal to DMX_OUT_TSDEMUX_TAP,
created via either DMX_SET_PES_FILTER or DMX_ADD_PID.

It is used by readers of /dev/dvb/adapterX/demuxY.

It may be called at any time, i.e. before or after the first filter on the shared file descriptor was started. It makes it possible to record multiple services without the need to
de-multiplex or re-multiplex TS packets.

SYNOPSIS

int ioctl(fd, int request = DMX_REMOVE_PID, __u16 ⋆);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals DMX_REMOVE_PID   for this command.                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u16   ⋆                                                                                  | PID of the PES filter to be removed.                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.
