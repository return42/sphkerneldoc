.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/skbuff.c

.. _`skb_panic`:

skb_panic
=========

.. c:function:: void skb_panic(struct sk_buff *skb, unsigned int sz, void *addr, const char msg)

    private function for out-of-line support

    :param skb:
        buffer
    :type skb: struct sk_buff \*

    :param sz:
        size
    :type sz: unsigned int

    :param addr:
        address
    :type addr: void \*

    :param msg:
        skb_over_panic or skb_under_panic
    :type msg: const char

.. _`skb_panic.description`:

Description
-----------

     Out-of-line support for \ :c:func:`skb_put`\  and \ :c:func:`skb_push`\ .
     Called via the wrapper \ :c:func:`skb_over_panic`\  or \ :c:func:`skb_under_panic`\ .
     Keep out of line to prevent kernel bloat.
     __builtin_return_address is not used because it is not always reliable.

.. _`__alloc_skb`:

__alloc_skb
===========

.. c:function:: struct sk_buff *__alloc_skb(unsigned int size, gfp_t gfp_mask, int flags, int node)

    allocate a network buffer

    :param size:
        size to allocate
    :type size: unsigned int

    :param gfp_mask:
        allocation mask
    :type gfp_mask: gfp_t

    :param flags:
        If SKB_ALLOC_FCLONE is set, allocate from fclone cache
        instead of head cache and allocate a cloned (child) skb.
        If SKB_ALLOC_RX is set, __GFP_MEMALLOC will be used for
        allocations in case the data is required for writeback
    :type flags: int

    :param node:
        numa node to allocate memory on
    :type node: int

.. _`__alloc_skb.description`:

Description
-----------

     Allocate a new \ :c:type:`struct sk_buff <sk_buff>`\ . The returned buffer has no headroom and a
     tail room of at least size bytes. The object has a reference count
     of one. The return is the buffer. On a failure the return is \ ``NULL``\ .

     Buffers may only be allocated from interrupts using a \ ``gfp_mask``\  of
     \ ``GFP_ATOMIC``\ .

.. _`__build_skb`:

__build_skb
===========

.. c:function:: struct sk_buff *__build_skb(void *data, unsigned int frag_size)

    build a network buffer

    :param data:
        data buffer provided by caller
    :type data: void \*

    :param frag_size:
        size of data, or 0 if head was kmalloced
    :type frag_size: unsigned int

.. _`__build_skb.description`:

Description
-----------

Allocate a new \ :c:type:`struct sk_buff <sk_buff>`\ . Caller provides space holding head and
skb_shared_info. \ ``data``\  must have been allocated by \ :c:func:`kmalloc`\  only if
\ ``frag_size``\  is 0, otherwise data should come from the page allocator
 or \ :c:func:`vmalloc`\ 
The return is the new skb buffer.
On a failure the return is \ ``NULL``\ , and \ ``data``\  is not freed.
Notes :
 Before IO, driver allocates only data buffer where NIC put incoming frame
 Driver should add room at head (NET_SKB_PAD) and
 MUST add room at tail (SKB_DATA_ALIGN(skb_shared_info))
 After IO, driver calls \ :c:func:`build_skb`\ , to allocate sk_buff and populate it
 before giving packet to stack.
 RX rings only contains data buffers, not full skbs.

.. _`netdev_alloc_frag`:

netdev_alloc_frag
=================

.. c:function:: void *netdev_alloc_frag(unsigned int fragsz)

    allocate a page fragment

    :param fragsz:
        fragment size
    :type fragsz: unsigned int

.. _`netdev_alloc_frag.description`:

Description
-----------

Allocates a frag from a page for receive buffer.
Uses GFP_ATOMIC allocations.

.. _`__netdev_alloc_skb`:

__netdev_alloc_skb
==================

.. c:function:: struct sk_buff *__netdev_alloc_skb(struct net_device *dev, unsigned int len, gfp_t gfp_mask)

    allocate an skbuff for rx on a specific device

    :param dev:
        network device to receive on
    :type dev: struct net_device \*

    :param len:
        length to allocate
    :type len: unsigned int

    :param gfp_mask:
        get_free_pages mask, passed to alloc_skb
    :type gfp_mask: gfp_t

.. _`__netdev_alloc_skb.description`:

Description
-----------

     Allocate a new \ :c:type:`struct sk_buff <sk_buff>`\  and assign it a usage count of one. The
     buffer has NET_SKB_PAD headroom built in. Users should allocate
     the headroom they think they need without accounting for the
     built in space. The built in space is used for optimisations.

     \ ``NULL``\  is returned if there is no free memory.

.. _`__napi_alloc_skb`:

__napi_alloc_skb
================

.. c:function:: struct sk_buff *__napi_alloc_skb(struct napi_struct *napi, unsigned int len, gfp_t gfp_mask)

    allocate skbuff for rx in a specific NAPI instance

    :param napi:
        napi instance this buffer was allocated for
    :type napi: struct napi_struct \*

    :param len:
        length to allocate
    :type len: unsigned int

    :param gfp_mask:
        get_free_pages mask, passed to alloc_skb and alloc_pages
    :type gfp_mask: gfp_t

.. _`__napi_alloc_skb.description`:

Description
-----------

     Allocate a new sk_buff for use in NAPI receive.  This buffer will
     attempt to allocate the head from a special reserved region used
     only for NAPI Rx allocation.  By doing this we can save several
     CPU cycles by avoiding having to disable and re-enable IRQs.

     \ ``NULL``\  is returned if there is no free memory.

