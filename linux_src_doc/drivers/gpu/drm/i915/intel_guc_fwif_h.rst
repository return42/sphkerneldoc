.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc_fwif.h

.. _`guc-firmware-layout`:

GuC Firmware Layout
===================

The GuC firmware layout looks like this:

    +-------------------------------+
    |         uc_css_header         |
    |                               |
    | contains major/minor version  |
    +-------------------------------+
    |             uCode             |
    +-------------------------------+
    |         RSA signature         |
    +-------------------------------+
    |          modulus key          |
    +-------------------------------+
    |          exponent val         |
    +-------------------------------+

The firmware may or may not have modulus key and exponent data. The header,
uCode and RSA signature are must-have components that will be used by driver.
Length of each components, which is all in dwords, can be found in header.
In the case that modulus and exponent are not present in fw, a.k.a truncated
image, the length value still appears in header.

Driver will do some basic fw size validation based on the following rules:

1. Header, uCode and RSA are must-have components.
2. All firmware components, if they present, are in the sequence illustrated
   in the layout table above.
3. Length info of each component can be found in header, in dwords.
4. Modulus and exponent key are not required by driver. They may not appear
   in fw. So driver will load a truncated firmware in this case.

HuC firmware layout is same as GuC firmware.

HuC firmware css header is different. However, the only difference is where
the version information is saved. The uc_css_header is unified to support
both. Driver should get HuC version from uc_css_header.huc_sw_version, while
uc_css_header.guc_sw_version for GuC.

.. _`ctb-based-communication`:

CTB based communication
=======================

The CTB (command transport buffer) communication between Host and GuC
is based on u32 data stream written to the shared buffer. One buffer can
be used to transmit data only in one direction (one-directional channel).

Current status of the each buffer is stored in the buffer descriptor.
Buffer descriptor holds tail and head fields that represents active data
stream. The tail field is updated by the data producer (sender), and head
field is updated by the data consumer (receiver)::

     +------------+
     | DESCRIPTOR |          +=================+============+========+
     +============+          |                 | MESSAGE(s) |        |
     | address    |--------->+=================+============+========+
     +------------+
     | head       |          ^-----head--------^
     +------------+
     | tail       |          ^---------tail-----------------^
     +------------+
     | size       |          ^---------------size--------------------^
     +------------+

Each message in data stream starts with the single u32 treated as a header,
followed by optional set of u32 data that makes message specific payload::

     +------------+---------+---------+---------+
     |         MESSAGE                          |
     +------------+---------+---------+---------+
     |   msg[0]   |   [1]   |   ...   |  [n-1]  |
     +------------+---------+---------+---------+
     |   MESSAGE  |       MESSAGE PAYLOAD       |
     +   HEADER   +---------+---------+---------+
     |            |    0    |   ...   |    n    |
     +======+=====+=========+=========+=========+
     | 31:16| code|         |         |         |
     +------+-----+         |         |         |
     |  15:5|flags|         |         |         |
     +------+-----+         |         |         |
     |   4:0|  len|         |         |         |
     +------+-----+---------+---------+---------+

                  ^-------------len-------------^

The message header consists of:

- **len**, indicates length of the message payload (in u32)
- **code**, indicates message code
- **flags**, holds various bits to control message handling

.. _`mmio-based-communication`:

MMIO based communication
========================

The MMIO based communication between Host and GuC uses software scratch
registers, where first register holds data treated as message header,
and other registers are used to hold message payload.

For Gen9+, GuC uses software scratch registers 0xC180-0xC1B8

     +-----------+---------+---------+---------+
     |  MMIO[0]  | MMIO[1] |   ...   | MMIO[n] |
     +-----------+---------+---------+---------+
     | header    |      optional payload       |
     +======+====+=========+=========+=========+
     | 31:28|type|         |         |         |
     +------+----+         |         |         |
     | 27:16|data|         |         |         |
     +------+----+         |         |         |
     |  15:0|code|         |         |         |
     +------+----+---------+---------+---------+

The message header consists of:

- **type**, indicates message type
- **code**, indicates message code, is specific for **type**
- **data**, indicates message data, optional, depends on **code**

The following message **types** are supported:

- **REQUEST**, indicates Host-to-GuC request, requested GuC action code
  must be priovided in **code** field. Optional action specific parameters
  can be provided in remaining payload registers or **data** field.

- **RESPONSE**, indicates GuC-to-Host response from earlier GuC request,
  action response status will be provided in **code** field. Optional
  response data can be returned in remaining payload registers or **data**
  field.

.. This file was automatic generated / don't edit.

