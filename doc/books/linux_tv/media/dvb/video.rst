
.. _dvb_video:

DVB Video Device
================

The DVB video device controls the MPEG2 video decoder of the DVB hardware. It can be accessed through **/dev/dvb/adapter0/video0**. Data types and and ioctl definitions can be
accessed by including **linux/dvb/video.h** in your application.

Note that the DVB video device only controls decoding of the MPEG video stream, not its presentation on the TV or computer screen. On PCs this is typically handled by an associated
video4linux device, e.g. **/dev/video**, which allows scaling and defining output windows.

Some DVB cards don’t have their own MPEG decoder, which results in the omission of the audio and video device as well as the video4linux device.

The ioctls that deal with SPUs (sub picture units) and navigation packets are only supported on some MPEG decoders made for DVD playback.

These ioctls were also used by V4L2 to control MPEG decoders implemented in V4L2. The use of these ioctls for that purpose has been made obsolete and proper V4L2 ioctls or controls
have been created to replace that functionality.


.. _video_types:

Video Data Types
================


.. _video-format-t:

video_format_t
==============

The ``video_format_t`` data type defined by


.. code-block:: c

    typedef enum {
        VIDEO_FORMAT_4_3,     /* Select 4:3 format */
        VIDEO_FORMAT_16_9,    /* Select 16:9 format. */
        VIDEO_FORMAT_221_1    /* 2.21:1 */
    } video_format_t;

is used in the VIDEO_SET_FORMAT function (??) to tell the driver which aspect ratio the output hardware (e.g. TV) has. It is also used in the data structures video_status (??)
returned by VIDEO_GET_STATUS (??) and video_event (??) returned by VIDEO_GET_EVENT (??) which report about the display format of the current video stream.


.. _video-displayformat-t:

video_displayformat_t
=====================

In case the display format of the video stream and of the display hardware differ the application has to specify how to handle the cropping of the picture. This can be done using
the VIDEO_SET_DISPLAY_FORMAT call (??) which accepts


.. code-block:: c

    typedef enum {
        VIDEO_PAN_SCAN,       /* use pan and scan format */
        VIDEO_LETTER_BOX,     /* use letterbox format */
        VIDEO_CENTER_CUT_OUT  /* use center cut out format */
    } video_displayformat_t;

as argument.


.. _video-stream-source-t:

video_stream_source_t
=====================

The video stream source is set through the VIDEO_SELECT_SOURCE call and can take the following values, depending on whether we are replaying from an internal (demuxer) or
external (user write) source.


.. code-block:: c

    typedef enum {
        VIDEO_SOURCE_DEMUX, /* Select the demux as the main source */
        VIDEO_SOURCE_MEMORY /* If this source is selected, the stream
                       comes from the user through the write
                       system call */
    } video_stream_source_t;

VIDEO_SOURCE_DEMUX selects the demultiplexer (fed either by the frontend or the DVR device) as the source of the video stream. If VIDEO_SOURCE_MEMORY is selected the stream
comes from the application through the **write()** system call.


.. _video-play-state-t:

video_play_state_t
==================

The following values can be returned by the VIDEO_GET_STATUS call representing the state of video playback.


.. code-block:: c

    typedef enum {
        VIDEO_STOPPED, /* Video is stopped */
        VIDEO_PLAYING, /* Video is currently playing */
        VIDEO_FREEZED  /* Video is freezed */
    } video_play_state_t;


.. _video-command:

struct video_command
====================

The structure must be zeroed before use by the application This ensures it can be extended safely in the future.


.. code-block:: c

    struct video_command {
        __u32 cmd;
        __u32 flags;
        union {
            struct {
                __u64 pts;
            } stop;

            struct {
                /* 0 or 1000 specifies normal speed,
                   1 specifies forward single stepping,
                   -1 specifies backward single stepping,
                   >>1: playback at speed/1000 of the normal speed,
                   <-1: reverse playback at (-speed/1000) of the normal speed. */
                __s32 speed;
                __u32 format;
            } play;

            struct {
                __u32 data[16];
            } raw;
        };
    };


