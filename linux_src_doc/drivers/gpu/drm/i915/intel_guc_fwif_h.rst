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

.. _`guc-log-buffer-layout`:

GuC Log buffer Layout
=====================

Page0  +-------------------------------+
       |   ISR state header (32 bytes) |
       |      DPC state header         |
       |   Crash dump state header     |
Page1  +-------------------------------+
       |           ISR logs            |
Page9  +-------------------------------+
       |           DPC logs            |
Page17 +-------------------------------+
       |         Crash Dump logs       |
       +-------------------------------+

Below state structure is used for coordination of retrieval of GuC firmware
logs. Separate state is maintained for each log buffer type.
read_ptr points to the location where i915 read last in log buffer and
is read only for GuC firmware. write_ptr is incremented by GuC with number
of bytes written for each log entry and is read only for i915.
When any type of log buffer becomes half full, GuC sends a flush interrupt.
GuC firmware expects that while it is writing to 2nd half of the buffer,
first half would get consumed by Host and then get a flush completed
acknowledgment from Host, so that it does not end up doing any overwrite
causing loss of logs. So when buffer gets half filled & i915 has requested
for interrupt, GuC will set flush_to_file field, set the sampled_write_ptr
to the value of write_ptr and raise the interrupt.
On receiving the interrupt i915 should read the buffer, clear flush_to_file
field and also update read_ptr with the value of sample_write_ptr, before
sending an acknowledgment to GuC. marker & version fields are for internal
usage of GuC and opaque to i915. buffer_full_cnt field is incremented every
time GuC detects the log buffer overflow.

.. This file was automatic generated / don't edit.

