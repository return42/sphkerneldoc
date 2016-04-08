
.. _netcore:

================
Linux Networking
================


Networking Base Types
=====================


.. toctree::
    :maxdepth: 1

    API-enum-sock-type
    API-struct-socket

Socket Buffer Functions
=======================


.. toctree::
    :maxdepth: 1

    API-struct-skb-shared-hwtstamps
    API-struct-skb-mstamp
    API-skb-mstamp-get
    API-skb-mstamp-us-delta
    API-struct-sk-buff
    API-skb-dst
    API-skb-dst-set
    API-skb-dst-set-noref
    API-skb-dst-is-noref
    API-skb-fclone-busy
    API-skb-queue-empty
    API-skb-queue-is-last
    API-skb-queue-is-first
    API-skb-queue-next
    API-skb-queue-prev
    API-skb-get
    API-skb-cloned
    API-skb-header-cloned
    API-skb-header-release
    API---skb-header-release
    API-skb-shared
    API-skb-share-check
    API-skb-unshare
    API-skb-peek
    API-skb-peek-next
    API-skb-peek-tail
    API-skb-queue-len
    API---skb-queue-head-init
    API-skb-queue-splice
    API-skb-queue-splice-init
    API-skb-queue-splice-tail
    API-skb-queue-splice-tail-init
    API---skb-queue-after
    API---skb-fill-page-desc
    API-skb-fill-page-desc
    API-skb-headroom
    API-skb-tailroom
    API-skb-availroom
    API-skb-reserve
    API-skb-tailroom-reserve
    API-pskb-trim-unique
    API-skb-orphan
    API-skb-orphan-frags
    API-netdev-alloc-skb
    API---dev-alloc-pages
    API---dev-alloc-page
    API-skb-propagate-pfmemalloc
    API-skb-frag-page
    API---skb-frag-ref
    API-skb-frag-ref
    API---skb-frag-unref
    API-skb-frag-unref
    API-skb-frag-address
    API-skb-frag-address-safe
    API---skb-frag-set-page
    API-skb-frag-set-page
    API-skb-frag-dma-map
    API-skb-clone-writable
    API-skb-cow
    API-skb-cow-head
    API-skb-padto
    API-skb-put-padto
    API-skb-linearize
    API-skb-has-shared-frag
    API-skb-linearize-cow
    API-skb-postpull-rcsum
    API-pskb-trim-rcsum
    API-skb-needs-linearize
    API-skb-get-timestamp
    API-skb-tx-timestamp
    API-skb-checksum-complete
    API-skb-checksum-none-assert
    API-skb-head-is-locked
    API-skb-gso-network-seglen
    API-struct-sock-common
    API-struct-sock
    API-sk-nulls-for-each-entry-offset
    API-unlock-sock-fast
    API-sk-wmem-alloc-get
    API-sk-rmem-alloc-get
    API-sk-has-allocations
    API-skwq-has-sleeper
    API-sock-poll-wait
    API-sk-page-frag
    API-sock-tx-timestamp
    API-sk-eat-skb
    API-sk-state-load
    API-sk-state-store
    API-sockfd-lookup
    API-sock-alloc
    API-sock-release
    API-kernel-recvmsg
    API-sock-register
    API-sock-unregister
    API---alloc-skb
    API-netdev-alloc-frag
    API---netdev-alloc-skb
    API---napi-alloc-skb
    API---kfree-skb
    API-kfree-skb
    API-skb-tx-error
    API-consume-skb
    API-skb-morph
    API-skb-copy-ubufs
    API-skb-clone
    API-skb-copy
    API---pskb-copy-fclone
    API-pskb-expand-head
    API-skb-copy-expand
    API-skb-pad
    API-pskb-put
    API-skb-put
    API-skb-push
    API-skb-pull
    API-skb-trim
    API---pskb-pull-tail
    API-skb-copy-bits
    API-skb-store-bits
    API-skb-zerocopy
    API-skb-dequeue
    API-skb-dequeue-tail
    API-skb-queue-purge
    API-skb-queue-head
    API-skb-queue-tail
    API-skb-unlink
    API-skb-append
    API-skb-insert
    API-skb-split
    API-skb-prepare-seq-read
    API-skb-seq-read
    API-skb-abort-seq-read
    API-skb-find-text
    API-skb-append-datato-frags
    API-skb-pull-rcsum
    API-skb-segment
    API-skb-cow-data
    API-skb-clone-sk
    API-skb-partial-csum-set
    API-skb-checksum-setup
    API-skb-checksum-trimmed
    API-skb-try-coalesce
    API-skb-scrub-packet
    API-skb-gso-transport-seglen
    API-alloc-skb-with-frags
    API-sk-ns-capable
    API-sk-capable
    API-sk-net-capable
    API-sk-set-memalloc
    API-sk-alloc
    API-sk-clone-lock
    API-skb-page-frag-refill
    API-sk-wait-data
    API---sk-mem-schedule
    API---sk-mem-reclaim
    API-lock-sock-fast
    API---skb-try-recv-datagram
    API-skb-kill-datagram
    API-skb-copy-datagram-iter
    API-skb-copy-datagram-from-iter
    API-zerocopy-sg-from-iter
    API-skb-copy-and-csum-datagram-msg
    API-datagram-poll
    API-sk-stream-write-space
    API-sk-stream-wait-connect
    API-sk-stream-wait-memory

