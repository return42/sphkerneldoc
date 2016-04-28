.. -*- coding: utf-8; mode: rst -*-

.. _snddev:

=============
Sound Devices
=============


.. toctree::
    :maxdepth: 1

    API-snd-printk
    API-snd-printd
    API-snd-BUG
    API-snd-printd-ratelimit
    API-snd-BUG-ON
    API-snd-printdd
    API-register-sound-special-device
    API-register-sound-mixer
    API-register-sound-midi
    API-register-sound-dsp
    API-unregister-sound-special
    API-unregister-sound-mixer
    API-unregister-sound-midi
    API-unregister-sound-dsp
    API-snd-pcm-stream-linked
    API-snd-pcm-stream-lock-irqsave
    API-snd-pcm-group-for-each-entry
    API-snd-pcm-running
    API-bytes-to-samples
    API-bytes-to-frames
    API-samples-to-bytes
    API-frames-to-bytes
    API-frame-aligned
    API-snd-pcm-lib-buffer-bytes
    API-snd-pcm-lib-period-bytes
    API-snd-pcm-playback-avail
    API-snd-pcm-capture-avail
    API-snd-pcm-playback-hw-avail
    API-snd-pcm-capture-hw-avail
    API-snd-pcm-playback-ready
    API-snd-pcm-capture-ready
    API-snd-pcm-playback-data
    API-snd-pcm-playback-empty
    API-snd-pcm-capture-empty
    API-snd-pcm-trigger-done
    API-params-channels
    API-params-rate
    API-params-period-size
    API-params-periods
    API-params-buffer-size
    API-params-buffer-bytes
    API-snd-pcm-hw-constraint-single
    API-snd-pcm-format-cpu-endian
    API-snd-pcm-set-runtime-buffer
    API-snd-pcm-gettime
    API-snd-pcm-lib-alloc-vmalloc-buffer
    API-snd-pcm-lib-alloc-vmalloc-32-buffer
    API-snd-pcm-sgbuf-get-addr
    API-snd-pcm-sgbuf-get-ptr
    API-snd-pcm-sgbuf-get-chunk-size
    API-snd-pcm-mmap-data-open
    API-snd-pcm-mmap-data-close
    API-snd-pcm-limit-isa-dma-size
    API-snd-pcm-stream-str
    API-snd-pcm-chmap-substream
    API-pcm-format-to-bits
    API-snd-pcm-format-name
    API-snd-pcm-new-stream
    API-snd-pcm-new
    API-snd-pcm-new-internal
    API-snd-pcm-notify
    API-snd-device-new
    API-snd-device-disconnect
    API-snd-device-free
    API-snd-device-register
    API-snd-info-get-line
    API-snd-info-get-str
    API-snd-info-create-module-entry
    API-snd-info-create-card-entry
    API-snd-info-free-entry
    API-snd-info-register
    API-snd-rawmidi-receive
    API-snd-rawmidi-transmit-empty
    API---snd-rawmidi-transmit-peek
    API-snd-rawmidi-transmit-peek
    API---snd-rawmidi-transmit-ack
    API-snd-rawmidi-transmit-ack
    API-snd-rawmidi-transmit
    API-snd-rawmidi-new
    API-snd-rawmidi-set-ops
    API-snd-request-card
    API-snd-lookup-minor-data
    API-snd-register-device
    API-snd-unregister-device
    API-copy-to-user-fromio
    API-copy-from-user-toio
    API-snd-pcm-lib-preallocate-free-for-all
    API-snd-pcm-lib-preallocate-pages
    API-snd-pcm-lib-preallocate-pages-for-all
    API-snd-pcm-sgbuf-ops-page
    API-snd-pcm-lib-malloc-pages
    API-snd-pcm-lib-free-pages
    API-snd-pcm-lib-free-vmalloc-buffer
    API-snd-pcm-lib-get-vmalloc-page
    API-snd-device-initialize
    API-snd-card-new
    API-snd-card-disconnect
    API-snd-card-free-when-closed
    API-snd-card-free
    API-snd-card-set-id
    API-snd-card-add-dev-attr
    API-snd-card-register
    API-snd-component-add
    API-snd-card-file-add
    API-snd-card-file-remove
    API-snd-power-wait
    API-snd-dma-program
    API-snd-dma-disable
    API-snd-dma-pointer
    API-snd-ctl-notify
    API-snd-ctl-new1
    API-snd-ctl-free-one
    API-snd-ctl-add
    API-snd-ctl-replace
    API-snd-ctl-remove
    API-snd-ctl-remove-id
    API-snd-ctl-activate-id
    API-snd-ctl-rename-id
    API-snd-ctl-find-numid
    API-snd-ctl-find-id
    API-snd-ctl-register-ioctl
    API-snd-ctl-register-ioctl-compat
    API-snd-ctl-unregister-ioctl
    API-snd-ctl-unregister-ioctl-compat
    API-snd-ctl-boolean-mono-info
    API-snd-ctl-boolean-stereo-info
    API-snd-ctl-enum-info
    API-snd-pcm-set-ops
    API-snd-pcm-set-sync
    API-snd-interval-refine
    API-snd-interval-ratnum
    API-snd-interval-list
    API-snd-interval-ranges
    API-snd-pcm-hw-rule-add
    API-snd-pcm-hw-constraint-mask64
    API-snd-pcm-hw-constraint-integer
    API-snd-pcm-hw-constraint-minmax
    API-snd-pcm-hw-constraint-list
    API-snd-pcm-hw-constraint-ranges
    API-snd-pcm-hw-constraint-ratnums
    API-snd-pcm-hw-constraint-ratdens
    API-snd-pcm-hw-constraint-msbits
    API-snd-pcm-hw-constraint-step
    API-snd-pcm-hw-constraint-pow2
    API-snd-pcm-hw-rule-noresample
    API-snd-pcm-hw-param-value
    API-snd-pcm-hw-param-first
    API-snd-pcm-hw-param-last
    API-snd-pcm-lib-ioctl
    API-snd-pcm-period-elapsed
    API-snd-pcm-add-chmap-ctls
    API-snd-hwdep-new
    API-snd-pcm-stream-lock
    API-snd-pcm-stream-unlock
    API-snd-pcm-stream-lock-irq
    API-snd-pcm-stream-unlock-irq
    API-snd-pcm-stream-unlock-irqrestore
    API-snd-pcm-stop
    API-snd-pcm-stop-xrun
    API-snd-pcm-suspend
    API-snd-pcm-suspend-all
    API-snd-pcm-lib-default-mmap
    API-snd-pcm-lib-mmap-iomem
    API-snd-malloc-pages
    API-snd-free-pages
    API-snd-dma-alloc-pages
    API-snd-dma-alloc-pages-fallback
    API-snd-dma-free-pages




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
