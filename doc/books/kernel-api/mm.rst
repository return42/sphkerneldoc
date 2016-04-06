
.. _mm:

==========================
Memory Management in Linux
==========================


The Slab Cache
==============


.. toctree::
    :maxdepth: 1

    API-kmalloc
    API-kmalloc-array
    API-kcalloc
    API-kzalloc
    API-kzalloc-node
    API-kmem-cache-alloc
    API-kmem-cache-alloc-node
    API-kmem-cache-free
    API-kfree
    API-ksize
    API-kfree-const
    API-kstrdup
    API-kstrdup-const
    API-kstrndup
    API-kmemdup
    API-memdup-user
    API-memdup-user-nul
    API-get-user-pages-fast

User Space Memory Access
========================


.. toctree::
    :maxdepth: 1

    API---copy-to-user-inatomic
    API---copy-to-user
    API---copy-from-user
    API-clear-user
    API---clear-user
    API--copy-to-user
    API--copy-from-user

More Memory Management Functions
================================


.. toctree::
    :maxdepth: 1

    API-read-cache-pages
    API-page-cache-sync-readahead
    API-page-cache-async-readahead
    API-delete-from-page-cache
    API-filemap-flush
    API-filemap-fdatawait-range
    API-filemap-fdatawait
    API-filemap-write-and-wait-range
    API-replace-page-cache-page
    API-add-to-page-cache-locked
    API-add-page-wait-queue
    API-unlock-page
    API-end-page-writeback
    API---lock-page
    API-page-cache-next-hole
    API-page-cache-prev-hole
    API-find-get-entry
    API-find-lock-entry
    API-pagecache-get-page
    API-find-get-pages-contig
    API-find-get-pages-tag
    API-find-get-entries-tag
    API-generic-file-read-iter
    API-filemap-fault
    API-read-cache-page
    API-read-cache-page-gfp
    API---generic-file-write-iter
    API-generic-file-write-iter
    API-try-to-release-page
    API-zap-vma-ptes
    API-vm-insert-page
    API-vm-insert-pfn
    API-vm-insert-pfn-prot
    API-remap-pfn-range
    API-vm-iomap-memory
    API-unmap-mapping-range
    API-follow-pfn
    API-vm-unmap-aliases
    API-vm-unmap-ram
    API-vm-map-ram
    API-unmap-kernel-range-noflush
    API-unmap-kernel-range
    API-vfree
    API-vunmap
    API-vmap
    API-vmalloc
    API-vzalloc
    API-vmalloc-user
    API-vmalloc-node
    API-vzalloc-node
    API-vmalloc-32
    API-vmalloc-32-user
    API-remap-vmalloc-range-partial
    API-remap-vmalloc-range
    API-alloc-vm-area
    API-alloc-pages-exact-nid
    API-nr-free-zone-pages
    API-nr-free-pagecache-pages
    API-find-next-best-node
    API-free-bootmem-with-active-regions
    API-sparse-memory-present-with-active-regions
    API-get-pfn-range-for-nid
    API-absent-pages-in-range
    API-node-map-pfn-alignment
    API-find-min-pfn-with-active-regions
    API-free-area-init-nodes
    API-set-dma-reserve
    API-setup-per-zone-wmarks
    API-get-pfnblock-flags-mask
    API-set-pfnblock-flags-mask
    API-alloc-contig-range
    API-mempool-destroy
    API-mempool-create
    API-mempool-resize
    API-mempool-alloc
    API-mempool-free
    API-dma-pool-create
    API-dma-pool-destroy
    API-dma-pool-alloc
    API-dma-pool-free
    API-dmam-pool-create
    API-dmam-pool-destroy
    API-balance-dirty-pages-ratelimited
    API-tag-pages-for-writeback
    API-write-cache-pages
    API-generic-writepages
    API-write-one-page
    API-wait-for-stable-page
    API-truncate-inode-pages-range
    API-truncate-inode-pages
    API-truncate-inode-pages-final
    API-invalidate-mapping-pages
    API-invalidate-inode-pages2-range
    API-invalidate-inode-pages2
    API-truncate-pagecache
    API-truncate-setsize
    API-pagecache-isize-extended
    API-truncate-pagecache-range
