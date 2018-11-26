.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/random.c

.. _`randomize_page`:

randomize_page
==============

.. c:function:: unsigned long randomize_page(unsigned long start, unsigned long range)

    Generate a random, page aligned address

    :param start:
        The smallest acceptable address the caller will take.
    :type start: unsigned long

    :param range:
        The size of the area, starting at \ ``start``\ , within which the
        random address must fall.
    :type range: unsigned long

.. _`randomize_page.description`:

Description
-----------

If \ ``start``\  + \ ``range``\  would overflow, \ ``range``\  is capped.

.. _`randomize_page.note`:

NOTE
----

Historical use of randomize_range, which this replaces, presumed that
\ ``start``\  was already page aligned.  We now align it regardless.

.. _`randomize_page.return`:

Return
------

A page aligned address within [start, start + range).  On error,
\ ``start``\  is returned.

.. This file was automatic generated / don't edit.

