.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-pio-blacklist.c

.. _`ide_scan_pio_blacklist`:

ide_scan_pio_blacklist
======================

.. c:function:: int ide_scan_pio_blacklist(char *model)

    check for a blacklisted drive

    :param char \*model:
        Drive model string

.. _`ide_scan_pio_blacklist.description`:

Description
-----------

This routine searches the ide_pio_blacklist for an entry
matching the start/whole of the supplied model name.

Returns -1 if no match found.
Otherwise returns the recommended PIO mode from ide_pio_blacklist[].

.. This file was automatic generated / don't edit.