.. _`__kfree_skb`:

__kfree_skb
===========

.. c:function:: void __kfree_skb(struct sk_buff *skb)

    private function

    :param skb:
        buffer
    :type skb: struct sk_buff \*

.. _`__kfree_skb.description`:

Description
-----------

     Free an sk_buff. Release anything attached to the buffer.
     Clean the state. This is an internal helper function. Users should
     always call kfree_skb

.. _`kfree_skb`:

kfree_skb
=========

.. c:function:: void kfree_skb(struct sk_buff *skb)

    free an sk_buff

    :param skb:
        buffer to free
    :type skb: struct sk_buff \*

.. _`kfree_skb.description`:

Description
-----------

     Drop a reference to the buffer and free it if the usage count has
     hit zero.

.. _`skb_tx_error`:

skb_tx_error
============

.. c:function:: void skb_tx_error(struct sk_buff *skb)

    report an sk_buff xmit error

    :param skb:
        buffer that triggered an error
    :type skb: struct sk_buff \*

.. _`skb_tx_error.description`:

Description
-----------

     Report xmit error if a device callback is tracking this skb.
     skb must be freed afterwards.

.. _`consume_skb`:

consume_skb
===========

.. c:function:: void consume_skb(struct sk_buff *skb)

    free an skbuff

    :param skb:
        buffer to free
    :type skb: struct sk_buff \*

.. _`consume_skb.description`:

Description
-----------

     Drop a ref to the buffer and free it if the usage count has hit zero
     Functions identically to kfree_skb, but kfree_skb assumes that the frame
     is being dropped after a failure and notes that

.. _`__consume_stateless_skb`:

__consume_stateless_skb
=======================

.. c:function:: void __consume_stateless_skb(struct sk_buff *skb)

    free an skbuff, assuming it is stateless

    :param skb:
        buffer to free
    :type skb: struct sk_buff \*

.. _`__consume_stateless_skb.description`:

Description
-----------

     Alike \ :c:func:`consume_skb`\ , but this variant assumes that this is the last
     skb reference and all the head states have been already dropped

.. _`skb_morph`:

skb_morph
=========

.. c:function:: struct sk_buff *skb_morph(struct sk_buff *dst, struct sk_buff *src)

    morph one skb into another

    :param dst:
        the skb to receive the contents
    :type dst: struct sk_buff \*

    :param src:
        the skb to supply the contents
    :type src: struct sk_buff \*

.. _`skb_morph.description`:

Description
-----------

     This is identical to skb_clone except that the target skb is
     supplied by the user.

     The target skb is returned upon exit.

.. _`skb_copy_ubufs`:

skb_copy_ubufs
==============

.. c:function:: int skb_copy_ubufs(struct sk_buff *skb, gfp_t gfp_mask)

    copy userspace skb frags buffers to kernel

    :param skb:
        the skb to modify
    :type skb: struct sk_buff \*

    :param gfp_mask:
        allocation priority
    :type gfp_mask: gfp_t

.. _`skb_copy_ubufs.description`:

Description
-----------

     This must be called on SKBTX_DEV_ZEROCOPY skb.
     It will copy all frags into kernel and drop the reference
     to userspace pages.

     If this function is called from an interrupt \ :c:func:`gfp_mask`\  must be
     \ ``GFP_ATOMIC``\ .

     Returns 0 on success or a negative error code on failure
     to allocate kernel memory to copy to.

.. _`skb_clone`:

skb_clone
=========

.. c:function:: struct sk_buff *skb_clone(struct sk_buff *skb, gfp_t gfp_mask)

    duplicate an sk_buff

    :param skb:
        buffer to clone
    :type skb: struct sk_buff \*

    :param gfp_mask:
        allocation priority
    :type gfp_mask: gfp_t

.. _`skb_clone.description`:

Description
-----------

     Duplicate an \ :c:type:`struct sk_buff <sk_buff>`\ . The new one is not owned by a socket. Both
     copies share the same packet data but not structure. The new
     buffer has a reference count of 1. If the allocation fails the
     function returns \ ``NULL``\  otherwise the new buffer is returned.

     If this function is called from an interrupt \ :c:func:`gfp_mask`\  must be
     \ ``GFP_ATOMIC``\ .

.. _`skb_copy`:

skb_copy
========

.. c:function:: struct sk_buff *skb_copy(const struct sk_buff *skb, gfp_t gfp_mask)

    create private copy of an sk_buff

    :param skb:
        buffer to copy
    :type skb: const struct sk_buff \*

    :param gfp_mask:
        allocation priority
    :type gfp_mask: gfp_t

.. _`skb_copy.description`:

Description
-----------

     Make a copy of both an \ :c:type:`struct sk_buff <sk_buff>`\  and its data. This is used when the
     caller wishes to modify the data and needs a private copy of the
     data to alter. Returns \ ``NULL``\  on failure or the pointer to the buffer
     on success. The returned buffer has a reference count of 1.

     As by-product this function converts non-linear \ :c:type:`struct sk_buff <sk_buff>`\  to linear
     one, so that \ :c:type:`struct sk_buff <sk_buff>`\  becomes completely private and caller is allowed
     to modify all the data of returned buffer. This means that this
     function is not recommended for use in circumstances when only
     header is going to be modified. Use \ :c:func:`pskb_copy`\  instead.

.. _`__pskb_copy_fclone`:

__pskb_copy_fclone
==================

