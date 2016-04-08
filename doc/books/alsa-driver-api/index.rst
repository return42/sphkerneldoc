
+++++++++++++++++++
The ALSA Driver API
+++++++++++++++++++

This document is free; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of
the License, or (at your option) any later version.

This document is distributed in the hope that it will be useful, but *WITHOUT ANY WARRANTY*; without even the implied warranty of *MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE*. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
MA 02111-1307 USA


===============================
Management of Cards and Devices
===============================


Card Management
===============


.. toctree::
    :maxdepth: 1

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

Device Components
=================


.. toctree::
    :maxdepth: 1

    API-snd-device-new
    API-snd-device-disconnect
    API-snd-device-free
    API-snd-device-register

Module requests and Device File Entries
=======================================


.. toctree::
    :maxdepth: 1

    API-snd-request-card
    API-snd-lookup-minor-data
    API-snd-register-device
    API-snd-unregister-device

Memory Management Helpers
=========================


.. toctree::
    :maxdepth: 1

    API-copy-to-user-fromio
    API-copy-from-user-toio
    API-snd-malloc-pages
    API-snd-free-pages
    API-snd-dma-alloc-pages
    API-snd-dma-alloc-pages-fallback
    API-snd-dma-free-pages

=======
PCM API
=======


PCM Core
========


.. toctree::
    :maxdepth: 1

    API-snd-pcm-format-name
    API-snd-pcm-new-stream
    API-snd-pcm-new
    API-snd-pcm-new-internal
    API-snd-pcm-notify
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

PCM Format Helpers
==================


.. toctree::
    :maxdepth: 1

    API-snd-pcm-format-signed
    API-snd-pcm-format-unsigned
    API-snd-pcm-format-linear
    API-snd-pcm-format-little-endian
    API-snd-pcm-format-big-endian
    API-snd-pcm-format-width
    API-snd-pcm-format-physical-width
    API-snd-pcm-format-size
    API-snd-pcm-format-silence-64
    API-snd-pcm-format-set-silence
    API-snd-pcm-limit-hw-rates
    API-snd-pcm-rate-to-rate-bit
    API-snd-pcm-rate-bit-to-rate
    API-snd-pcm-rate-mask-intersect
    API-snd-pcm-rate-range-to-bits

PCM Memory Management
=====================


.. toctree::
    :maxdepth: 1

    API-snd-pcm-lib-preallocate-free-for-all
    API-snd-pcm-lib-preallocate-pages
    API-snd-pcm-lib-preallocate-pages-for-all
    API-snd-pcm-sgbuf-ops-page
    API-snd-pcm-lib-malloc-pages
    API-snd-pcm-lib-free-pages
    API-snd-pcm-lib-free-vmalloc-buffer
    API-snd-pcm-lib-get-vmalloc-page

PCM DMA Engine API
==================


.. toctree::
    :maxdepth: 1

    API-snd-hwparams-to-dma-slave-config
    API-snd-dmaengine-pcm-set-config-from-dai-data
    API-snd-dmaengine-pcm-trigger
    API-snd-dmaengine-pcm-pointer-no-residue
    API-snd-dmaengine-pcm-pointer
    API-snd-dmaengine-pcm-request-channel
    API-snd-dmaengine-pcm-open
    API-snd-dmaengine-pcm-open-request-chan
    API-snd-dmaengine-pcm-close
    API-snd-dmaengine-pcm-close-release-chan
    API-snd-pcm-substream-to-dma-direction
    API-struct-snd-dmaengine-dai-dma-data
    API-struct-snd-dmaengine-pcm-config

=================
Control/Mixer API
=================


General Control Interface
=========================


.. toctree::
    :maxdepth: 1

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

AC97 Codec API
==============


.. toctree::
    :maxdepth: 1

    API-snd-ac97-write
    API-snd-ac97-read
    API-snd-ac97-write-cache
    API-snd-ac97-update
    API-snd-ac97-update-bits
    API-snd-ac97-get-short-name
    API-snd-ac97-bus
    API-snd-ac97-mixer
    API-snd-ac97-update-power
    API-snd-ac97-suspend
    API-snd-ac97-resume
    API-snd-ac97-tune-hardware
    API-snd-ac97-set-rate
    API-snd-ac97-pcm-assign
    API-snd-ac97-pcm-open
    API-snd-ac97-pcm-close
    API-snd-ac97-pcm-double-rate-rules