.. _video-size-t:

video_size_t
============


.. code-block:: c

    typedef struct {
        int w;
        int h;
        video_format_t aspect_ratio;
    } video_size_t;


.. _video-event:

struct video_event
==================

The following is the structure of a video event as it is returned by the VIDEO_GET_EVENT call.


.. code-block:: c

    struct video_event {
        __s32 type;
    #define VIDEO_EVENT_SIZE_CHANGED    1
    #define VIDEO_EVENT_FRAME_RATE_CHANGED  2
    #define VIDEO_EVENT_DECODER_STOPPED     3
    #define VIDEO_EVENT_VSYNC       4
        __kernel_time_t timestamp;
        union {
            video_size_t size;
            unsigned int frame_rate;    /* in frames per 1000sec */
            unsigned char vsync_field;  /* unknown/odd/even/progressive */
        } u;
    };


.. _video-status:

struct video_status
===================

The VIDEO_GET_STATUS call returns the following structure informing about various states of the playback operation.


.. code-block:: c

    struct video_status {
        int                   video_blank;   /* blank video on freeze? */
        video_play_state_t    play_state;    /* current state of playback */
        video_stream_source_t stream_source; /* current source (demux/memory) */
        video_format_t        video_format;  /* current aspect ratio of stream */
        video_displayformat_t display_format;/* selected cropping mode */
    };

If video_blank is set video will be blanked out if the channel is changed or if playback is stopped. Otherwise, the last picture will be displayed. play_state indicates if the
video is currently frozen, stopped, or being played back. The stream_source corresponds to the seleted source for the video stream. It can come either from the demultiplexer or
from memory. The video_format indicates the aspect ratio (one of 4:3 or 16:9) of the currently played video stream. Finally, display_format corresponds to the selected cropping
mode in case the source video format is not the same as the format of the output device.


.. _video-still-picture:

struct video_still_picture
==========================

An I-frame displayed via the VIDEO_STILLPICTURE call is passed on within the following structure.


.. code-block:: c

    /* pointer to and size of a single iframe in memory */
    struct video_still_picture {
        char *iFrame;        /* pointer to a single iframe in memory */
        int32_t size;
    };


.. _video_caps:

video capabilities
==================

A call to VIDEO_GET_CAPABILITIES returns an unsigned integer with the following bits set according to the hardwares capabilities.


.. code-block:: c

     /* bit definitions for capabilities: */
     /* can the hardware decode MPEG1 and/or MPEG2? */
     #define VIDEO_CAP_MPEG1   1
     #define VIDEO_CAP_MPEG2   2
     /* can you send a system and/or program stream to video device?
        (you still have to open the video and the audio device but only
         send the stream to the video device) */
     #define VIDEO_CAP_SYS     4
     #define VIDEO_CAP_PROG    8
     /* can the driver also handle SPU, NAVI and CSS encoded data?
        (CSS API is not present yet) */
     #define VIDEO_CAP_SPU    16
     #define VIDEO_CAP_NAVI   32
     #define VIDEO_CAP_CSS    64


.. _video-system:

video_system_t
==============

A call to VIDEO_SET_SYSTEM sets the desired video system for TV output. The following system types can be set:


.. code-block:: c

    typedef enum {
         VIDEO_SYSTEM_PAL,
         VIDEO_SYSTEM_NTSC,
         VIDEO_SYSTEM_PALN,
         VIDEO_SYSTEM_PALNc,
         VIDEO_SYSTEM_PALM,
         VIDEO_SYSTEM_NTSC60,
         VIDEO_SYSTEM_PAL60,
         VIDEO_SYSTEM_PALM60
    } video_system_t;


.. _video-highlight:

struct video_highlight
======================

Calling the ioctl VIDEO_SET_HIGHLIGHTS posts the SPU highlight information. The call expects the following format for that information:


.. code-block:: c

     typedef
     struct video_highlight {
         boolean active;      /*    1=show highlight, 0=hide highlight */
         uint8_t contrast1;   /*    7- 4  Pattern pixel contrast */
                      /*    3- 0  Background pixel contrast */
         uint8_t contrast2;   /*    7- 4  Emphasis pixel-2 contrast */
                      /*    3- 0  Emphasis pixel-1 contrast */
         uint8_t color1;      /*    7- 4  Pattern pixel color */
                      /*    3- 0  Background pixel color */
         uint8_t color2;      /*    7- 4  Emphasis pixel-2 color */
                      /*    3- 0  Emphasis pixel-1 color */
         uint32_t ypos;       /*   23-22  auto action mode */
                      /*   21-12  start y */
                      /*    9- 0  end y */
         uint32_t xpos;       /*   23-22  button color number */
                      /*   21-12  start x */
                      /*    9- 0  end x */
     } video_highlight_t;


.. _video-spu:

struct video_spu
================

Calling VIDEO_SET_SPU deactivates or activates SPU decoding, according to the following format:


.. code-block:: c

     typedef
     struct video_spu {
         boolean active;
         int stream_id;
     } video_spu_t;


.. _video-spu-palette:

struct video_spu_palette
========================

The following structure is used to set the SPU palette by calling VIDEO_SPU_PALETTE:


.. code-block:: c

     typedef
     struct video_spu_palette {
         int length;
         uint8_t *palette;
     } video_spu_palette_t;


.. _video-navi-pack:

struct video_navi_pack
======================

In order to get the navigational data the following structure has to be passed to the ioctl VIDEO_GET_NAVI:


.. code-block:: c

     typedef
     struct video_navi_pack {
         int length;         /* 0 ... 1024 */
         uint8_t data[1024];
     } video_navi_pack_t;


.. _video-attributes-t:

video_attributes_t
==================

The following attributes can be set by a call to VIDEO_SET_ATTRIBUTES:


.. code-block:: c

     typedef uint16_t video_attributes_t;
     /*   bits: descr. */
     /*   15-14 Video compression mode (0=MPEG-1, 1=MPEG-2) */
     /*   13-12 TV system (0=525/60, 1=625/50) */
     /*   11-10 Aspect ratio (0=4:3, 3=16:9) */
     /*    9- 8 permitted display mode on 4:3 monitor (0=both, 1=only pan-sca */
     /*    7    line 21-1 data present in GOP (1=yes, 0=no) */
     /*    6    line 21-2 data present in GOP (1=yes, 0=no) */
     /*    5- 3 source resolution (0=720x480/576, 1=704x480/576, 2=352x480/57 */
     /*    2    source letterboxed (1=yes, 0=no) */
     /*    0    film/camera mode (0=camera, 1=film (625/50 only)) */


.. _video_function_calls:

Video Function Calls
====================


.. _video_fopen:

open()
======

DESCRIPTION

This system call opens a named video device (e.g. /dev/dvb/adapter0/video0) for subsequent use.

When an open() call has succeeded, the device will be ready for use. The significance of blocking or non-blocking mode is described in the documentation for functions where there
is a difference. It does not affect the semantics of the open() call itself. A device opened in blocking mode can later be put into non-blocking mode (and vice versa) using the
F_SETFL command of the fcntl system call. This is a standard system call, documented in the Linux manual page for fcntl. Only one user can open the Video Device in O_RDWR mode.
All other attempts to open the device in this mode will fail, and an error-code will be returned. If the Video Device is opened in O_RDONLY mode, the only ioctl call that can be
used is VIDEO_GET_STATUS. All other call will return an error code.

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



.. _video_fclose:

close()
=======

DESCRIPTION

This system call closes a previously opened video device.

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



.. _video_fwrite:

write()
=======

DESCRIPTION

This system call can only be used if VIDEO_SOURCE_MEMORY is selected in the ioctl call VIDEO_SELECT_SOURCE. The data provided shall be in PES format, unless the capability
allows other formats. If O_NONBLOCK is not specified the function will block until buffer space is available. The amount of data to be transferred is implied by count.

SYNOPSIS