.. c:function:: struct sk_buff *__pskb_copy_fclone(struct sk_buff *skb, int headroom, gfp_t gfp_mask, bool fclone)

    create copy of an sk_buff with private head.

    :param skb:
        buffer to copy
    :type skb: struct sk_buff \*

    :param headroom:
        headroom of new skb
    :type headroom: int

    :param gfp_mask:
        allocation priority
    :type gfp_mask: gfp_t

    :param fclone:
        if true allocate the copy of the skb from the fclone
        cache instead of the head cache; it is recommended to set this
        to true for the cases where the copy will likely be cloned
    :type fclone: bool

.. _`__pskb_copy_fclone.description`:

Description
-----------

     Make a copy of both an \ :c:type:`struct sk_buff <sk_buff>`\  and part of its data, located
     in header. Fragmented data remain shared. This is used when
     the caller wishes to modify only header of \ :c:type:`struct sk_buff <sk_buff>`\  and needs
     private copy of the header to alter. Returns \ ``NULL``\  on failure
     or the pointer to the buffer on success.
     The returned buffer has a reference count of 1.

.. _`pskb_expand_head`:

pskb_expand_head
================

.. c:function:: int pskb_expand_head(struct sk_buff *skb, int nhead, int ntail, gfp_t gfp_mask)

    reallocate header of \ :c:type:`struct sk_buff <sk_buff>`\ 

    :param skb:
        buffer to reallocate
    :type skb: struct sk_buff \*

    :param nhead:
        room to add at head
    :type nhead: int

    :param ntail:
        room to add at tail
    :type ntail: int

    :param gfp_mask:
        allocation priority
    :type gfp_mask: gfp_t

.. _`pskb_expand_head.description`:

Description
-----------

     Expands (or creates identical copy, if \ ``nhead``\  and \ ``ntail``\  are zero)
     header of \ ``skb``\ . \ :c:type:`struct sk_buff <sk_buff>`\  itself is not changed. \ :c:type:`struct sk_buff <sk_buff>`\  MUST have
     reference count of 1. Returns zero in the case of success or error,
     if expansion failed. In the last case, \ :c:type:`struct sk_buff <sk_buff>`\  is not changed.

     All the pointers pointing into skb header may change and must be
     reloaded after call to this function.

.. _`skb_copy_expand`:

skb_copy_expand
===============

.. c:function:: struct sk_buff *skb_copy_expand(const struct sk_buff *skb, int newheadroom, int newtailroom, gfp_t gfp_mask)

    copy and expand sk_buff

    :param skb:
        buffer to copy
    :type skb: const struct sk_buff \*

    :param newheadroom:
        new free bytes at head
    :type newheadroom: int

    :param newtailroom:
        new free bytes at tail
    :type newtailroom: int

    :param gfp_mask:
        allocation priority
    :type gfp_mask: gfp_t

.. _`skb_copy_expand.description`:

Description
-----------

     Make a copy of both an \ :c:type:`struct sk_buff <sk_buff>`\  and its data and while doing so
     allocate additional space.

     This is used when the caller wishes to modify the data and needs a
     private copy of the data to alter as well as more space for new fields.
     Returns \ ``NULL``\  on failure or the pointer to the buffer
     on success. The returned buffer has a reference count of 1.

     You must pass \ ``GFP_ATOMIC``\  as the allocation priority if this function
     is called from an interrupt.

.. _`__skb_pad`:

__skb_pad
=========

.. c:function:: int __skb_pad(struct sk_buff *skb, int pad, bool free_on_error)

    zero pad the tail of an skb

    :param skb:
        buffer to pad
    :type skb: struct sk_buff \*

    :param pad:
        space to pad
    :type pad: int

    :param free_on_error:
        free buffer on error
    :type free_on_error: bool

.. _`__skb_pad.description`:

Description
-----------

     Ensure that a buffer is followed by a padding area that is zero
     filled. Used by network drivers which may DMA or transfer data
     beyond the buffer end onto the wire.

     May return error in out of memory cases. The skb is freed on error
     if \ ``free_on_error``\  is true.

.. _`pskb_put`:

pskb_put
========

.. c:function:: void *pskb_put(struct sk_buff *skb, struct sk_buff *tail, int len)

    add data to the tail of a potentially fragmented buffer

    :param skb:
        start of the buffer to use
    :type skb: struct sk_buff \*

    :param tail:
        tail fragment of the buffer to use
    :type tail: struct sk_buff \*

    :param len:
        amount of data to add
    :type len: int

.. _`pskb_put.description`:

Description
-----------

     This function extends the used data area of the potentially
     fragmented buffer. \ ``tail``\  must be the last fragment of \ ``skb``\  -- or
     \ ``skb``\  itself. If this would exceed the total buffer size the kernel
     will panic. A pointer to the first byte of the extra data is
     returned.

.. _`skb_put`:

skb_put
=======

.. c:function:: void *skb_put(struct sk_buff *skb, unsigned int len)

    add data to a buffer

    :param skb:
        buffer to use
    :type skb: struct sk_buff \*

    :param len:
        amount of data to add
    :type len: unsigned int

.. _`skb_put.description`:

Description
-----------

     This function extends the used data area of the buffer. If this would
     exceed the total buffer size the kernel will panic. A pointer to the
     first byte of the extra data is returned.

.. _`skb_push`:

skb_push
========

.. c:function:: void *skb_push(struct sk_buff *skb, unsigned int len)

    add data to the start of a buffer

    :param skb:
        buffer to use
    :type skb: struct sk_buff \*

    :param len:
        amount of data to add
    :type len: unsigned int

.. _`skb_push.description`:

Description
-----------

     This function extends the used data area of the buffer at the buffer
     start. If this would exceed the total buffer headroom the kernel will
     panic. A pointer to the first byte of the extra data is returned.

.. _`skb_pull`:

skb_pull
========

.. c:function:: void *skb_pull(struct sk_buff *skb, unsigned int len)

    remove data from the start of a buffer

    :param skb:
        buffer to use
    :type skb: struct sk_buff \*

    :param len:
        amount of data to remove
    :type len: unsigned int

.. _`skb_pull.description`:

Description
-----------

     This function removes data from the start of a buffer, returning
     the memory to the headroom. A pointer to the next data in the buffer
     is returned. Once the data has been pulled future pushes will overwrite
     the old data.

.. _`skb_trim`:

skb_trim
========

.. c:function:: void skb_trim(struct sk_buff *skb, unsigned int len)

    remove end from a buffer

    :param skb:
        buffer to alter
    :type skb: struct sk_buff \*

    :param len:
        new length
    :type len: unsigned int

.. _`skb_trim.description`:

Description
-----------

     Cut the length of a buffer down by removing data from the tail. If
     the buffer is already under the length specified it is not modified.
     The skb must be linear.

.. _`__pskb_pull_tail`:

__pskb_pull_tail
================

.. c:function:: void *__pskb_pull_tail(struct sk_buff *skb, int delta)

    advance tail of skb header

    :param skb:
        buffer to reallocate
    :type skb: struct sk_buff \*

    :param delta:
        number of bytes to advance tail
    :type delta: int

.. _`__pskb_pull_tail.description`:

Description
-----------

     The function makes a sense only on a fragmented \ :c:type:`struct sk_buff <sk_buff>`\ ,
     it expands header moving its tail forward and copying necessary
     data from fragmented part.

     \ :c:type:`struct sk_buff <sk_buff>`\  MUST have reference count of 1.

     Returns \ ``NULL``\  (and \ :c:type:`struct sk_buff <sk_buff>`\  does not change) if pull failed
     or value of new tail of skb in the case of success.

     All the pointers pointing into skb header may change and must be
     reloaded after call to this function.

.. _`skb_copy_bits`:

skb_copy_bits
=============

.. c:function:: int skb_copy_bits(const struct sk_buff *skb, int offset, void *to, int len)

    copy bits from skb to kernel buffer

    :param skb:
        source skb
    :type skb: const struct sk_buff \*

    :param offset:
        offset in source
    :type offset: int

    :param to:
        destination buffer
    :type to: void \*

    :param len:
        number of bytes to copy
    :type len: int

.. _`skb_copy_bits.description`:

Description
-----------

     Copy the specified number of bytes from the source skb to the
     destination buffer.

     CAUTION ! :
             If its prototype is ever changed,
             check arch/{*}/net/{*}.S files,
             since it is called from BPF assembly code.

.. _`skb_store_bits`:

skb_store_bits
==============

.. c:function:: int skb_store_bits(struct sk_buff *skb, int offset, const void *from, int len)

    store bits from kernel buffer to skb

    :param skb:
        destination buffer
    :type skb: struct sk_buff \*

    :param offset:
        offset in destination
    :type offset: int

    :param from:
        source buffer
    :type from: const void \*

    :param len:
        number of bytes to copy
    :type len: int

.. _`skb_store_bits.description`:

Description
-----------

     Copy the specified number of bytes from the source buffer to the
     destination skb.  This function handles all the messy bits of
     traversing fragment lists and such.

.. _`skb_zerocopy`:

skb_zerocopy
============

.. c:function:: int skb_zerocopy(struct sk_buff *to, struct sk_buff *from, int len, int hlen)

    Zero copy skb to skb

    :param to:
        destination buffer
    :type to: struct sk_buff \*

    :param from:
        source buffer
    :type from: struct sk_buff \*

    :param len:
        number of bytes to copy from source buffer
    :type len: int

    :param hlen:
        size of linear headroom in destination buffer
    :type hlen: int

.. _`skb_zerocopy.description`:

Description
-----------

     Copies up to `len` bytes from `from` to `to` by creating references
     to the frags in the source buffer.

     The `hlen` as calculated by \ :c:func:`skb_zerocopy_headlen`\  specifies the
     headroom in the `to` buffer.

.. _`skb_zerocopy.return-value`:

Return value
------------

     0: everything is OK
     -ENOMEM: couldn't orphan frags of \ ``from``\  due to lack of memory
     -EFAULT: \ :c:func:`skb_copy_bits`\  found some problem with skb geometry

.. _`skb_dequeue`:

skb_dequeue
===========

.. c:function:: struct sk_buff *skb_dequeue(struct sk_buff_head *list)

    remove from the head of the queue

    :param list:
        list to dequeue from
    :type list: struct sk_buff_head \*

.. _`skb_dequeue.description`:

Description
-----------

     Remove the head of the list. The list lock is taken so the function
     may be used safely with other locking list functions. The head item is
     returned or \ ``NULL``\  if the list is empty.

.. _`skb_dequeue_tail`:

skb_dequeue_tail
================

.. c:function:: struct sk_buff *skb_dequeue_tail(struct sk_buff_head *list)

    remove from the tail of the queue

    :param list:
        list to dequeue from
    :type list: struct sk_buff_head \*

.. _`skb_dequeue_tail.description`:

Description
-----------

     Remove the tail of the list. The list lock is taken so the function
     may be used safely with other locking list functions. The tail item is
     returned or \ ``NULL``\  if the list is empty.

.. _`skb_queue_purge`:

skb_queue_purge
===============

.. c:function:: void skb_queue_purge(struct sk_buff_head *list)

    empty a list

    :param list:
        list to empty
    :type list: struct sk_buff_head \*

.. _`skb_queue_purge.description`:

Description
-----------

     Delete all buffers on an \ :c:type:`struct sk_buff <sk_buff>`\  list. Each buffer is removed from
     the list and one reference dropped. This function takes the list
     lock and is atomic with respect to other list locking functions.

.. _`skb_rbtree_purge`:

skb_rbtree_purge
================

.. c:function:: unsigned int skb_rbtree_purge(struct rb_root *root)

    empty a skb rbtree

    :param root:
        root of the rbtree to empty
        Return value: the sum of truesizes of all purged skbs.
    :type root: struct rb_root \*

.. _`skb_rbtree_purge.description`:

Description
-----------

     Delete all buffers on an \ :c:type:`struct sk_buff <sk_buff>`\  rbtree. Each buffer is removed from
     the list and one reference dropped. This function does not take
     any lock. Synchronization should be handled by the caller (e.g., TCP
     out-of-order queue is protected by the socket lock).

.. _`skb_queue_head`:

skb_queue_head
==============

.. c:function:: void skb_queue_head(struct sk_buff_head *list, struct sk_buff *newsk)

    queue a buffer at the list head

    :param list:
        list to use
    :type list: struct sk_buff_head \*

    :param newsk:
        buffer to queue
    :type newsk: struct sk_buff \*

.. _`skb_queue_head.description`:

Description
-----------

     Queue a buffer at the start of the list. This function takes the
     list lock and can be used safely with other locking \ :c:type:`struct sk_buff <sk_buff>`\  functions
     safely.

     A buffer cannot be placed on two lists at the same time.

.. _`skb_queue_tail`:

skb_queue_tail
==============

.. c:function:: void skb_queue_tail(struct sk_buff_head *list, struct sk_buff *newsk)

    queue a buffer at the list tail

    :param list:
        list to use
    :type list: struct sk_buff_head \*

    :param newsk:
        buffer to queue
    :type newsk: struct sk_buff \*

.. _`skb_queue_tail.description`:

Description
-----------

     Queue a buffer at the tail of the list. This function takes the
     list lock and can be used safely with other locking \ :c:type:`struct sk_buff <sk_buff>`\  functions
     safely.

     A buffer cannot be placed on two lists at the same time.

.. _`skb_unlink`:

skb_unlink
==========

.. c:function:: void skb_unlink(struct sk_buff *skb, struct sk_buff_head *list)

    remove a buffer from a list

    :param skb:
        buffer to remove
    :type skb: struct sk_buff \*

    :param list:
        list to use
    :type list: struct sk_buff_head \*

.. _`skb_unlink.description`:

Description
-----------

     Remove a packet from a list. The list locks are taken and this
     function is atomic with respect to other list locked calls

     You must know what list the SKB is on.

.. _`skb_append`:

skb_append
==========

.. c:function:: void skb_append(struct sk_buff *old, struct sk_buff *newsk, struct sk_buff_head *list)

    append a buffer

    :param old:
        buffer to insert after
    :type old: struct sk_buff \*

    :param newsk:
        buffer to insert
    :type newsk: struct sk_buff \*

    :param list:
        list to use
    :type list: struct sk_buff_head \*

.. _`skb_append.description`:

Description
-----------

     Place a packet after a given packet in a list. The list locks are taken
     and this function is atomic with respect to other list locked calls.
     A buffer cannot be placed on two lists at the same time.

.. _`skb_insert`:

skb_insert
==========

.. c:function:: void skb_insert(struct sk_buff *old, struct sk_buff *newsk, struct sk_buff_head *list)

    insert a buffer

    :param old:
        buffer to insert before
    :type old: struct sk_buff \*

    :param newsk:
        buffer to insert
    :type newsk: struct sk_buff \*

    :param list:
        list to use
    :type list: struct sk_buff_head \*

.. _`skb_insert.description`:

Description
-----------

     Place a packet before a given packet in a list. The list locks are
     taken and this function is atomic with respect to other list locked
     calls.

     A buffer cannot be placed on two lists at the same time.

.. _`skb_split`:

skb_split
=========

.. c:function:: void skb_split(struct sk_buff *skb, struct sk_buff *skb1, const u32 len)

    Split fragmented skb to two parts at length len.

    :param skb:
        the buffer to split
    :type skb: struct sk_buff \*

    :param skb1:
        the buffer to receive the second part
    :type skb1: struct sk_buff \*

    :param len:
        new length for skb
    :type len: const u32

.. _`skb_shift`:

skb_shift
=========

.. c:function:: int skb_shift(struct sk_buff *tgt, struct sk_buff *skb, int shiftlen)

    Shifts paged data partially from skb to another

    :param tgt:
        buffer into which tail data gets added
    :type tgt: struct sk_buff \*

    :param skb:
        buffer from which the paged data comes from
    :type skb: struct sk_buff \*

    :param shiftlen:
        shift up to this many bytes
    :type shiftlen: int

.. _`skb_shift.description`:

Description
-----------

Attempts to shift up to shiftlen worth of bytes, which may be less than
the length of the skb, from skb to tgt. Returns number bytes shifted.
It's up to caller to free skb if everything was shifted.

If \ ``tgt``\  runs out of frags, the whole operation is aborted.

Skb cannot include anything else but paged data while tgt is allowed
to have non-paged data as well.

TODO: full sized shift could be optimized but that would need
specialized skb free'er to handle frags without up-to-date nr_frags.

