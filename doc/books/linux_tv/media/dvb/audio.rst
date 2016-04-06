
.. _dvb_audio:

DVB Audio Device
================

The DVB audio device controls the MPEG2 audio decoder of the DVB hardware. It can be accessed through ``/dev/dvb/adapter?/audio?``. Data types and and ioctl definitions can be
accessed by including ``linux/dvb/audio.h`` in your application.

Please note that some DVB cards don’t have their own MPEG decoder, which results in the omission of the audio and video device.

These ioctls were also used by V4L2 to control MPEG decoders implemented in V4L2. The use of these ioctls for that purpose has been made obsolete and proper V4L2 ioctls or controls
have been created to replace that functionality.


.. _audio_data_types:

Audio Data Types
================

This section describes the structures, data types and defines used when talking to the audio device.


.. _audio-stream-source-t:

audio_stream_source_t
=====================

The audio stream source is set through the AUDIO_SELECT_SOURCE call and can take the following values, depending on whether we are replaying from an internal (demux) or external
(user write) source.


.. code-block:: c

    typedef enum {
        AUDIO_SOURCE_DEMUX,
        AUDIO_SOURCE_MEMORY
    } audio_stream_source_t;

AUDIO_SOURCE_DEMUX selects the demultiplexer (fed either by the frontend or the DVR device) as the source of the video stream. If AUDIO_SOURCE_MEMORY is selected the stream
comes from the application through the ``write()`` system call.


.. _audio-play-state-t:

audio_play_state_t
==================

The following values can be returned by the AUDIO_GET_STATUS call representing the state of audio playback.


.. code-block:: c

    typedef enum {
        AUDIO_STOPPED,
        AUDIO_PLAYING,
        AUDIO_PAUSED
    } audio_play_state_t;


.. _audio-channel-select-t:

audio_channel_select_t
======================

The audio channel selected via AUDIO_CHANNEL_SELECT is determined by the following values.


.. code-block:: c

    typedef enum {
        AUDIO_STEREO,
        AUDIO_MONO_LEFT,
        AUDIO_MONO_RIGHT,
        AUDIO_MONO,
        AUDIO_STEREO_SWAPPED
    } audio_channel_select_t;


.. _audio-status:

struct audio_status
===================

The AUDIO_GET_STATUS call returns the following structure informing about various states of the playback operation.


.. code-block:: c

    typedef struct audio_status {
        boolean AV_sync_state;
        boolean mute_state;
        audio_play_state_t play_state;
        audio_stream_source_t stream_source;
        audio_channel_select_t channel_select;
        boolean bypass_mode;
        audio_mixer_t mixer_state;
    } audio_status_t;


.. _audio-mixer:

struct audio_mixer
==================

The following structure is used by the AUDIO_SET_MIXER call to set the audio volume.


.. code-block:: c

    typedef struct audio_mixer {
        unsigned int volume_left;
        unsigned int volume_right;
    } audio_mixer_t;


.. _audio_encodings:

audio encodings
===============

A call to AUDIO_GET_CAPABILITIES returns an unsigned integer with the following bits set according to the hardwares capabilities.


.. code-block:: c

     #define AUDIO_CAP_DTS    1
     #define AUDIO_CAP_LPCM   2
     #define AUDIO_CAP_MP1    4
     #define AUDIO_CAP_MP2    8
     #define AUDIO_CAP_MP3   16
     #define AUDIO_CAP_AAC   32
     #define AUDIO_CAP_OGG   64
     #define AUDIO_CAP_SDDS 128
     #define AUDIO_CAP_AC3  256


.. _audio-karaoke:

struct audio_karaoke
====================

The ioctl AUDIO_SET_KARAOKE uses the following format:


.. code-block:: c

    typedef
    struct audio_karaoke {
        int vocal1;
        int vocal2;
        int melody;
    } audio_karaoke_t;

If Vocal1 or Vocal2 are non-zero, they get mixed into left and right t at 70% each. If both, Vocal1 and Vocal2 are non-zero, Vocal1 gets mixed into the left channel and Vocal2 into
the right channel at 100% each. Ff Melody is non-zero, the melody channel gets mixed into left and right.


