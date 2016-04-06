
.. _rds:

RDS Interface
=============

The Radio Data System transmits supplementary information in binary format, for example the station name or travel information, on an inaudible audio subcarrier of a radio program.
This interface is aimed at devices capable of receiving and/or transmitting RDS information.

For more information see the core RDS standard :ref:`iec62106` and the RBDS standard :ref:`nrsc4`.

Note that the RBDS standard as is used in the USA is almost identical to the RDS standard. Any RDS decoder/encoder can also handle RBDS. Only some of the fields have slightly
different meanings. See the RBDS standard for more information.

The RBDS standard also specifies support for MMBS (Modified Mobile Search). This is a proprietary format which seems to be discontinued. The RDS interface does not support this
format. Should support for MMBS (or the so-called 'E blocks' in general) be needed, then please contact the linux-media mailing list: https://linuxtv.org/lists.php.


Querying Capabilities
=====================

Devices supporting the RDS capturing API set the ``V4L2_CAP_RDS_CAPTURE`` flag in the ``capabilities`` field of struct :ref:`v4l2_capability <v4l2-capability>` returned by the
:ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl. Any tuner that supports RDS will set the ``V4L2_TUNER_CAP_RDS`` flag in the ``capability`` field of struct
:ref:`v4l2_tuner <v4l2-tuner>`. If the driver only passes RDS blocks without interpreting the data the ``V4L2_TUNER_CAP_RDS_BLOCK_IO`` flag has to be set, see
:ref:`Reading RDS data <reading-rds-data>`. For future use the flag ``V4L2_TUNER_CAP_RDS_CONTROLS`` has also been defined. However, a driver for a radio tuner with this
capability does not yet exist, so if you are planning to write such a driver you should discuss this on the linux-media mailing list: https://linuxtv.org/lists.php.

Whether an RDS signal is present can be detected by looking at the ``rxsubchans`` field of struct :ref:`v4l2_tuner <v4l2-tuner>`: the ``V4L2_TUNER_SUB_RDS`` will be set if RDS
data was detected.

Devices supporting the RDS output API set the ``V4L2_CAP_RDS_OUTPUT`` flag in the ``capabilities`` field of struct :ref:`v4l2_capability <v4l2-capability>` returned by the
:ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl. Any modulator that supports RDS will set the ``V4L2_TUNER_CAP_RDS`` flag in the ``capability`` field of struct
:ref:`v4l2_modulator <v4l2-modulator>`. In order to enable the RDS transmission one must set the ``V4L2_TUNER_SUB_RDS`` bit in the ``txsubchans`` field of struct
:ref:`v4l2_modulator <v4l2-modulator>`. If the driver only passes RDS blocks without interpreting the data the ``V4L2_TUNER_CAP_RDS_BLOCK_IO`` flag has to be set. If the tuner
is capable of handling RDS entities like program identification codes and radio text, the flag ``V4L2_TUNER_CAP_RDS_CONTROLS`` should be set, see
:ref:`Writing RDS data <writing-rds-data>` and :ref:`FM Transmitter Control Reference <fm-tx-controls>`.


.. _reading-rds-data:

Reading RDS data
================

RDS data can be read from the radio device with the :ref:`read() <func-read>` function. The data is packed in groups of three bytes.


.. _writing-rds-data:

Writing RDS data
================

RDS data can be written to the radio device with the :ref:`write() <func-write>` function. The data is packed in groups of three bytes, as follows:


RDS datastructures
==================


.. _v4l2-rds-data:

.. table:: struct v4l2_rds_data

    +---------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------+
    | __u8                      | ``lsb``                   | Least Significant Byte of RDS Block                                                                                              |
    +---------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------+
    | __u8                      | ``msb``                   | Most Significant Byte of RDS Block                                                                                               |
    +---------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------+
    | __u8                      | ``block``                 | Block description                                                                                                                |
    +---------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------+



.. _v4l2-rds-block:

.. table:: Block description

    +--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Bits 0-2                       | Block (aka offset) of the received data.                                                                                                               |
    +--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Bits 3-5                       | Deprecated. Currently identical to bits 0-2. Do not use these bits.                                                                                    |
    +--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Bit 6                          | Corrected bit. Indicates that an error was corrected for this data block.                                                                              |
    +--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Bit 7                          | Error bit. Indicates that an uncorrectable error occurred during reception of this block.                                                              |
    +--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+



.. _v4l2-rds-block-codes:

.. table:: Block defines

    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+
    | V4L2_RDS_BLOCK_MSK     |                        | 7                      | Mask for bits 0-2 to get the block ID.                                                                           |
    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+
    | V4L2_RDS_BLOCK_A       |                        | 0                      | Block A.                                                                                                         |
    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+
    | V4L2_RDS_BLOCK_B       |                        | 1                      | Block B.                                                                                                         |
    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+
    | V4L2_RDS_BLOCK_C       |                        | 2                      | Block C.                                                                                                         |
    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+
    | V4L2_RDS_BLOCK_D       |                        | 3                      | Block D.                                                                                                         |
    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+
    | V4L2_RDS_BLOCK_C_A     |                        | 4                      | Block C'.                                                                                                        |
    | LT                     |                        |                        |                                                                                                                  |
    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+
    | V4L2_RDS_BLOCK_INVA    | read-only              | 7                      | An invalid block.                                                                                                |
    | LID                    |                        |                        |                                                                                                                  |
    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+
    | V4L2_RDS_BLOCK_CORR    | read-only              | 0x40                   | A bit error was detected but corrected.                                                                          |
    | ECTED                  |                        |                        |                                                                                                                  |
    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+
    | V4L2_RDS_BLOCK_ERRO    | read-only              | 0x80                   | An uncorrectable error occurred.                                                                                 |
    | R                      |                        |                        |                                                                                                                  |
    +------------------------+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------+


