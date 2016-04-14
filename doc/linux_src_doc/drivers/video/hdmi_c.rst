.. -*- coding: utf-8; mode: rst -*-

======
hdmi.c
======

.. _`hdmi_avi_infoframe_init`:

hdmi_avi_infoframe_init
=======================

.. c:function:: int hdmi_avi_infoframe_init (struct hdmi_avi_infoframe *frame)

    initialize an HDMI AVI infoframe

    :param struct hdmi_avi_infoframe \*frame:
        HDMI AVI infoframe


.. _`hdmi_avi_infoframe_init.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.


.. _`hdmi_avi_infoframe_pack`:

hdmi_avi_infoframe_pack
=======================

.. c:function:: ssize_t hdmi_avi_infoframe_pack (struct hdmi_avi_infoframe *frame, void *buffer, size_t size)

    write HDMI AVI infoframe to binary buffer

    :param struct hdmi_avi_infoframe \*frame:
        HDMI AVI infoframe

    :param void \*buffer:
        destination buffer

    :param size_t size:
        size of buffer


.. _`hdmi_avi_infoframe_pack.description`:

Description
-----------

Packs the information contained in the ``frame`` structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.


.. _`hdmi_spd_infoframe_init`:

hdmi_spd_infoframe_init
=======================

.. c:function:: int hdmi_spd_infoframe_init (struct hdmi_spd_infoframe *frame, const char *vendor, const char *product)

    initialize an HDMI SPD infoframe

    :param struct hdmi_spd_infoframe \*frame:
        HDMI SPD infoframe

    :param const char \*vendor:
        vendor string

    :param const char \*product:
        product string


.. _`hdmi_spd_infoframe_init.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.


.. _`hdmi_spd_infoframe_pack`:

hdmi_spd_infoframe_pack
=======================

.. c:function:: ssize_t hdmi_spd_infoframe_pack (struct hdmi_spd_infoframe *frame, void *buffer, size_t size)

    write HDMI SPD infoframe to binary buffer

    :param struct hdmi_spd_infoframe \*frame:
        HDMI SPD infoframe

    :param void \*buffer:
        destination buffer

    :param size_t size:
        size of buffer


.. _`hdmi_spd_infoframe_pack.description`:

Description
-----------

Packs the information contained in the ``frame`` structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.


.. _`hdmi_audio_infoframe_init`:

hdmi_audio_infoframe_init
=========================

.. c:function:: int hdmi_audio_infoframe_init (struct hdmi_audio_infoframe *frame)

    initialize an HDMI audio infoframe

    :param struct hdmi_audio_infoframe \*frame:
        HDMI audio infoframe


.. _`hdmi_audio_infoframe_init.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.


.. _`hdmi_audio_infoframe_pack`:

hdmi_audio_infoframe_pack
=========================

.. c:function:: ssize_t hdmi_audio_infoframe_pack (struct hdmi_audio_infoframe *frame, void *buffer, size_t size)

    write HDMI audio infoframe to binary buffer

    :param struct hdmi_audio_infoframe \*frame:
        HDMI audio infoframe

    :param void \*buffer:
        destination buffer

    :param size_t size:
        size of buffer


.. _`hdmi_audio_infoframe_pack.description`:

Description
-----------

Packs the information contained in the ``frame`` structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.


.. _`hdmi_vendor_infoframe_init`:

hdmi_vendor_infoframe_init
==========================

.. c:function:: int hdmi_vendor_infoframe_init (struct hdmi_vendor_infoframe *frame)

    initialize an HDMI vendor infoframe

    :param struct hdmi_vendor_infoframe \*frame:
        HDMI vendor infoframe


.. _`hdmi_vendor_infoframe_init.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.


.. _`hdmi_vendor_infoframe_pack`:

hdmi_vendor_infoframe_pack
==========================

.. c:function:: ssize_t hdmi_vendor_infoframe_pack (struct hdmi_vendor_infoframe *frame, void *buffer, size_t size)

    write a HDMI vendor infoframe to binary buffer

    :param struct hdmi_vendor_infoframe \*frame:
        HDMI infoframe

    :param void \*buffer:
        destination buffer

    :param size_t size:
        size of buffer


.. _`hdmi_vendor_infoframe_pack.description`:

Description
-----------

Packs the information contained in the ``frame`` structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.


.. _`hdmi_infoframe_pack`:

hdmi_infoframe_pack
===================

.. c:function:: ssize_t hdmi_infoframe_pack (union hdmi_infoframe *frame, void *buffer, size_t size)

    write a HDMI infoframe to binary buffer

    :param union hdmi_infoframe \*frame:
        HDMI infoframe

    :param void \*buffer:
        destination buffer

    :param size_t size:
        size of buffer


.. _`hdmi_infoframe_pack.description`:

Description
-----------

Packs the information contained in the ``frame`` structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.


