
.. _vfs:

=============
The Linux VFS
=============


.. _the_filesystem_types:

The Filesystem types
====================


.. toctree::
    :maxdepth: 1

    API-enum-positive-aop-returns
    API-sb-end-write
    API-sb-end-pagefault
    API-sb-end-intwrite
    API-sb-start-write
    API-sb-start-pagefault
    API-inode-inc-iversion

.. _the_directory_cache:

The Directory Cache
===================


.. toctree::
    :maxdepth: 1

    API---d-drop
    API-shrink-dcache-sb
    API-have-submounts
    API-shrink-dcache-parent
    API-d-invalidate
    API-d-alloc
    API-d-alloc-pseudo
    API-d-instantiate
    API-d-instantiate-no-diralias
    API-d-find-any-alias
    API-d-obtain-alias
    API-d-obtain-root
    API-d-add-ci
    API-d-lookup
    API-d-hash-and-lookup
    API-d-delete
    API-d-rehash
    API-d-add
    API-d-exact-alias
    API-dentry-update-name-case
    API-d-splice-alias
    API-d-path
    API-dget-dlock
    API-d-unhashed
    API-d-really-is-negative
    API-d-really-is-positive
    API-d-inode
    API-d-inode-rcu
    API-d-backing-inode
    API-d-backing-dentry

.. _inode_handling:

Inode Handling
==============


.. toctree::
    :maxdepth: 1

    API-inode-init-always
    API-drop-nlink
    API-clear-nlink
    API-set-nlink
    API-inc-nlink
    API-inode-sb-list-add
    API---insert-inode-hash
    API---remove-inode-hash
    API-new-inode
    API-unlock-new-inode
    API-lock-two-nondirectories
    API-unlock-two-nondirectories
    API-iget5-locked
    API-iget-locked
    API-iunique
    API-ilookup5-nowait
    API-ilookup5
    API-ilookup
    API-find-inode-nowait
    API-iput
    API-bmap
    API-file-update-time
    API-inode-init-owner
    API-inode-owner-or-capable
    API-inode-dio-wait
    API-make-bad-inode
    API-is-bad-inode
    API-iget-failed

.. _registration_and_superblocks:

Registration and Superblocks
============================


.. toctree::
    :maxdepth: 1

    API-deactivate-locked-super
    API-deactivate-super
    API-generic-shutdown-super
    API-sget
    API-iterate-supers-type
    API-get-super
    API-get-super-thawed
    API-freeze-super
    API-thaw-super

.. _file_locks:

File Locks
==========


.. toctree::
    :maxdepth: 1

    API-posix-lock-file
    API-locks-mandatory-area
    API---break-lease
    API-lease-get-mtime
    API-generic-setlease
    API-vfs-setlease
    API-locks-lock-inode-wait
    API-vfs-test-lock
    API-vfs-lock-file
    API-posix-unblock-lock
    API-vfs-cancel-lock
    API-posix-lock-inode-wait
    API-locks-mandatory-locked
    API-fcntl-getlease
    API-check-conflicting-open
    API-fcntl-setlease
    API-flock-lock-inode-wait
    API-sys-flock

.. _other_functions:

Other Functions
===============


.. toctree::
    :maxdepth: 1

    API-mpage-readpages
    API-mpage-writepages
    API-generic-permission
    API---inode-permission
    API-inode-permission
    API-path-get
    API-path-put
    API-vfs-path-lookup
    API-lookup-one-len
    API-lookup-one-len-unlocked
    API-vfs-unlink
    API-vfs-link
    API-vfs-rename
    API-sync-mapping-buffers
    API-mark-buffer-dirty
    API---bread-gfp
    API-block-invalidatepage
    API-ll-rw-block
    API-bh-uptodate-or-lock
    API-bh-submit-read
    API-bio-reset
    API-bio-chain
    API-bio-alloc-bioset
    API-bio-put
    API---bio-clone-fast
    API-bio-clone-fast
    API-bio-clone-bioset
    API-bio-add-pc-page
    API-bio-add-page
    API-submit-bio-wait
    API-bio-advance
    API-bio-alloc-pages
    API-bio-copy-data
    API-bio-uncopy-user
    API-bio-unmap-user
    API-bio-map-kern
    API-bio-copy-kern
    API-bio-endio
    API-bio-split
    API-bio-trim
    API-bioset-create
    API-bioset-create-nobvec
    API-bio-associate-blkcg
    API-bio-associate-current
    API-seq-open
    API-seq-read
    API-seq-lseek
    API-seq-release
    API-seq-escape
    API-mangle-path
    API-seq-path
    API-seq-file-path
    API-seq-write
    API-seq-pad
    API-seq-hlist-start
    API-seq-hlist-start-head
    API-seq-hlist-next
    API-seq-hlist-start-rcu
    API-seq-hlist-start-head-rcu
    API-seq-hlist-next-rcu
    API-seq-hlist-start-percpu
    API-seq-hlist-next-percpu
    API-register-filesystem
    API-unregister-filesystem
    API-wbc-account-io
    API-inode-congested
    API---mark-inode-dirty
    API-writeback-inodes-sb-nr
    API-writeback-inodes-sb
    API-try-to-writeback-inodes-sb-nr
    API-try-to-writeback-inodes-sb
    API-sync-inodes-sb
    API-write-inode-now
    API-sync-inode
    API-sync-inode-metadata
    API-freeze-bdev
    API-thaw-bdev
    API-bdev-read-page
    API-bdev-write-page
    API-bdev-direct-access
    API-bdgrab
    API-bd-link-disk-holder
    API-bd-unlink-disk-holder
    API-check-disk-size-change
    API-revalidate-disk
    API-blkdev-get
    API-blkdev-get-by-path
    API-blkdev-get-by-dev
    API-lookup-bdev