Virtual Master Control API
==========================


.. toctree::
    :maxdepth: 1

    API-snd-ctl-make-virtual-master
    API-snd-ctl-add-vmaster-hook
    API-snd-ctl-sync-vmaster
    API-snd-ctl-add-slave
    API-snd-ctl-add-slave-uncached

========
MIDI API
========


Raw MIDI API
============


.. toctree::
    :maxdepth: 1

    API-snd-rawmidi-receive
    API-snd-rawmidi-transmit-empty
    API---snd-rawmidi-transmit-peek
    API-snd-rawmidi-transmit-peek
    API---snd-rawmidi-transmit-ack
    API-snd-rawmidi-transmit-ack
    API-snd-rawmidi-transmit
    API-snd-rawmidi-new
    API-snd-rawmidi-set-ops

MPU401-UART API
===============


.. toctree::
    :maxdepth: 1

    API-snd-mpu401-uart-interrupt
    API-snd-mpu401-uart-interrupt-tx
    API-snd-mpu401-uart-new

=============
Proc Info API
=============


Proc Info Interface
===================


.. toctree::
    :maxdepth: 1

    API-snd-info-get-line
    API-snd-info-get-str
    API-snd-info-create-module-entry
    API-snd-info-create-card-entry
    API-snd-info-free-entry
    API-snd-info-register

================
Compress Offload
================


Compress Offload API
====================


.. toctree::
    :maxdepth: 1

    API-snd-compress-register
    API-struct-snd-compressed-buffer
    API-struct-snd-compr-params
    API-struct-snd-compr-tstamp
    API-struct-snd-compr-avail
    API-struct-snd-compr-caps
    API-struct-snd-compr-codec-caps
    API-enum-sndrv-compress-encoder
    API-struct-snd-compr-metadata
    API-SNDRV-COMPRESS-IOCTL-VERSION
    API-struct-snd-enc-vorbis
    API-struct-snd-enc-real
    API-struct-snd-enc-flac
    API-struct-snd-compr-runtime
    API-struct-snd-compr-stream
    API-struct-snd-compr-ops
    API-struct-snd-compr

====
ASoC
====


ASoC Core API
=============


.. toctree::
    :maxdepth: 1

    API-struct-snd-soc-jack-pin
    API-struct-snd-soc-jack-zone
    API-struct-snd-soc-jack-gpio
    API-snd-soc-component-to-codec
    API-snd-soc-component-to-platform
    API-snd-soc-dapm-to-component
    API-snd-soc-dapm-to-codec
    API-snd-soc-dapm-to-platform
    API-snd-soc-component-get-dapm
    API-snd-soc-codec-get-dapm
    API-snd-soc-codec-init-bias-level
    API-snd-soc-codec-get-bias-level
    API-snd-soc-codec-force-bias-level
    API-snd-soc-dapm-kcontrol-codec
    API-snd-soc-cache-sync
    API-snd-soc-codec-init-regmap
    API-snd-soc-codec-exit-regmap
    API-snd-soc-kcontrol-component
    API-snd-soc-kcontrol-codec
    API-snd-soc-kcontrol-platform
    API-snd-soc-add-dai-link
    API-snd-soc-remove-dai-link
    API-snd-soc-runtime-set-dai-fmt
    API-snd-soc-cnew
    API-snd-soc-add-component-controls
    API-snd-soc-add-codec-controls
    API-snd-soc-add-platform-controls
    API-snd-soc-add-card-controls
    API-snd-soc-add-dai-controls
    API-snd-soc-dai-set-sysclk
    API-snd-soc-codec-set-sysclk
    API-snd-soc-dai-set-clkdiv
    API-snd-soc-dai-set-pll
    API-snd-soc-dai-set-bclk-ratio
    API-snd-soc-dai-set-fmt
    API-snd-soc-dai-set-tdm-slot
    API-snd-soc-dai-set-channel-map
    API-snd-soc-dai-set-tristate
    API-snd-soc-dai-digital-mute
    API-snd-soc-register-card
    API-snd-soc-unregister-card
    API-snd-soc-register-dai
    API-snd-soc-component-init-regmap
    API-snd-soc-component-exit-regmap
    API-snd-soc-unregister-component
    API-snd-soc-add-platform
    API-snd-soc-register-platform
    API-snd-soc-remove-platform
    API-snd-soc-unregister-platform
    API-snd-soc-register-codec
    API-snd-soc-unregister-codec
    API-devm-snd-soc-register-component
    API-devm-snd-soc-register-platform
    API-devm-snd-soc-register-card
    API-devm-snd-dmaengine-pcm-register
    API-snd-soc-component-read
    API-snd-soc-component-write
    API-snd-soc-component-update-bits
    API-snd-soc-component-update-bits-async
    API-snd-soc-component-async-complete
    API-snd-soc-component-test-bits
    API-snd-soc-update-bits
    API-snd-soc-test-bits
    API-snd-soc-set-runtime-hwparams
    API-snd-soc-info-enum-double
    API-snd-soc-get-enum-double
    API-snd-soc-put-enum-double
    API-snd-soc-info-volsw
    API-snd-soc-info-volsw-sx
    API-snd-soc-get-volsw
    API-snd-soc-put-volsw
    API-snd-soc-get-volsw-sx
    API-snd-soc-put-volsw-sx
    API-snd-soc-info-volsw-range
    API-snd-soc-put-volsw-range
    API-snd-soc-get-volsw-range
    API-snd-soc-limit-volume
    API-snd-soc-info-xr-sx
    API-snd-soc-get-xr-sx
    API-snd-soc-put-xr-sx
    API-snd-soc-get-strobe
    API-snd-soc-put-strobe
    API-snd-soc-new-compress