.. _`skb_prepare_seq_read`:

skb_prepare_seq_read
====================

.. c:function:: void skb_prepare_seq_read(struct sk_buff *skb, unsigned int from, unsigned int to, struct skb_seq_state *st)

    Prepare a sequential read of skb data

    :param skb:
        the buffer to read
    :type skb: struct sk_buff \*

    :param from:
        lower offset of data to be read
    :type from: unsigned int

    :param to:
        upper offset of data to be read
    :type to: unsigned int

    :param st:
        state variable
    :type st: struct skb_seq_state \*

.. _`skb_prepare_seq_read.description`:

Description
-----------

Initializes the specified state variable. Must be called before
invoking \ :c:func:`skb_seq_read`\  for the first time.

.. _`skb_seq_read`:

skb_seq_read
============

.. c:function:: unsigned int skb_seq_read(unsigned int consumed, const u8 **data, struct skb_seq_state *st)

    Sequentially read skb data

    :param consumed:
        number of bytes consumed by the caller so far
    :type consumed: unsigned int

    :param data:
        destination pointer for data to be returned
    :type data: const u8 \*\*

    :param st:
        state variable
    :type st: struct skb_seq_state \*

.. _`skb_seq_read.description`:

Description
-----------

Reads a block of skb data at \ ``consumed``\  relative to the
lower offset specified to \ :c:func:`skb_prepare_seq_read`\ . Assigns
the head of the data block to \ ``data``\  and returns the length
of the block or 0 if the end of the skb data or the upper
offset has been reached.

The caller is not required to consume all of the data
returned, i.e. \ ``consumed``\  is typically set to the number
of bytes already consumed and the next call to
\ :c:func:`skb_seq_read`\  will return the remaining part of the block.

Note 1: The size of each block of data returned can be arbitrary,
      this limitation is the cost for zerocopy sequential
      reads of potentially non linear data.

Note 2: Fragment lists within fragments are not implemented
      at the moment, state->root_skb could be replaced with
      a stack for this purpose.

.. _`skb_abort_seq_read`:

skb_abort_seq_read
==================

.. c:function:: void skb_abort_seq_read(struct skb_seq_state *st)

    Abort a sequential read of skb data

    :param st:
        state variable
    :type st: struct skb_seq_state \*

.. _`skb_abort_seq_read.description`:

Description
-----------

Must be called if \ :c:func:`skb_seq_read`\  was not called until it
returned 0.

.. _`skb_find_text`:

skb_find_text
=============

.. c:function:: unsigned int skb_find_text(struct sk_buff *skb, unsigned int from, unsigned int to, struct ts_config *config)

    Find a text pattern in skb data

    :param skb:
        the buffer to look in
    :type skb: struct sk_buff \*

    :param from:
        search offset
    :type from: unsigned int

    :param to:
        search limit
    :type to: unsigned int

    :param config:
        textsearch configuration
    :type config: struct ts_config \*

.. _`skb_find_text.description`:

Description
-----------

Finds a pattern in the skb data according to the specified
textsearch configuration. Use \ :c:func:`textsearch_next`\  to retrieve
subsequent occurrences of the pattern. Returns the offset
to the first occurrence or UINT_MAX if no match was found.

.. _`skb_pull_rcsum`:

skb_pull_rcsum
==============

.. c:function:: void *skb_pull_rcsum(struct sk_buff *skb, unsigned int len)

    pull skb and update receive checksum

    :param skb:
        buffer to update
    :type skb: struct sk_buff \*

    :param len:
        length of data pulled
    :type len: unsigned int

.. _`skb_pull_rcsum.description`:

Description
-----------

     This function performs an skb_pull on the packet and updates
     the CHECKSUM_COMPLETE checksum.  It should be used on
     receive path processing instead of skb_pull unless you know
     that the checksum difference is zero (e.g., a valid IP header)
     or you are setting ip_summed to CHECKSUM_NONE.

.. _`skb_segment`:

skb_segment
===========

.. c:function:: struct sk_buff *skb_segment(struct sk_buff *head_skb, netdev_features_t features)

    Perform protocol segmentation on skb.

    :param head_skb:
        buffer to segment
    :type head_skb: struct sk_buff \*

    :param features:
        features for the output path (see dev->features)
    :type features: netdev_features_t

.. _`skb_segment.description`:

Description
-----------

     This function performs segmentation on the given skb.  It returns
     a pointer to the first in a list of new skbs for the segments.
     In case of error it returns ERR_PTR(err).

.. _`skb_to_sgvec`:

skb_to_sgvec
============

.. c:function:: int skb_to_sgvec(struct sk_buff *skb, struct scatterlist *sg, int offset, int len)

    Fill a scatter-gather list from a socket buffer

    :param skb:
        Socket buffer containing the buffers to be mapped
    :type skb: struct sk_buff \*

    :param sg:
        The scatter-gather list to map into
    :type sg: struct scatterlist \*

    :param offset:
        The offset into the buffer's contents to start mapping
    :type offset: int

    :param len:
        Length of buffer space to be mapped
    :type len: int

.. _`skb_to_sgvec.description`:

Description
-----------

     Fill the specified scatter-gather list with mappings/pointers into a
     region of the buffer space attached to a socket buffer. Returns either
     the number of scatterlist items used, or -EMSGSIZE if the contents
     could not fit.

.. _`skb_cow_data`:

skb_cow_data
============