.. _`hdmi_avi_infoframe_log`:

hdmi_avi_infoframe_log
======================

.. c:function:: void hdmi_avi_infoframe_log (const char *level, struct device *dev, struct hdmi_avi_infoframe *frame)

    log info of HDMI AVI infoframe

    :param const char \*level:
        logging level

    :param struct device \*dev:
        device

    :param struct hdmi_avi_infoframe \*frame:
        HDMI AVI infoframe


.. _`hdmi_spd_infoframe_log`:

hdmi_spd_infoframe_log
======================

.. c:function:: void hdmi_spd_infoframe_log (const char *level, struct device *dev, struct hdmi_spd_infoframe *frame)

    log info of HDMI SPD infoframe

    :param const char \*level:
        logging level

    :param struct device \*dev:
        device

    :param struct hdmi_spd_infoframe \*frame:
        HDMI SPD infoframe


.. _`hdmi_audio_infoframe_log`:

hdmi_audio_infoframe_log
========================

.. c:function:: void hdmi_audio_infoframe_log (const char *level, struct device *dev, struct hdmi_audio_infoframe *frame)

    log info of HDMI AUDIO infoframe

    :param const char \*level:
        logging level

    :param struct device \*dev:
        device

    :param struct hdmi_audio_infoframe \*frame:
        HDMI AUDIO infoframe


.. _`hdmi_vendor_any_infoframe_log`:

hdmi_vendor_any_infoframe_log
=============================

.. c:function:: void hdmi_vendor_any_infoframe_log (const char *level, struct device *dev, union hdmi_vendor_any_infoframe *frame)

    log info of HDMI VENDOR infoframe

    :param const char \*level:
        logging level

    :param struct device \*dev:
        device

    :param union hdmi_vendor_any_infoframe \*frame:
        HDMI VENDOR infoframe


.. _`hdmi_infoframe_log`:

hdmi_infoframe_log
==================

.. c:function:: void hdmi_infoframe_log (const char *level, struct device *dev, union hdmi_infoframe *frame)

    log info of HDMI infoframe

    :param const char \*level:
        logging level

    :param struct device \*dev:
        device

    :param union hdmi_infoframe \*frame:
        HDMI infoframe


.. _`hdmi_avi_infoframe_unpack`:

hdmi_avi_infoframe_unpack
=========================

.. c:function:: int hdmi_avi_infoframe_unpack (struct hdmi_avi_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI AVI infoframe

    :param struct hdmi_avi_infoframe \*frame:
        HDMI AVI infoframe

    :param void \*buffer:
        source buffer


.. _`hdmi_avi_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary ``buffer`` into a structured
``frame`` of the HDMI Auxiliary Video (AVI) information frame.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.


.. _`hdmi_spd_infoframe_unpack`:

hdmi_spd_infoframe_unpack
=========================

.. c:function:: int hdmi_spd_infoframe_unpack (struct hdmi_spd_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI SPD infoframe

    :param struct hdmi_spd_infoframe \*frame:
        HDMI SPD infoframe

    :param void \*buffer:
        source buffer


.. _`hdmi_spd_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary ``buffer`` into a structured
``frame`` of the HDMI Source Product Description (SPD) information frame.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.


.. _`hdmi_audio_infoframe_unpack`:

hdmi_audio_infoframe_unpack
===========================

.. c:function:: int hdmi_audio_infoframe_unpack (struct hdmi_audio_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI AUDIO infoframe

    :param struct hdmi_audio_infoframe \*frame:
        HDMI Audio infoframe

    :param void \*buffer:
        source buffer


.. _`hdmi_audio_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary ``buffer`` into a structured
``frame`` of the HDMI Audio information frame.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.


.. _`hdmi_vendor_any_infoframe_unpack`:

hdmi_vendor_any_infoframe_unpack
================================

.. c:function:: int hdmi_vendor_any_infoframe_unpack (union hdmi_vendor_any_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI vendor infoframe

    :param union hdmi_vendor_any_infoframe \*frame:
        HDMI Vendor infoframe

    :param void \*buffer:
        source buffer


.. _`hdmi_vendor_any_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary ``buffer`` into a structured
``frame`` of the HDMI Vendor information frame.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.


.. _`hdmi_infoframe_unpack`:

hdmi_infoframe_unpack
=====================

.. c:function:: int hdmi_infoframe_unpack (union hdmi_infoframe *frame, void *buffer)

    unpack binary buffer to a HDMI infoframe

    :param union hdmi_infoframe \*frame:
        HDMI infoframe

    :param void \*buffer:
        source buffer


.. _`hdmi_infoframe_unpack.description`:

Description
-----------

Unpacks the information contained in binary buffer ``buffer`` into a structured
``frame`` of a HDMI infoframe.
Also verifies the checksum as required by section 5.3.5 of the HDMI 1.4
specification.

Returns 0 on success or a negative error code on failure.

