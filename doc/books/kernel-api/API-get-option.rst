
.. _API-get-option:

==========
get_option
==========

*man get_option(9)*

*4.6.0-rc1*

Parse integer from an option string


Synopsis
========

.. c:function:: int get_option( char ** str, int * pint )

Arguments
=========

``str``
    option string

``pint``
    (output) integer value parsed from ``str``


Description
===========

Read an int from an option string; if available accept a subsequent comma as well.


Return values
=============

0 - no int in string 1 - int found, no subsequent comma 2 - int found including a subsequent comma 3 - hyphen found to denote a range
