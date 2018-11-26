.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/thinkpad_acpi.c

.. _`tpacpi_check_quirks`:

tpacpi_check_quirks
===================

.. c:function:: unsigned long tpacpi_check_quirks(const struct tpacpi_quirk *qlist, unsigned int qlist_size)

    search BIOS/EC version on a list

    :param qlist:
        array of \ :c:type:`struct tpacpi_quirk <tpacpi_quirk>`\ 
    :type qlist: const struct tpacpi_quirk \*

    :param qlist_size:
        number of elements in \ ``qlist``\ 
    :type qlist_size: unsigned int

.. _`tpacpi_check_quirks.description`:

Description
-----------

Iterates over a quirks list until one is found that matches the
ThinkPad's vendor, BIOS and EC model.

Returns 0 if nothing matches, otherwise returns the quirks field of
the matching \ :c:type:`struct tpacpi_quirk <tpacpi_quirk>`\  entry.

.. _`tpacpi_check_quirks.the-match-criteria-is`:

The match criteria is
---------------------

vendor, ec and bios much match.

.. _`tpacpi_battery_acpi_eval`:

tpacpi_battery_acpi_eval
========================

.. c:function:: acpi_status tpacpi_battery_acpi_eval(char *method, int *ret, int param)

    ACPI extension. The specifics are that an error is marked in the 32rd bit of the response, so we just check that here.

    :param method:
        *undescribed*
    :type method: char \*

    :param ret:
        *undescribed*
    :type ret: int \*

    :param param:
        *undescribed*
    :type param: int

.. This file was automatic generated / don't edit.

