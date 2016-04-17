
.. _vidioc-enumstd:

====================
ioctl VIDIOC_ENUMSTD
====================

*man VIDIOC_ENUMSTD(2)*

Enumerate supported video standards


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct v4l2_standard *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.

``request``
    VIDIOC_ENUMSTD

``argp``


Description
===========

To query the attributes of a video standard, especially a custom (driver defined) one, applications initialize the ``index`` field of struct :ref:`v4l2_standard <v4l2-standard>`
and call the ``VIDIOC_ENUMSTD`` ioctl with a pointer to this structure. Drivers fill the rest of the structure or return an EINVAL error code when the index is out of bounds. To
enumerate all standards applications shall begin at index zero, incrementing by one until the driver returns EINVAL. Drivers may enumerate a different set of standards after
switching the video input or output. [1]_


.. _v4l2-standard:

.. table:: struct v4l2_standard

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``index``                                     | Number of the video standard, set by the application.                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | :ref:`v4l2_std_id    <v4l2-std-id>`           | ``id``                                        | The bits in this field identify the standard as one of the common standards listed in      |
    |                                               |                                               | :ref:`v4l2-std-id`,   or if bits 32 to 63 are set as custom standards. Multiple bits can   |
    |                                               |                                               | be set if the hardware does not distinguish between these standards, however separate      |
    |                                               |                                               | indices do not indicate the opposite. The ``id`` must be unique. No other enumerated       |
    |                                               |                                               | ``v4l2_standard`` structure, for this input or output anyway, can contain the same set of  |
    |                                               |                                               | bits.                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``name``  [24]                                | Name of the standard, a NUL-terminated ASCII string, for example: "PAL-B/G", "NTSC Japan". |
    |                                               |                                               | This information is intended for the user.                                                 |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct :ref:`v4l2_fract   <v4l2-fract>`       | ``frameperiod``                               | The frame period (not field period) is numerator / denominator. For example M/NTSC has a   |
    |                                               |                                               | frame period of 1001 / 30000 seconds.                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``framelines``                                | Total lines per frame including blanking, e. g. 625 for B/PAL.                             |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``reserved``  [4]                             | Reserved for future extensions. Drivers must set the array to zero.                        |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-fract:

.. table:: struct v4l2_fract

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``numerator``                                 |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``denominator``                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-std-id:

.. table:: typedef v4l2_std_id

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u64                                         | ``v4l2_std_id``                               | This type is a set, each bit representing another video standard as listed below and in    |
    |                                               |                                               | :ref:`video-standards`.   The 32 most significant bits are reserved for custom (driver     |
    |                                               |                                               | defined) video standards.                                                                  |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. code-block:: c

    #define V4L2_STD_PAL_B          ((v4l2_std_id)0x00000001)
    #define V4L2_STD_PAL_B1         ((v4l2_std_id)0x00000002)
    #define V4L2_STD_PAL_G          ((v4l2_std_id)0x00000004)
    #define V4L2_STD_PAL_H          ((v4l2_std_id)0x00000008)
    #define V4L2_STD_PAL_I          ((v4l2_std_id)0x00000010)
    #define V4L2_STD_PAL_D          ((v4l2_std_id)0x00000020)
    #define V4L2_STD_PAL_D1         ((v4l2_std_id)0x00000040)
    #define V4L2_STD_PAL_K          ((v4l2_std_id)0x00000080)

    #define V4L2_STD_PAL_M          ((v4l2_std_id)0x00000100)
    #define V4L2_STD_PAL_N          ((v4l2_std_id)0x00000200)
    #define V4L2_STD_PAL_Nc         ((v4l2_std_id)0x00000400)
    #define V4L2_STD_PAL_60         ((v4l2_std_id)0x00000800)

``V4L2_STD_PAL_60`` is a hybrid standard with 525 lines, 60 Hz refresh rate, and PAL color modulation with a 4.43 MHz color subcarrier. Some PAL video recorders can play back NTSC
tapes in this mode for display on a 50/60 Hz agnostic PAL TV.


.. code-block:: c

    #define V4L2_STD_NTSC_M         ((v4l2_std_id)0x00001000)
    #define V4L2_STD_NTSC_M_JP      ((v4l2_std_id)0x00002000)
    #define V4L2_STD_NTSC_443       ((v4l2_std_id)0x00004000)

``V4L2_STD_NTSC_443`` is a hybrid standard with 525 lines, 60 Hz refresh rate, and NTSC color modulation with a 4.43 MHz color subcarrier.


.. code-block:: c

    #define V4L2_STD_NTSC_M_KR      ((v4l2_std_id)0x00008000)

    #define V4L2_STD_SECAM_B        ((v4l2_std_id)0x00010000)
    #define V4L2_STD_SECAM_D        ((v4l2_std_id)0x00020000)
    #define V4L2_STD_SECAM_G        ((v4l2_std_id)0x00040000)
    #define V4L2_STD_SECAM_H        ((v4l2_std_id)0x00080000)
    #define V4L2_STD_SECAM_K        ((v4l2_std_id)0x00100000)
    #define V4L2_STD_SECAM_K1       ((v4l2_std_id)0x00200000)
    #define V4L2_STD_SECAM_L        ((v4l2_std_id)0x00400000)
    #define V4L2_STD_SECAM_LC       ((v4l2_std_id)0x00800000)

    /* ATSC/HDTV */
    #define V4L2_STD_ATSC_8_VSB     ((v4l2_std_id)0x01000000)
    #define V4L2_STD_ATSC_16_VSB    ((v4l2_std_id)0x02000000)

