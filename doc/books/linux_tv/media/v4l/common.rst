
.. _common:

===================
Common API Elements
===================

Programming a V4L2 device consists of these steps:

-  Opening the device

-  Changing device properties, selecting a video and audio input, video standard, picture brightness a. o.

-  Negotiating a data format

-  Negotiating an input/output method

-  The actual input/output loop

-  Closing the device

In practice most steps are optional and can be executed out of order. It depends on the V4L2 device type, you can read about the details in :ref:`devices`. In this chapter we
will discuss the basic concepts applicable to all devices.


.. _open:

Opening and Closing Devices
===========================


Device Naming
=============

V4L2 drivers are implemented as kernel modules, loaded manually by the system administrator or automatically when a device is first discovered. The driver modules plug into the
"videodev" kernel module. It provides helper functions and a common application interface specified in this document.

Each driver thus loaded registers one or more device nodes with major number 81 and a minor number between 0 and 255. Minor numbers are allocated dynamically unless the kernel is
compiled with the kernel option CONFIG_VIDEO_FIXED_MINOR_RANGES. In that case minor numbers are allocated in ranges depending on the device node type (video, radio, etc.).

Many drivers support "video_nr", "radio_nr" or "vbi_nr" module options to select specific video/radio/vbi node numbers. This allows the user to request that the device node is
named e.g. /dev/video5 instead of leaving it to chance. When the driver supports multiple devices of the same type more than one device node number can be assigned, separated by
commas:



::

    > modprobe mydriver video_nr=0,1 radio_nr=0,1
In ``/etc/modules.conf`` this may be written as:



::

    options mydriver video_nr=0,1 radio_nr=0,1
When no device node number is given as module option the driver supplies a default.

Normally udev will create the device nodes in /dev automatically for you. If udev is not installed, then you need to enable the CONFIG_VIDEO_FIXED_MINOR_RANGES kernel option in
order to be able to correctly relate a minor number to a device node number. I.e., you need to be certain that minor number 5 maps to device node name video5. With this kernel
option different device types have different minor number ranges. These ranges are listed in :ref:`devices`.

The creation of character special files (with mknod) is a privileged operation and devices cannot be opened by major and minor number. That means applications cannot *reliable*
scan for loaded or installed drivers. The user must enter a device name, or the application can try the conventional device names.


.. _related:

Related Devices
===============

Devices can support several functions. For example video capturing, VBI capturing and radio support.

The V4L2 API creates different nodes for each of these functions.

The V4L2 API was designed with the idea that one device node could support all functions. However, in practice this never worked: this 'feature' was never used by applications and
many drivers did not support it and if they did it was certainly never tested. In addition, switching a device node between different functions only works when using the streaming
I/O API, not with the read()/write() API.

Today each device node supports just one function.

Besides video input or output the hardware may also support audio sampling or playback. If so, these functions are implemented as ALSA PCM devices with optional ALSA audio mixer
devices.

One problem with all these devices is that the V4L2 API makes no provisions to find these related devices. Some really complex devices use the Media Controller (see
:ref:`media_controller`) which can be used for this purpose. But most drivers do not use it, and while some code exists that uses sysfs to discover related devices (see
libmedia_dev in the `v4l-utils`_ git repository), there is no library yet that can provide a single API towards both Media Controller-based devices and devices that do not use the
Media Controller. If you want to work on this please write to the linux-media mailing list: https://linuxtv.org/lists.php.


Multiple Opens
==============

V4L2 devices can be opened more than once. [1]_ When this is supported by the driver, users can for example start a "panel" application to change controls like brightness or audio
volume, while another application captures video and audio. In other words, panel applications are comparable to an ALSA audio mixer application. Just opening a V4L2 device should
not change the state of the device. [2]_

Once an application has allocated the memory buffers needed for streaming data (by calling the :ref:`VIDIOC_REQBUFS <vidioc-reqbufs>` or
:ref:`VIDIOC_CREATE_BUFS <vidioc-create-bufs>` ioctls, or implicitly by calling the :ref:`read() <func-read>` or :ref:`write() <func-write>` functions) that application
(filehandle) becomes the owner of the device. It is no longer allowed to make changes that would affect the buffer sizes (e.g. by calling the :ref:`VIDIOC_S_FMT <vidioc-g-fmt>`
ioctl) and other applications are no longer allowed to allocate buffers or start or stop streaming. The EBUSY error code will be returned instead.

Merely opening a V4L2 device does not grant exclusive access. [3]_ Initiating data exchange however assigns the right to read or write the requested type of data, and to change
related properties, to this file descriptor. Applications can request additional access privileges using the priority mechanism described in :ref:`app-pri`.


Shared Data Streams
===================

V4L2 drivers should not support multiple applications reading or writing the same data stream on a device by copying buffers, time multiplexing or similar means. This is better
handled by a proxy application in user space.


Functions
=========

