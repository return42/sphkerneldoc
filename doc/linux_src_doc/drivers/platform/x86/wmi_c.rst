.. -*- coding: utf-8; mode: rst -*-

=====
wmi.c
=====


.. _`wmi_parse_hexbyte`:

wmi_parse_hexbyte
=================

.. c:function:: int wmi_parse_hexbyte (const u8 *src)

    Convert a ASCII hex number to a byte

    :param const u8 \*src:
        Pointer to at least 2 characters to convert.



.. _`wmi_parse_hexbyte.description`:

Description
-----------

Convert a two character ASCII hex string to a number.



.. _`wmi_parse_hexbyte.return`:

Return
------

0-255  Success, the byte was parsed correctly

         -1     Error, an invalid character was supplied



.. _`wmi_swap_bytes`:

wmi_swap_bytes
==============

.. c:function:: void wmi_swap_bytes (u8 *src, u8 *dest)

    Rearrange GUID bytes to match GUID binary

    :param u8 \*src:
        Memory block holding binary GUID (16 bytes)

    :param u8 \*dest:
        Memory block to hold byte swapped binary GUID (16 bytes)



.. _`wmi_swap_bytes.description`:

Description
-----------

Byte swap a binary GUID to match it's real GUID value



.. _`wmi_parse_guid`:

wmi_parse_guid
==============

.. c:function:: bool wmi_parse_guid (const u8 *src, u8 *dest)

    Convert GUID from ASCII to binary

    :param const u8 \*src:
        36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

    :param u8 \*dest:
        Memory block to hold binary GUID (16 bytes)



.. _`wmi_parse_guid.description`:

Description
-----------

N.B. The GUID need not be NULL terminated.



.. _`wmi_parse_guid.return`:

Return
------

'true'   ``dest`` contains binary GUID
'false'  ``dest`` contents are undefined



.. _`wmi_evaluate_method`:

wmi_evaluate_method
===================

.. c:function:: acpi_status wmi_evaluate_method (const char *guid_string, u8 instance, u32 method_id, const struct acpi_buffer *in, struct acpi_buffer *out)

    Evaluate a WMI method

    :param const char \*guid_string:
        36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

    :param u8 instance:
        Instance index

    :param u32 method_id:
        Method ID to call

    :param const struct acpi_buffer \*in:

        *undescribed*

    :param struct acpi_buffer \*out:

        *undescribed*



.. _`wmi_evaluate_method.-in`:

&in
---

Buffer containing input for the method call



.. _`wmi_evaluate_method.-out`:

&out
----

Empty buffer to return the method results

Call an ACPI-WMI method



.. _`wmi_query_block`:

wmi_query_block
===============

.. c:function:: acpi_status wmi_query_block (const char *guid_string, u8 instance, struct acpi_buffer *out)

    Return contents of a WMI block

    :param const char \*guid_string:
        36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

    :param u8 instance:
        Instance index

    :param struct acpi_buffer \*out:

        *undescribed*



.. _`wmi_query_block.-out`:

&out
----

Empty buffer to return the contents of the data block to

Return the contents of an ACPI-WMI data block to a buffer



.. _`wmi_set_block`:

wmi_set_block
=============

.. c:function:: acpi_status wmi_set_block (const char *guid_string, u8 instance, const struct acpi_buffer *in)

    Write to a WMI block

    :param const char \*guid_string:
        36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

    :param u8 instance:
        Instance index

    :param const struct acpi_buffer \*in:

        *undescribed*



.. _`wmi_set_block.-in`:

&in
---

Buffer containing new values for the data block

Write the contents of the input buffer to an ACPI-WMI data block



.. _`wmi_install_notify_handler`:

wmi_install_notify_handler
==========================

.. c:function:: acpi_status wmi_install_notify_handler (const char *guid, wmi_notify_handler handler, void *data)

    Register handler for WMI events

    :param const char \*guid:

        *undescribed*

    :param wmi_notify_handler handler:
        Function to handle notifications

    :param void \*data:
        Data to be returned to handler when event is fired



.. _`wmi_install_notify_handler.description`:

Description
-----------

Register a handler for events sent to the ACPI-WMI mapper device.



.. _`wmi_remove_notify_handler`:

wmi_remove_notify_handler
=========================

.. c:function:: acpi_status wmi_remove_notify_handler (const char *guid)

    Unregister handler for WMI events

    :param const char \*guid:

        *undescribed*



.. _`wmi_remove_notify_handler.description`:

Description
-----------


Unregister handler for events sent to the ACPI-WMI mapper device.



.. _`wmi_get_event_data`:

wmi_get_event_data
==================

.. c:function:: acpi_status wmi_get_event_data (u32 event, struct acpi_buffer *out)

    Get WMI data associated with an event

    :param u32 event:
        Event to find

    :param struct acpi_buffer \*out:
        Buffer to hold event data. out->pointer should be freed with :c:func:`kfree`



.. _`wmi_get_event_data.description`:

Description
-----------

Returns extra data associated with an event in WMI.



.. _`wmi_has_guid`:

wmi_has_guid
============

.. c:function:: bool wmi_has_guid (const char *guid_string)

    Check if a GUID is available

    :param const char \*guid_string:
        36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba



.. _`wmi_has_guid.description`:

Description
-----------

Check if a given GUID is defined by _WDG

