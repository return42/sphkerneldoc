.. -*- coding: utf-8; mode: rst -*-

================
sound_firmware.c
================


.. _`mod_firmware_load`:

mod_firmware_load
=================

.. c:function:: int mod_firmware_load (const char *fn, char **fp)

    load sound driver firmware

    :param const char \*fn:
        filename

    :param char \*\*fp:
        return for the buffer.



.. _`mod_firmware_load.description`:

Description
-----------

Load the firmware for a sound module (up to 128K) into a buffer.
The buffer is returned in \*fp. It is allocated with vmalloc so is
virtually linear and not DMAable. The caller should free it with
vfree when finished.

The length of the buffer is returned on a successful load, the
value zero on a failure.



.. _`mod_firmware_load.caution`:

Caution
-------

This API is not recommended. Firmware should be loaded via
request_firmware.