To open and close V4L2 devices applications use the :ref:`open() <func-open>` and :ref:`close() <func-close>` function, respectively. Devices are programmed using the
:ref:`ioctl() <func-ioctl>` function as explained in the following sections.


.. _querycap:

Querying Capabilities
=====================

Because V4L2 covers a wide variety of devices not all aspects of the API are equally applicable to all types of devices. Furthermore devices of the same type have different
capabilities and this specification permits the omission of a few complicated and less important parts of the API.

The :ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl is available to check if the kernel device is compatible with this specification, and to query the
:ref:`functions <devices>` and :ref:`I/O methods <io>` supported by the device.

Starting with kernel version 3.1, VIDIOC-QUERYCAP will return the V4L2 API version used by the driver, with generally matches the Kernel version. There's no need of using
:ref:`VIDIOC_QUERYCAP <vidioc-querycap>` to check if a specific ioctl is supported, the V4L2 core now returns ENOTTY if a driver doesn't provide support for an ioctl.

Other features can be queried by calling the respective ioctl, for example :ref:`VIDIOC_ENUMINPUT <vidioc-enuminput>` to learn about the number, types and names of video
connectors on the device. Although abstraction is a major objective of this API, the :ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl also allows driver specific applications to
reliably identify the driver.

All V4L2 drivers must support ``VIDIOC_QUERYCAP``. Applications should always call this ioctl after opening the device.


.. _app-pri:

Application Priority
====================

When multiple applications share a device it may be desirable to assign them different priorities. Contrary to the traditional "rm -rf /" school of thought a video recording
application could for example block other applications from changing video controls or switching the current TV channel. Another objective is to permit low priority applications
working in background, which can be preempted by user controlled applications and automatically regain control of the device at a later time.

Since these features cannot be implemented entirely in user space V4L2 defines the :ref:`VIDIOC_G_PRIORITY <vidioc-g-priority>` and
:ref:`VIDIOC_S_PRIORITY <vidioc-g-priority>` ioctls to request and query the access priority associate with a file descriptor. Opening a device assigns a medium priority,
compatible with earlier versions of V4L2 and drivers not supporting these ioctls. Applications requiring a different priority will usually call ``VIDIOC_S_PRIORITY`` after
verifying the device with the :ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl.

Ioctls changing driver properties, such as :ref:`VIDIOC_S_INPUT <vidioc-g-input>`, return an EBUSY error code after another application obtained higher priority.


.. _video:

Video Inputs and Outputs
========================

Video inputs and outputs are physical connectors of a device. These can be for example RF connectors (antenna/cable), CVBS a.k.a. Composite Video, S-Video or RGB connectors. Video
and VBI capture devices have inputs. Video and VBI output devices have outputs, at least one each. Radio devices have no video inputs or outputs.

To learn about the number and attributes of the available inputs and outputs applications can enumerate them with the :ref:`VIDIOC_ENUMINPUT <vidioc-enuminput>` and
:ref:`VIDIOC_ENUMOUTPUT <vidioc-enumoutput>` ioctl, respectively. The struct :ref:`v4l2_input <v4l2-input>` returned by the ``VIDIOC_ENUMINPUT`` ioctl also contains signal
status information applicable when the current video input is queried.

The :ref:`VIDIOC_G_INPUT <vidioc-g-input>` and :ref:`VIDIOC_G_OUTPUT <vidioc-g-output>` ioctls return the index of the current video input or output. To select a different
input or output applications call the :ref:`VIDIOC_S_INPUT <vidioc-g-input>` and :ref:`VIDIOC_S_OUTPUT <vidioc-g-output>` ioctls. Drivers must implement all the input
ioctls when the device has one or more inputs, all the output ioctls when the device has one or more outputs.


.. code-block:: c

    struct v4l2_input input;
    int index;

    if (-1 == ioctl(fd, VIDIOC_G_INPUT, &index)) {
        perror("VIDIOC_G_INPUT");
        exit(EXIT_FAILURE);
    }

    memset(&input, 0, sizeof(input));
    input.index = index;

    if (-1 == ioctl(fd, VIDIOC_ENUMINPUT, &input)) {
        perror("VIDIOC_ENUMINPUT");
        exit(EXIT_FAILURE);
    }

    printf("Current input: %s\\n", input.name);


.. code-block:: c

    int index;

    index = 0;

    if (-1 == ioctl(fd, VIDIOC_S_INPUT, &index)) {
        perror("VIDIOC_S_INPUT");
        exit(EXIT_FAILURE);
    }


.. _audio:

Audio Inputs and Outputs
========================

Audio inputs and outputs are physical connectors of a device. Video capture devices have inputs, output devices have outputs, zero or more each. Radio devices have no audio inputs
or outputs. They have exactly one tuner which in fact *is* an audio source, but this API associates tuners with video inputs or outputs only, and radio devices have none of
these. [4]_ A connector on a TV card to loop back the received audio signal to a sound card is not considered an audio output.

