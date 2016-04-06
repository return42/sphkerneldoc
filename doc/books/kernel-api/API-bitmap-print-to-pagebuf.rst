
.. _API-bitmap-print-to-pagebuf:

=======================
bitmap_print_to_pagebuf
=======================

*man bitmap_print_to_pagebuf(9)*

*4.6.0-rc1*

convert bitmap to list or hex format ASCII string


Synopsis
========

.. c:function:: int bitmap_print_to_pagebuf( bool list, char * buf, const unsigned long * maskp, int nmaskbits )

Arguments
=========

``list``
    indicates whether the bitmap must be list

``buf``
    page aligned buffer into which string is placed

``maskp``
    pointer to bitmap to convert

``nmaskbits``
    size of bitmap, in bits


Description
===========

Output format is a comma-separated list of decimal numbers and ranges if list is specified or hex digits grouped into comma-separated sets of 8 digits/set. Returns the number of
characters written to buf.

It is assumed that ``buf`` is a pointer into a PAGE_SIZE area and that sufficient storage remains at ``buf`` to accommodate the ``bitmap_print_to_pagebuf`` output.
