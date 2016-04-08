
.. _drivers:

========================
RapidIO driver interface
========================

Drivers are provided a set of calls in order to interface with the subsystem to gather info on devices, request/map memory region resources, and manage mailboxes/doorbells.


.. _Functions:

Functions
=========


.. toctree::
    :maxdepth: 1

    API-rio-local-read-config-32
    API-rio-local-write-config-32
    API-rio-local-read-config-16
    API-rio-local-write-config-16
    API-rio-local-read-config-8
    API-rio-local-write-config-8
    API-rio-read-config-32
    API-rio-write-config-32
    API-rio-read-config-16
    API-rio-write-config-16
    API-rio-read-config-8
    API-rio-write-config-8
    API-rio-send-doorbell
    API-rio-init-mbox-res
    API-rio-init-dbell-res
    API-RIO-DEVICE
    API-rio-add-outb-message
    API-rio-add-inb-buffer
    API-rio-get-inb-message
    API-rio-name
    API-rio-get-drvdata
    API-rio-set-drvdata
    API-rio-dev-get
    API-rio-dev-put
    API-rio-register-driver
    API-rio-unregister-driver
    API-rio-local-get-device-id
    API-rio-query-mport
    API-rio-alloc-net
    API-rio-local-set-device-id
    API-rio-add-device
    API-rio-request-inb-mbox
    API-rio-release-inb-mbox
    API-rio-request-outb-mbox
    API-rio-release-outb-mbox
    API-rio-request-inb-dbell
    API-rio-release-inb-dbell
    API-rio-request-outb-dbell
    API-rio-release-outb-dbell
    API-rio-add-mport-pw-handler
    API-rio-del-mport-pw-handler
    API-rio-request-inb-pwrite
    API-rio-release-inb-pwrite
    API-rio-pw-enable
    API-rio-map-inb-region
    API-rio-unmap-inb-region
    API-rio-map-outb-region
    API-rio-unmap-outb-region
    API-rio-mport-get-physefb
    API-rio-get-comptag
    API-rio-set-port-lockout
    API-rio-enable-rx-tx-port
    API-rio-mport-chk-dev-access
    API-rio-inb-pwrite-handler
    API-rio-mport-get-efb
    API-rio-mport-get-feature
    API-rio-get-asm
    API-rio-get-device
    API-rio-lock-device
    API-rio-unlock-device
    API-rio-route-add-entry
    API-rio-route-get-entry
    API-rio-route-clr-table
    API-rio-request-mport-dma
    API-rio-request-dma
    API-rio-release-dma
    API-rio-dma-prep-xfer
    API-rio-dma-prep-slave-sg
    API-rio-register-scan
    API-rio-unregister-scan