Audio and video inputs and outputs are associated. Selecting a video source also selects an audio source. This is most evident when the video and audio source is a tuner. Further
audio connectors can combine with more than one video input or output. Assumed two composite video inputs and two audio inputs exist, there may be up to four valid combinations.
The relation of video and audio connectors is defined in the ``audioset`` field of the respective struct :ref:`v4l2_input <v4l2-input>` or struct
:ref:`v4l2_output <v4l2-output>`, where each bit represents the index number, starting at zero, of one audio input or output.

To learn about the number and attributes of the available inputs and outputs applications can enumerate them with the :ref:`VIDIOC_ENUMAUDIO <vidioc-enumaudio>` and
:ref:`VIDIOC_ENUMAUDOUT <vidioc-enumaudioout>` ioctl, respectively. The struct :ref:`v4l2_audio <v4l2-audio>` returned by the ``VIDIOC_ENUMAUDIO`` ioctl also contains signal
status information applicable when the current audio input is queried.

The :ref:`VIDIOC_G_AUDIO <vidioc-g-audio>` and :ref:`VIDIOC_G_AUDOUT <vidioc-g-audioout>` ioctls report the current audio input and output, respectively. Note that, unlike
:ref:`VIDIOC_G_INPUT <vidioc-g-input>` and :ref:`VIDIOC_G_OUTPUT <vidioc-g-output>` these ioctls return a structure as ``VIDIOC_ENUMAUDIO`` and ``VIDIOC_ENUMAUDOUT`` do,
not just an index.

To select an audio input and change its properties applications call the :ref:`VIDIOC_S_AUDIO <vidioc-g-audio>` ioctl. To select an audio output (which presently has no
changeable properties) applications call the :ref:`VIDIOC_S_AUDOUT <vidioc-g-audioout>` ioctl.

Drivers must implement all audio input ioctls when the device has multiple selectable audio inputs, all audio output ioctls when the device has multiple selectable audio outputs.
When the device has any audio inputs or outputs the driver must set the ``V4L2_CAP_AUDIO`` flag in the struct :ref:`v4l2_capability <v4l2-capability>` returned by the
:ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl.


.. code-block:: c

    struct v4l2_audio audio;

    memset(&audio, 0, sizeof(audio));

    if (-1 == ioctl(fd, VIDIOC_G_AUDIO, &audio)) {
        perror("VIDIOC_G_AUDIO");
        exit(EXIT_FAILURE);
    }

    printf("Current input: %s\\n", audio.name);


.. code-block:: c

    struct v4l2_audio audio;

    memset(&audio, 0, sizeof(audio)); /* clear audio.mode, audio.reserved */

    audio.index = 0;

    if (-1 == ioctl(fd, VIDIOC_S_AUDIO, &audio)) {
        perror("VIDIOC_S_AUDIO");
        exit(EXIT_FAILURE);
    }


.. _tuner:

Tuners and Modulators
=====================


Tuners
======

Video input devices can have one or more tuners demodulating a RF signal. Each tuner is associated with one or more video inputs, depending on the number of RF connectors on the
tuner. The ``type`` field of the respective struct :ref:`v4l2_input <v4l2-input>` returned by the :ref:`VIDIOC_ENUMINPUT <vidioc-enuminput>` ioctl is set to
``V4L2_INPUT_TYPE_TUNER`` and its ``tuner`` field contains the index number of the tuner.

Radio input devices have exactly one tuner with index zero, no video inputs.

To query and change tuner properties applications use the :ref:`VIDIOC_G_TUNER <vidioc-g-tuner>` and :ref:`VIDIOC_S_TUNER <vidioc-g-tuner>` ioctls, respectively. The struct
:ref:`v4l2_tuner <v4l2-tuner>` returned by ``VIDIOC_G_TUNER`` also contains signal status information applicable when the tuner of the current video or radio input is queried.
Note that ``VIDIOC_S_TUNER`` does not switch the current tuner, when there is more than one at all. The tuner is solely determined by the current video input. Drivers must support
both ioctls and set the ``V4L2_CAP_TUNER`` flag in the struct :ref:`v4l2_capability <v4l2-capability>` returned by the :ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl when the
device has one or more tuners.


Modulators
==========

Video output devices can have one or more modulators, uh, modulating a video signal for radiation or connection to the antenna input of a TV set or video recorder. Each modulator
is associated with one or more video outputs, depending on the number of RF connectors on the modulator. The ``type`` field of the respective struct
:ref:`v4l2_output <v4l2-output>` returned by the :ref:`VIDIOC_ENUMOUTPUT <vidioc-enumoutput>` ioctl is set to ``V4L2_OUTPUT_TYPE_MODULATOR`` and its ``modulator`` field
contains the index number of the modulator.

Radio output devices have exactly one modulator with index zero, no video outputs.

A video or radio device cannot support both a tuner and a modulator. Two separate device nodes will have to be used for such hardware, one that supports the tuner functionality and
one that supports the modulator functionality. The reason is a limitation with the :ref:`VIDIOC_S_FREQUENCY <vidioc-g-frequency>` ioctl where you cannot specify whether the
frequency is for a tuner or a modulator.

