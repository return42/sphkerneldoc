.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/ksm.c

.. _`overview`:

Overview
========

A few notes about the KSM scanning process,
to make it easier to understand the data structures below:

In order to reduce excessive scanning, KSM sorts the memory pages by their
contents into a data structure that holds pointers to the pages' locations.

Since the contents of the pages may change at any moment, KSM cannot just
insert the pages into a normal sorted tree and expect it to find anything.
Therefore KSM uses two data structures - the stable and the unstable tree.

The stable tree holds pointers to all the merged pages (ksm pages), sorted
by their contents.  Because each such page is write-protected, searching on
this tree is fully assured to be working (except when pages are unmapped),
and therefore this tree is called the stable tree.

The stable tree node includes information required for reverse
mapping from a KSM page to virtual addresses that map this page.

In order to avoid large latencies of the rmap walks on KSM pages,
KSM maintains two types of nodes in the stable tree:

* the regular nodes that keep the reverse mapping structures in a
  linked list
* the "chains" that link nodes ("dups") that represent the same
  write protected memory content, but each "dup" corresponds to a
  different KSM page copy of that content

Internally, the regular nodes, "dups" and "chains" are represented
using the same :c:type:`struct stable_node` structure.

In addition to the stable tree, KSM uses a second data structure called the
unstable tree: this tree holds pointers to pages which have been found to
be "unchanged for a period of time".  The unstable tree sorts these pages
by their contents, but since they are not write-protected, KSM cannot rely
upon the unstable tree to work correctly - the unstable tree is liable to
be corrupted as its contents are modified, and so it is called unstable.

KSM solves this problem by several techniques:

1) The unstable tree is flushed every time KSM completes scanning all
   memory areas, and then the tree is rebuilt again from the beginning.
2) KSM will only insert into the unstable tree, pages whose hash value
   has not changed since the previous scan of all memory areas.
3) The unstable tree is a RedBlack Tree - so its balancing is based on the
   colors of the nodes and not on their contents, assuring that even when
   the tree gets "corrupted" it won't get out of balance, so scanning time
   remains the same (also, searching and inserting nodes in an rbtree uses
   the same algorithm, so we have no overhead when we flush and rebuild).
4) KSM never flushes the stable tree, which means that even if it were to
   take 10 attempts to find a page in the unstable tree, once it is found,
   it is secured in the stable tree.  (When we scan a new page, we first
   compare it against the stable tree, and then against the unstable tree.)

If the merge_across_nodes tunable is unset, then KSM maintains multiple
stable trees and multiple unstable trees: one of each for each NUMA node.

.. _`mm_slot`:

struct mm_slot
==============

.. c:type:: struct mm_slot

    ksm information per mm that is being scanned

.. _`mm_slot.definition`:

Definition
----------

.. code-block:: c

    struct mm_slot {
        struct hlist_node link;
        struct list_head mm_list;
        struct rmap_item *rmap_list;
        struct mm_struct *mm;
    }

.. _`mm_slot.members`:

Members
-------

link
    link to the mm_slots hash list

mm_list
    link into the mm_slots list, rooted in ksm_mm_head

rmap_list
    head for this mm_slot's singly-linked list of rmap_items

mm
    the mm that this information is valid for

.. _`ksm_scan`:

struct ksm_scan
===============

.. c:type:: struct ksm_scan

    cursor for scanning

.. _`ksm_scan.definition`:

Definition
----------

.. code-block:: c

    struct ksm_scan {
        struct mm_slot *mm_slot;
        unsigned long address;
        struct rmap_item **rmap_list;
        unsigned long seqnr;
    }

.. _`ksm_scan.members`:

Members
-------

mm_slot
    the current mm_slot we are scanning

address
    the next address inside that to be scanned

rmap_list
    link to the next rmap to be scanned in the rmap_list

seqnr
    count of completed full scans (needed when removing unstable node)

.. _`ksm_scan.description`:

