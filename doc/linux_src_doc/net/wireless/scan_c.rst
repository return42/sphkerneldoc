.. -*- coding: utf-8; mode: rst -*-

======
scan.c
======


.. _`bss-tree-list-structure`:

BSS tree/list structure
=======================

At the top level, the BSS list is kept in both a list in each
registered device (\ ``bss_list``\ ) as well as an RB-tree for faster
lookup. In the RB-tree, entries can be looked up using their
channel, MESHID, MESHCONF (for MBSSes) or channel, BSSID, SSID
for other BSSes.

Due to the possibility of hidden SSIDs, there's a second level
structure, the "hidden_list" and "hidden_beacon_bss" pointer.
The hidden_list connects all BSSes belonging to a single AP
that has a hidden SSID, and connects beacon and probe response
entries. For a probe response entry for a hidden SSID, the
hidden_beacon_bss pointer points to the BSS struct holding the
beacon's information.

Reference counting is done for all these references except for
the hidden_list, so that a beacon BSS struct that is otherwise
not referenced has one reference for being on the bss_list and
one for each probe response entry that points to it using the
hidden_beacon_bss pointer. When a BSS struct that has such a
pointer is get/put, the refcount update is also propagated to
the referenced struct, this ensure that it cannot get removed
while somebody is using the probe response version.

Note that the hidden_beacon_bss pointer never changes, due to
the reference counting. Therefore, no locking is needed for
it.

Also note that the hidden_beacon_bss pointer is only relevant
if the driver uses something other than the IEs, e.g. private
data stored stored in the BSS struct, since the beacon IEs are
also linked into the probe response struct.



.. _`bss_compare_mode`:

enum bss_compare_mode
=====================

.. c:type:: bss_compare_mode

    BSS compare mode


.. _`bss_compare_mode.definition`:

Definition
----------

.. code-block:: c

    enum bss_compare_mode {
      BSS_CMP_REGULAR,
      BSS_CMP_HIDE_ZLEN,
      BSS_CMP_HIDE_NUL
    };


.. _`bss_compare_mode.constants`:

Constants
---------

:``BSS_CMP_REGULAR``:
    regular compare mode (for insertion and normal find)

:``BSS_CMP_HIDE_ZLEN``:
    find hidden SSID with zero-length mode

:``BSS_CMP_HIDE_NUL``:
    find hidden SSID with NUL-ed out mode