To query and change modulator properties applications use the :ref:`VIDIOC_G_MODULATOR <vidioc-g-modulator>` and :ref:`VIDIOC_S_MODULATOR <vidioc-g-modulator>` ioctl. Note
that ``VIDIOC_S_MODULATOR`` does not switch the current modulator, when there is more than one at all. The modulator is solely determined by the current video output. Drivers must
support both ioctls and set the ``V4L2_CAP_MODULATOR`` flag in the struct :ref:`v4l2_capability <v4l2-capability>` returned by the :ref:`VIDIOC_QUERYCAP <vidioc-querycap>`
ioctl when the device has one or more modulators.


Radio Frequency
===============

To get and set the tuner or modulator radio frequency applications use the :ref:`VIDIOC_G_FREQUENCY <vidioc-g-frequency>` and :ref:`VIDIOC_S_FREQUENCY <vidioc-g-frequency>`
ioctl which both take a pointer to a struct :ref:`v4l2_frequency <v4l2-frequency>`. These ioctls are used for TV and radio devices alike. Drivers must support both ioctls when
the tuner or modulator ioctls are supported, or when the device is a radio device.


.. _standard:

Video Standards
===============

Video devices typically support one or more different video standards or variations of standards. Each video input and output may support another set of standards. This set is
reported by the ``std`` field of struct :ref:`v4l2_input <v4l2-input>` and struct :ref:`v4l2_output <v4l2-output>` returned by the
:ref:`VIDIOC_ENUMINPUT <vidioc-enuminput>` and :ref:`VIDIOC_ENUMOUTPUT <vidioc-enumoutput>` ioctls, respectively.

V4L2 defines one bit for each analog video standard currently in use worldwide, and sets aside bits for driver defined standards, e. g. hybrid standards to watch NTSC video tapes
on PAL TVs and vice versa. Applications can use the predefined bits to select a particular standard, although presenting the user a menu of supported standards is preferred. To
enumerate and query the attributes of the supported standards applications use the :ref:`VIDIOC_ENUMSTD <vidioc-enumstd>` ioctl.

Many of the defined standards are actually just variations of a few major standards. The hardware may in fact not distinguish between them, or do so internal and switch
automatically. Therefore enumerated standards also contain sets of one or more standard bits.

Assume a hypothetic tuner capable of demodulating B/PAL, G/PAL and I/PAL signals. The first enumerated standard is a set of B and G/PAL, switched automatically depending on the
selected radio frequency in UHF or VHF band. Enumeration gives a "PAL-B/G" or "PAL-I" choice. Similar a Composite input may collapse standards, enumerating "PAL-B/G/H/I", "NTSC-M"
and "SECAM-D/K". [5]_

To query and select the standard used by the current video input or output applications call the :ref:`VIDIOC_G_STD <vidioc-g-std>` and :ref:`VIDIOC_S_STD <vidioc-g-std>`
ioctl, respectively. The *received* standard can be sensed with the :ref:`VIDIOC_QUERYSTD <vidioc-querystd>` ioctl. Note that the parameter of all these ioctls is a pointer to a
:ref:`v4l2_std_id <v4l2-std-id>` type (a standard set), *not* an index into the standard enumeration. Drivers must implement all video standard ioctls when the device has one
or more video inputs or outputs.

Special rules apply to devices such as USB cameras where the notion of video standards makes little sense. More generally for any capture or output device which is:

-  incapable of capturing fields or frames at the nominal rate of the video standard, or

-  that does not support the video standard formats at all.

Here the driver shall set the ``std`` field of struct :ref:`v4l2_input <v4l2-input>` and struct :ref:`v4l2_output <v4l2-output>` to zero and the ``VIDIOC_G_STD``,
``VIDIOC_S_STD``, ``VIDIOC_QUERYSTD`` and ``VIDIOC_ENUMSTD`` ioctls shall return the ENOTTY error code or the EINVAL error code.

Applications can make use of the :ref:`input-capabilities` and :ref:`output-capabilities` flags to determine whether the video standard ioctls can be used with the given input
or output.


.. code-block:: c

    v4l2_std_id std_id;
    struct v4l2_standard standard;

    if (-1 == ioctl(fd, VIDIOC_G_STD, &std_id)) {
        /* Note when VIDIOC_ENUMSTD always returns ENOTTY this
           is no video device or it falls under the USB exception,
           and VIDIOC_G_STD returning ENOTTY is no error. */

        perror("VIDIOC_G_STD");
        exit(EXIT_FAILURE);
    }

    memset(&standard, 0, sizeof(standard));
    standard.index = 0;

    while (0 == ioctl(fd, VIDIOC_ENUMSTD, &standard)) {
        if (standard.id & std_id) {
               printf("Current video standard: %s\\n", standard.name);
               exit(EXIT_SUCCESS);
        }

        standard.index++;
    }

    /* EINVAL indicates the end of the enumeration, which cannot be
       empty unless this device falls under the USB exception. */

    if (errno == EINVAL || standard.index == 0) {
        perror("VIDIOC_ENUMSTD");
        exit(EXIT_FAILURE);
    }