.. _audio-attributes-t:

audio attributes
================

The following attributes can be set by a call to AUDIO_SET_ATTRIBUTES:


.. code-block:: c

     typedef uint16_t audio_attributes_t;
     /*   bits: descr. */
     /*   15-13 audio coding mode (0=ac3, 2=mpeg1, 3=mpeg2ext, 4=LPCM, 6=DTS, */
     /*   12    multichannel extension */
     /*   11-10 audio type (0=not spec, 1=language included) */
     /*    9- 8 audio application mode (0=not spec, 1=karaoke, 2=surround) */
     /*    7- 6 Quantization / DRC (mpeg audio: 1=DRC exists)(lpcm: 0=16bit,  */
     /*    5- 4 Sample frequency fs (0=48kHz, 1=96kHz) */
     /*    2- 0 number of audio channels (n+1 channels) */


.. _audio_function_calls:

Audio Function Calls
====================


.. _audio_fopen:

open()
======

DESCRIPTION

This system call opens a named audio device (e.g. /dev/dvb/adapter0/audio0) for subsequent use. When an open() call has succeeded, the device will be ready for use. The
significance of blocking or non-blocking mode is described in the documentation for functions where there is a difference. It does not affect the semantics of the open() call
itself. A device opened in blocking mode can later be put into non-blocking mode (and vice versa) using the F_SETFL command of the fcntl system call. This is a standard system
call, documented in the Linux manual page for fcntl. Only one user can open the Audio Device in O_RDWR mode. All other attempts to open the device in this mode will fail, and an
error code will be returned. If the Audio Device is opened in O_RDONLY mode, the only ioctl call that can be used is AUDIO_GET_STATUS. All other call will return with an error
code.

SYNOPSIS

int open(const char ⋆deviceName, int flags);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | const char ⋆deviceName                                                                     | Name of specific audio device.                                                             |
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
    | EBUSY                                                                                      | Device or resource busy.                                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | Invalid argument.                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _audio_fclose:

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



.. _audio_fwrite:

write()
=======

DESCRIPTION

This system call can only be used if AUDIO_SOURCE_MEMORY is selected in the ioctl call AUDIO_SELECT_SOURCE. The data provided shall be in PES format. If O_NONBLOCK is not
specified the function will block until buffer space is available. The amount of data to be transferred is implied by count.

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
    | EPERM                                                                                      | Mode AUDIO_SOURCE_MEMORY   not selected.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ENOMEM                                                                                     | Attempted to write more data than the internal buffer can hold.                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EBADF                                                                                      | fd is not a valid open file descriptor.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _AUDIO_STOP:

AUDIO_STOP
==========

DESCRIPTION

This ioctl call asks the Audio Device to stop playing the current stream.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_STOP);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_STOP  for this command.                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_PLAY:

AUDIO_PLAY
==========

DESCRIPTION

This ioctl call asks the Audio Device to start playing an audio stream from the selected source.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_PLAY);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_PLAY  for this command.                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_PAUSE:

AUDIO_PAUSE
===========

DESCRIPTION

This ioctl call suspends the audio stream being played. Decoding and playing are paused. It is then possible to restart again decoding and playing process of the audio stream using
AUDIO_CONTINUE command.

If AUDIO_SOURCE_MEMORY is selected in the ioctl call AUDIO_SELECT_SOURCE, the DVB-subsystem will not decode (consume) any more data until the ioctl call AUDIO_CONTINUE or
AUDIO_PLAY is performed.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_PAUSE);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_PAUSE  for this command.                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_CONTINUE:

AUDIO_CONTINUE
==============

DESCRIPTION

This ioctl restarts the decoding and playing process previously paused with AUDIO_PAUSE command.

It only works if the stream were previously stopped with AUDIO_PAUSE

SYNOPSIS

int ioctl(int fd, int request = AUDIO_CONTINUE);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_CONTINUE  for this command.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_SELECT_SOURCE:

AUDIO_SELECT_SOURCE
===================

DESCRIPTION

This ioctl call informs the audio device which source shall be used for the input data. The possible sources are demux or memory. If AUDIO_SOURCE_MEMORY is selected, the data is
fed to the Audio Device through the write command.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_SELECT_SOURCE, audio_stream_source_t source);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_SELECT_SOURCE   for this command.                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | audio_stream_source_t    source                                                            | Indicates the source that shall be used for the Audio stream.                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_SET_MUTE:

AUDIO_SET_MUTE
==============

DESCRIPTION

This ioctl is for DVB devices only. To control a V4L2 decoder use the V4L2 :ref:`VIDIOC_DECODER_CMD <vidioc-decoder-cmd>` with the ``V4L2_DEC_CMD_START_MUTE_AUDIO`` flag
instead.

This ioctl call asks the audio device to mute the stream that is currently being played.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_SET_MUTE, boolean state);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_SET_MUTE   for this command.                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | boolean state                                                                              | Indicates if audio device shall mute or not.                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | TRUE Audio Mute                                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | FALSE Audio Un-mute                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_SET_AV_SYNC:

AUDIO_SET_AV_SYNC
=================

DESCRIPTION

This ioctl call asks the Audio Device to turn ON or OFF A/V synchronization.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_SET_AV_SYNC, boolean state);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_AV_SYNC   for this command.                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | boolean state                                                                              | Tells the DVB subsystem if A/V synchronization shall be ON or OFF.                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | TRUE AV-sync ON                                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | FALSE AV-sync OFF                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_SET_BYPASS_MODE:

AUDIO_SET_BYPASS_MODE
=====================

DESCRIPTION

This ioctl call asks the Audio Device to bypass the Audio decoder and forward the stream without decoding. This mode shall be used if streams that can’t be handled by the DVB
system shall be decoded. Dolby DigitalTM streams are automatically forwarded by the DVB subsystem if the hardware can handle it.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_SET_BYPASS_MODE, boolean mode);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_SET_BYPASS_MODE    for this command.                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | boolean mode                                                                               | Enables or disables the decoding of the current Audio stream in the DVB subsystem.         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | TRUE Bypass is disabled                                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | FALSE Bypass is enabled                                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_CHANNEL_SELECT:

AUDIO_CHANNEL_SELECT
====================

DESCRIPTION

This ioctl is for DVB devices only. To control a V4L2 decoder use the V4L2 ``V4L2_CID_MPEG_AUDIO_DEC_PLAYBACK`` control instead.

This ioctl call asks the Audio Device to select the requested channel if possible.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_CHANNEL_SELECT, audio_channel_select_t);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_CHANNEL_SELECT   for this command.                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | audio_channel_select_t    ch                                                               | Select the output format of the audio (mono left/right, stereo).                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_BILINGUAL_CHANNEL_SELECT:

AUDIO_BILINGUAL_CHANNEL_SELECT
==============================

DESCRIPTION

This ioctl is obsolete. Do not use in new drivers. It has been replaced by the V4L2 ``V4L2_CID_MPEG_AUDIO_DEC_MULTILINGUAL_PLAYBACK`` control for MPEG decoders controlled through
V4L2.

This ioctl call asks the Audio Device to select the requested channel for bilingual streams if possible.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_BILINGUAL_CHANNEL_SELECT, audio_channel_select_t);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_BILINGUAL_CHANNEL_SELECT    for this command.                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | audio_channel_select_t    ch                                                               | Select the output format of the audio (mono left/right, stereo).                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_GET_PTS:

AUDIO_GET_PTS
=============

DESCRIPTION

This ioctl is obsolete. Do not use in new drivers. If you need this functionality, then please contact the linux-media mailing list (https://linuxtv.org/lists.php).

This ioctl call asks the Audio Device to return the current PTS timestamp.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_GET_PTS, __u64 ⋆pts);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_GET_PTS   for this command.                                                   |
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


