.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/hdmi.c

.. _`hdmi_avi_infoframe_init`:

hdmi_avi_infoframe_init
=======================

.. c:function:: int hdmi_avi_infoframe_init(struct hdmi_avi_infoframe *frame)

    initialize an HDMI AVI infoframe

    :param frame:
        HDMI AVI infoframe
    :type frame: struct hdmi_avi_infoframe \*

.. _`hdmi_avi_infoframe_init.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`hdmi_avi_infoframe_pack`:

hdmi_avi_infoframe_pack
=======================

.. c:function:: ssize_t hdmi_avi_infoframe_pack(struct hdmi_avi_infoframe *frame, void *buffer, size_t size)

    write HDMI AVI infoframe to binary buffer

    :param frame:
        HDMI AVI infoframe
    :type frame: struct hdmi_avi_infoframe \*

    :param buffer:
        destination buffer
    :type buffer: void \*

    :param size:
        size of buffer
    :type size: size_t

.. _`hdmi_avi_infoframe_pack.description`:

Description
-----------

Packs the information contained in the \ ``frame``\  structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.

.. _`hdmi_spd_infoframe_init`:

hdmi_spd_infoframe_init
=======================

.. c:function:: int hdmi_spd_infoframe_init(struct hdmi_spd_infoframe *frame, const char *vendor, const char *product)

    initialize an HDMI SPD infoframe

    :param frame:
        HDMI SPD infoframe
    :type frame: struct hdmi_spd_infoframe \*

    :param vendor:
        vendor string
    :type vendor: const char \*

    :param product:
        product string
    :type product: const char \*

.. _`hdmi_spd_infoframe_init.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`hdmi_spd_infoframe_pack`:

hdmi_spd_infoframe_pack
=======================

.. c:function:: ssize_t hdmi_spd_infoframe_pack(struct hdmi_spd_infoframe *frame, void *buffer, size_t size)

    write HDMI SPD infoframe to binary buffer

    :param frame:
        HDMI SPD infoframe
    :type frame: struct hdmi_spd_infoframe \*

    :param buffer:
        destination buffer
    :type buffer: void \*

    :param size:
        size of buffer
    :type size: size_t

.. _`hdmi_spd_infoframe_pack.description`:

Description
-----------

Packs the information contained in the \ ``frame``\  structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.

.. _`hdmi_audio_infoframe_init`:

hdmi_audio_infoframe_init
=========================

.. c:function:: int hdmi_audio_infoframe_init(struct hdmi_audio_infoframe *frame)

    initialize an HDMI audio infoframe

    :param frame:
        HDMI audio infoframe
    :type frame: struct hdmi_audio_infoframe \*

.. _`hdmi_audio_infoframe_init.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`hdmi_audio_infoframe_pack`:

hdmi_audio_infoframe_pack
=========================

.. c:function:: ssize_t hdmi_audio_infoframe_pack(struct hdmi_audio_infoframe *frame, void *buffer, size_t size)

    write HDMI audio infoframe to binary buffer

    :param frame:
        HDMI audio infoframe
    :type frame: struct hdmi_audio_infoframe \*

    :param buffer:
        destination buffer
    :type buffer: void \*

    :param size:
        size of buffer
    :type size: size_t

.. _`hdmi_audio_infoframe_pack.description`:

Description
-----------

Packs the information contained in the \ ``frame``\  structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.

.. _`hdmi_vendor_infoframe_init`:

hdmi_vendor_infoframe_init
==========================

.. c:function:: int hdmi_vendor_infoframe_init(struct hdmi_vendor_infoframe *frame)

    initialize an HDMI vendor infoframe

    :param frame:
        HDMI vendor infoframe
    :type frame: struct hdmi_vendor_infoframe \*

.. _`hdmi_vendor_infoframe_init.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`hdmi_vendor_infoframe_pack`:

hdmi_vendor_infoframe_pack
==========================

.. c:function:: ssize_t hdmi_vendor_infoframe_pack(struct hdmi_vendor_infoframe *frame, void *buffer, size_t size)

    write a HDMI vendor infoframe to binary buffer

    :param frame:
        HDMI infoframe
    :type frame: struct hdmi_vendor_infoframe \*

    :param buffer:
        destination buffer
    :type buffer: void \*

    :param size:
        size of buffer
    :type size: size_t

.. _`hdmi_vendor_infoframe_pack.description`:

Description
-----------

Packs the information contained in the \ ``frame``\  structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.

.. _`hdmi_infoframe_pack`:

hdmi_infoframe_pack
===================

.. c:function:: ssize_t hdmi_infoframe_pack(union hdmi_infoframe *frame, void *buffer, size_t size)

    write a HDMI infoframe to binary buffer

    :param frame:
        HDMI infoframe
    :type frame: union hdmi_infoframe \*

    :param buffer:
        destination buffer
    :type buffer: void \*

    :param size:
        size of buffer
    :type size: size_t

.. _`hdmi_infoframe_pack.description`:

Description
-----------

Packs the information contained in the \ ``frame``\  structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.

.. _`hdmi_avi_infoframe_log`:

hdmi_avi_infoframe_log
======================

.. c:function:: void hdmi_avi_infoframe_log(const char *level, struct device *dev, struct hdmi_avi_infoframe *frame)

    log info of HDMI AVI infoframe

    :param level:
        logging level
    :type level: const char \*

    :param dev:
        device
    :type dev: struct device \*

    :param frame:
        HDMI AVI infoframe
    :type frame: struct hdmi_avi_infoframe \*

.. _`hdmi_spd_infoframe_log`:

hdmi_spd_infoframe_log
======================

.. c:function:: void hdmi_spd_infoframe_log(const char *level, struct device *dev, struct hdmi_spd_infoframe *frame)

    log info of HDMI SPD infoframe

    :param level:
        logging level
    :type level: const char \*

    :param dev:
        device
    :type dev: struct device \*

    :param frame:
        HDMI SPD infoframe
    :type frame: struct hdmi_spd_infoframe \*

.. _`hdmi_audio_infoframe_log`:

hdmi_audio_infoframe_log
========================

.. c:function:: void hdmi_audio_infoframe_log(const char *level, struct device *dev, struct hdmi_audio_infoframe *frame)

    log info of HDMI AUDIO infoframe

    :param level:
        logging level
    :type level: const char \*

    :param dev:
        device
    :type dev: struct device \*

    :param frame:
        HDMI AUDIO infoframe
    :type frame: struct hdmi_audio_infoframe \*

.. _`hdmi_vendor_any_infoframe_log`:

hdmi_vendor_any_infoframe_log
=============================

.. c:function:: void hdmi_vendor_any_infoframe_log(const char *level, struct device *dev, union hdmi_vendor_any_infoframe *frame)

    log info of HDMI VENDOR infoframe

    :param level:
        logging level
    :type level: const char \*

    :param dev:
        device
    :type dev: struct device \*

    :param frame:
        HDMI VENDOR infoframe
    :type frame: union hdmi_vendor_any_infoframe \*

.. _`hdmi_infoframe_log`:

hdmi_infoframe_log
==================

.. c:function:: void hdmi_infoframe_log(const char *level, struct device *dev, union hdmi_infoframe *frame)

    log info of HDMI infoframe

    :param level:
        logging level
    :type level: const char \*

    :param dev:
        device
    :type dev: struct device \*

    :param frame:
        HDMI infoframe
    :type frame: union hdmi_infoframe \*

.. _`hdmi_avi_infoframe_unpack`:

hdmi_avi_infoframe_unpack
=========================

.. c:function:: int hdmi_avi_infoframe_unpack(struct hdmi_avi_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI AVI infoframe

    :param frame:
        HDMI AVI infoframe
    :type frame: struct hdmi_avi_infoframe \*

    :param buffer:
        source buffer
    :type buffer: void \*

.. _`hdmi_avi_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary \ ``buffer``\  into a structured
\ ``frame``\  of the HDMI Auxiliary Video (AVI) information frame.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.

.. _`hdmi_spd_infoframe_unpack`:

hdmi_spd_infoframe_unpack
=========================

.. c:function:: int hdmi_spd_infoframe_unpack(struct hdmi_spd_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI SPD infoframe

    :param frame:
        HDMI SPD infoframe
    :type frame: struct hdmi_spd_infoframe \*

    :param buffer:
        source buffer
    :type buffer: void \*

.. _`hdmi_spd_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary \ ``buffer``\  into a structured
\ ``frame``\  of the HDMI Source Product Description (SPD) information frame.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.

.. _`hdmi_audio_infoframe_unpack`:

hdmi_audio_infoframe_unpack
===========================

.. c:function:: int hdmi_audio_infoframe_unpack(struct hdmi_audio_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI AUDIO infoframe

    :param frame:
        HDMI Audio infoframe
    :type frame: struct hdmi_audio_infoframe \*

    :param buffer:
        source buffer
    :type buffer: void \*

.. _`hdmi_audio_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary \ ``buffer``\  into a structured
\ ``frame``\  of the HDMI Audio information frame.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.

.. _`hdmi_vendor_any_infoframe_unpack`:

hdmi_vendor_any_infoframe_unpack
================================

.. c:function:: int hdmi_vendor_any_infoframe_unpack(union hdmi_vendor_any_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI vendor infoframe

    :param frame:
        HDMI Vendor infoframe
    :type frame: union hdmi_vendor_any_infoframe \*

    :param buffer:
        source buffer
    :type buffer: void \*

.. _`hdmi_vendor_any_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary \ ``buffer``\  into a structured
\ ``frame``\  of the HDMI Vendor information frame.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.

.. _`hdmi_infoframe_unpack`:

hdmi_infoframe_unpack
=====================

.. c:function:: int hdmi_infoframe_unpack(union hdmi_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI infoframe

    :param frame:
        HDMI infoframe
    :type frame: union hdmi_infoframe \*

    :param buffer:
        source buffer
    :type buffer: void \*

.. _`hdmi_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary buffer \ ``buffer``\  into a structured
\ ``frame``\  of a HDMI infoframe.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.

.. This file was automatic generated / don't edit.