.. code-block:: c

    struct v4l2_input input;
    struct v4l2_standard standard;

    memset(&input, 0, sizeof(input));

    if (-1 == ioctl(fd, VIDIOC_G_INPUT, &input.index)) {
        perror("VIDIOC_G_INPUT");
        exit(EXIT_FAILURE);
    }

    if (-1 == ioctl(fd, VIDIOC_ENUMINPUT, &input)) {
        perror("VIDIOC_ENUM_INPUT");
        exit(EXIT_FAILURE);
    }

    printf("Current input %s supports:\\n", input.name);

    memset(&standard, 0, sizeof(standard));
    standard.index = 0;

    while (0 == ioctl(fd, VIDIOC_ENUMSTD, &standard)) {
        if (standard.id & input.std)
            printf("%s\\n", standard.name);

        standard.index++;
    }

    /* EINVAL indicates the end of the enumeration, which cannot be
       empty unless this device falls under the USB exception. */

    if (errno != EINVAL || standard.index == 0) {
        perror("VIDIOC_ENUMSTD");
        exit(EXIT_FAILURE);
    }


.. code-block:: c

    struct v4l2_input input;
    v4l2_std_id std_id;

    memset(&input, 0, sizeof(input));

    if (-1 == ioctl(fd, VIDIOC_G_INPUT, &input.index)) {
        perror("VIDIOC_G_INPUT");
        exit(EXIT_FAILURE);
    }

    if (-1 == ioctl(fd, VIDIOC_ENUMINPUT, &input)) {
        perror("VIDIOC_ENUM_INPUT");
        exit(EXIT_FAILURE);
    }

    if (0 == (input.std & V4L2_STD_PAL_BG)) {
        fprintf(stderr, "Oops. B/G PAL is not supported.\\n");
        exit(EXIT_FAILURE);
    }

    /* Note this is also supposed to work when only B
       or G/PAL is supported. */

    std_id = V4L2_STD_PAL_BG;

    if (-1 == ioctl(fd, VIDIOC_S_STD, &std_id)) {
        perror("VIDIOC_S_STD");
        exit(EXIT_FAILURE);
    }


.. _dv-timings:

Digital Video (DV) Timings
==========================

The video standards discussed so far have been dealing with Analog TV and the corresponding video timings. Today there are many more different hardware interfaces such as High
Definition TV interfaces (HDMI), VGA, DVI connectors etc., that carry video signals and there is a need to extend the API to select the video timings for these interfaces. Since it
is not possible to extend the :ref:`v4l2_std_id <v4l2-std-id>` due to the limited bits available, a new set of ioctls was added to set/get video timings at the input and
output.

These ioctls deal with the detailed digital video timings that define each video format. This includes parameters such as the active video width and height, signal polarities,
frontporches, backporches, sync widths etc. The ``linux/v4l2-dv-timings.h`` header can be used to get the timings of the formats in the :ref:`cea861` and :ref:`vesadmt`
standards.

To enumerate and query the attributes of the DV timings supported by a device applications use the :ref:`VIDIOC_ENUM_DV_TIMINGS <vidioc-enum-dv-timings>` and
:ref:`VIDIOC_DV_TIMINGS_CAP <vidioc-dv-timings-cap>` ioctls. To set DV timings for the device applications use the :ref:`VIDIOC_S_DV_TIMINGS <vidioc-g-dv-timings>` ioctl
and to get current DV timings they use the :ref:`VIDIOC_G_DV_TIMINGS <vidioc-g-dv-timings>` ioctl. To detect the DV timings as seen by the video receiver applications use the
:ref:`VIDIOC_QUERY_DV_TIMINGS <vidioc-query-dv-timings>` ioctl.

Applications can make use of the :ref:`input-capabilities` and :ref:`output-capabilities` flags to determine whether the digital video ioctls can be used with the given input
or output.


.. toctree::
    :maxdepth: 1

    controls

.. _format:

Data Formats
============


Data Format Negotiation
=======================

Different devices exchange different kinds of data with applications, for example video images, raw or sliced VBI data, RDS datagrams. Even within one kind many different formats
are possible, in particular an abundance of image formats. Although drivers must provide a default and the selection persists across closing and reopening a device, applications
should always negotiate a data format before engaging in data exchange. Negotiation means the application asks for a particular format and the driver selects and reports the best
the hardware can do to satisfy the request. Of course applications can also just query the current selection.

A single mechanism exists to negotiate all data formats using the aggregate struct :ref:`v4l2_format <v4l2-format>` and the :ref:`VIDIOC_G_FMT <vidioc-g-fmt>` and
:ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctls. Additionally the :ref:`VIDIOC_TRY_FMT <vidioc-g-fmt>` ioctl can be used to examine what the hardware *could* do, without actually
selecting a new data format. The data formats supported by the V4L2 API are covered in the respective device section in :ref:`devices`. For a closer look at image formats see
:ref:`pixfmt`.

