.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/huge_memory.c

.. _`mm_slot`:

struct mm_slot
==============

.. c:type:: struct mm_slot

    hash lookup from mm to mm_slot

.. _`mm_slot.definition`:

Definition
----------

.. code-block:: c

    struct mm_slot {
        struct hlist_node hash;
        struct list_head mm_node;
        struct mm_struct *mm;
    }

.. _`mm_slot.members`:

Members
-------

hash
    hash collision list

mm_node
    khugepaged scan list headed in khugepaged_scan.mm_head

mm
    the mm that this information is valid for

.. _`khugepaged_scan`:

struct khugepaged_scan
======================

.. c:type:: struct khugepaged_scan

    cursor for scanning

.. _`khugepaged_scan.definition`:

Definition
----------

.. code-block:: c

    struct khugepaged_scan {
        struct list_head mm_head;
        struct mm_slot *mm_slot;
        unsigned long address;
    }

.. _`khugepaged_scan.members`:

Members
-------

mm_head
    the head of the mm list to scan

mm_slot
    the current mm_slot we are scanning

address
    the next address inside that to be scanned

.. _`khugepaged_scan.description`:

Description
-----------

There is only the one khugepaged_scan instance of this cursor structure.

.. This file was automatic generated / don't edit.