.. c:function:: int skb_cow_data(struct sk_buff *skb, int tailbits, struct sk_buff **trailer)

    Check that a socket buffer's data buffers are writable

    :param skb:
        The socket buffer to check.
    :type skb: struct sk_buff \*

    :param tailbits:
        Amount of trailing space to be added
    :type tailbits: int

    :param trailer:
        Returned pointer to the skb where the \ ``tailbits``\  space begins
    :type trailer: struct sk_buff \*\*

.. _`skb_cow_data.description`:

Description
-----------

     Make sure that the data buffers attached to a socket buffer are
     writable. If they are not, private copies are made of the data buffers
     and the socket buffer is set to use these instead.

     If \ ``tailbits``\  is given, make sure that there is space to write \ ``tailbits``\ 
     bytes of data beyond current end of socket buffer.  \ ``trailer``\  will be
     set to point to the skb in which this space begins.

     The number of scatterlist elements required to completely map the
     COW'd and extended socket buffer will be returned.

.. _`skb_clone_sk`:

skb_clone_sk
============

.. c:function:: struct sk_buff *skb_clone_sk(struct sk_buff *skb)

    create clone of skb, and take reference to socket

    :param skb:
        the skb to clone
    :type skb: struct sk_buff \*

.. _`skb_clone_sk.description`:

Description
-----------

This function creates a clone of a buffer that holds a reference on
sk_refcnt.  Buffers created via this function are meant to be
returned using sock_queue_err_skb, or free via kfree_skb.

When passing buffers allocated with this function to sock_queue_err_skb
it is necessary to wrap the call with sock_hold/sock_put in order to
prevent the socket from being released prior to being enqueued on
the sk_error_queue.

.. _`skb_partial_csum_set`:

skb_partial_csum_set
====================

.. c:function:: bool skb_partial_csum_set(struct sk_buff *skb, u16 start, u16 off)

    set up and verify partial csum values for packet

    :param skb:
        the skb to set
    :type skb: struct sk_buff \*

    :param start:
        the number of bytes after skb->data to start checksumming.
    :type start: u16

    :param off:
        the offset from start to place the checksum.
    :type off: u16

.. _`skb_partial_csum_set.description`:

Description
-----------

For untrusted partially-checksummed packets, we need to make sure the values
for skb->csum_start and skb->csum_offset are valid so we don't oops.

This function checks and sets those values and skb->ip_summed: if this
returns false you should drop the packet.

.. _`skb_checksum_setup`:

skb_checksum_setup
==================

.. c:function:: int skb_checksum_setup(struct sk_buff *skb, bool recalculate)

    set up partial checksum offset

    :param skb:
        the skb to set up
    :type skb: struct sk_buff \*

    :param recalculate:
        if true the pseudo-header checksum will be recalculated
    :type recalculate: bool

.. _`skb_checksum_maybe_trim`:

skb_checksum_maybe_trim
=======================

.. c:function:: struct sk_buff *skb_checksum_maybe_trim(struct sk_buff *skb, unsigned int transport_len)

    maybe trims the given skb

    :param skb:
        the skb to check
    :type skb: struct sk_buff \*

    :param transport_len:
        the data length beyond the network header
    :type transport_len: unsigned int

.. _`skb_checksum_maybe_trim.description`:

Description
-----------

Checks whether the given skb has data beyond the given transport length.
If so, returns a cloned skb trimmed to this transport length.
Otherwise returns the provided skb. Returns NULL in error cases
(e.g. transport_len exceeds skb length or out-of-memory).

Caller needs to set the skb transport header and free any returned skb if it
differs from the provided skb.

.. _`skb_checksum_trimmed`:

skb_checksum_trimmed
====================

.. c:function:: struct sk_buff *skb_checksum_trimmed(struct sk_buff *skb, unsigned int transport_len, __sum16(*skb_chkf)(struct sk_buff *skb))

    validate checksum of an skb

    :param skb:
        the skb to check
    :type skb: struct sk_buff \*

    :param transport_len:
        the data length beyond the network header
    :type transport_len: unsigned int

    :param __sum16(\*skb_chkf)(struct sk_buff \*skb):
        checksum function to use

.. _`skb_checksum_trimmed.description`:

Description
-----------

Applies the given checksum function skb_chkf to the provided skb.
Returns a checked and maybe trimmed skb. Returns NULL on error.

If the skb has data beyond the given transport length, then a
trimmed & cloned skb is checked and returned.

Caller needs to set the skb transport header and free any returned skb if it
differs from the provided skb.

.. _`skb_try_coalesce`:

skb_try_coalesce
================

.. c:function:: bool skb_try_coalesce(struct sk_buff *to, struct sk_buff *from, bool *fragstolen, int *delta_truesize)

    try to merge skb to prior one

    :param to:
        prior buffer
    :type to: struct sk_buff \*

    :param from:
        buffer to add
    :type from: struct sk_buff \*

    :param fragstolen:
        pointer to boolean
    :type fragstolen: bool \*

    :param delta_truesize:
        how much more was allocated than was requested
    :type delta_truesize: int \*

.. _`skb_scrub_packet`:

skb_scrub_packet
================

.. c:function:: void skb_scrub_packet(struct sk_buff *skb, bool xnet)

    scrub an skb

    :param skb:
        buffer to clean
    :type skb: struct sk_buff \*

    :param xnet:
        packet is crossing netns
    :type xnet: bool

.. _`skb_scrub_packet.description`:

Description
-----------

skb_scrub_packet can be used after encapsulating or decapsulting a packet
into/from a tunnel. Some information have to be cleared during these
operations.
skb_scrub_packet can also be used to clean a skb before injecting it in
another namespace (@xnet == true). We have to clear all information in the
skb that could impact namespace isolation.