The ``VIDIOC_S_FMT`` ioctl is a major turning-point in the initialization sequence. Prior to this point multiple panel applications can access the same device concurrently to
select the current input, change controls or modify other properties. The first ``VIDIOC_S_FMT`` assigns a logical stream (video data, VBI data etc.) exclusively to one file
descriptor.

Exclusive means no other application, more precisely no other file descriptor, can grab this stream or change device properties inconsistent with the negotiated parameters. A video
standard change for example, when the new standard uses a different number of scan lines, can invalidate the selected image format. Therefore only the file descriptor owning the
stream can make invalidating changes. Accordingly multiple file descriptors which grabbed different logical streams prevent each other from interfering with their settings. When
for example video overlay is about to start or already in progress, simultaneous video capturing may be restricted to the same cropping and image size.

When applications omit the ``VIDIOC_S_FMT`` ioctl its locking side effects are implied by the next step, the selection of an I/O method with the
:ref:`VIDIOC_REQBUFS <vidioc-reqbufs>` ioctl or implicit with the first :ref:`read() <func-read>` or :ref:`write() <func-write>` call.

Generally only one logical stream can be assigned to a file descriptor, the exception being drivers permitting simultaneous video capturing and overlay using the same file
descriptor for compatibility with V4L and earlier versions of V4L2. Switching the logical stream or returning into "panel mode" is possible by closing and reopening the device.
Drivers *may* support a switch using ``VIDIOC_S_FMT``.

All drivers exchanging data with applications must support the ``VIDIOC_G_FMT`` and ``VIDIOC_S_FMT`` ioctl. Implementation of the ``VIDIOC_TRY_FMT`` is highly recommended but
optional.


Image Format Enumeration
========================

Apart of the generic format negotiation functions a special ioctl to enumerate all image formats supported by video capture, overlay or output devices is available. [6]_

The :ref:`VIDIOC_ENUM_FMT <vidioc-enum-fmt>` ioctl must be supported by all drivers exchanging image data with applications.

    **Important**

    Drivers are not supposed to convert image formats in kernel space. They must enumerate only formats directly supported by the hardware. If necessary driver writers should
    publish an example conversion routine or library for integration into applications.


.. toctree::
    :maxdepth: 1

    planar-apis

.. _crop:

Image Cropping, Insertion and Scaling
=====================================

Some video capture devices can sample a subsection of the picture and shrink or enlarge it to an image of arbitrary size. We call these abilities cropping and scaling. Some video
output devices can scale an image up or down and insert it at an arbitrary scan line and horizontal offset into a video signal.

Applications can use the following API to select an area in the video signal, query the default area and the hardware limits. *Despite their name, the
:ref:`VIDIOC_CROPCAP <vidioc-cropcap>`, :ref:`VIDIOC_G_CROP <vidioc-g-crop>` and :ref:`VIDIOC_S_CROP <vidioc-g-crop>` ioctls apply to input as well as output devices.*

Scaling requires a source and a target. On a video capture or overlay device the source is the video signal, and the cropping ioctls determine the area actually sampled. The target
are images read by the application or overlaid onto the graphics screen. Their size (and position for an overlay) is negotiated with the :ref:`VIDIOC_G_FMT <vidioc-g-fmt>` and
:ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctls.

On a video output device the source are the images passed in by the application, and their size is again negotiated with the ``VIDIOC_G/S_FMT`` ioctls, or may be encoded in a
compressed video stream. The target is the video signal, and the cropping ioctls determine the area where the images are inserted.

Source and target rectangles are defined even if the device does not support scaling or the ``VIDIOC_G/S_CROP`` ioctls. Their size (and position where applicable) will be fixed in
this case. *All capture and output device must support the ``VIDIOC_CROPCAP`` ioctl such that applications can determine if scaling takes place.*


Cropping Structures
===================


.. _crop-scale:

.. figure::  common_files/crop.*
    :alt:    crop.pdf / crop.gif
    :align:  center

    Image Cropping, Insertion and Scaling

    The cropping, insertion and scaling process



For capture devices the coordinates of the top left corner, width and height of the area which can be sampled is given by the ``bounds`` substructure of the struct
:ref:`v4l2_cropcap <v4l2-cropcap>` returned by the ``VIDIOC_CROPCAP`` ioctl. To support a wide range of hardware this specification does not define an origin or units. However
by convention drivers should horizontally count unscaled samples relative to 0H (the leading edge of the horizontal sync pulse, see :ref:`vbi-hsync`). Vertically ITU-R line
numbers of the first field (:ref:`vbi-525`, :ref:`vbi-625`), multiplied by two if the driver can capture both fields.