Description
-----------

There is only the one ksm_scan instance of this cursor structure.

.. _`stable_node`:

struct stable_node
==================

.. c:type:: struct stable_node

    node of the stable rbtree

.. _`stable_node.definition`:

Definition
----------

.. code-block:: c

    struct stable_node {
        union {
            struct rb_node node;
            struct {
                struct list_head *head;
                struct {
                    struct hlist_node hlist_dup;
                    struct list_head list;
                } ;
            } ;
        } ;
        struct hlist_head hlist;
        union {
            unsigned long kpfn;
            unsigned long chain_prune_time;
        } ;
    #define STABLE_NODE_CHAIN -1024
        int rmap_hlist_len;
    #ifdef CONFIG_NUMA
        int nid;
    #endif
    }

.. _`stable_node.members`:

Members
-------

{unnamed_union}
    anonymous

node
    rb node of this ksm page in the stable tree

{unnamed_struct}
    anonymous

head
    (overlaying parent) \ :c:type:`struct migrate_nodes <migrate_nodes>`\  indicates temporarily on that list

{unnamed_struct}
    anonymous

hlist_dup
    linked into the stable_node->hlist with a stable_node chain

list
    linked into migrate_nodes, pending placement in the proper node tree

hlist
    hlist head of rmap_items using this ksm page

{unnamed_union}
    anonymous

kpfn
    page frame number of this ksm page (perhaps temporarily on wrong nid)

chain_prune_time
    time of the last full garbage collection

rmap_hlist_len
    number of rmap_item entries in hlist or STABLE_NODE_CHAIN

nid
    NUMA node id of stable tree in which linked (may not match kpfn)

.. _`rmap_item`:

struct rmap_item
================

.. c:type:: struct rmap_item

    reverse mapping item for virtual addresses

.. _`rmap_item.definition`:

Definition
----------

.. code-block:: c

    struct rmap_item {
        struct rmap_item *rmap_list;
        union {
            struct anon_vma *anon_vma;
    #ifdef CONFIG_NUMA
            int nid;
    #endif
        } ;
        struct mm_struct *mm;
        unsigned long address;
        unsigned int oldchecksum;
        union {
            struct rb_node node;
            struct {
                struct stable_node *head;
                struct hlist_node hlist;
            } ;
        } ;
    }

.. _`rmap_item.members`:

Members
-------

rmap_list
    next rmap_item in mm_slot's singly-linked rmap_list

{unnamed_union}
    anonymous

anon_vma
    pointer to anon_vma for this mm,address, when in stable tree

nid
    NUMA node id of unstable tree in which linked (may not match page)

mm
    the memory structure this rmap_item is pointing into

address
    the virtual address this rmap_item tracks (+ flags in low bits)

oldchecksum
    previous checksum of the page at that virtual address

{unnamed_union}
    anonymous

node
    rb node of this rmap_item in the unstable tree

{unnamed_struct}
    anonymous

head
    pointer to stable_node heading this list in the stable tree

hlist
    link into hlist of rmap_items hanging off that stable_node

.. _`replace_page`:

replace_page
============

.. c:function:: int replace_page(struct vm_area_struct *vma, struct page *page, struct page *kpage, pte_t orig_pte)

    replace page in vma by new ksm page

    :param struct vm_area_struct \*vma:
        vma that holds the pte pointing to page

    :param struct page \*page:
        the page we are replacing by kpage

    :param struct page \*kpage:
        the ksm page we replace page by

    :param pte_t orig_pte:
        the original value of the pte

.. _`replace_page.description`:

Description
-----------

Returns 0 on success, -EFAULT on failure.

.. _`ksm_do_scan`:

ksm_do_scan
===========

.. c:function:: void ksm_do_scan(unsigned int scan_npages)

    the ksm scanner main worker function.

    :param unsigned int scan_npages:
        number of pages we want to scan before we return.

.. This file was automatic generated / don't edit.

