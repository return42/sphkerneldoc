
.. _API-dmi-get-date:

============
dmi_get_date
============

*man dmi_get_date(9)*

*4.6.0-rc1*

parse a DMI date


Synopsis
========

.. c:function:: bool dmi_get_date( int field, int * yearp, int * monthp, int * dayp )

Arguments
=========

``field``
    data index (see enum dmi_field)

``yearp``
    optional out parameter for the year

``monthp``
    optional out parameter for the month

``dayp``
    optional out parameter for the day


Description
===========

The date field is assumed to be in the form resembling [mm[/dd]]/yy[yy] and the result is stored in the out parameters any or all of which can be omitted.

If the field doesn't exist, all out parameters are set to zero and false is returned. Otherwise, true is returned with any invalid part of date set to zero.

On return, year, month and day are guaranteed to be in the range of [0,9999], [0,12] and [0,31] respectively.
