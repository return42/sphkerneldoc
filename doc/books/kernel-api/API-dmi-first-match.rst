
.. _API-dmi-first-match:

===============
dmi_first_match
===============

*man dmi_first_match(9)*

*4.6.0-rc1*

find dmi_system_id structure matching system DMI data


Synopsis
========

.. c:function:: const struct dmi_system_id ⋆ dmi_first_match( const struct dmi_system_id * list )

Arguments
=========

``list``
    array of dmi_system_id structures to match against All non-null elements of the list must match their slot's (field index's) data (i.e., each list string must be a substring
    of the specified DMI slot's string data) to be considered a successful match.


Description
===========

Walk the blacklist table until the first match is found. Return the pointer to the matching entry or NULL if there's no match.
