.. -*- coding: utf-8; mode: rst -*-

.. _hardware:

===================
Hardware Interfaces
===================


Interrupt Handling
==================


.. toctree::
    :maxdepth: 1

    API-synchronize-hardirq
    API-synchronize-irq
    API-irq-set-affinity-notifier
    API-irq-set-vcpu-affinity
    API-disable-irq-nosync
    API-disable-irq
    API-disable-hardirq
    API-enable-irq
    API-irq-set-irq-wake
    API-irq-wake-thread
    API-setup-irq
    API-remove-irq
    API-free-irq
    API-request-threaded-irq
    API-request-any-context-irq
    API-irq-percpu-is-enabled
    API-free-percpu-irq
    API-request-percpu-irq
    API-irq-get-irqchip-state
    API-irq-set-irqchip-state


DMA Channels
============


.. toctree::
    :maxdepth: 1

    API-request-dma
    API-free-dma


Resources Management
====================


.. toctree::
    :maxdepth: 1

    API-request-resource-conflict
    API-reallocate-resource
    API-lookup-resource
    API-insert-resource-conflict
    API-insert-resource-expand-to-fit
    API-resource-alignment
    API-release-mem-region-adjustable
    API-request-resource
    API-release-resource
    API-region-intersects
    API-allocate-resource
    API-insert-resource
    API-remove-resource
    API-adjust-resource
    API---request-region
    API---release-region
    API-devm-request-resource
    API-devm-release-resource


MTRR Handling
=============


.. toctree::
    :maxdepth: 1

    API-arch-phys-wc-add


PCI Support Library
===================


.. toctree::
    :maxdepth: 1

    API-pci-bus-max-busnr
    API-pci-find-capability
    API-pci-bus-find-capability
    API-pci-find-next-ext-capability
    API-pci-find-ext-capability
    API-pci-find-next-ht-capability
    API-pci-find-ht-capability
    API-pci-find-parent-resource
    API-pci-find-pcie-root-port
    API---pci-complete-power-transition
    API-pci-set-power-state
    API-pci-choose-state
    API-pci-save-state
    API-pci-restore-state
    API-pci-store-saved-state
    API-pci-load-saved-state
    API-pci-load-and-free-saved-state
    API-pci-reenable-device
    API-pci-enable-device-io
    API-pci-enable-device-mem
    API-pci-enable-device
    API-pcim-enable-device
    API-pcim-pin-device
    API-pci-disable-device
    API-pci-set-pcie-reset-state
    API-pci-pme-capable
    API-pci-pme-active
    API---pci-enable-wake
    API-pci-wake-from-d3
    API-pci-prepare-to-sleep
    API-pci-back-from-sleep
    API-pci-dev-run-wake
    API-pci-common-swizzle
    API-pci-release-region
    API-pci-request-region
    API-pci-request-region-exclusive
    API-pci-release-selected-regions
    API-pci-request-selected-regions
    API-pci-release-regions
    API-pci-request-regions
    API-pci-request-regions-exclusive
    API-pci-set-master
    API-pci-clear-master
    API-pci-set-cacheline-size
    API-pci-set-mwi
    API-pci-try-set-mwi
    API-pci-clear-mwi
    API-pci-intx
    API-pci-intx-mask-supported
    API-pci-check-and-mask-intx
    API-pci-check-and-unmask-intx
    API-pci-wait-for-pending-transaction
    API-pci-reset-bridge-secondary-bus
    API---pci-reset-function
    API---pci-reset-function-locked
    API-pci-reset-function
    API-pci-try-reset-function
    API-pci-probe-reset-slot
    API-pci-reset-slot
    API-pci-try-reset-slot
    API-pci-probe-reset-bus
    API-pci-reset-bus
    API-pci-try-reset-bus
    API-pcix-get-max-mmrbc
    API-pcix-get-mmrbc
    API-pcix-set-mmrbc
    API-pcie-get-readrq
    API-pcie-set-readrq
    API-pcie-get-mps
    API-pcie-set-mps
    API-pcie-get-minimum-link
    API-pci-select-bars
    API-pci-add-dynid
    API-pci-match-id
    API---pci-register-driver
    API-pci-unregister-driver
    API-pci-dev-driver
    API-pci-dev-get
    API-pci-dev-put
    API-pci-stop-and-remove-bus-device
    API-pci-find-bus
    API-pci-find-next-bus
    API-pci-get-slot
    API-pci-get-domain-bus-and-slot
    API-pci-get-subsys
    API-pci-get-device
    API-pci-get-class
    API-pci-dev-present
    API-pci-msi-mask-irq
    API-pci-msi-unmask-irq
    API-pci-msi-vec-count
    API-pci-msix-vec-count
    API-pci-enable-msix
    API-pci-msi-enabled
    API-pci-enable-msi-range
    API-pci-enable-msix-range
    API-pci-msi-create-irq-domain
    API-pci-bus-alloc-resource
    API-pci-bus-add-device
    API-pci-bus-add-devices
    API-pci-bus-set-ops
    API-pci-read-vpd
    API-pci-write-vpd
    API-pci-set-vpd-size
    API-pci-cfg-access-lock
    API-pci-cfg-access-trylock
    API-pci-cfg-access-unlock
    API-pci-lost-interrupt
    API---ht-create-irq
    API-ht-create-irq
    API-ht-destroy-irq
    API-pci-scan-slot
    API-pci-rescan-bus
    API-pci-create-slot
    API-pci-destroy-slot
    API-pci-hp-create-module-link
    API-pci-hp-remove-module-link
    API-pci-enable-rom
    API-pci-disable-rom
    API-pci-map-rom
    API-pci-unmap-rom
    API-pci-platform-rom
    API-pci-enable-sriov
    API-pci-disable-sriov
    API-pci-num-vf
    API-pci-vfs-assigned
    API-pci-sriov-set-totalvfs
    API-pci-sriov-get-totalvfs
    API-pci-read-legacy-io
    API-pci-write-legacy-io
    API-pci-mmap-legacy-mem
    API-pci-mmap-legacy-io
    API-pci-adjust-legacy-attr
    API-pci-create-legacy-files
    API-pci-mmap-resource
    API-pci-remove-resource-files
    API-pci-create-resource-files
    API-pci-write-rom
    API-pci-read-rom
    API-pci-remove-sysfs-dev-files


PCI Hotplug Support Library
===========================


.. toctree::
    :maxdepth: 1

    API---pci-hp-register
    API-pci-hp-deregister
    API-pci-hp-change-slot-info




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