The top left corner, width and height of the source rectangle, that is the area actually sampled, is given by struct :ref:`v4l2_crop <v4l2-crop>` using the same coordinate
system as struct :ref:`v4l2_cropcap <v4l2-cropcap>`. Applications can use the ``VIDIOC_G_CROP`` and ``VIDIOC_S_CROP`` ioctls to get and set this rectangle. It must lie
completely within the capture boundaries and the driver may further adjust the requested size and/or position according to hardware limitations.

Each capture device has a default source rectangle, given by the ``defrect`` substructure of struct :ref:`v4l2_cropcap <v4l2-cropcap>`. The center of this rectangle shall align
with the center of the active picture area of the video signal, and cover what the driver writer considers the complete picture. Drivers shall reset the source rectangle to the
default when the driver is first loaded, but not later.

For output devices these structures and ioctls are used accordingly, defining the *target* rectangle where the images will be inserted into the video signal.


Scaling Adjustments
===================

Video hardware can have various cropping, insertion and scaling limitations. It may only scale up or down, support only discrete scaling factors, or have different scaling
abilities in horizontal and vertical direction. Also it may not support scaling at all. At the same time the struct :ref:`v4l2_crop <v4l2-crop>` rectangle may have to be
aligned, and both the source and target rectangles may have arbitrary upper and lower size limits. In particular the maximum ``width`` and ``height`` in struct
:ref:`v4l2_crop <v4l2-crop>` may be smaller than the struct :ref:`v4l2_cropcap <v4l2-cropcap>`. ``bounds`` area. Therefore, as usual, drivers are expected to adjust the
requested parameters and return the actual values selected.

Applications can change the source or the target rectangle first, as they may prefer a particular image size or a certain area in the video signal. If the driver has to adjust both
to satisfy hardware limitations, the last requested rectangle shall take priority, and the driver should preferably adjust the opposite one. The
:ref:`VIDIOC_TRY_FMT <vidioc-g-fmt>` ioctl however shall not change the driver state and therefore only adjust the requested rectangle.

Suppose scaling on a video capture device is restricted to a factor 1:1 or 2:1 in either direction and the target image size must be a multiple of 16 × 16 pixels. The source
cropping rectangle is set to defaults, which are also the upper limit in this example, of 640 × 400 pixels at offset 0, 0. An application requests an image size of 300 × 225
pixels, assuming video will be scaled down from the "full picture" accordingly. The driver sets the image size to the closest possible values 304 × 224, then chooses the cropping
rectangle closest to the requested size, that is 608 × 224 (224 × 2:1 would exceed the limit 400). The offset 0, 0 is still valid, thus unmodified. Given the default cropping
rectangle reported by ``VIDIOC_CROPCAP`` the application can easily propose another offset to center the cropping rectangle.

Now the application may insist on covering an area using a picture aspect ratio closer to the original request, so it asks for a cropping rectangle of 608 × 456 pixels. The present
scaling factors limit cropping to 640 × 384, so the driver returns the cropping size 608 × 384 and adjusts the image size to closest possible 304 × 192.


Examples
========

Source and target rectangles shall remain unchanged across closing and reopening a device, such that piping data into or out of a device will work without special preparations.
More advanced applications should ensure the parameters are suitable before starting I/O.

(A video capture device is assumed; change ``V4L2_BUF_TYPE_VIDEO_CAPTURE`` for other devices.)


.. code-block:: c

    struct v4l2_cropcap cropcap;
    struct v4l2_crop crop;

    memset (&cropcap, 0, sizeof (cropcap));
    cropcap.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    if (-1 == ioctl (fd, VIDIOC_CROPCAP, &cropcap)) {
        perror ("VIDIOC_CROPCAP");
        exit (EXIT_FAILURE);
    }

    memset (&crop, 0, sizeof (crop));
    crop.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    crop.c = cropcap.defrect;

    /* Ignore if cropping is not supported (EINVAL). */

    if (-1 == ioctl (fd, VIDIOC_S_CROP, &crop)
        && errno != EINVAL) {
        perror ("VIDIOC_S_CROP");
        exit (EXIT_FAILURE);
    }

(A video capture device is assumed.)


.. code-block:: c

    struct v4l2_cropcap cropcap;
    struct v4l2_format format;

    reset_cropping_parameters ();

    /* Scale down to 1/4 size of full picture. */

    memset (&format, 0, sizeof (format)); /* defaults */

    format.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    format.fmt.pix.width = cropcap.defrect.width >> 1;
    format.fmt.pix.height = cropcap.defrect.height >> 1;
    format.fmt.pix.pixelformat = V4L2_PIX_FMT_YUYV;

    if (-1 == ioctl (fd, VIDIOC_S_FMT, &format)) {
        perror ("VIDIOC_S_FORMAT");
        exit (EXIT_FAILURE);
    }

    /* We could check the actual image size now, the actual scaling factor
       or if the driver can scale at all. */