ASoC DAPM API
=============


.. toctree::
    :maxdepth: 1

    API-snd-soc-dapm-kcontrol-widget
    API-snd-soc-dapm-kcontrol-dapm
    API-snd-soc-dapm-force-bias-level
    API-snd-soc-dapm-sync-unlocked
    API-snd-soc-dapm-sync
    API-snd-soc-dapm-add-routes
    API-snd-soc-dapm-del-routes
    API-snd-soc-dapm-weak-routes
    API-snd-soc-dapm-new-widgets
    API-snd-soc-dapm-get-volsw
    API-snd-soc-dapm-put-volsw
    API-snd-soc-dapm-get-enum-double
    API-snd-soc-dapm-put-enum-double
    API-snd-soc-dapm-info-pin-switch
    API-snd-soc-dapm-get-pin-switch
    API-snd-soc-dapm-put-pin-switch
    API-snd-soc-dapm-new-controls
    API-snd-soc-dapm-enable-pin-unlocked
    API-snd-soc-dapm-enable-pin
    API-snd-soc-dapm-force-enable-pin-unlocked
    API-snd-soc-dapm-force-enable-pin
    API-snd-soc-dapm-disable-pin-unlocked
    API-snd-soc-dapm-disable-pin
    API-snd-soc-dapm-nc-pin-unlocked
    API-snd-soc-dapm-nc-pin
    API-snd-soc-dapm-get-pin-status
    API-snd-soc-dapm-ignore-suspend
    API-snd-soc-dapm-free

ASoC DMA Engine API
===================


.. toctree::
    :maxdepth: 1

    API-snd-dmaengine-pcm-prepare-slave-config
    API-snd-dmaengine-pcm-register
    API-snd-dmaengine-pcm-unregister

=======================
Miscellaneous Functions
=======================


Hardware-Dependent Devices API
==============================


.. toctree::
    :maxdepth: 1

    API-snd-hwdep-new

Jack Abstraction Layer API
==========================


.. toctree::
    :maxdepth: 1

    API-enum-snd-jack-types
    API-snd-jack-add-new-kctl
    API-snd-jack-new
    API-snd-jack-set-parent
    API-snd-jack-set-key
    API-snd-jack-report
    API-snd-soc-card-jack-new
    API-snd-soc-jack-report
    API-snd-soc-jack-add-zones
    API-snd-soc-jack-get-type
    API-snd-soc-jack-add-pins
    API-snd-soc-jack-notifier-register
    API-snd-soc-jack-notifier-unregister
    API-snd-soc-jack-add-gpios
    API-snd-soc-jack-add-gpiods
    API-snd-soc-jack-free-gpios

ISA DMA Helpers
===============


.. toctree::
    :maxdepth: 1

    API-snd-dma-program
    API-snd-dma-disable
    API-snd-dma-pointer

Other Helper Macros
===================


.. toctree::
    :maxdepth: 1

    API-snd-printk
    API-snd-printd
    API-snd-BUG
    API-snd-printd-ratelimit
    API-snd-BUG-ON
    API-snd-printdd