.. _AUDIO_GET_STATUS:

AUDIO_GET_STATUS
================

DESCRIPTION

This ioctl call asks the Audio Device to return the current state of the Audio Device.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_GET_STATUS, struct audio_status ⋆status);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_GET_STATUS   for this command.                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct audio_status  ⋆status                                                               | Returns the current state of Audio Device.                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_GET_CAPABILITIES:

AUDIO_GET_CAPABILITIES
======================

DESCRIPTION

This ioctl call asks the Audio Device to tell us about the decoding capabilities of the audio hardware.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_GET_CAPABILITIES, unsigned int ⋆cap);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_GET_CAPABILITIES   for this command.                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | unsigned int ⋆cap                                                                          | Returns a bit array of supported sound formats.                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_CLEAR_BUFFER:

AUDIO_CLEAR_BUFFER
==================

DESCRIPTION

This ioctl call asks the Audio Device to clear all software and hardware buffers of the audio decoder device.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_CLEAR_BUFFER);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_CLEAR_BUFFER   for this command.                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_SET_ID:

AUDIO_SET_ID
============

DESCRIPTION

This ioctl selects which sub-stream is to be decoded if a program or system stream is sent to the video device. If no audio stream type is set the id has to be in [0xC0,0xDF] for
MPEG sound, in [0x80,0x87] for AC3 and in [0xA0,0xA7] for LPCM. More specifications may follow for other stream types. If the stream type is set the id just specifies the substream
id of the audio stream and only the first 5 bits are recognized.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_SET_ID, int id);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_SET_ID   for this command.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int id                                                                                     | audio sub-stream id                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_SET_MIXER:

AUDIO_SET_MIXER
===============

DESCRIPTION

This ioctl lets you adjust the mixer settings of the audio decoder.

SYNOPSIS

int ioctl(int fd, int request = AUDIO_SET_MIXER, audio_mixer_t ⋆mix);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_SET_ID   for this command.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | audio_mixer_t   ⋆mix                                                                       | mixer settings.                                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _AUDIO_SET_STREAMTYPE:

AUDIO_SET_STREAMTYPE
====================

DESCRIPTION

This ioctl tells the driver which kind of audio stream to expect. This is useful if the stream offers several audio sub-streams like LPCM and AC3.

SYNOPSIS

int ioctl(fd, int request = AUDIO_SET_STREAMTYPE, int type);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_SET_STREAMTYPE   for this command.                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int type                                                                                   | stream type                                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | type is not a valid or supported stream type.                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _AUDIO_SET_EXT_ID:

AUDIO_SET_EXT_ID
================

DESCRIPTION

This ioctl can be used to set the extension id for MPEG streams in DVD playback. Only the first 3 bits are recognized.

SYNOPSIS

int ioctl(fd, int request = AUDIO_SET_EXT_ID, int id);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_SET_EXT_ID    for this command.                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int id                                                                                     | audio sub_stream_id                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | id is not a valid id.                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _AUDIO_SET_ATTRIBUTES:

AUDIO_SET_ATTRIBUTES
====================

DESCRIPTION

This ioctl is intended for DVD playback and allows you to set certain information about the audio stream.

SYNOPSIS

int ioctl(fd, int request = AUDIO_SET_ATTRIBUTES, audio_attributes_t attr );

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_SET_ATTRIBUTES   for this command.                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | audio_attributes_t   attr                                                                  | audio attributes according to section ??                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | attr is not a valid or supported attribute setting.                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _AUDIO_SET_KARAOKE:

AUDIO_SET_KARAOKE
=================

DESCRIPTION

This ioctl allows one to set the mixer settings for a karaoke DVD.

SYNOPSIS

int ioctl(fd, int request = AUDIO_SET_KARAOKE, audio_karaoke_t ⋆karaoke);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals AUDIO_SET_KARAOKE   for this command.                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | audio_karaoke_t   ⋆karaoke                                                                 | karaoke settings according to section ??.                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | karaoke is not a valid or supported karaoke setting.                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


