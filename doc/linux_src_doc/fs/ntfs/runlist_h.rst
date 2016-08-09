.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/runlist.h

.. _`runlist_element`:

typedef runlist_element
=======================

.. c:type:: typedef runlist_element

    in memory vcn to lcn mapping array element

.. _`runlist_element.description`:

Description
-----------

The last vcn (in fact the last vcn + 1) is reached when length == 0.

When lcn == -1 this means that the count vcns starting at vcn are not
physically allocated (i.e. this is a hole / data is sparse).

.. _`runlist`:

typedef runlist
===============

.. c:type:: typedef runlist

    in memory vcn to lcn mapping array including a read/write lock

.. This file was automatic generated / don't edit.

