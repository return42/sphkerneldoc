.. -*- coding: utf-8; mode: rst -*-

.. _usbcore:

=============
USB Core APIs
=============

There are two basic I/O models in the USB API. The most elemental one is
asynchronous: drivers submit requests in the form of an URB, and the
URB's completion callback handle the next step. All USB transfer types
support that model, although there are special cases for control URBs
(which always have setup and status stages, but may not have a data
stage) and isochronous URBs (which allow large packets and include
per-packet fault reports). Built on top of that is synchronous API
support, where a driver calls a routine that allocates one or more URBs,
submits them, and waits until they complete. There are synchronous
wrappers for single-buffer control and bulk transfers (which are awkward
to use in some driver disconnect scenarios), and for scatterlist based
streaming i/o (bulk or interrupt).

USB drivers need to provide buffers that can be used for DMA, although
they don't necessarily need to provide the DMA mapping themselves. There
are APIs to use used when allocating DMA buffers, which can prevent use
of bounce buffers on some systems. In some cases, drivers may be able to
rely on 64bit DMA to eliminate another kind of bounce buffer.


.. toctree::
    :maxdepth: 1

    API-usb-init-urb
    API-usb-alloc-urb
    API-usb-free-urb
    API-usb-get-urb
    API-usb-anchor-urb
    API-usb-unanchor-urb
    API-usb-submit-urb
    API-usb-unlink-urb
    API-usb-kill-urb
    API-usb-poison-urb
    API-usb-block-urb
    API-usb-kill-anchored-urbs
    API-usb-poison-anchored-urbs
    API-usb-unpoison-anchored-urbs
    API-usb-unlink-anchored-urbs
    API-usb-anchor-suspend-wakeups
    API-usb-anchor-resume-wakeups
    API-usb-wait-anchor-empty-timeout
    API-usb-get-from-anchor
    API-usb-scuttle-anchored-urbs
    API-usb-anchor-empty
    API-usb-control-msg
    API-usb-interrupt-msg
    API-usb-bulk-msg
    API-usb-sg-init
    API-usb-sg-wait
    API-usb-sg-cancel
    API-usb-get-descriptor
    API-usb-string
    API-usb-get-status
    API-usb-clear-halt
    API-usb-reset-endpoint
    API-usb-set-interface
    API-usb-reset-configuration
    API-usb-driver-set-configuration
    API-usb-register-dev
    API-usb-deregister-dev
    API-usb-driver-claim-interface
    API-usb-driver-release-interface
    API-usb-match-id
    API-usb-register-device-driver
    API-usb-deregister-device-driver
    API-usb-register-driver
    API-usb-deregister
    API-usb-enable-autosuspend
    API-usb-disable-autosuspend
    API-usb-autopm-put-interface
    API-usb-autopm-put-interface-async
    API-usb-autopm-put-interface-no-suspend
    API-usb-autopm-get-interface
    API-usb-autopm-get-interface-async
    API-usb-autopm-get-interface-no-resume
    API-usb-find-alt-setting
    API-usb-ifnum-to-if
    API-usb-altnum-to-altsetting
    API-usb-find-interface
    API-usb-for-each-dev
    API-usb-alloc-dev
    API-usb-get-dev
    API-usb-put-dev
    API-usb-get-intf
    API-usb-put-intf
    API-usb-lock-device-for-reset
    API-usb-get-current-frame-number
    API-usb-alloc-coherent
    API-usb-free-coherent
    API-usb-buffer-map
    API-usb-buffer-dmasync
    API-usb-buffer-unmap
    API-usb-buffer-map-sg
    API-usb-buffer-dmasync-sg
    API-usb-buffer-unmap-sg
    API-usb-hub-clear-tt-buffer
    API-usb-set-device-state
    API-usb-root-hub-lost-power
    API-usb-reset-device
    API-usb-queue-reset-device
    API-usb-hub-find-child




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
