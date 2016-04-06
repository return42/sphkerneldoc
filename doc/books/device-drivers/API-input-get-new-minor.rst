
.. _API-input-get-new-minor:

===================
input_get_new_minor
===================

*man input_get_new_minor(9)*

*4.6.0-rc1*

allocates a new input minor number


Synopsis
========

.. c:function:: int input_get_new_minor( int legacy_base, unsigned int legacy_num, bool allow_dynamic )

Arguments
=========

``legacy_base``
    beginning or the legacy range to be searched

``legacy_num``
    size of legacy range

``allow_dynamic``
    whether we can also take ID from the dynamic range


Description
===========

This function allocates a new device minor for from input major namespace. Caller can request legacy minor by specifying ``legacy_base`` and ``legacy_num`` parameters and whether
ID can be allocated from dynamic range if there are no free IDs in legacy range.
