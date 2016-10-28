.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-xfer-mode.c

.. _`ide_xfer_verbose`:

ide_xfer_verbose
================

.. c:function:: const char *ide_xfer_verbose(u8 mode)

    return IDE mode names

    :param u8 mode:
        transfer mode

.. _`ide_xfer_verbose.description`:

Description
-----------

Returns a constant string giving the name of the mode
requested.

.. _`ide_get_best_pio_mode`:

ide_get_best_pio_mode
=====================

.. c:function:: u8 ide_get_best_pio_mode(ide_drive_t *drive, u8 mode_wanted, u8 max_mode)

    get PIO mode from drive

    :param ide_drive_t \*drive:
        drive to consider

    :param u8 mode_wanted:
        preferred mode

    :param u8 max_mode:
        highest allowed mode

.. _`ide_get_best_pio_mode.description`:

Description
-----------

This routine returns the recommended PIO settings for a given drive,
based on the drive->id information and the ide_pio_blacklist[].

Drive PIO mode is auto-selected if 255 is passed as mode_wanted.
This is used by most chipset support modules when "auto-tuning".

.. _`ide_rate_filter`:

ide_rate_filter
===============

.. c:function:: u8 ide_rate_filter(ide_drive_t *drive, u8 speed)

    filter transfer mode

    :param ide_drive_t \*drive:
        IDE device

    :param u8 speed:
        desired speed

.. _`ide_rate_filter.description`:

Description
-----------

Given the available transfer modes this function returns
the best available speed at or below the speed requested.

.. _`ide_rate_filter.todo`:

TODO
----

check device PIO capabilities

.. _`ide_set_xfer_rate`:

ide_set_xfer_rate
=================

.. c:function:: int ide_set_xfer_rate(ide_drive_t *drive, u8 rate)

    set transfer rate

    :param ide_drive_t \*drive:
        drive to set

    :param u8 rate:
        speed to attempt to set

.. _`ide_set_xfer_rate.description`:

Description
-----------

General helper for setting the speed of an IDE device. This
function knows about user enforced limits from the configuration
which ->set_pio_mode/->set_dma_mode does not.

.. This file was automatic generated / don't edit.

