.. -*- coding: utf-8; mode: rst -*-

===============
thinkpad_acpi.c
===============


.. _`tpacpi_check_quirks`:

tpacpi_check_quirks
===================

.. c:function:: unsigned long tpacpi_check_quirks (const struct tpacpi_quirk *qlist, unsigned int qlist_size)

    search BIOS/EC version on a list

    :param const struct tpacpi_quirk \*qlist:
        array of :c:type:`struct tpacpi_quirk <tpacpi_quirk>`

    :param unsigned int qlist_size:
        number of elements in ``qlist``



.. _`tpacpi_check_quirks.description`:

Description
-----------

Iterates over a quirks list until one is found that matches the
ThinkPad's vendor, BIOS and EC model.

Returns 0 if nothing matches, otherwise returns the quirks field of
the matching :c:type:`struct tpacpi_quirk <tpacpi_quirk>` entry.



.. _`tpacpi_check_quirks.the-match-criteria-is`:

The match criteria is
---------------------

vendor, ec and bios much match.