size_t write(int fd, const void ⋆buf, size_t count);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | void ⋆buf                                                                                  | Pointer to the buffer containing the PES data.                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | size_t  count                                                                              | Size of buf.                                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EPERM                                                                                      | Mode VIDEO_SOURCE_MEMORY   not selected.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ENOMEM                                                                                     | Attempted to write more data than the internal buffer can hold.                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EBADF                                                                                      | fd is not a valid open file descriptor.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _VIDEO_STOP:

VIDEO_STOP
==========

DESCRIPTION

This ioctl is for DVB devices only. To control a V4L2 decoder use the V4L2 :ref:`VIDIOC_DECODER_CMD <vidioc-decoder-cmd>` instead.

This ioctl call asks the Video Device to stop playing the current stream. Depending on the input parameter, the screen can be blanked out or displaying the last decoded frame.

SYNOPSIS

int ioctl(fd, int request = VIDEO_STOP, boolean mode);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_STOP  for this command.                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | Boolean mode                                                                               | Indicates how the screen shall be handled.                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | TRUE: Blank screen when stop.                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | FALSE: Show last decoded frame.                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_PLAY:

VIDEO_PLAY
==========

DESCRIPTION

This ioctl is for DVB devices only. To control a V4L2 decoder use the V4L2 :ref:`VIDIOC_DECODER_CMD <vidioc-decoder-cmd>` instead.

This ioctl call asks the Video Device to start playing a video stream from the selected source.

SYNOPSIS

int ioctl(fd, int request = VIDEO_PLAY);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_PLAY  for this command.                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_FREEZE:

VIDEO_FREEZE
============

DESCRIPTION

This ioctl is for DVB devices only. To control a V4L2 decoder use the V4L2 :ref:`VIDIOC_DECODER_CMD <vidioc-decoder-cmd>` instead.

This ioctl call suspends the live video stream being played. Decoding and playing are frozen. It is then possible to restart the decoding and playing process of the video stream
using the VIDEO_CONTINUE command. If VIDEO_SOURCE_MEMORY is selected in the ioctl call VIDEO_SELECT_SOURCE, the DVB subsystem will not decode any more data until the ioctl
call VIDEO_CONTINUE or VIDEO_PLAY is performed.

SYNOPSIS

int ioctl(fd, int request = VIDEO_FREEZE);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_FREEZE  for this command.                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_CONTINUE:

VIDEO_CONTINUE
==============

DESCRIPTION

This ioctl is for DVB devices only. To control a V4L2 decoder use the V4L2 :ref:`VIDIOC_DECODER_CMD <vidioc-decoder-cmd>` instead.

This ioctl call restarts decoding and playing processes of the video stream which was played before a call to VIDEO_FREEZE was made.

SYNOPSIS

int ioctl(fd, int request = VIDEO_CONTINUE);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_CONTINUE  for this command.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_SELECT_SOURCE:

VIDEO_SELECT_SOURCE
===================

DESCRIPTION

This ioctl is for DVB devices only. This ioctl was also supported by the V4L2 ivtv driver, but that has been replaced by the ivtv-specific ``IVTV_IOC_PASSTHROUGH_MODE`` ioctl.

This ioctl call informs the video device which source shall be used for the input data. The possible sources are demux or memory. If memory is selected, the data is fed to the
video device through the write command.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SELECT_SOURCE, video_stream_source_t source);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SELECT_SOURCE   for this command.                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_stream_source_t    source                                                            | Indicates which source shall be used for the Video stream.                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_SET_BLANK:

VIDEO_SET_BLANK
===============

DESCRIPTION

This ioctl call asks the Video Device to blank out the picture.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SET_BLANK, boolean mode);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_BLANK   for this command.                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | boolean mode                                                                               | TRUE: Blank screen when stop.                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | FALSE: Show last decoded frame.                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_GET_STATUS:

VIDEO_GET_STATUS
================

DESCRIPTION

This ioctl call asks the Video Device to return the current status of the device.

SYNOPSIS