``V4L2_STD_ATSC_8_VSB`` and ``V4L2_STD_ATSC_16_VSB`` are U.S. terrestrial digital TV standards. Presently the V4L2 API does not support digital TV. See also the Linux DVB API at
`https://linuxtv.org <https://linuxtv.org>`__.


.. code-block:: c

    #define V4L2_STD_PAL_BG         (V4L2_STD_PAL_B         |
                     V4L2_STD_PAL_B1        |
                     V4L2_STD_PAL_G)
    #define V4L2_STD_B              (V4L2_STD_PAL_B         |
                     V4L2_STD_PAL_B1        |
                     V4L2_STD_SECAM_B)
    #define V4L2_STD_GH             (V4L2_STD_PAL_G         |
                     V4L2_STD_PAL_H         |
                     V4L2_STD_SECAM_G       |
                     V4L2_STD_SECAM_H)
    #define V4L2_STD_PAL_DK         (V4L2_STD_PAL_D         |
                     V4L2_STD_PAL_D1        |
                     V4L2_STD_PAL_K)
    #define V4L2_STD_PAL            (V4L2_STD_PAL_BG        |
                     V4L2_STD_PAL_DK        |
                     V4L2_STD_PAL_H         |
                     V4L2_STD_PAL_I)
    #define V4L2_STD_NTSC           (V4L2_STD_NTSC_M        |
                     V4L2_STD_NTSC_M_JP     |
                     V4L2_STD_NTSC_M_KR)
    #define V4L2_STD_MN             (V4L2_STD_PAL_M         |
                     V4L2_STD_PAL_N         |
                     V4L2_STD_PAL_Nc        |
                     V4L2_STD_NTSC)
    #define V4L2_STD_SECAM_DK       (V4L2_STD_SECAM_D       |
                     V4L2_STD_SECAM_K       |
                     V4L2_STD_SECAM_K1)
    #define V4L2_STD_DK             (V4L2_STD_PAL_DK        |
                     V4L2_STD_SECAM_DK)

    #define V4L2_STD_SECAM          (V4L2_STD_SECAM_B       |
                     V4L2_STD_SECAM_G       |
                     V4L2_STD_SECAM_H       |
                     V4L2_STD_SECAM_DK      |
                     V4L2_STD_SECAM_L       |
                     V4L2_STD_SECAM_LC)

    #define V4L2_STD_525_60         (V4L2_STD_PAL_M         |
                     V4L2_STD_PAL_60        |
                     V4L2_STD_NTSC          |
                     V4L2_STD_NTSC_443)
    #define V4L2_STD_625_50         (V4L2_STD_PAL           |
                     V4L2_STD_PAL_N         |
                     V4L2_STD_PAL_Nc        |
                     V4L2_STD_SECAM)

    #define V4L2_STD_UNKNOWN        0
    #define V4L2_STD_ALL            (V4L2_STD_525_60        |
                     V4L2_STD_625_50)


.. _video-standards:

.. table:: Video Standards (based on [])

    +--------------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
    | Characteristics                                              | M/NTSC [2]_                                                  | M/PAL                                                        |
    +==============================================================+==============================================================+==============================================================+
    | Frame lines                                                  | 525                                                          | 625                                                          |
    +--------------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
    | Frame period (s)                                             | 1001/30000                                                   | 1/25                                                         |
    +--------------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
    | Chrominance sub-carrier frequency (Hz)                       | 3579545 ± 10                                                 | 3579611.49 ± 10                                              |
    +--------------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
    | Nominal radio-frequency channel bandwidth (MHz)              | 6                                                            | 6                                                            |
    +--------------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
    | Sound carrier relative to vision carrier (MHz)               | + 4.5                                                        | + 4.5                                                        |
    +--------------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+



Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.

EINVAL
    The struct :ref:`v4l2_standard <v4l2-standard>` ``index`` is out of bounds.

ENODATA
    Standard video timings are not supported for this input or output.

.. [1]
   The supported standards may overlap and we need an unambiguous set to find the current standard returned by ``VIDIOC_G_STD``.

.. [2]
   Japan uses a standard similar to M/NTSC (V4L2_STD_NTSC_M_JP).

.. [3]
   The values in brackets apply to the combination N/PAL a.k.a. N :sub:`C` used in Argentina (V4L2_STD_PAL_Nc).

.. [4]
   In the Federal Republic of Germany, Austria, Italy, the Netherlands, Slovakia and Switzerland a system of two sound carriers is used, the frequency of the second carrier being
   242.1875 kHz above the frequency of the first sound carrier. For stereophonic sound transmissions a similar system is used in Australia.

.. [5]
   New Zealand uses a sound carrier displaced 5.4996 ± 0.0005 MHz from the vision carrier.

.. [6]
   In Denmark, Finland, New Zealand, Sweden and Spain a system of two sound carriers is used. In Iceland, Norway and Poland the same system is being introduced. The second carrier
   is 5.85 MHz above the vision carrier and is DQPSK modulated with 728 kbit/s sound and data multiplex. (NICAM system)

.. [7]
   In the United Kingdom, a system of two sound carriers is used. The second sound carrier is 6.552 MHz above the vision carrier and is DQPSK modulated with a 728 kbit/s sound and
   data multiplex able to carry two sound channels. (NICAM system)

.. [8]
   In France, a digital carrier 5.85 MHz away from the vision carrier may be used in addition to the main sound carrier. It is modulated in differentially encoded QPSK with a 728
   kbit/s sound and data multiplexer capable of carrying two sound channels. (NICAM system)