Socket Filter
=============


.. toctree::
    :maxdepth: 1

    API-sk-filter
    API-bpf-prog-create
    API-bpf-prog-create-from-user
    API-sk-attach-filter

Generic Network Statistics
==========================


.. toctree::
    :maxdepth: 1

    API-struct-gnet-stats-basic
    API-struct-gnet-stats-rate-est
    API-struct-gnet-stats-rate-est64
    API-struct-gnet-stats-queue
    API-struct-gnet-estimator
    API-gnet-stats-start-copy-compat
    API-gnet-stats-start-copy
    API-gnet-stats-copy-basic
    API-gnet-stats-copy-rate-est
    API-gnet-stats-copy-queue
    API-gnet-stats-copy-app
    API-gnet-stats-finish-copy
    API-gen-new-estimator
    API-gen-kill-estimator
    API-gen-replace-estimator
    API-gen-estimator-active

SUN RPC subsystem
=================


.. toctree::
    :maxdepth: 1

    API-xdr-encode-opaque-fixed
    API-xdr-encode-opaque
    API-xdr-terminate-string
    API--copy-from-pages
    API-xdr-stream-pos
    API-xdr-init-encode
    API-xdr-commit-encode
    API-xdr-reserve-space
    API-xdr-truncate-encode
    API-xdr-restrict-buflen
    API-xdr-write-pages
    API-xdr-init-decode
    API-xdr-init-decode-pages
    API-xdr-set-scratch-buffer
    API-xdr-inline-decode
    API-xdr-read-pages
    API-xdr-enter-page
    API-xdr-buf-subsegment
    API-xdr-buf-trim
    API-svc-print-addr
    API-svc-reserve
    API-svc-find-xprt
    API-svc-xprt-names
    API-xprt-register-transport
    API-xprt-unregister-transport
    API-xprt-load-transport
    API-xprt-reserve-xprt
    API-xprt-release-xprt
    API-xprt-release-xprt-cong
    API-xprt-release-rqst-cong
    API-xprt-adjust-cwnd
    API-xprt-wake-pending-tasks
    API-xprt-wait-for-buffer-space
    API-xprt-write-space
    API-xprt-set-retrans-timeout-def
    API-xprt-set-retrans-timeout-rtt
    API-xprt-disconnect-done
    API-xprt-lookup-rqst
    API-xprt-complete-rqst
    API-xprt-get
    API-xprt-put
    API-rpc-wake-up
    API-rpc-wake-up-status
    API-rpc-malloc
    API-rpc-free
    API-xdr-skb-read-bits
    API-xdr-partial-copy-from-skb
    API-csum-partial-copy-to-xdr
    API-rpc-alloc-iostats
    API-rpc-free-iostats
    API-rpc-count-iostats-metrics
    API-rpc-count-iostats
    API-rpc-queue-upcall
    API-rpc-mkpipe-dentry
    API-rpc-unlink
    API-rpc-init-pipe-dir-head
    API-rpc-init-pipe-dir-object
    API-rpc-add-pipe-dir-object
    API-rpc-remove-pipe-dir-object
    API-rpc-find-or-alloc-pipe-dir-object
    API-rpcb-getport-async
    API-rpc-create
    API-rpc-clone-client
    API-rpc-clone-client-set-auth
    API-rpc-switch-client-transport
    API-rpc-clnt-iterate-for-each-xprt
    API-rpc-bind-new-program
    API-rpc-run-task
    API-rpc-call-sync
    API-rpc-call-async
    API-rpc-peeraddr
    API-rpc-peeraddr2str
    API-rpc-localaddr
    API-rpc-protocol
    API-rpc-net-ns
    API-rpc-max-payload
    API-rpc-get-timeout
    API-rpc-force-rebind
    API-rpc-clnt-test-and-add-xprt
    API-rpc-clnt-add-xprt

WiMAX
=====


.. toctree::
    :maxdepth: 1

    API-wimax-msg-alloc
    API-wimax-msg-data-len
    API-wimax-msg-data
    API-wimax-msg-len
    API-wimax-msg-send
    API-wimax-msg
    API-wimax-reset
    API-wimax-report-rfkill-hw
    API-wimax-report-rfkill-sw
    API-wimax-rfkill
    API-wimax-state-change
    API-wimax-state-get
    API-wimax-dev-init
    API-wimax-dev-add
    API-wimax-dev-rm
    API-struct-wimax-dev
    API-enum-wimax-st
