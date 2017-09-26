.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/ksm.c

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

struct
    *undescribed*

head
    (overlaying parent) \ :c:type:`struct migrate_nodes <migrate_nodes>`\  indicates temporarily on that list

struct
    *undescribed*

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

struct
    *undescribed*

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

    the ksm scanner main worker function. \ ``scan_npages``\  - number of pages we want to scan before we return.

    :param unsigned int scan_npages:
        *undescribed*

.. This file was automatic generated / don't edit.