.. code-block:: c

    struct v4l2_cropcap cropcap;
    struct v4l2_crop crop;

    memset (&cropcap, 0, sizeof (cropcap));
    cropcap.type = V4L2_BUF_TYPE_VIDEO_OUTPUT;

    if (-1 == ioctl (fd, VIDIOC_CROPCAP;, &cropcap)) {
        perror ("VIDIOC_CROPCAP");
        exit (EXIT_FAILURE);
    }

    memset (&crop, 0, sizeof (crop));

    crop.type = V4L2_BUF_TYPE_VIDEO_OUTPUT;
    crop.c = cropcap.defrect;

    /* Scale the width and height to 50 % of their original size
       and center the output. */

    crop.c.width /= 2;
    crop.c.height /= 2;
    crop.c.left += crop.c.width / 2;
    crop.c.top += crop.c.height / 2;

    /* Ignore if cropping is not supported (EINVAL). */

    if (-1 == ioctl (fd, VIDIOC_S_CROP, &crop)
        && errno != EINVAL) {
        perror ("VIDIOC_S_CROP");
        exit (EXIT_FAILURE);
    }

(A video capture device is assumed.)


.. code-block:: c

    struct v4l2_cropcap cropcap;
    struct v4l2_crop crop;
    struct v4l2_format format;
    double hscale, vscale;
    double aspect;
    int dwidth, dheight;

    memset (&cropcap, 0, sizeof (cropcap));
    cropcap.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    if (-1 == ioctl (fd, VIDIOC_CROPCAP, &cropcap)) {
        perror ("VIDIOC_CROPCAP");
        exit (EXIT_FAILURE);
    }

    memset (&crop, 0, sizeof (crop));
    crop.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    if (-1 == ioctl (fd, VIDIOC_G_CROP, &crop)) {
        if (errno != EINVAL) {
            perror ("VIDIOC_G_CROP");
            exit (EXIT_FAILURE);
        }

        /* Cropping not supported. */
        crop.c = cropcap.defrect;
    }

    memset (&format, 0, sizeof (format));
    format.fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    if (-1 == ioctl (fd, VIDIOC_G_FMT, &format)) {
        perror ("VIDIOC_G_FMT");
        exit (EXIT_FAILURE);
    }

    /* The scaling applied by the driver. */

    hscale = format.fmt.pix.width / (double) crop.c.width;
    vscale = format.fmt.pix.height / (double) crop.c.height;

    aspect = cropcap.pixelaspect.numerator /
         (double) cropcap.pixelaspect.denominator;
    aspect = aspect * hscale / vscale;

    /* Devices following ITU-R BT.601 do not capture
       square pixels. For playback on a computer monitor
       we should scale the images to this size. */

    dwidth = format.fmt.pix.width / aspect;
    dheight = format.fmt.pix.height;


.. toctree::
    :maxdepth: 1

    selection-api

.. _streaming-par:

Streaming Parameters
====================

Streaming parameters are intended to optimize the video capture process as well as I/O. Presently applications can request a high quality capture mode with the
:ref:`VIDIOC_S_PARM <vidioc-g-parm>` ioctl.

The current video standard determines a nominal number of frames per second. If less than this number of frames is to be captured or output, applications can request frame skipping
or duplicating on the driver side. This is especially useful when using the :ref:`read() <func-read>` or :ref:`write() <func-write>`, which are not augmented by timestamps or
sequence counters, and to avoid unnecessary data copying.

Finally these ioctls can be used to determine the number of buffers used internally by a driver in read/write mode. For implications see the section discussing the
:ref:`read() <func-read>` function.

To get and set the streaming parameters applications call the :ref:`VIDIOC_G_PARM <vidioc-g-parm>` and :ref:`VIDIOC_S_PARM <vidioc-g-parm>` ioctl, respectively. They take a
pointer to a struct :ref:`v4l2_streamparm <v4l2-streamparm>`, which contains a union holding separate parameters for input and output devices.

These ioctls are optional, drivers need not implement them. If so, they return the EINVAL error code.

.. [1]
   There are still some old and obscure drivers that have not been updated to allow for multiple opens. This implies that for such drivers :ref:`open() <func-open>` can return an
   EBUSY error code when the device is already in use.

.. [2]
   Unfortunately, opening a radio device often switches the state of the device to radio mode in many drivers. This behavior should be fixed eventually as it violates the V4L2
   specification.

.. [3]
   Drivers could recognize the ``O_EXCL`` open flag. Presently this is not required, so applications cannot know if it really works.

.. [4]
   Actually struct :ref:`v4l2_audio <v4l2-audio>` ought to have a ``tuner`` field like struct :ref:`v4l2_input <v4l2-input>`, not only making the API more consistent but also
   permitting radio devices with multiple tuners.

.. [5]
   Some users are already confused by technical terms PAL, NTSC and SECAM. There is no point asking them to distinguish between B, G, D, or K when the software or hardware can do
   that automatically.

.. [6]
   Enumerating formats an application has no a-priori knowledge of (otherwise it could explicitly ask for them and need not enumerate) seems useless, but there are applications
   serving as proxy between drivers and the actual video applications for which this is useful.

.. _v4l-utils: http://git.linuxtv.org/cgit.cgi/v4l-utils.git/