int ioctl(fd, int request = VIDEO_GET_STATUS, struct video_status ⋆status);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_GET_STATUS   for this command.                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct video_status  ⋆status                                                               | Returns the current status of the Video Device.                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_GET_FRAME_COUNT:

VIDEO_GET_FRAME_COUNT
=====================

DESCRIPTION

This ioctl is obsolete. Do not use in new drivers. For V4L2 decoders this ioctl has been replaced by the ``V4L2_CID_MPEG_VIDEO_DEC_FRAME`` control.

This ioctl call asks the Video Device to return the number of displayed frames since the decoder was started.

SYNOPSIS

int ioctl(int fd, int request = VIDEO_GET_FRAME_COUNT, __u64 ⋆pts);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_GET_FRAME_COUNT    for this command.                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u64   ⋆pts                                                                               | Returns the number of frames displayed since the decoder was started.                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_GET_PTS:

VIDEO_GET_PTS
=============

DESCRIPTION

This ioctl is obsolete. Do not use in new drivers. For V4L2 decoders this ioctl has been replaced by the ``V4L2_CID_MPEG_VIDEO_DEC_PTS`` control.

This ioctl call asks the Video Device to return the current PTS timestamp.

SYNOPSIS

int ioctl(int fd, int request = VIDEO_GET_PTS, __u64 ⋆pts);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_GET_PTS   for this command.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u64   ⋆pts                                                                               | Returns the 33-bit timestamp as defined in ITU T-REC-H.222.0 / ISO/IEC 13818-1.            |
    |                                                                                            |                                                                                            |
    |                                                                                            | The PTS should belong to the currently played frame if possible, but may also be a value   |
    |                                                                                            | close to it like the PTS of the last decoded frame or the last PTS extracted by the PES    |
    |                                                                                            | parser.                                                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_GET_FRAME_RATE:

VIDEO_GET_FRAME_RATE
====================

DESCRIPTION

This ioctl call asks the Video Device to return the current framerate.

SYNOPSIS

int ioctl(int fd, int request = VIDEO_GET_FRAME_RATE, unsigned int ⋆rate);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_GET_FRAME_RATE    for this command.                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | unsigned int ⋆rate                                                                         | Returns the framerate in number of frames per 1000 seconds.                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_GET_EVENT:

VIDEO_GET_EVENT
===============

DESCRIPTION

This ioctl is for DVB devices only. To get events from a V4L2 decoder use the V4L2 :ref:`VIDIOC_DQEVENT <vidioc-dqevent>` ioctl instead.

This ioctl call returns an event of type video_event if available. If an event is not available, the behavior depends on whether the device is in blocking or non-blocking mode. In
the latter case, the call fails immediately with errno set to EWOULDBLOCK. In the former case, the call blocks until an event becomes available. The standard Linux poll() and/or
select() system calls can be used with the device file descriptor to watch for new events. For select(), the file descriptor should be included in the exceptfds argument, and for
poll(), POLLPRI should be specified as the wake-up condition. Read-only permissions are sufficient for this ioctl call.

SYNOPSIS

int ioctl(fd, int request = VIDEO_GET_EVENT, struct video_event ⋆ev);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_GET_EVENT   for this command.                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct video_event  ⋆ev                                                                    | Points to the location where the event, if any, is to be stored.                           |
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



.. _VIDEO_COMMAND:

VIDEO_COMMAND
=============

DESCRIPTION

This ioctl is obsolete. Do not use in new drivers. For V4L2 decoders this ioctl has been replaced by the :ref:`VIDIOC_DECODER_CMD <vidioc-decoder-cmd>` ioctl.

This ioctl commands the decoder. The ``video_command`` struct is a subset of the ``v4l2_decoder_cmd`` struct, so refer to the :ref:`VIDIOC_DECODER_CMD <vidioc-decoder-cmd>`
documentation for more information.

SYNOPSIS

int ioctl(int fd, int request = VIDEO_COMMAND, struct video_command ⋆cmd);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_COMMAND  for this command.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct video_command  ⋆cmd                                                                 | Commands the decoder.                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_TRY_COMMAND:

VIDEO_TRY_COMMAND
=================

DESCRIPTION

This ioctl is obsolete. Do not use in new drivers. For V4L2 decoders this ioctl has been replaced by the :ref:`VIDIOC_TRY_DECODER_CMD <vidioc-decoder-cmd>` ioctl.

This ioctl tries a decoder command. The ``video_command`` struct is a subset of the ``v4l2_decoder_cmd`` struct, so refer to the
:ref:`VIDIOC_TRY_DECODER_CMD <vidioc-decoder-cmd>` documentation for more information.

SYNOPSIS

int ioctl(int fd, int request = VIDEO_TRY_COMMAND, struct video_command ⋆cmd);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_TRY_COMMAND   for this command.                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct video_command  ⋆cmd                                                                 | Try a decoder command.                                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_GET_SIZE:

VIDEO_GET_SIZE
==============

DESCRIPTION

This ioctl returns the size and aspect ratio.

SYNOPSIS

int ioctl(int fd, int request = VIDEO_GET_SIZE, video_size_t ⋆size);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_GET_SIZE   for this command.                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_size_t   ⋆size                                                                       | Returns the size and aspect ratio.                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_SET_DISPLAY_FORMAT:

VIDEO_SET_DISPLAY_FORMAT
========================

DESCRIPTION

This ioctl call asks the Video Device to select the video format to be applied by the MPEG chip on the video.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SET_DISPLAY_FORMAT, video_display_format_t format);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_DISPLAY_FORMAT    for this command.                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_display_format_t    format                                                           | Selects the video format to be used.                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_STILLPICTURE:

VIDEO_STILLPICTURE
==================

DESCRIPTION

This ioctl call asks the Video Device to display a still picture (I-frame). The input data shall contain an I-frame. If the pointer is NULL, then the current displayed still
picture is blanked.

SYNOPSIS

int ioctl(fd, int request = VIDEO_STILLPICTURE, struct video_still_picture ⋆sp);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_STILLPICTURE  for this command.                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct video_still_picture   ⋆sp                                                           | Pointer to a location where an I-frame and size is stored.                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_FAST_FORWARD:

VIDEO_FAST_FORWARD
==================

DESCRIPTION

This ioctl call asks the Video Device to skip decoding of N number of I-frames. This call can only be used if VIDEO_SOURCE_MEMORY is selected.

SYNOPSIS

int ioctl(fd, int request = VIDEO_FAST_FORWARD, int nFrames);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_FAST_FORWARD   for this command.                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int nFrames                                                                                | The number of frames to skip.                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EPERM                                                                                      | Mode VIDEO_SOURCE_MEMORY   not selected.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _VIDEO_SLOWMOTION:

VIDEO_SLOWMOTION
================

DESCRIPTION

This ioctl call asks the video device to repeat decoding frames N number of times. This call can only be used if VIDEO_SOURCE_MEMORY is selected.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SLOWMOTION, int nFrames);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SLOWMOTION  for this command.                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int nFrames                                                                                | The number of times to repeat each frame.                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EPERM                                                                                      | Mode VIDEO_SOURCE_MEMORY   not selected.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _VIDEO_GET_CAPABILITIES:

VIDEO_GET_CAPABILITIES
======================

DESCRIPTION

This ioctl call asks the video device about its decoding capabilities. On success it returns and integer which has bits set according to the defines in section ??.

SYNOPSIS

int ioctl(fd, int request = VIDEO_GET_CAPABILITIES, unsigned int ⋆cap);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_GET_CAPABILITIES   for this command.                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | unsigned int ⋆cap                                                                          | Pointer to a location where to store the capability information.                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_SET_ID:

VIDEO_SET_ID
============

DESCRIPTION

This ioctl selects which sub-stream is to be decoded if a program or system stream is sent to the video device.

SYNOPSIS

int ioctl(int fd, int request = VIDEO_SET_ID, int id);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_ID   for this command.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int id                                                                                     | video sub-stream id                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | Invalid sub-stream id.                                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _VIDEO_CLEAR_BUFFER:

VIDEO_CLEAR_BUFFER
==================

DESCRIPTION

This ioctl call clears all video buffers in the driver and in the decoder hardware.

SYNOPSIS

int ioctl(fd, int request = VIDEO_CLEAR_BUFFER);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_CLEAR_BUFFER   for this command.                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_SET_STREAMTYPE:

VIDEO_SET_STREAMTYPE
====================

DESCRIPTION

This ioctl tells the driver which kind of stream to expect being written to it. If this call is not used the default of video PES is used. Some drivers might not support this call
and always expect PES.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SET_STREAMTYPE, int type);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_STREAMTYPE   for this command.                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int type                                                                                   | stream type                                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_SET_FORMAT:

VIDEO_SET_FORMAT
================

DESCRIPTION

This ioctl sets the screen format (aspect ratio) of the connected output device (TV) so that the output of the decoder can be adjusted accordingly.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SET_FORMAT, video_format_t format);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_FORMAT   for this command.                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_format_t   format                                                                    | video format of TV as defined in section ??.                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | format is not a valid video format.                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _VIDEO_SET_SYSTEM:

VIDEO_SET_SYSTEM
================

DESCRIPTION

This ioctl sets the television output format. The format (see section ??) may vary from the color format of the displayed MPEG stream. If the hardware is not able to display the
requested format the call will return an error.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SET_SYSTEM , video_system_t system);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_FORMAT   for this command.                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_system_t   system                                                                    | video system of TV output.                                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | system is not a valid or supported video system.                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _VIDEO_SET_HIGHLIGHT:

VIDEO_SET_HIGHLIGHT
===================

DESCRIPTION

This ioctl sets the SPU highlight information for the menu access of a DVD.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SET_HIGHLIGHT ,video_highlight_t ⋆vhilite)

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_HIGHLIGHT   for this command.                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_highlight_t   ⋆vhilite                                                               | SPU Highlight information according to section ??.                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _VIDEO_SET_SPU:

VIDEO_SET_SPU
=============

DESCRIPTION

This ioctl activates or deactivates SPU decoding in a DVD input stream. It can only be used, if the driver is able to handle a DVD stream.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SET_SPU , video_spu_t ⋆spu)

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_SPU   for this command.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_spu_t   ⋆spu                                                                         | SPU decoding (de)activation and subid setting according to section ??.                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | input is not a valid spu setting or driver cannot handle SPU.                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _VIDEO_SET_SPU_PALETTE:

VIDEO_SET_SPU_PALETTE
=====================

DESCRIPTION

This ioctl sets the SPU color palette.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SET_SPU_PALETTE ,video_spu_palette_t ⋆palette )

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_SPU_PALETTE    for this command.                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_spu_palette_t    ⋆palette                                                            | SPU palette according to section ??.                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | input is not a valid palette or driver doesn’t handle SPU.                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _VIDEO_GET_NAVI:

VIDEO_GET_NAVI
==============

DESCRIPTION

This ioctl returns navigational information from the DVD stream. This is especially needed if an encoded stream has to be decoded by the hardware.

SYNOPSIS

int ioctl(fd, int request = VIDEO_GET_NAVI , video_navi_pack_t ⋆navipack)

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_GET_NAVI   for this command.                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_navi_pack_t    ⋆navipack                                                             | PCI or DSI pack (private stream 2) according to section ??.                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EFAULT                                                                                     | driver is not able to return navigational information                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _VIDEO_SET_ATTRIBUTES:

VIDEO_SET_ATTRIBUTES
====================

DESCRIPTION

This ioctl is intended for DVD playback and allows you to set certain information about the stream. Some hardware may not need this information, but the call also tells the
hardware to prepare for DVD playback.

SYNOPSIS

int ioctl(fd, int request = VIDEO_SET_ATTRIBUTE ,video_attributes_t vattr)

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals VIDEO_SET_ATTRIBUTE   for this command.                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | video_attributes_t   vattr                                                                 | video attributes according to section ??.                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | input is not a valid attribute setting.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


