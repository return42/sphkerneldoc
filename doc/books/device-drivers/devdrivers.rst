
.. _devdrivers:

=============================
Device drivers infrastructure
=============================


The Basic Device Driver-Model Structures
========================================


.. toctree::
    :maxdepth: 1

    API-struct-bus-type
    API-enum-probe-type
    API-struct-device-driver
    API-struct-subsys-interface
    API-struct-class
    API-struct-device
    API-module-driver
    API-builtin-driver

Device Drivers Base
===================


.. toctree::
    :maxdepth: 1

    API-driver-init
    API-driver-for-each-device
    API-driver-find-device
    API-driver-create-file
    API-driver-remove-file
    API-driver-register
    API-driver-unregister
    API-driver-find
    API-dev-driver-string
    API-device-create-file
    API-device-remove-file
    API-device-remove-file-self
    API-device-create-bin-file
    API-device-remove-bin-file
    API-device-initialize
    API-dev-set-name
    API-device-add
    API-device-register
    API-get-device
    API-put-device
    API-device-del
    API-device-unregister
    API-device-for-each-child
    API-device-for-each-child-reverse
    API-device-find-child
    API---root-device-register
    API-root-device-unregister
    API-device-create-vargs
    API-device-create
    API-device-create-with-groups
    API-device-destroy
    API-device-rename
    API-device-move
    API-set-primary-fwnode
    API-register-syscore-ops
    API-unregister-syscore-ops
    API-syscore-suspend
    API-syscore-resume
    API---class-create
    API-class-destroy
    API-class-dev-iter-init
    API-class-dev-iter-next
    API-class-dev-iter-exit
    API-class-for-each-device
    API-class-find-device
    API-class-compat-register
    API-class-compat-unregister
    API-class-compat-create-link
    API-class-compat-remove-link
    API-unregister-node
    API-request-firmware
    API-request-firmware-direct
    API-release-firmware
    API-request-firmware-nowait
    API-transport-class-register
    API-transport-class-unregister
    API-anon-transport-class-register
    API-anon-transport-class-unregister
    API-transport-setup-device
    API-transport-add-device
    API-transport-configure-device
    API-transport-remove-device
    API-transport-destroy-device
    API-device-bind-driver
    API-wait-for-device-probe
    API-device-attach
    API-driver-attach
    API-device-release-driver
    API-platform-device-register-resndata
    API-platform-device-register-simple
    API-platform-device-register-data
    API-platform-get-resource
    API-platform-get-irq
    API-platform-irq-count
    API-platform-get-resource-byname
    API-platform-get-irq-byname
    API-platform-add-devices
    API-platform-device-put
    API-platform-device-alloc
    API-platform-device-add-resources
    API-platform-device-add-data
    API-platform-device-add-properties
    API-platform-device-add
    API-platform-device-del
    API-platform-device-register
    API-platform-device-unregister
    API-platform-device-register-full
    API---platform-driver-register
    API-platform-driver-unregister
    API---platform-driver-probe
    API---platform-create-bundle
    API---platform-register-drivers
    API-platform-unregister-drivers
    API-bus-for-each-dev
    API-bus-find-device
    API-bus-find-device-by-name
    API-subsys-find-device-by-id
    API-bus-for-each-drv
    API-bus-rescan-devices
    API-device-reprobe
    API-bus-register
    API-bus-unregister
    API-subsys-dev-iter-init
    API-subsys-dev-iter-next
    API-subsys-dev-iter-exit
    API-subsys-system-register
    API-subsys-virtual-register

Device Drivers DMA Management
=============================


.. toctree::
    :maxdepth: 1

    API-dma-buf-export
    API-dma-buf-fd
    API-dma-buf-get
    API-dma-buf-put
    API-dma-buf-attach
    API-dma-buf-detach
    API-dma-buf-map-attachment
    API-dma-buf-unmap-attachment
    API-dma-buf-begin-cpu-access
    API-dma-buf-end-cpu-access
    API-dma-buf-kmap-atomic
    API-dma-buf-kunmap-atomic
    API-dma-buf-kmap
    API-dma-buf-kunmap
    API-dma-buf-mmap
    API-dma-buf-vmap
    API-dma-buf-vunmap
    API-fence-context-alloc
    API-fence-signal-locked
    API-fence-signal
    API-fence-wait-timeout
    API-fence-enable-sw-signaling
    API-fence-add-callback
    API-fence-remove-callback
    API-fence-default-wait
    API-fence-wait-any-timeout
    API-fence-init


=============================
drivers/dma-buf/seqno-fence.c
=============================

*man drivers/dma-buf/seqno-fence.c(None)*

Document generation inconsistency


Oops
====

    **Warning**

    The template for this document tried to insert the structured comment from the file ``drivers/dma-buf/seqno-fence.c`` at this point, but none was found. This dummy section is
    inserted to allow generation to continue.


.. toctree::
    :maxdepth: 1

    API-struct-fence
    API-struct-fence-cb
    API-struct-fence-ops
    API-fence-get
    API-fence-get-rcu
    API-fence-put
    API-fence-is-signaled-locked
    API-fence-is-signaled
    API-fence-is-later
    API-fence-later
    API-fence-wait
    API-to-seqno-fence
    API-seqno-fence-init


=============================
drivers/dma-buf/reservation.c
=============================

*man drivers/dma-buf/reservation.c(None)*

Document generation inconsistency


Oops
====

    **Warning**

    The template for this document tried to insert the structured comment from the file ``drivers/dma-buf/reservation.c`` at this point, but none was found. This dummy section is
    inserted to allow generation to continue.



===========================
include/linux/reservation.h
===========================

*man include/linux/reservation.h(None)*

Document generation inconsistency


Oops
====

    **Warning**

    The template for this document tried to insert the structured comment from the file ``include/linux/reservation.h`` at this point, but none was found. This dummy section is
    inserted to allow generation to continue.


.. toctree::
    :maxdepth: 1

    API-dma-alloc-from-coherent
    API-dma-release-from-coherent
    API-dma-mmap-from-coherent
    API-dmam-alloc-coherent
    API-dmam-free-coherent
    API-dmam-alloc-noncoherent
    API-dmam-free-noncoherent
    API-dmam-declare-coherent-memory
    API-dmam-release-declared-memory

Device Drivers Power Management
===============================


.. toctree::
    :maxdepth: 1

    API-dpm-resume-start
    API-dpm-resume-end
    API-dpm-suspend-end
    API-dpm-suspend-start
    API-device-pm-wait-for-dev
    API-dpm-for-each-dev

Device Drivers ACPI Support
===========================


.. toctree::
    :maxdepth: 1

    API-acpi-bus-scan
    API-acpi-bus-trim
    API-acpi-scan-drop-device
    API-acpi-dma-supported
    API-acpi-get-dma-attr

Device drivers PnP support
==========================


.. toctree::
    :maxdepth: 1

    API-pnp-register-protocol
    API-pnp-unregister-protocol
    API-pnp-request-card-device
    API-pnp-release-card-device
    API-pnp-register-card-driver
    API-pnp-unregister-card-driver
    API-pnp-add-id
    API-pnp-start-dev
    API-pnp-stop-dev
    API-pnp-activate-dev
    API-pnp-disable-dev
    API-pnp-is-active

Userspace IO devices
====================


.. toctree::
    :maxdepth: 1

    API-uio-event-notify
    API---uio-register-device
    API-uio-unregister-device
    API-struct-uio-mem
    API-struct-uio-port
    API-struct-uio-info