.. _`skb_gso_transport_seglen`:

skb_gso_transport_seglen
========================

.. c:function:: unsigned int skb_gso_transport_seglen(const struct sk_buff *skb)

    Return length of individual segments of a gso packet

    :param skb:
        GSO skb
    :type skb: const struct sk_buff \*

.. _`skb_gso_transport_seglen.description`:

Description
-----------

skb_gso_transport_seglen is used to determine the real size of the
individual segments, including Layer4 headers (TCP/UDP).

The MAC/L2 or network (IP, IPv6) headers are not accounted for.

.. _`skb_gso_network_seglen`:

skb_gso_network_seglen
======================

.. c:function:: unsigned int skb_gso_network_seglen(const struct sk_buff *skb)

    Return length of individual segments of a gso packet

    :param skb:
        GSO skb
    :type skb: const struct sk_buff \*

.. _`skb_gso_network_seglen.description`:

Description
-----------

skb_gso_network_seglen is used to determine the real size of the
individual segments, including Layer3 (IP, IPv6) and L4 headers (TCP/UDP).

The MAC/L2 header is not accounted for.

.. _`skb_gso_mac_seglen`:

skb_gso_mac_seglen
==================

.. c:function:: unsigned int skb_gso_mac_seglen(const struct sk_buff *skb)

    Return length of individual segments of a gso packet

    :param skb:
        GSO skb
    :type skb: const struct sk_buff \*

.. _`skb_gso_mac_seglen.description`:

Description
-----------

skb_gso_mac_seglen is used to determine the real size of the
individual segments, including MAC/L2, Layer3 (IP, IPv6) and L4
headers (TCP/UDP).

.. _`skb_gso_size_check`:

skb_gso_size_check
==================

.. c:function:: bool skb_gso_size_check(const struct sk_buff *skb, unsigned int seg_len, unsigned int max_len)

    check the skb size, considering GSO_BY_FRAGS

    :param skb:
        GSO skb
    :type skb: const struct sk_buff \*

    :param seg_len:
        The segmented length (from skb_gso_*_seglen). In the
        GSO_BY_FRAGS case this will be [header sizes + GSO_BY_FRAGS].
    :type seg_len: unsigned int

    :param max_len:
        The maximum permissible length.
    :type max_len: unsigned int

.. _`skb_gso_size_check.description`:

Description
-----------

There are a couple of instances where we have a GSO skb, and we
want to determine what size it would be after it is segmented.

Returns true if the segmented length <= max length.

.. _`skb_gso_size_check.we-might-want-to-check`:

We might want to check
----------------------

-    L3+L4+payload size (e.g. IP forwarding)
- L2+L3+L4+payload size (e.g. sanity check before passing to driver)

This is a helper to do that correctly considering GSO_BY_FRAGS.

.. _`skb_gso_validate_network_len`:

skb_gso_validate_network_len
============================

.. c:function:: bool skb_gso_validate_network_len(const struct sk_buff *skb, unsigned int mtu)

    Will a split GSO skb fit into a given MTU?

    :param skb:
        GSO skb
    :type skb: const struct sk_buff \*

    :param mtu:
        MTU to validate against
    :type mtu: unsigned int

.. _`skb_gso_validate_network_len.description`:

Description
-----------

skb_gso_validate_network_len validates if a given skb will fit a
wanted MTU once split. It considers L3 headers, L4 headers, and the
payload.

.. _`skb_gso_validate_mac_len`:

skb_gso_validate_mac_len
========================

.. c:function:: bool skb_gso_validate_mac_len(const struct sk_buff *skb, unsigned int len)

    Will a split GSO skb fit in a given length?

    :param skb:
        GSO skb
    :type skb: const struct sk_buff \*

    :param len:
        length to validate against
    :type len: unsigned int

.. _`skb_gso_validate_mac_len.description`:

Description
-----------

skb_gso_validate_mac_len validates if a given skb will fit a wanted
length once split, including L2, L3 and L4 headers and the payload.

.. _`alloc_skb_with_frags`:

alloc_skb_with_frags
====================

.. c:function:: struct sk_buff *alloc_skb_with_frags(unsigned long header_len, unsigned long data_len, int max_page_order, int *errcode, gfp_t gfp_mask)

    allocate skb with page frags

    :param header_len:
        size of linear part
    :type header_len: unsigned long

    :param data_len:
        needed length in frags
    :type data_len: unsigned long

    :param max_page_order:
        max page order desired.
    :type max_page_order: int

    :param errcode:
        pointer to error code if any
    :type errcode: int \*

    :param gfp_mask:
        allocation mask
    :type gfp_mask: gfp_t

.. _`alloc_skb_with_frags.description`:

Description
-----------

This can be used to allocate a paged skb, given a maximal order for frags.

.. _`skb_condense`:

skb_condense
============

.. c:function:: void skb_condense(struct sk_buff *skb)

    try to get rid of fragments/frag_list if possible

    :param skb:
        buffer
    :type skb: struct sk_buff \*

.. _`skb_condense.description`:

Description
-----------

Can be used to save memory before skb is added to a busy queue.
If packet has bytes in frags and enough tail room in skb->head,
pull all of them, so that we can free the frags right now and adjust
truesize.

.. _`skb_condense.notes`:

Notes
-----

     We do not reallocate skb->head thus can not fail.
     Caller must re-evaluate skb->truesize if needed.

.. This file was automatic generated / don't edit.

