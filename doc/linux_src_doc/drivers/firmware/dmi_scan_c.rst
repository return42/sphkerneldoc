.. -*- coding: utf-8; mode: rst -*-

==========
dmi_scan.c
==========



.. _xref_dmi_set_dump_stack_arch_desc:

dmi_set_dump_stack_arch_desc
============================

.. c:function:: void dmi_set_dump_stack_arch_desc ( void)

    set arch description for dump_stack()

    :param void:
        no arguments



Description
-----------



Invoke :c:func:`dump_stack_set_arch_desc` with DMI system information so that
DMI identifiers are printed out on task dumps.  Arch boot code should
call this function after :c:func:`dmi_scan_machine` if it wants to print out DMI
identifiers on task dumps.




.. _xref_dmi_matches:

dmi_matches
===========

.. c:function:: bool dmi_matches (const struct dmi_system_id * dmi)

    check if dmi_system_id structure matches system DMI data

    :param const struct dmi_system_id * dmi:
        pointer to the dmi_system_id structure to check




.. _xref_dmi_is_end_of_table:

dmi_is_end_of_table
===================

.. c:function:: bool dmi_is_end_of_table (const struct dmi_system_id * dmi)

    check for end-of-table marker

    :param const struct dmi_system_id * dmi:
        pointer to the dmi_system_id structure to check




.. _xref_dmi_check_system:

dmi_check_system
================

.. c:function:: int dmi_check_system (const struct dmi_system_id * list)

    check system DMI data

    :param const struct dmi_system_id * list:
        array of dmi_system_id structures to match against
        		All non-null elements of the list must match
        		their slot's (field index's) data (i.e., each
        		list string must be a substring of the specified
        		DMI slot's string data) to be considered a
        		successful match.



Description
-----------

	Walk the blacklist table running matching functions until someone
	returns non zero or we hit the end. Callback function is called for
	each successful match. Returns the number of matches.




.. _xref_dmi_first_match:

dmi_first_match
===============

.. c:function:: const struct dmi_system_id * dmi_first_match (const struct dmi_system_id * list)

    find dmi_system_id structure matching system DMI data

    :param const struct dmi_system_id * list:
        array of dmi_system_id structures to match against
        		All non-null elements of the list must match
        		their slot's (field index's) data (i.e., each
        		list string must be a substring of the specified
        		DMI slot's string data) to be considered a
        		successful match.



Description
-----------

	Walk the blacklist table until the first match is found.  Return the
	pointer to the matching entry or NULL if there's no match.




.. _xref_dmi_get_system_info:

dmi_get_system_info
===================

.. c:function:: const char * dmi_get_system_info (int field)

    return DMI data value

    :param int field:
        data index (see enum dmi_field)



Description
-----------

	Returns one DMI data value, can be used to perform
	complex DMI data checks.




.. _xref_dmi_name_in_serial:

dmi_name_in_serial
==================

.. c:function:: int dmi_name_in_serial (const char * str)

    Check if string is in the DMI product serial information

    :param const char * str:
        string to check for




.. _xref_dmi_name_in_vendors:

dmi_name_in_vendors
===================

.. c:function:: int dmi_name_in_vendors (const char * str)

    Check if string is in the DMI system or board vendor name

    :param const char * str:
        Case sensitive Name




.. _xref_dmi_find_device:

dmi_find_device
===============

.. c:function:: const struct dmi_device * dmi_find_device (int type, const char * name, const struct dmi_device * from)

    find onboard device by type/name

    :param int type:
        device type or ``DMI_DEV_TYPE_ANY`` to match all device types

    :param const char * name:
        device name string or ``NULL`` to match all

    :param const struct dmi_device * from:
        previous device found in search, or ``NULL`` for new search.



Description
-----------

	Iterates through the list of known onboard devices. If a device is
	found with a matching **type** and **name**, a pointer to its device
	structure is returned.  Otherwise, ``NULL`` is returned.
	A new search is initiated by passing ``NULL`` as the **from** argument.
	If **from** is not ``NULL``, searches continue from next device.




.. _xref_dmi_get_date:

dmi_get_date
============

.. c:function:: bool dmi_get_date (int field, int * yearp, int * monthp, int * dayp)

    parse a DMI date

    :param int field:
        data index (see enum dmi_field)

    :param int * yearp:
        optional out parameter for the year

    :param int * monthp:
        optional out parameter for the month

    :param int * dayp:
        optional out parameter for the day



Description
-----------

	The date field is assumed to be in the form resembling
	[mm[/dd]]/yy[yy] and the result is stored in the out
	parameters any or all of which can be omitted.


	If the field doesn't exist, all out parameters are set to zero
	and false is returned.  Otherwise, true is returned with any
	invalid part of date set to zero.


	On return, year, month and day are guaranteed to be in the
	range of [0,9999], [0,12] and [0,31] respectively.




.. _xref_dmi_walk:

dmi_walk
========

.. c:function:: int dmi_walk (void (*decode) (const struct dmi_header *, void *, void * private_data)

    Walk the DMI table and get called back for every record

    :param void (*)(const struct dmi_header *, void *) decode:
        Callback function

    :param void * private_data:
        Private data to be passed to the callback function



Description
-----------

	Returns -1 when the DMI table can't be reached, 0 on success.




.. _xref_dmi_match:

dmi_match
=========

.. c:function:: bool dmi_match (enum dmi_field f, const char * str)

    compare a string to the dmi field (if exists)

    :param enum dmi_field f:
        DMI field identifier

    :param const char * str:
        string to compare the DMI field to



Description
-----------

Returns true if the requested field equals to the str (including NULL).


