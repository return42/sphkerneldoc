.. -*- coding: utf-8; mode: rst -*-

.. _blkdev:

=============
Block Devices
=============


.. toctree::
    :maxdepth: 1

    API-blk-get-backing-dev-info
    API-blk-delay-queue
    API-blk-start-queue-async
    API-blk-start-queue
    API-blk-stop-queue
    API-blk-sync-queue
    API---blk-run-queue-uncond
    API---blk-run-queue
    API-blk-run-queue-async
    API-blk-run-queue
    API-blk-queue-bypass-start
    API-blk-queue-bypass-end
    API-blk-cleanup-queue
    API-blk-init-queue
    API-blk-make-request
    API-blk-rq-set-block-pc
    API-blk-requeue-request
    API-part-round-stats
    API-blk-add-request-payload
    API-generic-make-request
    API-submit-bio
    API-blk-insert-cloned-request
    API-blk-rq-err-bytes
    API-blk-peek-request
    API-blk-start-request
    API-blk-fetch-request
    API-blk-update-request
    API-blk-unprep-request
    API-blk-end-request
    API-blk-end-request-all
    API-blk-end-request-cur
    API-blk-end-request-err
    API---blk-end-request
    API---blk-end-request-all
    API---blk-end-request-cur
    API---blk-end-request-err
    API-rq-flush-dcache-pages
    API-blk-lld-busy
    API-blk-rq-unprep-clone
    API-blk-rq-prep-clone
    API-blk-start-plug
    API-blk-pm-runtime-init
    API-blk-pre-runtime-suspend
    API-blk-post-runtime-suspend
    API-blk-pre-runtime-resume
    API-blk-post-runtime-resume
    API-blk-set-runtime-active
    API---blk-drain-queue
    API-rq-ioc
    API---get-request
    API-get-request
    API-blk-attempt-plug-merge
    API-blk-cloned-rq-check-limits
    API-blk-end-bidi-request
    API---blk-end-bidi-request
    API-blk-rq-map-user-iov
    API-blk-rq-unmap-user
    API-blk-rq-map-kern
    API-blk-release-queue
    API-blk-queue-prep-rq
    API-blk-queue-unprep-rq
    API-blk-set-default-limits
    API-blk-set-stacking-limits
    API-blk-queue-make-request
    API-blk-queue-bounce-limit
    API-blk-queue-max-hw-sectors
    API-blk-queue-chunk-sectors
    API-blk-queue-max-discard-sectors
    API-blk-queue-max-write-same-sectors
    API-blk-queue-max-segments
    API-blk-queue-max-segment-size
    API-blk-queue-logical-block-size
    API-blk-queue-physical-block-size
    API-blk-queue-alignment-offset
    API-blk-limits-io-min
    API-blk-queue-io-min
    API-blk-limits-io-opt
    API-blk-queue-io-opt
    API-blk-queue-stack-limits
    API-blk-stack-limits
    API-bdev-stack-limits
    API-disk-stack-limits
    API-blk-queue-dma-pad
    API-blk-queue-update-dma-pad
    API-blk-queue-dma-drain
    API-blk-queue-segment-boundary
    API-blk-queue-virt-boundary
    API-blk-queue-dma-alignment
    API-blk-queue-update-dma-alignment
    API-blk-queue-flush
    API-blk-execute-rq-nowait
    API-blk-execute-rq
    API-blkdev-issue-flush
    API-blkdev-issue-discard
    API-blkdev-issue-write-same
    API-blkdev-issue-zeroout
    API-blk-queue-find-tag
    API-blk-free-tags
    API-blk-queue-free-tags
    API-blk-init-tags
    API-blk-queue-init-tags
    API-blk-queue-resize-tags
    API-blk-queue-end-tag
    API-blk-queue-start-tag
    API-blk-queue-invalidate-tags
    API---blk-queue-free-tags
    API-blk-rq-count-integrity-sg
    API-blk-rq-map-integrity-sg
    API-blk-integrity-compare
    API-blk-integrity-register
    API-blk-integrity-unregister
    API-blk-trace-ioctl
    API-blk-trace-shutdown
    API-blk-add-trace-rq
    API-blk-add-trace-bio
    API-blk-add-trace-bio-remap
    API-blk-add-trace-rq-remap
    API-blk-mangle-minor
    API-blk-alloc-devt
    API-blk-free-devt
    API-disk-replace-part-tbl
    API-disk-expand-part-tbl
    API-disk-block-events
    API-disk-unblock-events
    API-disk-flush-events
    API-disk-clear-events
    API-disk-get-part
    API-disk-part-iter-init
    API-disk-part-iter-next
    API-disk-part-iter-exit
    API-disk-map-sector-rcu
    API-register-blkdev
    API-add-disk
    API-get-gendisk
    API-bdget-disk




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
